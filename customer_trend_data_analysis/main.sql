SELECT * FROM customer_behavior.customer LIMIT 20;

-- 1st question
select gender,sum(purchase_amount) total_revenue from customer_behavior.customer group by gender
-- 2nd question
select customer_id  from customer_behavior.customer where discount_applied = "Yes" and purchase_amount > (
      SELECT AVG(purchase_amount)
      FROM customer_behavior.customer
  );
  -- 3rd question
select item_purchased , avg(review_rating) from customer_behavior.customer group by item_purchased order by avg(review_rating) desc limit 5
 -- 4th question
select shipping_type , avg(purchase_amount) from customer_behavior.customer where shipping_type in ("Express","Standard") group by shipping_type;
 -- 5th question
 select case when subscription_status ="Yes" then "Subscribed" else "Not-Subscribed" end as isSubscribed,count(customer_id), sum(purchase_amount),avg(purchase_amount) from customer_behavior.customer group by isSubscribed
 -- 6th question
 select item_purchased,sum(case when discount_applied = "Yes" then 1 else 0 end)* 100.0 / count(*) as numberss from customer_behavior.customer group by item_purchased order by numberss desc limit 5
 -- 7th question
 with customer_type as (
 select customer_id,previous_purchases,case when previous_purchases = 1 then "New" when previous_purchases between 1 and 10 then "Returning" else "Loyal" end as customer_segment from customer_behavior.customer
 )
 select customer_segment, count(*) from customer_type group by 
 -- 8th question
 select item_purchased,category,count(customer_id) as total_customer , row_number() over (partition by category order by count(customer_id) desc) as itemrank from customer_behavior.customer group by category,item_purchased
 -- 9th question
 select subscription_status,count(customer_id) as repeat_buyers from customer_behavior.customer where previous_purchases > 5 group by subscription_status
 -- 10th question
 with sum_per_cate as (select age_group , sum(purchase_amount) as total_per_age from customer_behavior.customer group by age_group)
 select age_group,total_per_age,total_per_age *100 / sum(total_per_age) over() as percentage_in_revenue  from sum_per_cate