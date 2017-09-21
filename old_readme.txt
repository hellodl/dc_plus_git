1. 直接对FC_Block进行训练。 

The optimizer selected is Nadam.
The default arguments are:
 >> lr = 2.0e-03
 >> epsilon = 1.0e-08
 >> beta_1 = 0.90
 >> beta_2 = 0.9990
 >> schedule_decay = 0.0040
From configuration:
 >> lr is set to 1.0e-05.


23000/23000 [==============================] - 31s - loss: 0.1167 - acc: 0.9621 - val_loss: 0.0425 - val_acc: 0.9869
Epoch 2/200
23000/23000 [==============================] - 30s - loss: 0.0290 - acc: 0.9908 - val_loss: 0.0421 - val_acc: 0.9882
Epoch 3/200
23000/23000 [==============================] - 27s - loss: 0.0126 - acc: 0.9952 - val_loss: 0.0441 - val_acc: 0.9889
Epoch 4/200
23000/23000 [==============================] - 27s - loss: 0.0068 - acc: 0.9973 - val_loss: 0.0456 - val_acc: 0.9884
Epoch 5/200
23000/23000 [==============================] - 27s - loss: 0.0045 - acc: 0.9984 - val_loss: 0.0530 - val_acc: 0.9878
Epoch 6/200
23000/23000 [==============================] - 27s - loss: 0.0030 - acc: 0.9990 - val_loss: 0.0517 - val_acc: 0.9886
Epoch 7/200
23000/23000 [==============================] - 27s - loss: 0.0018 - acc: 0.9994 - val_loss: 0.0577 - val_acc: 0.9878
Epoch 8/200
23000/23000 [==============================] - 27s - loss: 0.0019 - acc: 0.9995 - val_loss: 0.0545 - val_acc: 0.9876
Epoch 9/200
23000/23000 [==============================] - 27s - loss: 0.0026 - acc: 0.9993 - val_loss: 0.0583 - val_acc: 0.9879
Epoch 10/200
23000/23000 [==============================] - 27s - loss: 0.0020 - acc: 0.9994 - val_loss: 0.0637 - val_acc: 0.9874
Epoch 11/200
23000/23000 [==============================] - 27s - loss: 0.0011 - acc: 0.9997 - val_loss: 0.0673 - val_acc: 0.9880


最好的logloss不如只训练最后一层FC。
很快进入过拟合。

2. 对最后一层FC进行训练，初始权重为vgg16

The optimizer selected is Nadam.
The default arguments are:
 >> lr = 2.0e-03
 >> epsilon = 1.0e-08
 >> beta_1 = 0.90
 >> beta_2 = 0.9990
 >> schedule_decay = 0.0040
From configuration:
 >> lr is set to 1.0e-05.

