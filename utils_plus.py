from keras import backend as K
K.set_image_dim_ordering('th')
from keras.models import Sequential
from keras.layers.core import Lambda, Flatten, Dense, Dropout
from keras.layers.convolutional import ZeroPadding2D, Conv2D
from keras.layers.pooling import MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.models import save_model, load_model
from keras.optimizers import SGD, RMSprop, Adam, Nadam, Adadelta, Adamax, Adagrad
from keras.preprocessing import image
import numpy as np
from math import ceil
from dc_utils import onehot,get_batch,save_array,load_array


def aug_trn_batches():
    gen = image.ImageDataGenerator(rotation_range=10,
                                   width_shift_range=0.05,
                                   zoom_range=0.05,
                                   channel_shift_range=10,
                                   height_shift_range=0.05,
                                   shear_range=0.05,
                                   vertical_flip=True,
                                   horizontal_flip=True)
    trn_batches = get_batch('./data/train/',
                            target_size=[224,224],
                            class_mode='categorical',
                            gen=gen,
                            batch_size=64)
    return trn_batches


def create_vgg16():
    vgg_mean = np.array([123.68, 116.779, 103.939], dtype=np.float32).reshape((3, 1, 1))

    def vgg_preprocess(x):
        x = x - vgg_mean
        return x[:, ::-1]

    def ConvBlock(model, nb_block, nb_layer, nb_filter, activation):
        for i in range(nb_block):
            for j in range(nb_layer[i]):
                model.add(ZeroPadding2D((1, 1)))
                model.add(Conv2D(nb_filter[i], (3, 3), activation=activation))
            model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    def FCBlock(model, classes, nb_neuron, dropout, activation):
        for i in range(len(nb_neuron)):
            model.add(Dense(nb_neuron[i], activation=activation[i], name='dense_%s' % i))
            model.add(Dropout(dropout[i], name='dropout_%s' % i))

        model.add(Dense(classes, activation='softmax', name='dense_out'))

    model = Sequential()
    model.add(
        Lambda(vgg_preprocess, input_shape=(3, 224, 224), output_shape=(3, 224, 224)))

    ConvBlock(model,
              nb_block=5,
              nb_layer=[2, 2, 3, 3, 3],
              nb_filter=[64, 128, 256, 512, 512],
              activation='relu')

    model.add(Flatten())
    FCBlock(model,
            classes=1000,
            nb_neuron=[4096, 4096],
            dropout=[0.5, 0.5],
            activation=['relu', 'relu', 'softmax'])

    model.load_weights('vgg16.h5')
    return model


def create_vgg16_bn():
    vgg_mean = np.array([123.68, 116.779, 103.939], dtype=np.float32).reshape((3, 1, 1))

    def vgg_preprocess(x):
        x = x - vgg_mean
        return x[:, ::-1]  # reverse axis rgb->bgr

    def ConvBlock(model, nb_block, nb_layer, nb_filter, activation):
        for i in range(nb_block):
            for j in range(nb_layer[i]):
                model.add(ZeroPadding2D((1, 1)))
                model.add(Conv2D(nb_filter[i], (3, 3), activation=activation))
            model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    def FCBlock(model, classes, nb_neuron, dropout, activation):
        for i in range(len(nb_neuron)):
            model.add(Dense(nb_neuron[i], activation=activation[i], name='dense_%s' % i))
            model.add(BatchNormalization())  # before dropout
            model.add(Dropout(dropout[i], name='dropout_%s' % i))

        model.add(Dense(classes, activation='softmax', name='dense_out'))

    model = Sequential()
    model.add(
        Lambda(vgg_preprocess, input_shape=(3, 224, 224), output_shape=(3, 224, 224)))

    ConvBlock(model,
              nb_block=5,
              nb_layer=[2, 2, 3, 3, 3],
              nb_filter=[64, 128, 256, 512, 512],
              activation='relu')

    model.add(Flatten())
    FCBlock(model,
            classes=1000,
            nb_neuron=[4096, 4096],
            dropout=[0.5, 0.5],
            activation=['relu', 'relu', 'softmax'])

    model.load_weights('vgg16_bn.h5')
    return model


def create_vgg16_bn_no_ll():
    model = create_vgg16_bn()
    model.pop();model.pop();model.pop()
    for layer in model.layers: layer.trainable = False
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def combine_vgg16_bn_with_fc(conv_model, fc_model, dropout, opt, fc_in_shape, last_conv_idx):
    for layer in conv_model.layers: layer.trainable = False
    for layer in get_fc_layers(dropout, fc_in_shape): conv_model.add(layer)
    for l1,l2 in zip(conv_model.layers[last_conv_idx+1:], fc_model.layers):
        l1.set_weights(l2.get_weights())

    conv_model.compile(optimizer=opt, loss='categorical_crossentropy',
                       metrics=['accuracy'])

    return conv_model


