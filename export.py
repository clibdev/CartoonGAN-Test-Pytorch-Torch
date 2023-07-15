import argparse
import os
import torch
from network.Transformer import Transformer
import onnx
from onnxsim import simplify


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--weights', type=str, default='./pretrained_model/Hayao_net_G_float.pth', help='Weights path')
    parser.add_argument('--device', default='cpu', type=str, help='cuda:0 or cpu')
    parser.add_argument('--dynamic', action='store_true', default=False, help='enable dynamic axis in onnx model')
    args = parser.parse_args()

    if not os.path.exists(args.weights):
        print('Cannot find weights: {0}'.format(args.weights))
        exit()

    model = Transformer()
    model.load_state_dict(torch.load(args.weights))
    model = model.to(args.device)
    model.eval()

    model_path = os.path.splitext(args.weights)[0] + '.onnx'

    dummy_input = torch.randn(1, 3, 450, 450).to(args.device)
    dynamic_axes = {'input': {2: '?', 3: '?'}, 'output': {2: '?', 3: '?'}} if args.dynamic else None
    torch.onnx.export(
        model,
        dummy_input,
        model_path,
        verbose=False,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes=dynamic_axes,
        opset_version=17
    )

    model_onnx = onnx.load(model_path)
    if args.dynamic:
        model_onnx, _ = simplify(model_onnx)
    else:
        model_onnx, _ = simplify(model_onnx, tensor_size_threshold='1KB')
    onnx.save(model_onnx, model_path)