Epoch 181/200
23000/23000 [==============================] - 5s - loss: 0.0387 - acc: 0.9856 - val_loss: 0.0384 - val_acc: 0.9874rom 0.03843 to 0.03839, saving model to ./model/ft_last.h5
Epoch 182/200
23000/23000 [==============================] - 6s - loss: 0.0388 - acc: 0.9867 - val_loss: 0.0382 - val_acc: 0.9874rom 0.03839 to 0.03822, saving model to ./model/ft_last.h5
Epoch 183/200
23000/23000 [==============================] - 4s - loss: 0.0372 - acc: 0.9856 - val_loss: 0.0383 - val_acc: 0.9874prove
Epoch 184/200
23000/23000 [==============================] - 4s - loss: 0.0386 - acc: 0.9853 - val_loss: 0.0385 - val_acc: 0.9876prove
Epoch 185/200
23000/23000 [==============================] - 4s - loss: 0.0389 - acc: 0.9859 - val_loss: 0.0385 - val_acc: 0.9875prove
Epoch 186/200
23000/23000 [==============================] - 5s - loss: 0.0387 - acc: 0.9858 - val_loss: 0.0382 - val_acc: 0.9877rom 0.03822 to 0.03818, saving model to ./model/ft_last.h5
Epoch 187/200
23000/23000 [==============================] - 4s - loss: 0.0385 - acc: 0.9855 - val_loss: 0.0383 - val_acc: 0.9876prove
Epoch 188/200
23000/23000 [==============================] - 4s - loss: 0.0379 - acc: 0.9850 - val_loss: 0.0385 - val_acc: 0.9878prove
Epoch 189/200
23000/23000 [==============================] - 4s - loss: 0.0400 - acc: 0.9850 - val_loss: 0.0391 - val_acc: 0.9874prove
Epoch 190/200
23000/23000 [==============================] - 4s - loss: 0.0392 - acc: 0.9851 - val_loss: 0.0383 - val_acc: 0.9874prove
Epoch 191/200
23000/23000 [==============================] - 4s - loss: 0.0381 - acc: 0.9860 - val_loss: 0.0384 - val_acc: 0.9875prove
Epoch 192/200
23000/23000 [==============================] - 4s - loss: 0.0390 - acc: 0.9857 - val_loss: 0.0383 - val_acc: 0.9874prove
Epoch 193/200
23000/23000 [==============================] - 4s - loss: 0.0379 - acc: 0.9863 - val_loss: 0.0386 - val_acc: 0.9874prove
Epoch 194/200
23000/23000 [==============================] - 4s - loss: 0.0390 - acc: 0.9853 - val_loss: 0.0385 - val_acc: 0.9874prove
Epoch 195/200
23000/23000 [==============================] - 4s - loss: 0.0381 - acc: 0.9855 - val_loss: 0.0384 - val_acc: 0.9874prove
Epoch 196/200
23000/23000 [==============================] - 4s - loss: 0.0385 - acc: 0.9862 - val_loss: 0.0383 - val_acc: 0.9876prove
Epoch 197/200
23000/23000 [==============================] - 5s - loss: 0.0379 - acc: 0.9863 - val_loss: 0.0381 - val_acc: 0.9876rom 0.03818 to 0.03806, saving model to ./model/ft_last.h5
Epoch 198/200
23000/23000 [==============================] - 4s - loss: 0.0385 - acc: 0.9862 - val_loss: 0.0382 - val_acc: 0.9876prove
Epoch 199/200
23000/23000 [==============================] - 4s - loss: 0.0376 - acc: 0.9860 - val_loss: 0.0385 - val_acc: 0.9874prove
Epoch 200/200
23000/23000 [==============================] - 4s - loss: 0.0373 - acc: 0.9853 - val_loss: 0.0382 - val_acc: 0.9876prove

并没有过拟合。

Next: lr / 5

The optimizer selected is Nadam.
The default arguments are:
 >> lr = 2.0e-03
 >> epsilon = 1.0e-08
 >> beta_1 = 0.90
 >> beta_2 = 0.9990
 >> schedule_decay = 0.0040
From configuration:
 >> lr is set to 2.0e-06.


Epoch 181/200
23000/23000 [==============================] - 4s - loss: 0.0349 - acc: 0.9873 - val_loss: 0.0375 - val_acc: 0.9879prove
Epoch 182/200
23000/23000 [==============================] - 4s - loss: 0.0373 - acc: 0.9866 - val_loss: 0.0375 - val_acc: 0.9878prove
Epoch 183/200
23000/23000 [==============================] - 4s - loss: 0.0348 - acc: 0.9874 - val_loss: 0.0376 - val_acc: 0.9878prove
Epoch 184/200
23000/23000 [==============================] - 4s - loss: 0.0384 - acc: 0.9853 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 185/200
23000/23000 [==============================] - 4s - loss: 0.0364 - acc: 0.9857 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 186/200
23000/23000 [==============================] - 4s - loss: 0.0353 - acc: 0.9864 - val_loss: 0.0376 - val_acc: 0.9878prove
Epoch 187/200
23000/23000 [==============================] - 4s - loss: 0.0385 - acc: 0.9851 - val_loss: 0.0376 - val_acc: 0.9878prove
Epoch 188/200
23000/23000 [==============================] - 4s - loss: 0.0363 - acc: 0.9862 - val_loss: 0.0375 - val_acc: 0.9878prove
Epoch 189/200
23000/23000 [==============================] - 5s - loss: 0.0359 - acc: 0.9871 - val_loss: 0.0374 - val_acc: 0.9878rom 0.03743 to 0.03743, saving model to ./model/ft_last.h5
Epoch 190/200
23000/23000 [==============================] - 4s - loss: 0.0359 - acc: 0.9859 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 191/200
23000/23000 [==============================] - 5s - loss: 0.0365 - acc: 0.9860 - val_loss: 0.0374 - val_acc: 0.9880rom 0.03743 to 0.03740, saving model to ./model/ft_last.h5
Epoch 192/200
23000/23000 [==============================] - 4s - loss: 0.0359 - acc: 0.9865 - val_loss: 0.0374 - val_acc: 0.9880prove
Epoch 193/200
23000/23000 [==============================] - 4s - loss: 0.0349 - acc: 0.9872 - val_loss: 0.0374 - val_acc: 0.9880prove
Epoch 194/200
23000/23000 [==============================] - 4s - loss: 0.0349 - acc: 0.9869 - val_loss: 0.0375 - val_acc: 0.9878prove
Epoch 195/200
23000/23000 [==============================] - 4s - loss: 0.0348 - acc: 0.9871 - val_loss: 0.0375 - val_acc: 0.9879prove
Epoch 196/200
23000/23000 [==============================] - 4s - loss: 0.0342 - acc: 0.9877 - val_loss: 0.0374 - val_acc: 0.9880prove
Epoch 197/200
23000/23000 [==============================] - 4s - loss: 0.0371 - acc: 0.9865 - val_loss: 0.0375 - val_acc: 0.9878prove
Epoch 198/200
23000/23000 [==============================] - 4s - loss: 0.0340 - acc: 0.9872 - val_loss: 0.0375 - val_acc: 0.9878prove
Epoch 199/200
23000/23000 [==============================] - 4s - loss: 0.0372 - acc: 0.9859 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 200/200
23000/23000 [==============================] - 4s - loss: 0.0346 - acc: 0.9873 - val_loss: 0.0375 - val_acc: 0.9879prove

