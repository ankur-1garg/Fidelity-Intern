WITH pending_orders AS (
    SELECT 
        c.customerNumber,
        c.customerName,
        CONCAT(c.contactFirstName, ' ', c.contactLastName) as contact_name,
        c.phone,
        CONCAT(c.addressLine1, 
               CASE WHEN c.addressLine2 IS NOT NULL 
                    THEN CONCAT(', ', c.addressLine2) 
                    ELSE '' 
               END,
               ', ', c.city,
               CASE WHEN c.state IS NOT NULL 
                    THEN CONCAT(', ', c.state) 
                    ELSE '' 
               END,
               ', ', c.country) as full_address,
        o.orderNumber,
        DATE_FORMAT(o.orderDate, '%Y-%m-%d') as order_date,
        DATE_FORMAT(o.requiredDate, '%Y-%m-%d') as required_date,
        SUM(od.quantityOrdered * od.priceEach) as order_value
    FROM fil.customers c
    INNER JOIN fil.orders o ON c.customerNumber = o.customerNumber
    INNER JOIN fil.orderdetails od ON o.orderNumber = od.orderNumber
    WHERE o.status = 'Pending'
    GROUP BY 
        c.customerNumber, c.customerName, c.contactFirstName, c.contactLastName,
        c.phone, c.addressLine1, c.addressLine2, c.city, c.state, c.country,
        o.orderNumber, o.orderDate, o.requiredDate
)
SELECT 
    customerNumber,
    customerName,
    contact_name,
    phone,
    full_address,
    COUNT(orderNumber) as pending_order_count,
    SUM(order_value) as total_pending_value,
    MIN(order_date) as oldest_pending_order,
    MIN(required_date) as earliest_delivery_due
FROM pending_orders
GROUP BY 
    customerNumber, customerName, contact_name,
    phone, full_address
HAVING pending_order_count > 0
ORDER BY pending_order_count DESC, total_pending_value DESC