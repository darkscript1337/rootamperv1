# RooTamperV1

2019 yılında bir scriptte SQL açığı buldum, ancak bu scripti kullanan birçok sitede WAF (Web Application Firewall) vardı. Her site için manuel olarak SQL enjeksiyon denemeleri yapmak yerine, bunu SQLMap ile otomatikleştirdim. Ancak, mevcut SQLMap tamper betikleri çok karışıktı ve hangisinin nerede etkili olduğu tam olarak belli değildi. Bu yüzden, order, union, and, select gibi anahtar SQL ifadelerini bypass etmek için belirli tekniklerle müdahale eden bu özel tamper betiğini yazdım.

# Özellikler:
UNION SELECT ifadesi için farklı bypass tekniklerini kullanır.
ORDER BY, AND, ve SELECT gibi kritik SQL ifadelerini hedef alarak bypass sağlar.
Hedef sitelerdeki WAF'ları atlatmak için rastgele ve belirli bypass yöntemlerini dener.
SQLMap'in tamper klasörüne ekleyerek kolayca kullanabilirsiniz.