模型优化缓慢，验证集表现进步缓慢

Next: lr / 5


Epoch 181/200
23000/23000 [==============================] - 6s - loss: 0.0331 - acc: 0.9882 - val_loss: 0.0373 - val_acc: 0.9880rom 0.03735 to 0.03735, saving model to ./model/ft_last.h5
Epoch 182/200
23000/23000 [==============================] - 4s - loss: 0.0346 - acc: 0.9871 - val_loss: 0.0373 - val_acc: 0.9880prove
Epoch 183/200
23000/23000 [==============================] - 4s - loss: 0.0343 - acc: 0.9864 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 184/200
23000/23000 [==============================] - 4s - loss: 0.0362 - acc: 0.9861 - val_loss: 0.0374 - val_acc: 0.9878prove
Epoch 185/200
23000/23000 [==============================] - 4s - loss: 0.0368 - acc: 0.9855 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 186/200
23000/23000 [==============================] - 4s - loss: 0.0355 - acc: 0.9863 - val_loss: 0.0374 - val_acc: 0.9878prove
Epoch 187/200
23000/23000 [==============================] - 4s - loss: 0.0373 - acc: 0.9865 - val_loss: 0.0374 - val_acc: 0.9878prove
Epoch 188/200
23000/23000 [==============================] - 4s - loss: 0.0344 - acc: 0.9863 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 189/200
23000/23000 [==============================] - 4s - loss: 0.0357 - acc: 0.9869 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 190/200
23000/23000 [==============================] - 4s - loss: 0.0339 - acc: 0.9870 - val_loss: 0.0374 - val_acc: 0.9878prove
Epoch 191/200
23000/23000 [==============================] - 4s - loss: 0.0353 - acc: 0.9867 - val_loss: 0.0374 - val_acc: 0.9878prove
Epoch 192/200
23000/23000 [==============================] - 4s - loss: 0.0337 - acc: 0.9874 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 193/200
23000/23000 [==============================] - 4s - loss: 0.0363 - acc: 0.9865 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 194/200
23000/23000 [==============================] - 6s - loss: 0.0370 - acc: 0.9863 - val_loss: 0.0373 - val_acc: 0.9879rom 0.03735 to 0.03735, saving model to ./model/ft_last.h5
Epoch 195/200
23000/23000 [==============================] - 4s - loss: 0.0355 - acc: 0.9861 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 196/200
23000/23000 [==============================] - 4s - loss: 0.0359 - acc: 0.9865 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 197/200
23000/23000 [==============================] - 4s - loss: 0.0335 - acc: 0.9876 - val_loss: 0.0374 - val_acc: 0.9879prove
Epoch 198/200
23000/23000 [==============================] - 4s - loss: 0.0362 - acc: 0.9858 - val_loss: 0.0374 - val_acc: 0.9878prove
Epoch 199/200
23000/23000 [==============================] - 4s - loss: 0.0347 - acc: 0.9872 - val_loss: 0.0374 - val_acc: 0.9878prove
Epoch 200/200
23000/23000 [==============================] - 4s - loss: 0.0370 - acc: 0.9862 - val_loss: 0.0374 - val_acc: 0.9878prove


模型优化缓慢，验证集表现几乎停滞


