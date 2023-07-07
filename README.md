# Fork of [CartoonGAN-Test-Pytorch-Torch](https://github.com/Yijunmaverick/CartoonGAN-Test-Pytorch-Torch)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.0. (🔥)
* Original pretrained models from GitHub [releases page](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases). (🔥)
* Installation with [requirements.txt](requirements.txt) file.
* The following deprecations has been fixed:
  * UserWarning: volatile was removed and now has no effect.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

| Name    | Link                                                                                                                 |
|---------|----------------------------------------------------------------------------------------------------------------------|
| Hayao   | [PyTorch](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/Hayao_net_G_float.pth)   |
| Hosoda  | [PyTorch](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/Hosoda_net_G_float.pth)  |
| Paprika | [PyTorch](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/Paprika_net_G_float.pth) |
| Shinkai | [PyTorch](https://github.com/clibdev/CartoonGAN-Test-Pytorch-Torch/releases/latest/download/Shinkai_net_G_float.pth) |

# Inference

```shell
python test.py --model_path pretrained_model --style Hayao --input_dir test_img --output_dir test_out
python test.py --model_path pretrained_model --style Hosoda --input_dir test_img --output_dir test_out
python test.py --model_path pretrained_model --style Paprika --input_dir test_img --output_dir test_out
python test.py --model_path pretrained_model --style Shinkai --input_dir test_img --output_dir test_out
```
