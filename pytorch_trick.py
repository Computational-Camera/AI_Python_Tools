#image to 4D tensor
image_tensor = (torch.from_numpy(image).permute(2, 0, 1).contiguous()).unsqueeze(0)

#tensor to cuda tensor
tensor_gpu = Variable(tesnor_cpu).cuda(async=True)

#tensor to numpy
data = tensor_gpu.cpu().numpy()
#in case grad use
data = tensor_gpu.detach().cpu().numpy()

