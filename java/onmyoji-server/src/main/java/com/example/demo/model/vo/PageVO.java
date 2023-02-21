package com.example.demo.model.vo;

import lombok.Builder;
import lombok.Data;

import java.util.List;

/**
 * @Classname PageVO
 * @Description 储存分页信息
 * @Date 2023/1/24 19:41
 * @Created by orcakill
 */
@Data
@Builder
public class PageVO<T> {
  protected List<T> records;
  protected long total;
  protected long size;
  protected long current;
}