3. 经过对最后一层的训练，接下来训练整个FC模块。


The optimizer selected is Nadam.
The default arguments are:
 >> lr = 2.0e-03
 >> epsilon = 1.0e-08
 >> beta_1 = 0.90
 >> beta_2 = 0.9990
 >> schedule_decay = 0.0040
From configuration:
 >> lr is set to 8.0e-08.


Train on 23000 samples, validate on 12500 samples
epoch(1) 's lr: 0.000000080
Epoch 1/200
23000/23000 [==============================] - 32s - loss: 0.0325 - acc: 0.9875 - val_loss: 0.0376 - val_acc: 0.9878om inf to 0.03763, saving model to ./model/ft_block.h5
Epoch 2/200
23000/23000 [==============================] - 31s - loss: 0.0346 - acc: 0.9876 - val_loss: 0.0375 - val_acc: 0.9878om 0.03763 to 0.03752, saving model to ./model/ft_block.h5
Epoch 3/200
23000/23000 [==============================] - 31s - loss: 0.0342 - acc: 0.9880 - val_loss: 0.0373 - val_acc: 0.9879om 0.03752 to 0.03734, saving model to ./model/ft_block.h5
Epoch 4/200
23000/23000 [==============================] - 31s - loss: 0.0340 - acc: 0.9877 - val_loss: 0.0373 - val_acc: 0.9879om 0.03734 to 0.03726, saving model to ./model/ft_block.h5
Epoch 5/200
23000/23000 [==============================] - 28s - loss: 0.0325 - acc: 0.9873 - val_loss: 0.0373 - val_acc: 0.9881rove
Epoch 6/200
23000/23000 [==============================] - 28s - loss: 0.0326 - acc: 0.9874 - val_loss: 0.0374 - val_acc: 0.9880rove
Epoch 7/200
23000/23000 [==============================] - 28s - loss: 0.0317 - acc: 0.9883 - val_loss: 0.0373 - val_acc: 0.9879rove
Epoch 8/200
23000/23000 [==============================] - 28s - loss: 0.0312 - acc: 0.9877 - val_loss: 0.0373 - val_acc: 0.9879rove
Epoch 9/200
23000/23000 [==============================] - 32s - loss: 0.0322 - acc: 0.9877 - val_loss: 0.0373 - val_acc: 0.9878om 0.03726 to 0.03726, saving model to ./model/ft_block.h5
Epoch 10/200
23000/23000 [==============================] - 28s - loss: 0.0300 - acc: 0.9889 - val_loss: 0.0373 - val_acc: 0.9879rove
Epoch 11/200
23000/23000 [==============================] - 32s - loss: 0.0287 - acc: 0.9895 - val_loss: 0.0372 - val_acc: 0.9881om 0.03726 to 0.03720, saving model to ./model/ft_block.h5
Epoch 12/200
23000/23000 [==============================] - 32s - loss: 0.0296 - acc: 0.9885 - val_loss: 0.0372 - val_acc: 0.9882om 0.03720 to 0.03716, saving model to ./model/ft_block.h5
Epoch 13/200
23000/23000 [==============================] - 32s - loss: 0.0295 - acc: 0.9895 - val_loss: 0.0370 - val_acc: 0.9884om 0.03716 to 0.03704, saving model to ./model/ft_block.h5
Epoch 14/200
23000/23000 [==============================] - 28s - loss: 0.0298 - acc: 0.9879 - val_loss: 0.0371 - val_acc: 0.9882rove
Epoch 15/200
23000/23000 [==============================] - 28s - loss: 0.0294 - acc: 0.9890 - val_loss: 0.0371 - val_acc: 0.9882rove
Epoch 16/200
23000/23000 [==============================] - 32s - loss: 0.0277 - acc: 0.9896 - val_loss: 0.0370 - val_acc: 0.9882om 0.03704 to 0.03701, saving model to ./model/ft_block.h5
Epoch 17/200
23000/23000 [==============================] - 28s - loss: 0.0279 - acc: 0.9896 - val_loss: 0.0371 - val_acc: 0.9881rove
Epoch 18/200
23000/23000 [==============================] - 28s - loss: 0.0259 - acc: 0.9907 - val_loss: 0.0372 - val_acc: 0.9880rove
Epoch 19/200
23000/23000 [==============================] - 28s - loss: 0.0252 - acc: 0.9907 - val_loss: 0.0371 - val_acc: 0.9881rove
Epoch 20/200
23000/23000 [==============================] - 28s - loss: 0.0254 - acc: 0.9902 - val_loss: 0.0372 - val_acc: 0.9880rove
epoch(21) 's lr: 0.000000080
Epoch 21/200
23000/23000 [==============================] - 28s - loss: 0.0261 - acc: 0.9904 - val_loss: 0.0371 - val_acc: 0.9882rove
Epoch 22/200
23000/23000 [==============================] - 32s - loss: 0.0234 - acc: 0.9917 - val_loss: 0.0369 - val_acc: 0.9885om 0.03701 to 0.03693, saving model to ./model/ft_block.h5
Epoch 23/200
23000/23000 [==============================] - 32s - loss: 0.0245 - acc: 0.9910 - val_loss: 0.0369 - val_acc: 0.9885om 0.03693 to 0.03687, saving model to ./model/ft_block.h5
Epoch 24/200
23000/23000 [==============================] - 32s - loss: 0.0237 - acc: 0.9910 - val_loss: 0.0369 - val_acc: 0.9886om 0.03687 to 0.03686, saving model to ./model/ft_block.h5
Epoch 25/200
23000/23000 [==============================] - 32s - loss: 0.0244 - acc: 0.9904 - val_loss: 0.0369 - val_acc: 0.9885om 0.03686 to 0.03686, saving model to ./model/ft_block.h5
Epoch 26/200
23000/23000 [==============================] - 32s - loss: 0.0229 - acc: 0.9918 - val_loss: 0.0368 - val_acc: 0.9885om 0.03686 to 0.03682, saving model to ./model/ft_block.h5
Epoch 27/200
23000/23000 [==============================] - 28s - loss: 0.0241 - acc: 0.9912 - val_loss: 0.0369 - val_acc: 0.9884rove
Epoch 28/200
23000/23000 [==============================] - 28s - loss: 0.0218 - acc: 0.9917 - val_loss: 0.0370 - val_acc: 0.9885rove
Epoch 29/200
23000/23000 [==============================] - 28s - loss: 0.0214 - acc: 0.9923 - val_loss: 0.0369 - val_acc: 0.9885rove
Epoch 30/200
23000/23000 [==============================] - 28s - loss: 0.0215 - acc: 0.9922 - val_loss: 0.0369 - val_acc: 0.9886rove
Epoch 31/200
23000/23000 [==============================] - 28s - loss: 0.0200 - acc: 0.9926 - val_loss: 0.0370 - val_acc: 0.9884rove
Epoch 32/200
23000/23000 [==============================] - 28s - loss: 0.0205 - acc: 0.9921 - val_loss: 0.0370 - val_acc: 0.9885rove
Epoch 33/200

