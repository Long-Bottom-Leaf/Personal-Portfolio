package com.keyin.warehouseinventorysystem.datastructures;

import com.keyin.warehouseinventorysystem.models.Order;

public class OrderNode {

    public Order data;
    public OrderNode left, right;

    public OrderNode(Order data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
