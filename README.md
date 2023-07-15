# Fork of [CartoonGAN-Test-Pytorch-Torch](https://github.com/Yijunmaverick/CartoonGAN-Test-Pytorch-Torch)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.0. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases). (🔥)
* Model conversion to ONNX format using the [export.py](export.py) file. (🔥)
* [ONNX Simplifier](https://github.com/daquexian/onnx-simplifier) integration in the [export.py](export.py) file.
* Installation with [requirements.txt](requirements.txt) file.
* The following deprecations and errors has been fixed:
  * UserWarning: volatile was removed and now has no effect.
  * TypeError: can't multiply sequence by non-int of type 'float'.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

| Name    | Link                                                                                                                                                                                                                                     |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hayao   | [PyTorch](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/Hayao_net_G_float.pth), [ONNX](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/Hayao_net_G_float.onnx)     |
| Hosoda  | [PyTorch](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/Hosoda_net_G_float.pth), [ONNX](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/Hosoda_net_G_float.onnx)   |
| Paprika | [PyTorch](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/Paprika_net_G_float.pth), [ONNX](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/Paprika_net_G_float.onnx) |
| Shinkai | [PyTorch](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/Shinkai_net_G_float.pth), [ONNX](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/Shinkai_net_G_float.onnx) |

# Inference

```shell
python test.py --model_path pretrained_model --style Hayao --input_dir test_img --output_dir test_out
python test.py --model_path pretrained_model --style Hosoda --input_dir test_img --output_dir test_out
python test.py --model_path pretrained_model --style Paprika --input_dir test_img --output_dir test_out
python test.py --model_path pretrained_model --style Shinkai --input_dir test_img --output_dir test_out
```

# Export to ONNX format

```shell
pip install onnx onnxsim
```
```shell
python export.py --weights pretrained_model/Hayao_net_G_float.pth --dynamic
python export.py --weights pretrained_model/Hosoda_net_G_float.pth --dynamic
python export.py --weights pretrained_model/Paprika_net_G_float.pth --dynamic
python export.py --weights pretrained_model/Shinkai_net_G_float.pth --dynamic
```