训练集过拟合趋势，测试集提升有限, 保存的模型：ft_block_vl_0.0368_nadam_8e-8_

4. 数据扩充
	a. 'rotation_range': 25, 'shear_range': 0.1, 'zoom_range': [0.75, 1.05], 'width_shift_range': 0.2,
           'height_shift_range': 0.2, 'horizontal_flip': True, 'vertical_flip': True, 'fill_mode': 'constant'

	'base': './model/ft_block_aug_vl_0.324.h5',

	The default arguments are:
 	>> lr = 1.0e-02
 	>> momentum = 0.00
 	>> decay = 0.00
	>> nesterov = False
	From configuration: None
	Finetune the FC_block of VGG16 to predict 'CAT' or 'DOG'.
	
	Total params: 134,268,738
	Trainable params: 119,554,050 (FC_BLOCK)
	Non-trainable params: 14,714,688


	epoch(1) 's lr: 0.010000000
Epoch 1/200
360/360 [==============================] - 572s - loss: 0.1506 - acc: 0.9399 - val_loss: 0.0469 - val_acc: 0.9850m inf to 0.04689, saving model to ./model/ft_block_aug.h5
Epoch 2/200
360/360 [==============================] - 568s - loss: 0.1268 - acc: 0.9487 - val_loss: 0.0454 - val_acc: 0.9853m 0.04689 to 0.04535, saving model to ./model/ft_block_aug.h5
Epoch 3/200
360/360 [==============================] - 566s - loss: 0.1143 - acc: 0.9529 - val_loss: 0.0493 - val_acc: 0.9857ove
Epoch 4/200
360/360 [==============================] - 566s - loss: 0.1110 - acc: 0.9553 - val_loss: 0.0497 - val_acc: 0.9856ove
Epoch 5/200
360/360 [==============================] - 568s - loss: 0.1029 - acc: 0.9588 - val_loss: 0.0433 - val_acc: 0.9860m 0.04535 to 0.04332, saving model to ./model/ft_block_aug.h5
Epoch 6/200
360/360 [==============================] - 567s - loss: 0.1000 - acc: 0.9610 - val_loss: 0.0457 - val_acc: 0.9870ove
Epoch 7/200
360/360 [==============================] - 570s - loss: 0.0985 - acc: 0.9600 - val_loss: 0.0402 - val_acc: 0.9890m 0.04332 to 0.04024, saving model to ./model/ft_block_aug.h5
Epoch 8/200
360/360 [==============================] - 566s - loss: 0.0977 - acc: 0.9607 - val_loss: 0.0445 - val_acc: 0.9864ove
Epoch 9/200
360/360 [==============================] - 567s - loss: 0.0955 - acc: 0.9622 - val_loss: 0.0457 - val_acc: 0.9870ove
Epoch 10/200
360/360 [==============================] - 567s - loss: 0.0909 - acc: 0.9639 - val_loss: 0.0448 - val_acc: 0.9873ove
Epoch 11/200
360/360 [==============================] - 567s - loss: 0.0882 - acc: 0.9653 - val_loss: 0.0544 - val_acc: 0.9849ove
Epoch 12/200
360/360 [==============================] - 570s - loss: 0.0888 - acc: 0.9641 - val_loss: 0.0359 - val_acc: 0.9892m 0.04024 to 0.03586, saving model to ./model/ft_block_aug.h5
Epoch 13/200
360/360 [==============================] - 566s - loss: 0.0865 - acc: 0.9641 - val_loss: 0.0415 - val_acc: 0.9880ove
Epoch 14/200
360/360 [==============================] - 567s - loss: 0.0839 - acc: 0.9661 - val_loss: 0.0404 - val_acc: 0.9876ove
Epoch 15/200
360/360 [==============================] - 567s - loss: 0.0817 - acc: 0.9666 - val_loss: 0.0450 - val_acc: 0.9865ove
Epoch 16/200
360/360 [==============================] - 567s - loss: 0.0809 - acc: 0.9677 - val_loss: 0.0380 - val_acc: 0.9881ove
Epoch 17/200
360/360 [==============================] - 567s - loss: 0.0828 - acc: 0.9663 - val_loss: 0.0453 - val_acc: 0.9878ove
Epoch 18/200
360/360 [==============================] - 567s - loss: 0.0775 - acc: 0.9689 - val_loss: 0.0448 - val_acc: 0.9869ove
Epoch 19/200
360/360 [==============================] - 567s - loss: 0.0777 - acc: 0.9681 - val_loss: 0.0470 - val_acc: 0.9856ove
Epoch 20/200
360/360 [==============================] - 567s - loss: 0.0748 - acc: 0.9704 - val_loss: 0.0452 - val_acc: 0.9876ove
epoch(21) 's lr: 0.010000000
Epoch 21/200
360/360 [==============================] - 567s - loss: 0.0774 - acc: 0.9686 - val_loss: 0.0423 - val_acc: 0.9881ove
Epoch 22/200
360/360 [==============================] - 567s - loss: 0.0767 - acc: 0.9696 - val_loss: 0.0379 - val_acc: 0.9889ove
Epoch 23/200
360/360 [==============================] - 569s - loss: 0.0776 - acc: 0.9686 - val_loss: 0.0405 - val_acc: 0.9883ove
Epoch 24/200
360/360 [==============================] - 570s - loss: 0.0698 - acc: 0.9727 - val_loss: 0.0419 - val_acc: 0.9882ove
Epoch 25/200
360/360 [==============================] - 567s - loss: 0.0723 - acc: 0.9709 - val_loss: 0.0393 - val_acc: 0.9886ove
Epoch 26/200
360/360 [==============================] - 567s - loss: 0.0741 - acc: 0.9703 - val_loss: 0.0426 - val_acc: 0.9870ove
Epoch 27/200
360/360 [==============================] - 567s - loss: 0.0716 - acc: 0.9713 - val_loss: 0.0439 - val_acc: 0.9877ove
Epoch 28/200
360/360 [==============================] - 567s - loss: 0.0709 - acc: 0.9727 - val_loss: 0.0402 - val_acc: 0.9879ove
Epoch 29/200
360/360 [==============================] - 567s - loss: 0.0671 - acc: 0.9741 - val_loss: 0.0472 - val_acc: 0.9876ove
Epoch 30/200
360/360 [==============================] - 568s - loss: 0.0696 - acc: 0.9742 - val_loss: 0.0379 - val_acc: 0.9890ove
Epoch 31/200
360/360 [==============================] - 567s - loss: 0.0650 - acc: 0.9743 - val_loss: 0.0459 - val_acc: 0.9874ove
Epoch 32/200
360/360 [==============================] - 568s - loss: 0.0617 - acc: 0.9758 - val_loss: 0.0454 - val_acc: 0.9877ove
Epoch 33/200
360/360 [==============================] - 568s - loss: 0.0647 - acc: 0.9741 - val_loss: 0.0455 - val_acc: 0.9878ove
Epoch 34/200
360/360 [==============================] - 568s - loss: 0.0666 - acc: 0.9731 - val_loss: 0.0430 - val_acc: 0.9877ove
Epoch 35/200
360/360 [==============================] - 576s - loss: 0.0636 - acc: 0.9744 - val_loss: 0.0448 - val_acc: 0.9883ove
Epoch 36/200
360/360 [==============================] - 569s - loss: 0.0615 - acc: 0.9750 - val_loss: 0.0435 - val_acc: 0.9880ove
Epoch 37/200
360/360 [==============================] - 567s - loss: 0.0626 - acc: 0.9751 - val_loss: 0.0437 - val_acc: 0.9891ove
Epoch 38/200
360/360 [==============================] - 568s - loss: 0.0622 - acc: 0.9745 - val_loss: 0.0411 - val_acc: 0.9879ove
Epoch 39/200
360/360 [==============================] - 568s - loss: 0.0602 - acc: 0.9770 - val_loss: 0.0454 - val_acc: 0.9881ove
Epoch 40/200
360/360 [==============================] - 568s - loss: 0.0582 - acc: 0.9774 - val_loss: 0.0434 - val_acc: 0.9874ove
epoch(41) 's lr: 0.010000000
Epoch 41/200
360/360 [==============================] - 567s - loss: 0.0587 - acc: 0.9776 - val_loss: 0.0480 - val_acc: 0.9873ove
Epoch 42/200
360/360 [==============================] - 568s - loss: 0.0598 - acc: 0.9769 - val_loss: 0.0464 - val_acc: 0.9878ove
Epoch 43/200
360/360 [==============================] - 568s - loss: 0.0593 - acc: 0.9759 - val_loss: 0.0426 - val_acc: 0.9882ove
Epoch 44/200
360/360 [==============================] - 568s - loss: 0.0591 - acc: 0.9777 - val_loss: 0.0551 - val_acc: 0.9871ove
Epoch 45/200
360/360 [==============================] - 568s - loss: 0.0594 - acc: 0.9767 - val_loss: 0.0457 - val_acc: 0.9887ove
Epoch 46/200
360/360 [==============================] - 568s - loss: 0.0590 - acc: 0.9764 - val_loss: 0.0489 - val_acc: 0.9877ove
Epoch 47/200
360/360 [==============================] - 568s - loss: 0.0558 - acc: 0.9772 - val_loss: 0.0470 - val_acc: 0.9874ove
Epoch 48/200
360/360 [==============================] - 568s - loss: 0.0593 - acc: 0.9766 - val_loss: 0.0446 - val_acc: 0.9883ove
Epoch 49/200
360/360 [==============================] - 568s - loss: 0.0556 - acc: 0.9776 - val_loss: 0.0499 - val_acc: 0.9857ove
Epoch 50/200
360/360 [==============================] - 578s - loss: 0.0572 - acc: 0.9772 - val_loss: 0.0472 - val_acc: 0.9888ove
Epoch 51/200
360/360 [==============================] - 569s - loss: 0.0556 - acc: 0.9778 - val_loss: 0.0383 - val_acc: 0.9894ove
Epoch 52/200
360/360 [==============================] - 569s - loss: 0.0529 - acc: 0.9803 - val_loss: 0.0415 - val_acc: 0.9887ove
Epoch 53/200
360/360 [==============================] - 569s - loss: 0.0554 - acc: 0.9780 - val_loss: 0.0436 - val_acc: 0.9879ove
Epoch 54/200
360/360 [==============================] - 576s - loss: 0.0533 - acc: 0.9792 - val_loss: 0.0486 - val_acc: 0.9882ove
Epoch 55/200
360/360 [==============================] - 579s - loss: 0.0534 - acc: 0.9782 - val_loss: 0.0443 - val_acc: 0.9870ove
Epoch 56/200
360/360 [==============================] - 567s - loss: 0.0524 - acc: 0.9788 - val_loss: 0.0472 - val_acc: 0.9873ove
Epoch 57/200
360/360 [==============================] - 568s - loss: 0.0539 - acc: 0.9794 - val_loss: 0.0465 - val_acc: 0.9880ove
Epoch 58/200
360/360 [==============================] - 568s - loss: 0.0528 - acc: 0.9798 - val_loss: 0.0457 - val_acc: 0.9885ove
Epoch 59/200
360/360 [==============================] - 567s - loss: 0.0523 - acc: 0.9803 - val_loss: 0.0433 - val_acc: 0.9875ove
Epoch 60/200
360/360 [==============================] - 561s - loss: 0.0509 - acc: 0.9800 - val_loss: 0.0445 - val_acc: 0.9878ove
epoch(61) 's lr: 0.010000000
Epoch 61/200
360/360 [==============================] - 560s - loss: 0.0517 - acc: 0.9796 - val_loss: 0.0438 - val_acc: 0.9880ove
Epoch 62/200
360/360 [==============================] - 562s - loss: 0.0530 - acc: 0.9785 - val_loss: 0.0438 - val_acc: 0.9884ove

