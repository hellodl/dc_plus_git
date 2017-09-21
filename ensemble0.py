from utils_plus import gen_ll_model, vgg16_feat_ll, vgg16bn_feat_ll, fit_ll_model, train_last_layer_bn, ensemble0

set_lr_ll=(1e-3, 1e-4)
set_ep_ll=(150, 50)  # (150, 50)
ensemble0(dropout=0.5, opt='SGD',
         set_lr_ll=set_lr_ll, set_ep_ll=set_ep_ll)