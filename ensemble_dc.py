from utils_plus import gen_ll_model, vgg16_feat_ll, vgg16bn_feat_ll, fit_ll_model, train_last_layer_bn, ensemble

set_lr_ll=(1e-5, 1e-7)
set_ep_ll=(150, 50)  # (150, 50)
set_lr_fc=(1e-7, 1e-5, 1e-5, 1e-7)
set_ep_fc=(1, 10, 20, 24)  # (2, 1, 8, 10)
ensemble(dropout=0.5, opt='Nadam',
         set_lr_ll=set_lr_ll, set_ep_ll=set_ep_ll,
         set_lr_fc=set_lr_fc, set_ep_fc=set_ep_fc)
