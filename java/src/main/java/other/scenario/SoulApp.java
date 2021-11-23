package other.scenario;

import other.scenario.controller.AutoLoginController;
import other.scenario.map.ExeAddress;
import other.scenario.service.ImageService;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import other.scenario.util.StartUpExeUtils;

import java.awt.*;

import static other.scenario.service.FightAutoService.soulBack;

/**
 * @Classname TempApp
 * @Description 刷御魂（随机时间）
 * @Date 2021/10/19 22:25
 * @Created by orcakill
 */
/*刷御魂*/
public class SoulApp {
	
	//	记录日志
	public static final Logger logger = LogManager.getLogger (SoulApp.class);

	public static void main (String[] args) throws Exception {
//	     重复 挑战150次
          soulBack (150);
	}
	
}

//	启动模拟器，需要调整成全屏后隐藏到后台
class loginApp {
	public static void main (String[] args) throws Exception {
//	    启动程序
		StartUpExeUtils.startUpExeOnly ("CMD /C " + ExeAddress.exeAddress ());
	}
}

/*拒接协战*/
class RefuseApp {
	//	记录日志
	public static final Logger logger = LogManager.getLogger (RefuseApp.class);
	
	public static void main (String[] args) throws Exception {
		refuse ();
	}
	
	public static void refuse () throws InterruptedException, AWTException {
		for (int i = 0; i <= 150; i++) {
			String file1 = "scenario/temp/御魂/拒接协战";
			ImageService.imagesClickBackNumber (file1, 30, false);
			
		}
	}
}
	
	//	自动登录到御魂界面
	class LoginSoulApp {
	
	}
	
	//	自动登录到御灵界面
	class LoginSpiritApp {
		public static void main (String[] args) throws Exception {
			AutoLoginController.spirit ();
		}
	}