欠拟合明显。降低dropout? 降低lr?

细节：每一次训练集loss大幅度下降，很有可能引起测试集loss明显提高


5. 只训练最后一层，调整dropout, vgg16权重，意图提高拟合。
The optimizer selected is SGD.
The default arguments are:
 >> lr = 1.0e-02
 >> momentum = 0.00
 >> decay = 0.00
 >> nesterov = False
From configuration:
None

	epoch: 150	
	decay: 0.2decay/100epoch   
	monitor: val_loss
	
 [0.4, 0.4] loss: 0.0357 - acc: 0.9863 - val_loss: 0.0334 - val_acc: 0.9865
 [0.3, 0.3] loss: 0.0288 - acc: 0.9889 - val_loss: 0.0319 - val_acc: 0.9845
 [0.2, 0.2] loss: 0.0210 - acc: 0.9927 - val_loss: 0.0322 - val_acc: 0.9860
 [0.1, 0.1] loss: 0.0216 - acc: 0.9926 - val_loss: 0.0333 - val_acc: 0.9840
 [0.0, 0.0] loss: 0.0201 - acc: 0.9939 - val_loss: 0.0327 - val_acc: 0.9870

6. 用5步骤中[0.3, 0.3]的模型对FC_BLOCK, 进行数据增扩训练
top_weights = ./model/ft_last_dp_3_dp_3.h5

