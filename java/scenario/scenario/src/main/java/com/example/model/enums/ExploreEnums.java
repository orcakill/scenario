package com.example.model.enums;

/**
 * @author orcakill
 * @version 1.0.0
 * @ClassName ExploreEnums.java
 * @Description 探索枚举
 * @createTime 2022年11月11日 08:35:00
 */
public enum ExploreEnums {
	explore_ZHYZ ("scenario/探索/困28"),
	explore_TS ("scenario/探索/探索"),
	explore_ZDLH("scenario/探索/自动轮换"),
	explore_XGZD("scenario/探索/小怪战斗"),
	explore_BOSSZD("scenario/探索/boss战"),
	explore_TCTZ("scenario/御魂/退出挑战"),
	explore_EWJL("scenario/探索/额外奖励"),
	explore_ZCBX("scenario/探索/左侧宝箱"),
	explore_QR("scenario/探索/确认"),
	explore_ZJFH("scenario/探索/章节返回"),
	explore_TSSSL("scenario/探索/探索界面式神录"),
	;
	
	
	
	ExploreEnums (String value) {
		this.value = value;
	}
	
	private final String value;
	
	public String getValue() {
		return value;
	}
}
