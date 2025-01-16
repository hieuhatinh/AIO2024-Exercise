# Exercise M07W01: UNet Architecture and its applications

## 1. Giới thiệu:
Ngoài ứng dụng của UNet trong phân đoạn (segmentation) ảnh y tế. Các ứng dụng của UNet trong bài tập này sẽ bao gồm: 
- **Super Resolution**: một phương pháp  nhằm tăng độ phân giải của hình ảnh. Phương pháp này có thể cải thiện chất lượng và chi tiết của hình ảnh, thường được áp dụng trong việc nâng cấp hình ảnh cũ, tăng cường hiệu suất giám sát video, và trong nhiều lĩnh vực ứng dụng khác.
- **Image Inpainting**: một phương pháp trong xử lý hình ảnh, được sử dụng để tái tạo hình ảnh bị thiếu một phần hoặc che khuất bằng cách dự đoán các pixel bị thiếu dựa trên thông tin có sẵn trong hình ảnh. Quá trình này có thể được thực hiện trong một hoặc hai giai đoạn. Trong inpainting, thông tin ngữ cảnh xung quanh các pixel bị thiếu là quan trọng để tái tạo hình ảnh một cách chính xác. Một số phương pháp inpainting sử dụng ví dụ hoặc các kỹ thuật khác để điền vào các pixel bị thiếu. Để biểu diễn một hình ảnh màu bị che khuất và mặt nạ (mask), ta thường tạo một hình ảnh kết hợp có bốn kênh, bao gồm hình ảnh gốc và mặt nạ (mask)

Hai bài tập trên sẽ dùng 2 kiến trúc UNet: UNet with Skip Connection và UNet without Skip Connection với mục đích so sánh và tìm hiểu việc Skip Connection có tác động thế nào đối với ảnh đầu ra

## 2. Kiến trúc UNet:
![unet architecture](readme_img/u-net-architecture.png "UNet Architecture")
UNet sử dụng kiến trúc mạng Encoder-Decoder, với mục đích chính của lớp Skip Connection là tạo đường dẫn ngắn từ đầu vào đến đầu ra. Hàm kích hoạt thường được sử dụng là ReLU.
- **Encoder:** phần này hoạt động giống như các mạng CNN, có thể dùng pretrained model như ResNet,... để đưa vào quá trình training. Cứ sau mỗi block, số feature map sẽ tăng lên 2 lần đồng thời height, weight của image giảm xuống 1 nửa nhằm mục đích lấy được thông tin global.

- **Decoder:**    
    - Sau mỗi block, số feature map sẽ giảm 1 nửa đồng thời height, weight tăng lên 2 lần, ngược lại với ***Encoder***
    
    - **UpSample**: Có nhiều cách để UpSample như:

        - ***Upsample Bilinear + Conv*** (cách thường dùng):
            ```
            nn.Sequential(
                nn.UpsamplingBilinear2d(scale_factor=2),
                nn.Conv2d(in_channels, out_channels*2, 1, 1, 0, bias=False),
                nn.BatchNorm2d(out_channels*2),
                nn.LeakyReLU()
            )
            ```
        - ***Pixel Shuffle***: 
            ```nn.PixelShuffle(2)```
        - ***UnPooling***
        - ***Convolution Transpose***: 
            ```
            nn.ConvTranspose2d(
                in_channels,
                out_channels, 
                kernel_size=4, 
                stride=2, 
                padding=1,
                output_padding=0
            )
            ```
    - Layer cuối cùng để ra output cần đi qua hàm Tanh (trong trường hợp range của input là [-1, 1]) hoặc Sigmoid (trong trường hợp range của output là [0, 1]) để chuẩn hóa range của output