# Fork of [CartoonGAN-Test-Pytorch-Torch](https://github.com/Yijunmaverick/CartoonGAN-Test-Pytorch-Torch)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.4. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases). (🔥)
* Model conversion to ONNX format using the [export.py](export.py) file. (🔥)
* [ONNX Simplifier](https://github.com/daquexian/onnx-simplifier) integration in the [export.py](export.py) file.
* Installation with [requirements.txt](requirements.txt) file.
* Minor modifications in the [test.py](test.py) file.
* The following deprecations and errors has been fixed:
  * UserWarning: volatile was removed and now has no effect.
  * FutureWarning: You are using 'torch.load' with 'weights_only=False'.
  * TypeError: can't multiply sequence by non-int of type 'float'.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

| Name               | Model Size (MB) | Link                                                                                                                                                                                                                                     | SHA-256                                                                                                                              |
|--------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| CartoonGAN Hayao   | 42.5<br>42.6    | [PyTorch](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/cartoongan-hayao.pth)<br>[ONNX](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/cartoongan-hayao.onnx)     | 8ab0e492efb3b705487db38679e363dc8b1f016692913bbe100587d695a9e2b5<br>6a581c2c633d0c4b85ec3eb64dbf400220d3da62533532a4eaf5824eae4dfc1a |
| CartoonGAN Hosoda  | 42.5<br>42.6    | [PyTorch](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/cartoongan-hosoda.pth)<br>[ONNX](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/cartoongan-hosoda.onnx)   | c666eea7700864d5972765cc43e926d900174648297bfef494006dc230fd1bf0<br>68fb08fa85f073627efc3148c0653aaf60ca86ba172a7c5586bd271dad47f422 |
| CartoonGAN Paprika | 42.5<br>42.6    | [PyTorch](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/cartoongan-paprika.pth)<br>[ONNX](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/cartoongan-paprika.onnx) | 0629352a54838e56a2ad7fca3e6e51e6889d4338c37469f9ddb43e5929ef9475<br>a66fa539d18a0012c3d45da186e35d07ee9e6923b8519bc48877756b2a5c4ba6 |
| CartoonGAN Shinkai | 42.5<br>42.6    | [PyTorch](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/cartoongan-shinkai.pth)<br>[ONNX](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/cartoongan-shinkai.onnx) | c3547f611e780e79aebde7f7bc2b6c278555d701620f125583d666351044c486<br>c8fd1cf51e3fe084dcc0a6d8e14b25a9148a2b73f1428fd70b71ae76a64c00d2 |

# Inference

```shell
python test.py --model_path pretrained_model --style hayao --input_dir test_img --output_dir test_out --load_size -1
python test.py --model_path pretrained_model --style hosoda --input_dir test_img --output_dir test_out --load_size -1
python test.py --model_path pretrained_model --style paprika --input_dir test_img --output_dir test_out --load_size -1
python test.py --model_path pretrained_model --style shinkai --input_dir test_img --output_dir test_out --load_size -1
```

# Export to ONNX format

```shell
pip install onnx onnxsim
```
```shell
python export.py --weights pretrained_model/cartoongan-hayao.pth --dynamic
python export.py --weights pretrained_model/cartoongan-hosoda.pth --dynamic
python export.py --weights pretrained_model/cartoongan-paprika.pth --dynamic
python export.py --weights pretrained_model/cartoongan-shinkai.pth --dynamic
```
