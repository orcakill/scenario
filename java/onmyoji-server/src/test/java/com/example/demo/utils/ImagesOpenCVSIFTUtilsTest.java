package com.example.demo.utils;

import com.example.demo.model.entity.PictureCollectionPO;
import com.example.demo.model.entity.PictureIdentifyWorkPO;
import com.example.demo.model.map.FolderPathMap;
import lombok.extern.log4j.Log4j2;
import org.junit.jupiter.api.Test;
import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;
import org.springframework.boot.test.context.SpringBootTest;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.List;

import static com.example.demo.model.var.CommVar.ghost_WXZ;
import static com.example.demo.utils.ImagesOpenCVSIFTUtils.getMat;

/**
 * @Classname ImagesOpenCVSIFTUtilsTest
 * @Description SIFT 算法测试类
 * @Date 2023/2/21 1:41
 * @Created by orcakill
 */
@SpringBootTest
@Log4j2
class ImagesOpenCVSIFTUtilsTest {
	
	/***
	 * @description: 测试算法 单次执行速度
	 * @return: void
	 * @author: orcakill
	 * @date: 2023/2/23 15:25
	 */
	@Test
	void findAllImgDataOpenCvAll () throws AWTException, IOException {
		long startTime = System.currentTimeMillis ();
		System.setProperty ("java.awt.headless", "false");
		System.loadLibrary (Core.NATIVE_LIBRARY_NAME);
		log.info ("测试开始");
		//来源图片
		BufferedImage Window = ScreenshotUtils.screenshotBack ("夜神模拟器");
		Mat originalImage = getMat (Window);
		Imgcodecs.imwrite ("D:\\source.jpg", originalImage);
		//String str_tem = "D:/a.jpg";
		//File file_tem = new File (str_tem);
		//BufferedImage Window = ImageIO.read (file_tem);
		//图片集
		long startTime1 = System.currentTimeMillis ();
		String path = FolderPathMap.folderPath ("图片总路径");
		List<PictureCollectionPO> pictureCollectionPOList =
				ReadFileUtils.readPictureCollectionPOList (path,ghost_WXZ, "SIFT");
		log.info ("图像录入用时{}毫秒", System.currentTimeMillis () - startTime1);
		//屏幕截图和图片对比
		List<PictureIdentifyWorkPO> mouseXY = ImagesOpenCVSIFTUtils.findPictureIdentifyWorkPOList (Window, pictureCollectionPOList, 0.7,
		                                                               5,true);
		log.info ("图像识别，用时{}毫秒", System.currentTimeMillis () - startTime1);
		assert mouseXY != null;
		MouseClickUtils.mouseClickBack (mouseXY, "谷歌浏览器", true);
		log.info ("测试结束");
		log.info ("图像识别点击用时{}毫秒", System.currentTimeMillis () - startTime);
	}
	
	/***
	 * @description: 测试算法 多次执行速度
	 * @return: void
	 * @author: orcakill
	 * @date: 2023/2/23 15:25
	 */
	@Test
	void findAllImgDataOpenCvAllS () throws AWTException, IOException {
		long startTime = System.currentTimeMillis ();
		System.setProperty ("java.awt.headless", "false");
		System.loadLibrary (Core.NATIVE_LIBRARY_NAME);
		log.info ("测试开始");
		int num=10;
		for(int i=1;i<num;i++){
			findAllImgDataOpenCvAll();
		}
		log.info ("测试结束");
		log.info ("用时{}毫秒", System.currentTimeMillis () - startTime);
		log.info ("平均用时{}毫秒", (System.currentTimeMillis () - startTime)/10);
	}
}