def combine_vgg16_bn_with_ll(ll_model, dropout=0.5):
    def get_ll_layers(p):
        return [
            BatchNormalization(input_shape=(4096,)),
            Dropout(p),
            Dense(2, activation='softmax')
        ]

    model = create_vgg16_bn_no_ll()
    ll_layers = get_ll_layers(dropout)
    for layer in ll_layers: model.add(layer)
    for l1, l2 in zip(ll_model.layers, model.layers[-3:]):
        l2.set_weights(l1.get_weights())
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def ensemble(dropout, opt, set_lr_ll, set_ep_ll, set_lr_fc, set_ep_fc):
    for i in range(5):
        i = str(i)
        model = train_last_layer_bn(dropout, opt=opt, set_lr=set_lr_ll, set_ep=set_ep_ll, idx=i)
        train_dense_layers_bn(model, dropout, opt=opt, set_lr=set_lr_fc, set_ep=set_ep_fc, idx=i)


def ensemble0(dropout, opt, set_lr_ll, set_ep_ll):
    model = train_last_layer_bn(dropout, opt=opt, set_lr=set_lr_ll, set_ep=set_ep_ll, idx='1')
    save_model('./model/ft_dense.hdf5')
        
        
def ensemble1(dropout, opt, set_lr_fc, set_ep_fc):
    model = load_model('./model/ft_dense.hdf5')
    train_dense_layers_bn(model, dropout, opt=opt, set_lr=set_lr_fc, set_ep=set_ep_fc, idx='1')

        
def get_conv_model(model):
    layers = model.layers
    last_conv_idx = [index for index,layer in enumerate(layers)
                         if type(layer) is Conv2D][-1]

    conv_layers = layers[:last_conv_idx+1]
    conv_model = Sequential(conv_layers)
    fc_layers = layers[last_conv_idx+1:]
    return conv_model, fc_layers, last_conv_idx


def get_fc_layers(p, in_shape):
    return [
        MaxPooling2D(input_shape=in_shape),
        Flatten(),
        Dense(4096, activation='relu'),
        BatchNormalization(),
        Dropout(p),
        Dense(4096, activation='relu'),
        BatchNormalization(),
        Dropout(p),
        Dense(2, activation='softmax')
        ]


def gen_fc_model(fc_in_shape, dropout, fc_layers, opt):
    model = Sequential(get_fc_layers(dropout, fc_in_shape))
    for l1, l2 in zip(model.layers, fc_layers):
        weights = l2.get_weights()
        l1.set_weights(weights)

    model.compile(opt, loss='categorical_crossentropy',
                     metrics=['accuracy'])
    return model


def get_val_batches():
    val_batches = get_batch('./data/valid/',
                            target_size=[224,224],
                            class_mode='categorical',
                            batch_size=64)
    return val_batches


def gen_feat_lbs(model, datapath, batch_size, img_size=(224,224)):
    batches = get_batch(datapath,
                        target_size=img_size,
                        class_mode='categorical',
                        shuffle=False,
                        batch_size=batch_size)
    labels = onehot(batches.classes)
    features = model.predict_generator(batches,
                                        ceil(batches.samples / batch_size),
                                        verbose=1)

    return features, labels


def gen_feat_ids(model, datapath, batch_size, img_size=(224,224)):
    batches = get_batch(
        datapath,
        target_size=img_size,
        class_mode='categorical',
        shuffle=False,
        batch_size=batch_size)

    ids = np.array([int(f[8:f.find('.')]) for f in batches.filenames])
    features = model.predict_generator(batches,
                                       ceil(batches.samples / batch_size),
                                       verbose=1)
    return features, ids


def gen_ll_model(dropout, opt):
    def get_ll_layers(p):
        return [
            BatchNormalization(input_shape=(4096,)),
            Dropout(p),
            Dense(2, activation='softmax')
        ]

    ll_layers = get_ll_layers(dropout)
    ll_model = Sequential(ll_layers)
    ll_model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    return ll_model


def fit_fc_model(model, feats, lr, ep):
    model.optimizer.lr = lr
    model.fit(feats['trn'][0], feats['trn'][1],
              validation_data=feats['val'],
              batch_size=64,
              epochs = ep)


def fit_ll_model(model, feats, lr, ep, verbose=1):
    model.optimizer.lr = lr
    model.fit(feats['trn'][0],feats['trn'][1],
              validation_data=feats['val'],
              batch_size=64,
              epochs=ep,
              verbose=verbose)


def fit_vgg16bn_model_fc(model, t_batches, v_batches, lr, ep):
    model.optimizer.lr = lr
    model.fit_generator(
        t_batches,
        steps_per_epoch=ceil(t_batches.samples / t_batches.batch_size),
        validation_data=v_batches,
        epochs=ep,
        validation_steps=ceil(v_batches.samples / v_batches.batch_size),
        callbacks=[]
    )


