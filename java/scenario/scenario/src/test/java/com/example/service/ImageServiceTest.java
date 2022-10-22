package com.example.service;

import com.example.model.entity.PictureIdentifyWorkPO;
import com.example.util.ComputerScaling;
import com.example.util.ImagesBackRec;
import com.example.util.MouseClick;
import com.example.util.StartUpExeUtils;
import junit.framework.TestCase;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.awt.*;
import java.io.File;

import org.junit.Test;

import static com.example.service.FightService.soulBack;

/**
 * @Classname ImageServiceTest
 * @Description TODO
 * @Date 2022/8/6 21:12
 * @Created by orcakill
 */
public class ImageServiceTest {
	
	public static final Logger logger = LogManager.getLogger ("ImageServiceTest ");
	
	public static boolean b1 = true;//是否开启测试
	
	@Test
	public void testImagesClick1 () throws InterruptedException, AWTException {
		double bl = ComputerScaling.getScale ();
		if (b1) {
			logger.info ("准备开始");
			Thread.sleep (5000);
			for (int i = 0; i < 10; i++) {
				String folderName = "scenario/首页/首页勾玉";
				File file = new File (
						System.getProperty ("user.dir") + "/src/main/resources/image/" + folderName);
				if (file.exists ()) {
					PictureIdentifyWorkPO pictureIdentifyWorkPO1 = ImagesBackRec.imagesRecognitionMouse (folderName,
							"夜神模拟器");
					logger.info ("初始图片x坐标：" + pictureIdentifyWorkPO1.getX () + "    初始y坐标" + pictureIdentifyWorkPO1.getY ());
					Point point = MouseInfo.getPointerInfo ()
					                       .getLocation ();
					logger.info ("当前x坐标：" + point.getX () * bl + "    当前y坐标" + point.getY () * bl / 1.1);
					double x = point.getX () * bl / pictureIdentifyWorkPO1.getX ();
					double y = point.getY () * bl / pictureIdentifyWorkPO1.getY ();
					logger.info ("当前x系数：" + x + "    当前y系数" + y);
				}
				else {
					System.out.println ("图片文件路径不存在");
				}
			}
		}
	}
	
	@Test
	public void testImagesClick2 () throws InterruptedException, AWTException {
		double bl = ComputerScaling.getScale ();
		String file1 = "scenario/寄养/好友标题";
		logger.info ("准备开始");
		if (b1) {
			Thread.sleep (5000);
			for (int i = 0; i < 10; i++) {
				File file = new File (
						System.getProperty ("user.dir") + "/src/main/resources/image/" + file1);
				if (file.exists ()) {
					PictureIdentifyWorkPO pictureIdentifyWorkPO1 = ImagesBackRec.imagesRecognitionMouse (file1,
							"夜神模拟器");
					logger.info ("初始图片x坐标：" + pictureIdentifyWorkPO1.getX () + "    初始y坐标" + pictureIdentifyWorkPO1.getY ());
					PictureIdentifyWorkPO pictureIdentifyWorkPO2 = new PictureIdentifyWorkPO ();
					pictureIdentifyWorkPO2.setX ((int) (pictureIdentifyWorkPO1.getX () * 1.0));
					pictureIdentifyWorkPO2.setY ((int) (pictureIdentifyWorkPO1.getY () * 1.6));
					PictureIdentifyWorkPO pictureIdentifyWorkPO3 = new PictureIdentifyWorkPO ();
					pictureIdentifyWorkPO3.setX ((int) (pictureIdentifyWorkPO1.getX () * 1.0));
					pictureIdentifyWorkPO3.setY ((int) (pictureIdentifyWorkPO1.getY () * 2.3));
					ImageService.imagesClickBackDrag (pictureIdentifyWorkPO2, pictureIdentifyWorkPO1, "夜神模拟器");
				}
				else {
					System.out.println ("图片文件路径不存在");
				}
			}
		}
	}
	
	@Test
	public void testImagesClick3 () throws InterruptedException, AWTException {
		double bl = ComputerScaling.getScale ();
		logger.info ("准备开始");
		if (b1) {
			Thread.sleep (5000);
			for (int i = 0; i < 1; i++) {
				Point point = MouseInfo.getPointerInfo ()
				                       .getLocation ();
				logger.info ("当前x坐标：" + point.getX () * bl + "    当前y坐标" + point.getY () * bl);
				MouseClick.mouseClickBack (point.getX () * bl, point.getY () * bl, "夜神模拟器");
			}
		}
	}
	
	@Test
	public void testImagesClick4 () throws InterruptedException, AWTException {
		double bl = ComputerScaling.getScale ();
		logger.info ("准备开始");
		if (b1) {
			Thread.sleep (5000);
			for (int i = 0; i < 1; i++) {
				MouseClick.mouseClickBack (964, 326, "夜神模拟器");
			}
		}
	}
	
	//重复挑战
	@Test
	public void testImagesClick5 () throws InterruptedException, AWTException {
		logger.info ("准备开始");
		if (b1) {
			Thread.sleep (5000);
			soulBack (6, 150);
		}
	}
	
	//好友邀请超鬼王
	@Test
	public void testImagesClick6 () throws InterruptedException, AWTException {
		logger.info ("准备开始");
		String file_YXXX = "scenario/活动/20221019/御香寻行";
		boolean boolean_YXXX = false;
		String file_JJ = "scenario/活动/20221019/集结";
		boolean boolean_JJ = false;
		String file_HY = "scenario/活动/20221019/好友";
		boolean boolean_HY = false;
		String file_YQ = "scenario/活动/20221019/邀请";
		boolean boolean_YQ = false;
		if (b1) {
			for (int i = 1; i <= 60; i++) {
				logger.info ("判断是否有御香寻行，有则点击寻找超鬼王");
				boolean_YXXX = ImageService.imagesClickBackIsEmpty (file_YXXX, 5);
				if (boolean_YXXX) {
					ImageService.imagesClickBack (file_YXXX);
					Thread.sleep (5000);
					logger.info ("判断是否有集结,有则准备点击集结");
					boolean_JJ = ImageService.imagesClickBackIsEmpty (file_JJ, 5);
					if (boolean_JJ) {
						ImageService.imagesClickBack (file_JJ);
					}
					Thread.sleep (2000);
					logger.info ("判断是否有好友,有则准备点击好友邀请");
					boolean_HY = ImageService.imagesClickBackIsEmpty (file_HY, 5);
					if (boolean_HY) {
						ImageService.imagesClickBack (file_HY);
					}
					Thread.sleep (2000);
					logger.info ("判断是否有邀请,有则准备点击邀请");
					boolean_YQ = ImageService.imagesClickBackIsEmpty (file_YQ, 5);
					if (boolean_YQ) {
						ImageService.imagesClickBack (file_YQ);
					}
				}
				logger.info ("等待一分钟");
				Thread.sleep (60 * 1000);
			}
		}
	}
	
}