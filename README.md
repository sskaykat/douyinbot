### 抖音视频无水印下载机器人
### Api来自 
[**PearNoDec/DouYinParse**](https://github.com/PearNoDec/DouYinParse)

---
## 运行
*把 config.ini 中的 bot-token 替换成自建的 bot-token*


```
docker  pull taohuajiu/dybot:0.0.1
```

```
docker run -d --name dydownbot -v /dockerapp/douyinbot/config.ini:/dybot/config.ini taohuajiu/dybot:0.0.1
```