def spilt_model(model):
    layers = model.layers
    last_conv_idx = [index for index, layer in enumerate(layers)
                     if type(layer) is Conv2D][-1]

    conv_layers = layers[:last_conv_idx + 1]
    conv_model = Sequential(conv_layers)
    fc_layers = layers[last_conv_idx + 1:]

    return conv_model, fc_layers, last_conv_idx


def train_dense_layers_bn(model, dropout, opt, set_lr, set_ep, idx):
    opt = eval(opt)()
    conv_model, fc_layers, last_conv_idx = get_conv_model(model)
    fc_in_shape = conv_model.output_shape[1:]

    feats = vgg16bn_feat_conv()
    fc_model = gen_fc_model(fc_in_shape, dropout, fc_layers, opt)
    fit_fc_model(fc_model, feats, lr=set_lr[0], ep=set_ep[0])

    trn_batches = aug_trn_batches()
    val_batches = get_val_batches()  # 这里和源程序shuffle参数不一样
    vgg16bn_model_fc = combine_vgg16_bn_with_fc(conv_model, fc_model,
                                                dropout, opt, fc_in_shape, last_conv_idx)
    vgg16bn_model_fc.save_weights('./model/' + 'vgg16_bn_fc_' + str(idx) + '.h5')
    fit_vgg16bn_model_fc(vgg16bn_model_fc, trn_batches, val_batches, lr=set_lr[1], ep=set_ep[1])

    for layer in vgg16bn_model_fc.layers[16:]: layer.trainable = True

    fit_vgg16bn_model_fc(vgg16bn_model_fc, trn_batches, val_batches, lr=set_lr[2], ep=set_ep[2])
    fit_vgg16bn_model_fc(vgg16bn_model_fc, trn_batches, val_batches, lr=set_lr[3], ep=set_ep[3])
    vgg16bn_model_fc.save_weights('./model/' + 'vgg16_bn_aug_' + str(idx) + '.h5')


def train_last_layer_bn(dropout, opt, set_lr, set_ep, idx):
    opt = eval(opt)()
    ll_bn_model = gen_ll_model(dropout=dropout, opt=opt)
    feats = vgg16bn_feat_ll()
    fit_ll_model(ll_bn_model, feats, lr=set_lr[0], ep=set_ep[0])
    fit_ll_model(ll_bn_model, feats, lr=set_lr[1], ep=set_ep[1])
    ll_bn_model.save_weights('./model/' + 'll_bn' + str(idx) + '.h5')

    vgg16bn_model=combine_vgg16_bn_with_ll(ll_bn_model)
    vgg16bn_model.save_weights('./model/' + '_bn' + str(idx) + '.h5')
    return vgg16bn_model


def vgg16_feat_ll():
    trn_feat = load_array('./data/feature/trn_ll_feat.bc')
    trn_lbs = load_array('./data/feature/trn_lbs.bc')
    val_feat = load_array('./data/feature/val_ll_feat.bc')
    val_lbs = load_array('./data/feature/val_lbs.bc')

    return {'trn': [trn_feat, trn_lbs], 'val': [val_feat, val_lbs]}


def vgg16bn_feat_ll():
    trn_feat = load_array('./data/feature/trn_ll_feat_bn.bc')
    trn_lbs = load_array('./data/feature/trn_lbs.bc')
    val_feat = load_array('./data/feature/val_ll_feat_bn.bc')
    val_lbs = load_array('./data/feature/val_lbs.bc')

    return {'trn':[trn_feat, trn_lbs], 'val':[val_feat, val_lbs]}


def vgg16_feat_conv():
    trn_feat = load_array('./data/feature/trn_cnv_feat.bc')
    trn_lbs = load_array('./data/feature/trn_lbs.bc')
    val_feat = load_array('./data/feature/val_cnv_feat.bc')
    val_lbs = load_array('./data/feature/val_lbs.bc')

    return {'trn': [trn_feat, trn_lbs], 'val': [val_feat, val_lbs]}


def vgg16bn_feat_conv():
    trn_feat = load_array('./data/feature/trn_cnv_feat_bn.bc')
    trn_lbs = load_array('./data/feature/trn_lbs.bc')
    val_feat = load_array('./data/feature/val_cnv_feat_bn.bc')
    val_lbs = load_array('./data/feature/val_lbs.bc')

    return {'trn': [trn_feat, trn_lbs], 'val': [val_feat, val_lbs]}


if __name__ == '__main__':
    vgg16_mdl = create_vgg16()
    conv_model,_,_ = spilt_model(vgg16_mdl)
    trn_feat, trn_lbs = gen_feat_lbs(conv_model,
                                     './data/train/',
                                     batch_size=64)
    val_feat, val_lbs = gen_feat_lbs(conv_model,
                                     './data/valid/',
                                     batch_size=64)

    save_array('./data/feature/trn_cnv_feat.bc', trn_feat)
    save_array('./data/feature/val_cnv_feat.bc', val_feat)
