package com.example.demo.service.impl;



import com.example.demo.model.entity.EmailBoxPO;
import com.example.demo.model.entity.MessageEventPO;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

import static com.example.demo.utils.SendMail.sendTextMail;

/**
 * @Classname MailServiceImpl
 * @Description MailServiceImpl
 * @Date 2022/8/8 1:34
 * @Created by orcakill
 */
public class MailServiceImpl {
	
	
	public  static List<EmailBoxPO>  messageToEmail (List<MessageEventPO> messageEventPOList){
		List<EmailBoxPO> emailBoxPOList=new ArrayList<> ();
		for (MessageEventPO messageEventPO : messageEventPOList) {
			EmailBoxPO emailBoxPO = new EmailBoxPO ();
			emailBoxPO.setSender ("orcakill@163.com");
			emailBoxPO.setReceiver ("orcakill@dingtalk.com");
			emailBoxPO.setTitle (messageEventPO.getMessageTitle ());
			emailBoxPO.setContent (messageEventPO.getMessageContent ());
			emailBoxPOList.add (emailBoxPO);
		}
		return  emailBoxPOList;
	}
	
	public static void sendMail () {
		Calendar calendar = Calendar.getInstance ();
		Date date = new Date ();
		calendar.setTime (date);
		List<MessageEventPO> messageEventPOList = new ArrayList<> ();
		MessageEventPO messageEventPO = new MessageEventPO ();
		messageEventPO.setMessageDate (date);
		messageEventPO.setMessageTitle ("结束");
		messageEventPO.setMessageContent ("程序运行结束");
		messageEventPO.setMessageType (0);
		messageEventPOList.add (messageEventPO);
		List<EmailBoxPO> emailBoxPOList = messageToEmail (messageEventPOList);
		for (EmailBoxPO emailBoxPO : emailBoxPOList) {
			sendTextMail (emailBoxPO);
		}
	}
}
