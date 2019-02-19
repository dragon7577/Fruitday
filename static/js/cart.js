// 所有的获取操作都要等待文档加载完毕后执行
$(function(){
    // 更新工具栏中的数量与价格
    countItem();
    // 1.全选与取消全选
    var isTrue = false;
    $("#checkall").click(function(){
        // 更改状态标识
        // 将取反值重新赋值给变量
        isTrue = !isTrue;
        if(isTrue){
            $("[name=check]").prop("checked","true");
            // 商品全选后,更新数量与价格
            countItem();
        }else{
            // $("[name=check]").prop("checked","false");
            $("[name=check]").removeAttr("checked")
            // 取消全选后也要重新统计,可以直接写在if语句外面
            countItem();

        }
    });

    // 2.反选
    /*
    onchange事件 判断两次内容是否一致
    输入框监听,判断两次输入是否一致
    按钮监听,表示选中与取消状态改变
    */
    $("[name=check]").change(function(){
        // 判断商品复选框未被选中的按钮数量 若<=0,则说明全选,需要更改checkall的选择状态
        // JS中的选择器::eq :not()
        // jQuery中:eq(index)  根据下标获取元素
        // not("")  获取元素,否定条件
        // input:checked 匹配被选中的输入框 
        // size()   获取数组长度,元素个数
        // 判断是否全选
        var isAll = $("[name=check]").not("input:checked").size() <= 0;
        if(isAll){
            // 修改全选按钮
            $("#checkall").prop("checked","true")
            // 修改全选的状态表示
            isTrue = true;
        }else{
            $("#checkall").removeAttr("checked");
            isTrue = false;
        }
        // 更新数量与价格
        countItem();
    });

    // 3.数量加减,价格联动
    $(".decrement").click(function(){
        // 判断输入框当前数量是否大于1,如果大于1,做--运算
        if($(this).next().val() > 1){
            // 值的--必须要时数值
            var value = $(this).next().val();
            $(this).next().val(--value); // 自动类型转换
            // 价格联动
            // 获取单价 &yen;188  
            var priceStr = $(this).parent().prev().html();
            // 截取字符串转为Number  substing范围[start,end) 注意&yen;是一个字符
            var price = Number(priceStr.substring(1,priceStr.length));
            // 修改总价
            $(this).parent().next().html("<b>&yen;"+price * value +"</b>");
        }
        countItem();
    });

    $(".increment").click(function(){
        var value = $(this).prev().val();
        $.ajax({
            url:'/cart/increments/',
            type:'get',
            data:$(this).prev().val(++ value),
            dataType:'json',
            async:true,
            success:function (data) {
                $(this).prev().val(data)
            }
        })

        // 价格联动
        // 获取单价 &yen;188  
        var priceStr = $(this).parent().prev().html();
        // 截取字符串转为Number  substing范围[start,end) 注意&yen;是一个字符
        var price = Number(priceStr.substring(1,priceStr.length));
        // 修改总价
        $(this).parent().next().html("<b>&yen;"+price * value +"</b>");
        countItem();
    });

    // 监听输入框
    $("[name=countText]").blur(function(){
        // 获取输入的值,更改总价
        var count = Number($(this).val());
        // 价格联动
        // 获取单价 &yen;188  
        var priceStr = $(this).parent().prev().html();
        // 截取字符串转为Number  substing范围[start,end) 注意&yen;是一个字符
        var price = Number(priceStr.substring(1,priceStr.length));
        // 修改总价
        $(this).parent().next().html("<b>&yen;"+price * count +"</b>");
        countItem();
    })

    // 4.移除商品
    $(".action a").click(function(){
        // 删除整条商品记录 .g-item,根据层级结构获取
        // $(this).parent().parent  当层级元素较多时不适用
        $(this).parents(".g-item").remove();
    })

    // 5. 工具栏中数量与价格的联动
    function countItem(){
        var sum = 0;  // 勾选的商品总数
        var priceSum = 0; // 对应的总价格
        /*
        1.遍历所有被勾选的元素
        2.获取被勾选元素中的数量与小计
        3.累加并显示在工具栏
        */
        // 匹配所有被选中的复选框
        $("[name=check]:checked").each(function(){
            sum += Number($(this).parents(".g-item").find("[name=countText]").val());
            // 实际上取的是b标签的内容
            var priceStr = $(this).parents(".g-item").find(".t-sum b").html();
            var price = Number(priceStr.substring(1,priceStr.length));
            // 价格的累加
            priceSum += price;
        })
        // 在工具栏显示价格
        $(".submit-count span").html(sum);
        $(".submit-price span").html("&yen;"+priceSum);
    }
})