The optimizer selected is SGD.
The default arguments are:
 >> lr = 1.0e-02
 >> momentum = 0.00
 >> decay = 0.00
 >> nesterov = False
From configuration:  ##  very slowly
 >> lr is set to 1.0e-04.
 >> momentum is set to 0.90.

->horizontal_flip : True
->vertical_flip : False
->rotation_range : 5
->height_shift_range : 0.1
->shear_range : 0.1
->zoom_range : [0.8, 1.0]
->width_shift_range : 0.1
->fill_mode : constant

Epoch 1/20
360/360 [==============================] - 400s - loss: 0.0412 - acc: 0.9832 - val_loss: 0.0320 - val_acc: 0.9875m inf to 0.03196, saving model to ./model/ftB_OF_3_3.h5
Epoch 2/20
360/360 [==============================] - 401s - loss: 0.0336 - acc: 0.9864 - val_loss: 0.0289 - val_acc: 0.9880m 0.03196 to 0.02885, saving model to ./model/ftB_OF_3_3.h5
Epoch 3/20
360/360 [==============================] - 403s - loss: 0.0330 - acc: 0.9876 - val_loss: 0.0225 - val_acc: 0.9905m 0.02885 to 0.02251, saving model to ./model/ftB_OF_3_3.h5
Epoch 4/20
360/360 [==============================] - 402s - loss: 0.0282 - acc: 0.9889 - val_loss: 0.0326 - val_acc: 0.9835ove
Epoch 5/20
360/360 [==============================] - 400s - loss: 0.0253 - acc: 0.9906 - val_loss: 0.0261 - val_acc: 0.9880ove
Epoch 6/20
360/360 [==============================] - 401s - loss: 0.0223 - acc: 0.9915 - val_loss: 0.0385 - val_acc: 0.9855ove
Epoch 7/20
360/360 [==============================] - 400s - loss: 0.0205 - acc: 0.9923 - val_loss: 0.0301 - val_acc: 0.9880ove


