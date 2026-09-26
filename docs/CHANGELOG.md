# Список изменений maERP

Секции переносятся сюда из общего макета `ОписаниеИзменений` при публикации CF
(правило в `docs/RELEASING.md`). Внутри релиза секции идут по сборкам, от новых
к старым, на всех языках конфигурации — ровно так, как их видел владелец в окне
«Что нового».

# Релиз 2.0.14.26 (2026-09-08)

Поставка: `maERP-2.0.14.26.cf`; обновление с 1.0.11.1, 2.0.12.14, 2.0.12.17,
2.0.12.18 и 2.0.14.3 — `maERP-2.0.14.26.cfu`. Меню «Главное» и раздел «Настройка»
по образцу УНФ, панель настроек по блокам, автотесты документов уровня 3.

## 2.0.14.26
### ru
- Выпуск продукции и поступление из переработки: устранена вторая неоднозначность в запросе коэффициентов техкарт, проведение проходит.
### fr
- Production et réception de sous-traitance : seconde ambiguïté supprimée dans la requête des coefficients de nomenclature, la validation passe.
### en
- Production output and receipt from processing: the second ambiguity in the tech card coefficient query is removed, posting succeeds.
### es
- Producción y recepción de maquila: eliminada la segunda ambigüedad en la consulta de coeficientes de fichas técnicas, la contabilización pasa.

## 2.0.14.25
### ru
- Исправлено проведение выпуска продукции и поступления из переработки: расчёт коэффициентов техкарт падал на неоднозначном поле запроса.
- Реализация по заказу и заказ покупателя: статус заказа, записанный в ту же секунду, что и предыдущий, больше не обрывает запись ошибкой дублирующего ключа истории статусов.
### fr
- Corrigée la validation de la production et de la réception de sous-traitance : le calcul des coefficients de nomenclature échouait sur un champ de requête ambigu.
- Vente sur commande et commande client : un statut de commande enregistré la même seconde que le précédent n'interrompt plus l'enregistrement par une erreur de clé en double dans l'historique des statuts.
### en
- Fixed posting of production output and receipt from processing: the tech card coefficient calculation failed on an ambiguous query field.
- Sale by order and customer order: an order status written in the same second as the previous one no longer aborts saving with a duplicate key error in the status history.
### es
- Corregida la contabilización de la producción y la recepción de maquila: el cálculo de coeficientes de fichas técnicas fallaba por un campo ambiguo de la consulta.
- Venta por pedido y pedido de cliente: un estado de pedido registrado en el mismo segundo que el anterior ya no interrumpe el guardado con un error de clave duplicada en el historial de estados.

## 2.0.14.24
### ru
- Автотесты документов: тестовый договор создаётся с описанием, а не наименованием (у договоров наименование отключено); прогон уровня 3 снова проходит стадию подготовки данных.
### fr
- Autotests des documents : le contrat de test est créé avec une description et non un nom (le nom est désactivé pour les contrats) ; le passage de niveau 3 franchit de nouveau la préparation des données.
### en
- Document autotests: the test contract is created with a description instead of a name (names are disabled for contracts); the level 3 run passes data preparation again.
### es
- Autotests de documentos: el contrato de prueba se crea con descripción y no con nombre (el nombre está desactivado en contratos); la ejecución de nivel 3 vuelve a superar la preparación de datos.

## 2.0.14.23
### ru
- Исправлена ошибка применения отрасли «Строительство»: реквизит «Площадь» не записывался из-за типа шире, чем у плана видов характеристик; типы реквизитов приведены к типу плана.
### fr
- Corrigée l'erreur d'application du secteur « Construction » : l'attribut « Surface » ne s'enregistrait pas à cause d'un type plus large que celui du plan des types de caractéristiques ; types alignés sur le plan.
### en
- Fixed applying the "Construction" industry: the "Surface" attribute failed to save because its type was wider than the chart of characteristic types allows; attribute types aligned with the chart.
### es
- Corregido el error al aplicar el sector «Construcción»: el atributo «Superficie» no se guardaba por un tipo más amplio que el del plan de tipos de características; tipos alineados con el plan.

## 2.0.14.22
### ru
- Настройка → Компания и учёт: смена отрасли перенастраивает базу как при первом запуске (заводит отраслевые реквизиты номенклатуры) после предупреждения об опасной операции.
- Меню «Настройка»: «Общее» первым в группе «Настройки программы», регламентные задания только со страницы «Обслуживание»; в группе «Оборудование» убраны повторы «Подключаемое оборудование» и «Драйверы оборудования».
- Исправлена ошибка открытия карточки номенклатуры «Неоднозначное поле Представления.Ссылка».
### fr
- Paramètres → Entreprise et comptabilité : changer de secteur reconfigure la base comme au premier lancement (attributs d'articles du secteur) après un avertissement sur l'opération risquée.
- Menu « Paramètres » : « Général » en premier dans « Paramètres du programme », les tâches réglementaires uniquement depuis la page « Maintenance » ; doublons « Matériel enfichable » et « Pilotes matériels » retirés du groupe « Matériel ».
- Corrigée l'erreur d'ouverture de la fiche article « Champ ambigu Представления.Ссылка ».
### en
- Settings → Company and accounting: changing the industry reconfigures the database as at first start (industry item attributes) after a warning about the risky operation.
- "Settings" menu: "General" first in "Program settings", scheduled jobs only from the "Maintenance" page; duplicate "Connected equipment" and "Equipment drivers" removed from the "Equipment" group.
- Fixed the item card opening error "Ambiguous field Представления.Ссылка".
### es
- Configuración → Empresa y contabilidad: cambiar el sector reconfigura la base como en el primer inicio (atributos de artículos del sector) tras una advertencia sobre la operación peligrosa.
- Menú «Configuración»: «General» primero en «Ajustes del programa», tareas programadas solo desde la página «Mantenimiento»; eliminados los duplicados «Equipo conectable» y «Controladores de equipos» del grupo «Equipo».
- Corregido el error al abrir la ficha de artículo «Campo ambiguo Представления.Ссылка».

## 2.0.14.21
### ru
- Автотесты проверяют панель настроек: запись настройки, признак включения раздела, список часовых поясов, заголовок окна.
- Значки разделов собираются из исходников `design/icons` одним скриптом; добавлен значок раздела «Главное».
### fr
- Les tests automatiques vérifient le panneau de paramètres : enregistrement d'un paramètre, indicateur d'activation de section, liste des fuseaux horaires, titre de la fenêtre.
- Les icônes des sections sont assemblées depuis les sources `design/icons` par un seul script ; ajout de l'icône de la section « Principal ».
### en
- Automated tests check the settings panel: saving a setting, the section-enabling flag, the time zone list, the window title.
- Section icons are built from the `design/icons` sources by one script; the "Main" section icon is added.
### es
- Las pruebas automáticas verifican el panel de configuración: guardado de un ajuste, indicador de activación de sección, lista de zonas horarias, título de la ventana.
- Los iconos de las secciones se generan desde las fuentes `design/icons` con un solo script; se añadió el icono de la sección «Principal».

## 2.0.14.20
### ru
- Раздел «Сервис» переименован в «Настройка» и перестроен: сверху пользователи, подключаемое оборудование и смена пароля, ниже группы «Настройки программы», «Пользователи и права» и «Оборудование» (рабочие места, драйверы). Группы «Предприятие», «Управление данными» и «Настройки пользователей и прав» упразднены, инструменты администратора открываются со страницы «Обслуживание». Пустые пункты «Фискальные регистраторы» и «Эквайринговые терминалы» из меню убраны.
### fr
- La section « Service » est renommée « Paramètres » et réorganisée : en haut les utilisateurs, le matériel connecté et le changement de mot de passe, en dessous les groupes « Paramètres du programme », « Utilisateurs et droits » et « Matériel » (postes de travail, pilotes). Les groupes « Entreprise », « Gestion de données » et « Paramètres utilisateur et droits » sont supprimés, les outils d'administration s'ouvrent depuis la page « Maintenance ». Les entrées vides « Registres fiscaux » et « Terminaux d'acquisition » sont retirées du menu.
### en
- The "Service" section is renamed "Settings" and reorganized: users, connected equipment and password change at the top, then the groups "Program settings", "Users and rights" and "Equipment" (workplaces, drivers). The groups "Company", "Data management" and "User settings and rights" are dissolved; admin tools open from the "Maintenance" page. The empty "Fiscal registers" and "Acquiring terminals" entries are removed from the menu.
### es
- La sección «Servicio» se renombró «Configuración» y se reorganizó: arriba usuarios, equipo conectado y cambio de contraseña; debajo los grupos «Configuración del programa», «Usuarios y derechos» y «Equipo» (puestos de trabajo, controladores). Los grupos «Compañía», «Gestión de datos» y «Parámetros de usuario y derechos» se suprimieron; las herramientas de administración se abren desde la página «Mantenimiento». Las entradas vacías «Registros fiscales» y «Terminales de adquisición» se quitaron del menú.

## 2.0.14.19
### ru
- Настройки программы: добавлены формы «Номенклатура», «Дополнительные реквизиты», «Продажи», «Закупки», «Производство», «Зарплата и кадры», «Обслуживание». Старая форма «Параметры» с закладками удалена, константы больше не выводятся отдельными командами в меню. Настройки «Печатать накладную (розница)», «Оповещать за кол. дней до запрета отгрузок» и «Страна производственного календаря» впервые доступны из интерфейса.
### fr
- Paramètres du programme : ajout des formulaires « Articles », « Attributs supplémentaires », « Ventes », « Achats », « Production », « Paie et personnel », « Maintenance ». L'ancien formulaire « Paramètres » à onglets est supprimé, les constantes ne figurent plus comme commandes séparées dans le menu. Les paramètres « Imprimer le bon de livraison (détail) », « Prévenir N jours avant le blocage des expéditions » et « Pays du calendrier de production » sont pour la première fois accessibles depuis l'interface.
### en
- Program settings: added the forms "Items", "Additional attributes", "Sales", "Purchases", "Production", "Payroll and HR", "Maintenance". The old tabbed "Parameters" form is removed and constants no longer appear as separate menu commands. The settings "Print delivery note (retail)", "Warn N days before the shipment ban" and "Production calendar country" are available from the interface for the first time.
### es
- Configuración del programa: se añadieron los formularios «Artículos», «Atributos adicionales», «Ventas», «Compras», «Producción», «Nómina y personal», «Mantenimiento». El antiguo formulario «Parámetros» con pestañas se eliminó y las constantes ya no aparecen como comandos separados en el menú. Las configuraciones «Imprimir albarán (minorista)», «Avisar N días antes del bloqueo de envíos» y «País del calendario de producción» están disponibles desde la interfaz por primera vez.

## 2.0.14.18
### ru
- Настройки программы по блокам: в разделе «Сервис» появилась группа «Настройки программы» с формами «Общее» (заголовок окна, часовой пояс базы с кнопкой применения, время сеанса, файлы, почта рассылки) и «Компания и учёт» (отрасль, валюта учёта, основной склад, автозакрытие периода, календарь, бухгалтерия). Каждое поле сохраняется сразу при изменении, включение бухгалтерии показывает раздел без перезапуска.
- Новая настройка «Часовой пояс базы».
### fr
- Paramètres du programme par blocs : la section « Service » a un groupe « Paramètres du programme » avec les formulaires « Général » (titre de la fenêtre, fuseau horaire de la base avec bouton d'application, heure de la session, fichiers, messagerie d'envoi) et « Entreprise et comptabilité » (secteur, devise comptable, entrepôt principal, clôture automatique, calendrier, comptabilité). Chaque champ est enregistré dès sa modification ; activer la comptabilité affiche la section sans redémarrage.
- Nouveau paramètre « Fuseau horaire de la base ».
### en
- Program settings by blocks: the "Service" section has a "Program settings" group with the forms "General" (window title, database time zone with an apply button, session time, files, mailing account) and "Company and accounting" (industry, accounting currency, main warehouse, automatic period closing, calendar, accounting). Every field is saved as soon as it changes; enabling accounting shows the section without a restart.
- New setting "Database time zone".
### es
- Configuración del programa por bloques: la sección «Servicio» tiene un grupo «Configuración del programa» con los formularios «General» (título de la ventana, zona horaria de la base con botón de aplicación, hora de la sesión, archivos, correo de envío) y «Empresa y contabilidad» (sector, moneda contable, almacén principal, cierre automático del período, calendario, contabilidad). Cada campo se guarda al cambiarlo; activar la contabilidad muestra la sección sin reiniciar.
- Nueva configuración «Zona horaria de la base».

## 2.0.14.17
### ru
- Раздел «Главное»: значок «три точки», в нём организации, структура предприятия, физические лица, ставки НДС, страны, валюты и базовый дашборд; список реализаций из него убран.
- Из раздела «Сервис» ушли операционные справочники: бренды — в «Закупки → Справочники», задачи заказов, виды и настройки заданий — в «Продажи → Работа с покупателями».
### fr
- Section « Principal » : icône « trois points », avec les entreprises, la structure de l'entreprise, les personnes physiques, les taux de TVA, les pays, les devises et le tableau de bord de base ; la liste des ventes en a été retirée.
- Les catalogues opérationnels ont quitté la section « Service » : les marques vont dans « Achats → Catalogues », les tâches des commandes, les types et paramètres des tâches dans « Ventes → Opération de vente ».
### en
- "Main" section: "three dots" icon, containing companies, company structure, individuals, VAT rates, countries, currencies and the basic dashboard; the sales list was removed from it.
- Operational catalogs left the "Service" section: brands go to "Purchases → Reference books", order tasks, task types and task settings to "Sales → Sales operation".
### es
- Sección «Principal»: icono de «tres puntos», con empresas, estructura de la empresa, personas físicas, tipos de IVA, países, monedas y el panel básico; la lista de ventas se quitó de ella.
- Los catálogos operativos salieron de la sección «Servicio»: las marcas van a «Compras → Manuales», las tareas de pedidos, tipos y configuración de tareas a «Ventas → Operación de ventas».

## 2.0.14.16
### ru
- Исправлено открытие карточки номенклатуры: подбор дополнительных реквизитов обращался к несуществующему полю и валил форму с ошибкой.
### fr
- Correction de l'ouverture de la fiche article : la sélection des attributs supplémentaires utilisait un champ inexistant et provoquait une erreur du formulaire.
### en
- Fixed opening the item card: the additional attributes lookup referenced a non-existent field and broke the form with an error.
### es
- Corregida la apertura de la ficha del artículo: la selección de atributos adicionales usaba un campo inexistente y provocaba un error del formulario.

## 2.0.14.15
### ru
- Автотесты: добавлен прогон жизненного цикла документов — закупка, заказ с реализацией и оплатой, возврат от покупателя, выпуск продукции по техкарте, переработка, начисление и выплата зарплаты, безналичные поступление и списание, дополнительные реквизиты и отрасль. Каждый сценарий выполняется в транзакции с откатом и данных базы не меняет.
- Исправлен долг перед переработчиком за услуги в поступлении из переработки: оплата поставщику теперь закрывает его, а не удваивает.
- Смок-тест открывает на образцах и формы для роли ECommerce, формы единицы и упаковки.
### fr
- Tests automatiques : ajout du cycle de vie des documents — achat, commande avec vente et paiement, retour client, production selon la nomenclature, sous-traitance, calcul et paiement des salaires, encaissement et décaissement bancaires, attributs supplémentaires et secteur d'activité. Chaque scénario s'exécute dans une transaction annulée et ne modifie pas les données.
- Correction de la dette envers le sous-traitant pour ses services dans la réception de sous-traitance : le paiement au fournisseur la solde désormais au lieu de la doubler.
- Le test de fumée ouvre aussi sur des exemples les formulaires du rôle ECommerce et les formulaires d'unité et d'emballage.
### en
- Automated tests: added the document life cycle run — purchase, order with sale and payment, customer return, production by the bill of materials, subcontracting, payroll accrual and payment, bank receipt and payment, additional attributes and industry. Each scenario runs in a rolled-back transaction and leaves the data unchanged.
- Fixed the debt to the processor for services in the receipt from processing: a supplier payment now closes it instead of doubling it.
- The smoke test also opens the ECommerce role forms and the unit and package forms on samples.
### es
- Pruebas automáticas: se añadió el ciclo de vida de los documentos: compra, pedido con venta y pago, devolución del cliente, producción según la lista de materiales, subcontratación, cálculo y pago de salarios, cobro y pago bancarios, atributos adicionales y sector. Cada escenario se ejecuta en una transacción revertida y no modifica los datos.
- Corregida la deuda con el subcontratista por sus servicios en la recepción de subcontratación: el pago al proveedor ahora la cierra en lugar de duplicarla.
- La prueba de humo también abre sobre ejemplos los formularios del rol ECommerce y los formularios de unidad y embalaje.

## 2.0.14.14
### ru
- Цены в заказе покупателя подставляются на дату документа, как в остальных документах продаж (раньше — на дату отгрузки).
- В карточке номенклатуры типы «Продукция», «Полуфабрикат» и «Сырьё» предлагаются только при включённом производстве.
- Исправлена выборка цен номенклатуры: цена без характеристики больше не теряется.
### fr
- Dans la commande client, les prix sont repris à la date du document, comme dans les autres documents de vente (auparavant à la date d'expédition).
- Dans la fiche article, les types « Produit fini », « Semi-fini » et « Matière première » ne sont proposés que si la production est activée.
- Correction de la sélection des prix des articles : un prix sans caractéristique n'est plus perdu.
### en
- In the customer order, prices are taken as of the document date, like in the other sales documents (previously as of the shipment date).
- In the item card, the types "Finished product", "Semi-finished product" and "Raw material" are offered only when production is enabled.
- Fixed the item price selection: a price without a characteristic is no longer lost.
### es
- En el pedido del cliente, los precios se toman a la fecha del documento, como en los demás documentos de venta (antes a la fecha de expedición).
- En la ficha del artículo, los tipos «Producto terminado», «Semielaborado» y «Materia prima» se ofrecen solo con la producción activada.
- Corregida la selección de precios de artículos: un precio sin característica ya no se pierde.

## 2.0.14.13
### ru
- Дополнительные реквизиты и сведения: администратор заводит свои поля для номенклатуры без изменения программы (раздел «Сервис → Управление данными → Дополнительные реквизиты»). Поля показываются на закладке «Дополнительно» карточки номенклатуры; заголовки задаются на каждом языке.
- Мастер первого запуска спрашивает отрасль: «Торговля», «Строительство и недвижимость», «Прочее». Для строительства сразу создаются реквизиты объекта недвижимости: признак объекта, этаж, площадь, номер права собственности.
- Отрасль передаётся и при автоматическом развёртывании базы (поле industry начального заполнения).
### fr
- Attributs et informations supplémentaires : l'administrateur ajoute ses propres champs aux articles sans modifier le programme (section « Service → Gestion des données → Attributs supplémentaires »). Les champs apparaissent sur l'onglet « Complément » de la fiche article ; les titres se définissent dans chaque langue.
- L'assistant de premier lancement demande le secteur d'activité : « Commerce », « Immobilier et construction », « Autre ». Pour l'immobilier, les attributs du bien sont créés d'emblée : indicateur de bien immobilier, étage, surface, titre foncier.
- Le secteur est aussi transmis lors du déploiement automatique de la base (champ industry du remplissage initial).
### en
- Additional attributes and information: the administrator adds custom fields to items without changing the application (section "Service → Data management → Additional attributes"). The fields are shown on the "Additional" tab of the item card; titles are set per language.
- The first-launch wizard asks for the industry: "Trade", "Construction and real estate", "Other". For real estate the property attributes are created at once: real estate flag, floor, surface, land title.
- The industry is also passed during automatic database deployment (the industry field of the initial fill).
### es
- Atributos e información adicionales: el administrador añade sus propios campos a los artículos sin modificar el programa (sección «Servicio → Gestión de datos → Atributos adicionales»). Los campos se muestran en la pestaña «Adicional» de la ficha del artículo; los títulos se definen en cada idioma.
- El asistente de primer inicio pregunta el sector de actividad: «Comercio», «Construcción e inmuebles», «Otro». Para inmuebles se crean de inmediato los atributos del bien: indicador de inmueble, piso, superficie, título de propiedad.
- El sector también se transmite en el despliegue automático de la base (campo industry del relleno inicial).

## 2.0.14.12
### ru
- Французский интерфейс выверен: «Место хранения» везде переводится как Entrepôt (раньше — Résidence), «Сумма» — Montant, «Количество» — Quantité, справочник «Номенклатура» — Articles, «Оплачено» — Payé, «Заказ покупателя» — Commande client. Внесено 90 правок из проверки французского языка от 31.08.2026: опечатки, отсутствующие диакритики, кальки с русского.
- Английский и испанский приведены к тем же терминам: Warehouse / Almacén для места хранения, Amount / Importe для суммы, Item(s) / Artículo(s) для номенклатуры.
- Убраны искажённые апострофы (« & apos; ») в бухгалтерских отчётах и макете договора.
### fr
- Interface française révisée : « Lieu de stockage » se traduit partout par Entrepôt (auparavant Résidence), « Montant » remplace « Somme », « Quantité » remplace « Nombre », le catalogue « Articles » remplace « Nomenclature », « Payé » remplace « Pour acquit », « Commande client » remplace « Commande de l'acheteur ». 90 corrections issues de la relecture du 31/08/2026 : fautes de frappe, accents manquants, calques du russe.
- L'anglais et l'espagnol sont alignés sur les mêmes termes : Warehouse / Almacén, Amount / Importe, Item(s) / Artículo(s).
- Les apostrophes déformées (« & apos; ») ont été corrigées dans les rapports comptables et le modèle de contrat.
### en
- French interface reviewed: "Storage location" is now Entrepôt everywhere (was Résidence), "Amount" is Montant, "Quantity" is Quantité, the "Items" catalog is Articles, "Paid" is Payé, "Customer order" is Commande client. 90 corrections from the French review of 31 Aug 2026 applied: typos, missing accents, calques from Russian.
- English and Spanish aligned to the same terms: Warehouse / Almacén for storage location, Amount / Importe for amount, Item(s) / Artículo(s) for items.
- Broken apostrophes ("& apos;") fixed in accounting reports and the contract template.
### es
- Interfaz francesa revisada: «Lugar de almacenamiento» se traduce siempre como Entrepôt (antes Résidence), «Importe» es Montant, «Cantidad» es Quantité, el catálogo «Artículos» es Articles, «Pagado» es Payé, «Pedido del cliente» es Commande client. Se aplicaron 90 correcciones de la revisión del francés del 31/08/2026: erratas, acentos ausentes, calcos del ruso.
- El inglés y el español se alinearon con los mismos términos: Warehouse / Almacén para el lugar de almacenamiento, Amount / Importe para el importe, Item(s) / Artículo(s) para los artículos.
- Se corrigieron los apóstrofos deformados (« & apos; ») en los informes contables y en la plantilla de contrato.

## 2.0.14.11
### ru
- Первый запуск: пароль служебного администратора tinycio-1c больше не задан заранее — он создаётся случайным при первом запуске и показывается один раз на последнем шаге мастера. Сохраните его: повторно он не выводится.
- Новая обработка «Начальное заполнение»: организацию, пользователей и служебного администратора можно завести из файла без мастера первого запуска — так базы клиентов разворачиваются автоматически через tinycio.
- Регламентное задание «Закрытие сеансов» больше не содержит встроенных учётных данных; оно завершает сеансы через администратора кластера.
- В свойствах программы указан поставщик TinyCIO, авторские права и адрес tinycio.com.
### fr
- Premier lancement : le mot de passe de l'administrateur de service tinycio-1c n'est plus prédéfini — il est généré aléatoirement au premier lancement et affiché une seule fois à la dernière étape de l'assistant. Notez-le : il ne sera plus affiché.
- Nouveau traitement « Remplissage initial » : l'organisation, les utilisateurs et l'administrateur de service peuvent être créés à partir d'un fichier sans l'assistant de premier lancement — c'est ainsi que les bases des clients sont déployées automatiquement via tinycio.
- La tâche planifiée « Fermeture des sessions » ne contient plus d'identifiants intégrés ; elle termine les sessions via l'administrateur du cluster.
- Les propriétés du programme indiquent l'éditeur TinyCIO, les droits d'auteur et l'adresse tinycio.com.
### en
- First launch: the password of the service administrator tinycio-1c is no longer preset — it is generated randomly at first launch and shown once on the last step of the wizard. Save it: it is not shown again.
- New data processor "Initial fill": the organization, users and the service administrator can be created from a file without the first-launch wizard — this is how client databases are deployed automatically via tinycio.
- The scheduled job "Close sessions" no longer contains built-in credentials; it terminates sessions via the cluster administrator.
- The application properties now show the vendor TinyCIO, the copyright and the address tinycio.com.
### es
- Primer inicio: la contraseña del administrador de servicio tinycio-1c ya no está predefinida — se genera aleatoriamente en el primer inicio y se muestra una sola vez en el último paso del asistente. Guárdela: no se vuelve a mostrar.
- Nuevo procesamiento «Relleno inicial»: la organización, los usuarios y el administrador de servicio pueden crearse desde un archivo sin el asistente de primer inicio — así se despliegan automáticamente las bases de los clientes a través de tinycio.
- La tarea programada «Cierre de sesiones» ya no contiene credenciales integradas; finaliza las sesiones a través del administrador del clúster.
- En las propiedades del programa figuran el proveedor TinyCIO, los derechos de autor y la dirección tinycio.com.

## 2.0.14.10
### ru
- Исправлено: списки продаж, кассовых ордеров, прочих расходов, сверок и списаний безналичных не открывались после обновления — ошибка в расчёте долга на закладке «Клиент». Списки открываются штатно.
### fr
- Correction : les listes des ventes, des ordres de caisse, des autres dépenses, des réconciliations et des décaissements bancaires ne s'ouvraient plus après la mise à jour — une erreur dans le calcul de la dette sur l'onglet « Client ». Les listes s'ouvrent normalement.
### en
- Fixed: the lists of sales, cash orders, other expenses, reconciliations and outgoing bank payments failed to open after the update — an error in the debt calculation on the "Customer" tab. The lists open normally.
### es
- Corregido: las listas de ventas, órdenes de caja, otros gastos, conciliaciones y pagos bancarios no se abrían tras la actualización — un error en el cálculo de la deuda en la pestaña «Cliente». Las listas se abren con normalidad.

## 2.0.14.9
### ru
- В панелях сведений всех списков знаки фильтров по сумме и долгу теперь показываются как «>», «<» и «=» на любом языке программы (раньше на французском виднелись цифры 0, 1, 2), а знак и поле ввода стоят одной строкой.
- Кнопка сворачивания панели переехала в самый низ панели.
- На закладке «Клиент» выводится карточка контрагента целиком: вид и категория, род деятельности, налоговые номера (NIF, RC, ICE, CIN), тип и условия оплаты, отсрочка, тип цены, кредитный лимит и запрет отгрузок, контактные данные и общий долг.
### fr
- Dans les panneaux d'informations de toutes les listes, les signes des filtres par montant et par dette s'affichent désormais « > », « < » et « = » dans toutes les langues du programme (auparavant, en français, on voyait les chiffres 0, 1, 2), et le signe et le champ de saisie sont sur une seule ligne.
- Le bouton de réduction du panneau est descendu tout en bas du panneau.
- L'onglet « Client » affiche la fiche du tiers en entier : type et catégorie, activité, numéros fiscaux (NIF, RC, ICE, CIN), mode et conditions de paiement, délai, type de prix, limite de crédit et blocage des expéditions, coordonnées et dette totale.
### en
- In the details panels of all lists, the amount and debt filter signs are now shown as ">", "<" and "=" in every program language (previously French showed the numbers 0, 1, 2), and the sign and the input field sit on one line.
- The panel collapse button moved to the very bottom of the panel.
- The "Customer" tab shows the whole counterparty card: kind and category, line of business, tax numbers (NIF, RC, ICE, CIN), payment type and terms, deferral, price type, credit limit and shipment block, contact details and total debt.
### es
- En los paneles de información de todas las listas, los signos de los filtros por importe y por deuda se muestran ahora como «>», «<» y «=» en cualquier idioma del programa (antes en francés se veían los números 0, 1, 2), y el signo y el campo de entrada van en una sola línea.
- El botón para contraer el panel se trasladó a la parte más baja del panel.
- La pestaña «Cliente» muestra la ficha de la contraparte completa: tipo y categoría, actividad, números fiscales (NIF, RC, ICE, CIN), tipo y condiciones de pago, aplazamiento, tipo de precio, límite de crédito y bloqueo de expediciones, datos de contacto y deuda total.

## 2.0.14.8
### ru
- Списки цен и планов переведены на новое оформление: установка цен номенклатуры, установка цен вручную, правило ценообразования и установка плановых показателей. Справа — панель со страницами «Фильтры» и «Детали», под списком — постраничный просмотр по 50 документов.
- На странице «Детали» видно содержимое документа: в установке цен — товары с ценой, при ручной установке — виды цен с ценой, в плановых показателях — сотрудники с планом.
- Этим завершён перевод списков документов на новое оформление: панель сведений, пагинация и колонки без горизонтальной прокрутки теперь во всех разделах программы, кроме кассовой смены и бухгалтерской операции.
### fr
- Les listes de prix et de plans passent à la nouvelle présentation : fixation des prix des articles, saisie manuelle des prix, règle de tarification et fixation des indicateurs prévisionnels. À droite, un panneau avec les pages « Filtres » et « Détails » ; sous la liste, un affichage par pages de 50 documents.
- La page « Détails » montre le contenu du document : pour la fixation des prix, les articles avec leur prix ; pour la saisie manuelle, les types de prix ; pour les indicateurs, les employés avec leur plan.
- Ainsi s'achève le passage des listes de documents à la nouvelle présentation : le panneau d'informations, la pagination et les colonnes sans défilement horizontal sont désormais dans toutes les sections, hormis la journée de caisse et l'opération comptable.
### en
- Price and plan lists moved to the new look: item price setting, manual price setting, pricing rule and target setting. On the right is a panel with the "Filters" and "Details" pages; below the list, paging by 50 documents.
- The "Details" page shows the document contents: items with prices for price setting, price types for manual setting, and employees with their targets for planning.
- This completes moving document lists to the new look: the details panel, pagination and columns without horizontal scrolling are now in every section except the cash session and the accounting entry.
### es
- Las listas de precios y planes pasan al nuevo diseño: fijación de precios de artículos, fijación manual de precios, regla de tarificación y fijación de indicadores previstos. A la derecha, un panel con las páginas «Filtros» y «Detalles»; bajo la lista, paginación de 50 documentos.
- La página «Detalles» muestra el contenido del documento: los artículos con su precio en la fijación de precios, los tipos de precio en la fijación manual y los empleados con su plan en los indicadores.
- Con esto concluye el paso de las listas de documentos al nuevo diseño: el panel de información, la paginación y las columnas sin desplazamiento horizontal están ya en todas las secciones, salvo la jornada de caja y el asiento contable.

## 2.0.14.7
### ru
- Зарплатные и кадровые списки переведены на новое оформление: начисление зарплаты, выплата зарплаты, платёжная ведомость на аванс, кадровый приказ, приказ на начисление-удержание и табель учёта рабочего времени. Справа — панель со страницами «Фильтры» и «Детали», под списком — постраничный просмотр по 50 документов.
- На странице «Детали» виден состав документа по сотрудникам: кто указан в документе и на какую сумму — по начислениям, выплатам и авансам.
### fr
- Les listes de paie et du personnel passent à la nouvelle présentation : calcul de la paie, versement des salaires, bordereau d'acompte, ordre du personnel, ordre de retenue ou de gain et feuille de temps. À droite, un panneau avec les pages « Filtres » et « Détails » ; sous la liste, un affichage par pages de 50 documents.
- La page « Détails » montre le contenu du document par employé : qui figure dans le document et pour quel montant — pour les calculs, les versements et les acomptes.
### en
- Payroll and HR lists moved to the new look: payroll calculation, salary payment, advance payroll sheet, HR order, accrual/deduction order and timesheet. On the right is a panel with the "Filters" and "Details" pages; below the list, paging by 50 documents.
- The "Details" page shows the document contents by employee: who is listed in the document and for how much — for calculations, payments and advances.
### es
- Las listas de nómina y personal pasan al nuevo diseño: cálculo de nómina, pago de salarios, nómina de anticipo, orden de personal, orden de devengo o retención y parte de horas. A la derecha, un panel con las páginas «Filtros» y «Detalles»; bajo la lista, paginación de 50 documentos.
- La página «Detalles» muestra el contenido del documento por empleado: quién figura en el documento y por qué importe — para cálculos, pagos y anticipos.

## 2.0.14.6
### ru
- Производственные списки переведены на новое оформление: выпуск продукции, передача в переработку и поступление из переработки. Справа — панель со страницами «Фильтры» (переработчик, наша компания, склад, ответственный) и «Детали» с составом документа, под списком — постраничный просмотр по 50 документов.
- Суммы и себестоимость в эти списки и в панель сведений не выводятся: оператор производства работает с составом документов, но цен не видит.
### fr
- Les listes de production passent à la nouvelle présentation : sortie de production, transfert en sous-traitance et réception de sous-traitance. À droite, un panneau avec les pages « Filtres » (sous-traitant, notre société, entrepôt, responsable) et « Détails » avec le contenu du document ; sous la liste, un affichage par pages de 50 documents.
- Les montants et le coût de revient n'apparaissent ni dans ces listes ni dans le panneau : l'opérateur de production travaille avec le contenu des documents, mais ne voit pas les prix.
### en
- Production lists moved to the new look: product output, transfer for processing and receipt from processing. On the right is a panel with the "Filters" (processor, our company, warehouse, responsible) and "Details" pages with the document contents; below the list, paging by 50 documents.
- Amounts and cost are shown neither in these lists nor in the panel: the production operator works with document contents but does not see prices.
### es
- Las listas de producción pasan al nuevo diseño: salida de producción, entrega a procesamiento y recepción de procesamiento. A la derecha, un panel con las páginas «Filtros» (procesador, nuestra empresa, almacén, responsable) y «Detalles» con el contenido del documento; bajo la lista, paginación de 50 documentos.
- Los importes y el coste no se muestran ni en estas listas ni en el panel: el operador de producción trabaja con el contenido de los documentos, pero no ve los precios.

## 2.0.14.5
### ru
- Денежные и налоговые списки переведены на новое оформление: поступление и списание безналичных, приходный и расходный кассовые ордера, корректировка долга, сверка взаиморасчётов, прочие расходы и их возврат, налоговые возвраты от покупателя и поставщику. Справа — панель со страницами «Фильтры» (контрагент, наша компания, склад, ответственный), «Контрагент» и «Детали», под списком — постраничный просмотр по 50 документов.
- Из этих списков убрана горизонтальная прокрутка: назначение платежа, статья ДДС, реквизиты платёжного поручения и прочие редко нужные колонки перенесены на страницу «Детали».
- В списке сверок взаиморасчётов сохранена кнопка группового формирования актов.
### fr
- Les listes de trésorerie et de fiscalité passent à la nouvelle présentation : encaissements et décaissements bancaires, entrées et sorties de caisse, correction de dette, réconciliation des comptes, autres dépenses et leur retour, retours fiscaux du client et au fournisseur. À droite, un panneau avec les pages « Filtres » (tiers, notre société, entrepôt, responsable), « Tiers » et « Détails » ; sous la liste, un affichage par pages de 50 documents.
- Le défilement horizontal a disparu de ces listes : l'objet du paiement, le poste de trésorerie, les références de l'ordre de paiement et les autres colonnes rarement utiles sont passés sur la page « Détails ».
- Le bouton de création groupée des actes est conservé dans la liste des réconciliations.
### en
- Cash and tax lists moved to the new look: incoming and outgoing bank payments, cash receipt and payment orders, debt adjustment, settlement reconciliation, other expenses and their return, tax returns from the customer and to the supplier. On the right is a panel with the "Filters" (counterparty, our company, warehouse, responsible), "Counterparty" and "Details" pages; below the list, paging by 50 documents.
- Horizontal scrolling is gone from these lists: payment purpose, cash flow item, payment order details and other rarely needed columns moved to the "Details" page.
- The bulk act creation button is kept in the reconciliation list.
### es
- Las listas de tesorería y fiscalidad pasan al nuevo diseño: cobros y pagos bancarios, órdenes de ingreso y de pago en efectivo, corrección de deuda, conciliación de cuentas, otros gastos y su devolución, devoluciones fiscales del cliente y al proveedor. A la derecha, un panel con las páginas «Filtros» (contraparte, nuestra empresa, almacén, responsable), «Contraparte» y «Detalles»; bajo la lista, paginación de 50 documentos.
- El desplazamiento horizontal desapareció de estas listas: el concepto del pago, la partida de tesorería, los datos de la orden de pago y otras columnas poco necesarias pasaron a la página «Detalles».
- En la lista de conciliaciones se conserva el botón de creación agrupada de actas.

## 2.0.14.4
### ru
- Складские списки переведены на новое оформление: перемещение, оприходование, списание, пересортица, пересчёт товаров, задание на пересчёт, уценка и акт разбора. Справа — скрываемая панель со страницами «Фильтры» (склад, наша компания, ответственный) и «Детали» (реквизиты документа и его состав), под списком — постраничный просмотр по 50 документов.
- В этих списках убрана горизонтальная прокрутка: редко нужные колонки перенесены на страницу «Детали», список открывается на высоту экрана.
### fr
- Les listes d'entrepôt passent à la nouvelle présentation : transfert, mise en stock, sortie, reclassement, recomptage des marchandises, ordre de recomptage, démarque et acte de démontage. À droite, un panneau masquable avec les pages « Filtres » (entrepôt, notre société, responsable) et « Détails » (attributs du document et son contenu) ; sous la liste, un affichage par pages de 50 documents.
- Le défilement horizontal a disparu de ces listes : les colonnes rarement utiles sont passées sur la page « Détails », et la liste s'ouvre sur la hauteur de l'écran.
### en
- Warehouse lists moved to the new look: transfer, stock-in, write-off, re-grading, recount of goods, recount task, markdown and disassembly act. On the right is a collapsible panel with the "Filters" (warehouse, our company, responsible) and "Details" (document attributes and contents) pages; below the list, paging by 50 documents.
- Horizontal scrolling is gone from these lists: rarely needed columns moved to the "Details" page, and the list opens to the screen height.
### es
- Las listas de almacén pasan al nuevo diseño: traslado, entrada en stock, baja, reclasificación, recuento de mercancías, orden de recuento, rebaja y acta de despiece. A la derecha, un panel ocultable con las páginas «Filtros» (almacén, nuestra empresa, responsable) y «Detalles» (atributos del documento y su contenido); bajo la lista, paginación de 50 documentos.
- El desplazamiento horizontal desapareció de estas listas: las columnas poco necesarias pasaron a la página «Detalles» y la lista se abre a la altura de la pantalla.

## 2.0.14.3
### ru
- Исправлено падение программы при открытии списка поступлений: кнопка «Оформить поступление» перенесена из таблицы заказов на саму закладку. Список открывается штатно.
### fr
- Correction du plantage du programme à l'ouverture de la liste des réceptions : le bouton « Créer la réception » a été déplacé du tableau des commandes vers l'onglet lui-même. La liste s'ouvre normalement.
### en
- Fixed the program crash when opening the receipt list: the "Create receipt" button moved from the orders table onto the tab itself. The list opens normally.
### es
- Corregido el fallo del programa al abrir la lista de recepciones: el botón «Crear la recepción» se trasladó de la tabla de pedidos a la propia pestaña. La lista se abre con normalidad.

## 2.0.14.2
### ru
- Списки закупок приведены к новому виду: поступления, заказы поставщикам, возвраты поставщику, налоговые накладные покупки, поступления доп. расходов и предложения поставщиков получили панель сведений (закладки «Фильтры», «Поставщик», «Детали» с составом), сворачивание в значки, пагинацию по 50 документов и колонки без горизонтальной прокрутки.
- В списке поступлений появилась закладка «Заказы поставщикам»: заказы с неполученным остатком видны прямо в списке, и по выделенным одной кнопкой оформляются поступления.
- В списке налоговых накладных покупки добавлена закладка «Поступления»: проведённые поступления без возможности добавления, уже выписанные показываются приглушённо. В сведениях накладной видно поступление-основание, а в сведениях поступления — выписанные по нему накладные и состав.
### fr
- Les listes des achats ont été mises au nouveau format : réceptions, commandes fournisseurs, retours au fournisseur, factures comptables d'achat, réceptions de frais supplémentaires et offres des fournisseurs ont reçu le panneau d'informations (onglets « Filtres », « Fournisseur », « Détails » avec le contenu), la réduction en icônes, la pagination par 50 documents et des colonnes sans défilement horizontal.
- Dans la liste des réceptions est apparu l'onglet « Commandes fournisseurs » : les commandes dont le reste n'est pas reçu sont visibles directement dans la liste, et un seul bouton crée les réceptions pour celles sélectionnées.
- Dans la liste des factures comptables d'achat a été ajouté l'onglet « Réceptions » : les réceptions validées sans possibilité d'ajout, celles déjà facturées s'affichent en grisé. Les informations de la facture montrent la réception d'origine, et celles de la réception — les factures émises et le contenu.
### en
- The purchase lists have been brought to the new look: receipts, supplier orders, returns to supplier, purchase accounting invoices, receipts of additional expenses and supplier offers got the details panel (the "Filters", "Supplier" and "Details" tabs with contents), collapsing into icons, pagination by 50 documents and columns without horizontal scrolling.
- The receipt list has a new "Supplier orders" tab: orders with an outstanding balance are visible right in the list, and one button creates receipts for the selected ones.
- The purchase accounting invoice list has a new "Receipts" tab: posted receipts with no way to add, and already invoiced ones shown dimmed. The invoice details show the source receipt, and the receipt details show the invoices issued for it and its contents.
### es
- Las listas de compras se han llevado al nuevo aspecto: recepciones, pedidos a proveedores, devoluciones al proveedor, facturas contables de compra, recepciones de gastos adicionales y ofertas de proveedores recibieron el panel de información (pestañas «Filtros», «Proveedor» y «Detalles» con el contenido), la contracción en iconos, la paginación por 50 documentos y columnas sin desplazamiento horizontal.
- En la lista de recepciones apareció la pestaña «Pedidos a proveedores»: los pedidos con saldo pendiente se ven directamente en la lista, y un solo botón crea las recepciones para los seleccionados.
- En la lista de facturas contables de compra se añadió la pestaña «Recepciones»: las recepciones validadas sin posibilidad de añadir, y las ya facturadas se muestran atenuadas. Los detalles de la factura muestran la recepción de origen, y los de la recepción, las facturas emitidas y su contenido.

## 2.0.14.1
### ru
- Документ «Отгрузка товара» удалён из программы: продажи оформляются продажей напрямую, вид операции «Накладная по отгрузкам товара» и регистр отгрузок больше не используются. Данные прежних отгрузок в новых документах не участвуют.
- «Сертификат на оплату» убран из меню и из ввода на основании: документ остаётся в системе для истории, но новые не создаются.
- Списки заказов покупателей, возвратов, сертификатов и налоговых накладных получили ту же панель сведений, что и список продаж: закладки «Фильтры», «Клиент», «Детали» с составом документа, сворачивание в значки, пагинация и колонки без горизонтальной прокрутки.
- В списке заказов появился значок статуса отгрузки рядом со значком оплаты: не отгружен, в работе, отгружен, доставлен, отменён. В фильтрах — переключатели по оплате и по отгрузке.
- В списке налоговых накладных добавлена закладка «Продажи»: проведённые продажи без возможности добавления, уже выписанные показываются приглушённо. В сведениях накладной видно продажу-основание, а в сведениях продажи — выписанные по ней накладные и состав.
### fr
- Le document « Bon de livraison » a été supprimé du programme : les ventes se font directement par la vente, le type d'opération « Facture sur la base des bons de livraison » et le registre des expéditions ne sont plus utilisés. Les anciennes expéditions n'interviennent plus dans les nouveaux documents.
- Le « Bon d'achat » est retiré du menu et de la saisie sur la base : le document reste dans le système pour l'historique, mais on n'en crée plus.
- Les listes des commandes clients, des retours, des bons d'achat et des factures comptables ont reçu le même panneau d'informations que la liste des ventes : onglets « Filtres », « Client », « Détails » avec le contenu du document, réduction en icônes, pagination et colonnes sans défilement horizontal.
- Dans la liste des commandes est apparue une icône de statut d'expédition à côté de celle du paiement : non expédié, en cours, expédié, livré, annulé. Dans les filtres — des bascules par paiement et par expédition.
- Dans la liste des factures comptables a été ajouté l'onglet « Ventes » : les ventes validées sans possibilité d'ajout, celles déjà facturées s'affichent en grisé. Les informations de la facture montrent la vente d'origine, et celles de la vente — les factures émises et le contenu.
### en
- The "Delivery note" document has been removed from the program: sales are made directly by the sale, the "Invoice based on delivery notes" operation type and the shipments register are no longer used. Data of former delivery notes no longer takes part in new documents.
- The "Purchase voucher" is removed from the menu and from entry on the basis: the document stays in the system for history, but new ones are not created.
- The lists of customer orders, returns, vouchers and accounting invoices got the same details panel as the sales list: "Filters", "Customer" and "Details" tabs with the document contents, collapsing into icons, pagination and columns without horizontal scrolling.
- The order list now shows a shipment status icon next to the payment one: not shipped, in progress, shipped, delivered, cancelled. The filters have toggles by payment and by shipment.
- The accounting invoice list has a new "Sales" tab: posted sales with no way to add, and already invoiced ones shown dimmed. The invoice details show the source sale, and the sale details show the invoices issued for it and its contents.
### es
- El documento «Nota de entrega» se ha eliminado del programa: las ventas se hacen directamente por la venta, el tipo de operación «Factura basada en albaranes» y el registro de expediciones ya no se usan. Los datos de las antiguas expediciones ya no participan en los nuevos documentos.
- El «Vale de compra» se quitó del menú y de la entrada sobre la base: el documento permanece en el sistema para el historial, pero no se crean nuevos.
- Las listas de pedidos de clientes, devoluciones, vales y facturas contables recibieron el mismo panel de información que la lista de ventas: pestañas «Filtros», «Cliente» y «Detalles» con el contenido del documento, contracción en iconos, paginación y columnas sin desplazamiento horizontal.
- En la lista de pedidos apareció un icono de estado de expedición junto al de pago: no expedido, en curso, expedido, entregado, cancelado. En los filtros hay conmutadores por pago y por expedición.
- En la lista de facturas contables se añadió la pestaña «Ventas»: las ventas validadas sin posibilidad de añadir, y las ya facturadas se muestran atenuadas. Los detalles de la factura muestran la venta de origen, y los de la venta, las facturas emitidas y su contenido.

## 2.0.13.5
### ru
- Кнопка сворачивания панели сведений перенесена в низ панели; в фильтрах появились отборы по сумме и долгу с выбором знака (больше / меньше / равно), а у фильтра операции вернулась позиция «В кредит».
- Панель сведений и список прокручиваются каждый по отдельности, форма списка больше не растягивается за пределы экрана.
- Счётчик строк на закладках документа показывается фирменным янтарным цветом вместо зелёного.
### fr
- Le bouton de réduction du panneau d'informations est déplacé en bas du panneau ; les filtres ont reçu des sélections par montant et par dette avec choix du signe (supérieur / inférieur / égal), et le filtre d'opération a retrouvé la position « À crédit ».
- Le panneau d'informations et la liste défilent chacun séparément, le formulaire de liste ne dépasse plus les limites de l'écran.
- Le compteur de lignes sur les onglets du document s'affiche en ambre de la marque au lieu du vert.
### en
- The details panel collapse button moved to the bottom of the panel; the filters got amount and debt selections with a sign choice (greater / less / equal), and the operation filter got its "On credit" position back.
- The details panel and the list scroll independently, and the list form no longer stretches beyond the screen.
- The row counter on document tabs is shown in the brand amber instead of green.
### es
- El botón para contraer el panel de información se trasladó a la parte inferior del panel; los filtros recibieron selecciones por importe y por deuda con elección de signo (mayor / menor / igual), y el filtro de operación recuperó la posición «A crédito».
- El panel de información y la lista se desplazan por separado, y el formulario de lista ya no se extiende más allá de la pantalla.
- El contador de filas en las pestañas del documento se muestra en ámbar corporativo en lugar de verde.

## 2.0.13.4
### ru
- Панель сведений списка продаж работает как в УНФ: кнопкой она сворачивается в узкий столбик значков, а щелчок по значку раскрывает её сразу на нужной странице. Страниц три: «Фильтры», «Клиент» — контакты покупателя и его общий долг, «Детали» — операция, наша компания, склад, суммы, ответственный, комментарий и состав документа.
- Список продаж выводится страницами по 50 документов: под списком кнопки ◀ ▶ и счётчик «страница / всего». Страницы считаются с учётом установленных фильтров.
- Колонки списка продаж уместились без горизонтальной прокрутки: операция и склад ушли на страницу «Детали», список открывается на высоту экрана.
- Значки статуса оплаты в списках стали одноцветными в стиле программы: оплачено — галочка, частично — полукруг, не оплачено — кольцо, просрочено — с пометкой внимания.
### fr
- Le panneau d'informations de la liste des ventes fonctionne comme dans UNF : un bouton le réduit en une colonne étroite d'icônes, et un clic sur une icône l'ouvre directement sur la bonne page. Trois pages : « Filtres », « Client » — les contacts de l'acheteur et sa dette totale, « Détails » — l'opération, notre société, l'entrepôt, les montants, le responsable, le commentaire et le contenu du document.
- La liste des ventes s'affiche par pages de 50 documents : sous la liste, les boutons ◀ ▶ et le compteur « page / total ». Les pages tiennent compte des filtres posés.
- Les colonnes de la liste des ventes tiennent sans défilement horizontal : l'opération et l'entrepôt sont passés sur la page « Détails », la liste s'ouvre sur la hauteur de l'écran.
- Les icônes de statut de paiement dans les listes sont désormais monochromes dans le style du programme : payé — une coche, partiellement — un demi-cercle, non payé — un anneau, en retard — avec une marque d'attention.
### en
- The details panel of the sales list works like in UNF: a button collapses it into a narrow column of icons, and clicking an icon opens it right on the needed page. There are three pages: "Filters", "Customer" — the buyer's contacts and total debt, "Details" — the operation, our company, warehouse, amounts, responsible person, comment and document contents.
- The sales list is shown in pages of 50 documents: below the list are ◀ ▶ buttons and a "page / total" counter. Pages respect the applied filters.
- The sales list columns now fit without horizontal scrolling: the operation and warehouse moved to the "Details" page, and the list opens to the screen height.
- Payment status icons in lists are now monochrome in the program style: paid — a check mark, partial — a half circle, unpaid — a ring, overdue — with an attention mark.
### es
- El panel de información de la lista de ventas funciona como en UNF: un botón lo contrae en una columna estrecha de iconos, y un clic en un icono lo abre directamente en la página necesaria. Hay tres páginas: «Filtros», «Cliente» — los contactos del comprador y su deuda total, «Detalles» — la operación, nuestra empresa, el almacén, los importes, el responsable, el comentario y el contenido del documento.
- La lista de ventas se muestra por páginas de 50 documentos: bajo la lista hay botones ◀ ▶ y un contador «página / total». Las páginas tienen en cuenta los filtros aplicados.
- Las columnas de la lista de ventas caben sin desplazamiento horizontal: la operación y el almacén pasaron a la página «Detalles», y la lista se abre a la altura de la pantalla.
- Los iconos de estado de pago en las listas ahora son monocromos al estilo del programa: pagado — una marca de verificación, parcial — un semicírculo, no pagado — un anillo, vencido — con una marca de atención.

## 2.0.13.3
### ru
- Окно «Что нового» теперь читаемо в тёмной теме: фон и текст подстраиваются под тему, заголовки версий — в фирменном янтарном цвете вместо зелёного.
### fr
- La fenêtre « Nouveautés » est désormais lisible dans le thème sombre : le fond et le texte s'adaptent au thème, les titres de versions sont en ambre de la marque au lieu du vert.
### en
- The "What's new" window is now readable in the dark theme: the background and text adapt to the theme, and version headings are in the brand amber instead of green.
### es
- La ventana «Novedades» ahora es legible en el tema oscuro: el fondo y el texto se adaptan al tema, y los títulos de versión van en el ámbar corporativo en lugar del verde.

## 2.0.13.2
### ru
- Фирменный стиль maERP: янтарный акцентный цвет кнопок, ссылок и выделений — одинаковый в светлой и тёмной темах, кремовый фон форм и тёплый цвет текста.
- Иконки разделов главного меню перерисованы: они стали контрастнее и перекрашиваются программой под выбранную тему, поэтому одинаково хорошо читаются и на светлом, и на тёмном фоне.
- В списке продаж появилась закладка «Заказы покупателей (к отгрузке)»: заказы, которые ещё не отгружены, видны прямо в списке, и по выделенным заказам одной кнопкой оформляются реализации.
- Справа в списке продаж — скрываемая панель сведений: закладка «Фильтры» с отборами по виду операции (переключателем), контрагенту, организации, складу и ответственному; закладка «Инфо» с реквизитами выбранного документа; закладка «Состав» с его товарами.
- Шапка формы продажи скомпонована компактнее: номер и дата в одну строку, вид операции выбирается из списка, кнопки печати перенесены вниз к кнопкам записи. В заголовке окна — номер без лидирующих нулей, клиент, наша компания и дата.
### fr
- Style de marque maERP : couleur d'accent ambre pour les boutons, liens et sélections — identique dans les thèmes clair et sombre, fond crème des formulaires et couleur de texte chaleureuse.
- Les icônes des sections du menu principal ont été redessinées : plus contrastées, elles sont recolorées par le programme selon le thème choisi et restent bien lisibles sur fond clair comme sur fond sombre.
- La liste des ventes a un nouvel onglet « Commandes clients (à expédier) » : les commandes non expédiées y sont visibles directement, et un seul bouton crée les ventes pour les commandes sélectionnées.
- À droite de la liste des ventes — un panneau d'informations masquable : l'onglet « Filtres » avec les sélections par type d'opération (bascule), client, société, entrepôt et responsable ; l'onglet « Infos » avec les attributs du document choisi ; l'onglet « Contenu » avec ses marchandises.
- L'en-tête du formulaire de vente est plus compact : le numéro et la date sur une seule ligne, le type d'opération se choisit dans une liste, les boutons d'impression sont déplacés en bas près des boutons d'enregistrement. Le titre de la fenêtre affiche le numéro sans zéros de tête, le client, notre société et la date.
### en
- maERP brand style: an amber accent color for buttons, links and selections — the same in the light and dark themes, a cream form background and a warm text color.
- The main menu section icons have been redrawn: they are more contrasty and are recolored by the program to match the chosen theme, so they read equally well on light and dark backgrounds.
- The sales list has a new tab, "Customer orders (to ship)": orders not yet shipped are visible right in the list, and one button creates sales for the selected orders.
- On the right of the sales list is a collapsible details panel: the "Filters" tab with selections by operation type (toggle), customer, company, warehouse and responsible person; the "Info" tab with the attributes of the chosen document; the "Contents" tab with its goods.
- The sales form header is more compact: the number and date on one line, the operation type is chosen from a list, and the print buttons moved down next to the save buttons. The window title shows the number without leading zeros, the customer, our company and the date.
### es
- Estilo corporativo maERP: color de acento ámbar para botones, enlaces y selecciones — el mismo en los temas claro y oscuro, fondo crema de los formularios y color de texto cálido.
- Los iconos de las secciones del menú principal se han redibujado: son más contrastados y el programa los recolorea según el tema elegido, por lo que se leen igual de bien sobre fondo claro y oscuro.
- La lista de ventas tiene una nueva pestaña «Pedidos de clientes (por expedir)»: los pedidos aún no expedidos se ven directamente en la lista, y un solo botón crea las ventas para los pedidos seleccionados.
- A la derecha de la lista de ventas hay un panel de información ocultable: la pestaña «Filtros» con selecciones por tipo de operación (conmutador), cliente, empresa, almacén y responsable; la pestaña «Info» con los atributos del documento elegido; la pestaña «Contenido» con sus mercancías.
- El encabezado del formulario de venta es más compacto: el número y la fecha en una sola línea, el tipo de operación se elige de una lista y los botones de impresión se trasladaron abajo junto a los botones de guardado. El título de la ventana muestra el número sin ceros iniciales, el cliente, nuestra empresa y la fecha.

## 2.0.13.1
### ru
- Обновлён вид форм продажи товаров, карточки и списка номенклатуры: убраны рамки вокруг блоков полей, шапка и итоги перестраиваются под ширину окна. Это первые формы нового оформления — остальные будут приводиться к тому же виду постепенно.
- Пароль можно сменить самому: в разделе «Сервис» появилась обработка «Смена пароля» — она спросит текущий пароль и дважды новый. Раньше пароль менял только администратор в карточке пользователя.
- Продолжено обновление вида форм: без рамок вокруг блоков полей и с перестройкой под ширину окна теперь работают документы продаж — возврат от покупателя, отгрузка, заказ покупателя, кассовая смена, установка цен и правило ценообразования.
- Форма продажи собрана заново: сверху вид операции переключателем, номер убран в свёрнутый раздел «Нумерация», реквизиты вынесены на закладку «Операция» — заказ клиента сразу за клиентом, наша компания рядом со складом, цены, НДС и зачёт авансов в одной группе. В заголовке окна теперь видно, кто кому и на какую сумму продаёт.
### fr
- Aspect renouvelé des formulaires de vente de marchandises, de la fiche et de la liste des articles : les cadres autour des blocs de champs ont été supprimés, l'en-tête et les totaux s'adaptent à la largeur de la fenêtre. Ce sont les premiers formulaires de la nouvelle présentation, les autres suivront progressivement.
- Vous pouvez changer votre mot de passe vous-même : le traitement « Changer le mot de passe » est apparu dans la section « Service » : il demande le mot de passe actuel et deux fois le nouveau. Auparavant, seul l'administrateur le changeait dans la fiche de l'utilisateur.
- Poursuite de la mise à jour de l'aspect des formulaires : les documents de vente — retour client, expédition, commande client, journée de caisse, fixation des prix et règle de tarification — sont désormais sans cadres autour des blocs de champs et s'adaptent à la largeur de la fenêtre.
- Le formulaire de vente a été réorganisé : le type d'opération en haut sous forme de bascule, le numéro déplacé dans la section repliée « Numérotation », les attributs regroupés dans l'onglet « Opération » — la commande du client juste après le client, notre société à côté de l'entrepôt, les prix, la TVA et l'imputation des acomptes dans un seul groupe. Le titre de la fenêtre indique désormais qui vend à qui et pour quel montant.
### en
- Refreshed the look of the goods sale form and of the item card and list: frames around field blocks are gone, and the header and totals adapt to the window width. These are the first forms in the new style; the rest will follow gradually.
- You can change your own password: the "Change password" data processor is now in the "Service" section: it asks for the current password and the new one twice. Previously only an administrator could change it from the user card.
- The form refresh continues: sales documents — customer return, shipment, sales order, cash session, price setting and pricing rule — now come without frames around field blocks and adapt to the window width.
- The sales form has been rebuilt: the operation type is a toggle at the top, the number moved into the collapsed "Numbering" section, and the attributes gathered on the "Operation" tab — the customer order right after the customer, our company next to the warehouse, prices, VAT and advance offsets in one group. The window title now shows who sells to whom and for how much.
### es
- Renovado el aspecto del formulario de venta de mercancías y de la ficha y la lista de artículos: se han quitado los marcos alrededor de los bloques de campos, y el encabezado y los totales se adaptan al ancho de la ventana. Son los primeros formularios del nuevo diseño; el resto seguirá poco a poco.
- Puede cambiar su contraseña usted mismo: en la sección «Servicio» apareció el procesamiento «Cambiar la contraseña»: pide la contraseña actual y dos veces la nueva. Antes solo el administrador la cambiaba en la ficha del usuario.
- Continúa la renovación del aspecto de los formularios: los documentos de ventas — devolución del cliente, expedición, pedido de cliente, jornada de caja, fijación de precios y regla de tarificación — ya no tienen marcos alrededor de los bloques de campos y se adaptan al ancho de la ventana.
- El formulario de venta se ha rehecho: el tipo de operación arriba como conmutador, el número trasladado a la sección plegada «Numeración» y los atributos reunidos en la pestaña «Operación»: el pedido del cliente justo después del cliente, nuestra empresa junto al almacén, precios, IVA y compensación de anticipos en un solo grupo. El título de la ventana muestra ahora quién vende a quién y por cuánto.

# Релиз 2.0.12.18 (2026-08-28)

Первая публикация CF после 1.0.11.1. Поставка: `maERP-2.0.12.18.cf`,
обновление с 1.0.11.1 — `maERP-2.0.12.18.cfu`.

## 2.0.12.18
### ru
- Исправлено открытие карточки товара из табличной части документа: команда обрывалась ошибкой запроса при проверке того, использован ли комплект в документах.
- В веб-клиенте программа сама предлагает установить расширение для работы с 1С:Предприятием, когда оно нужно: при печати на принтер, сохранении печатной формы в файл, звонке из карточки лида и работе с изображениями товара. Раньше в браузере такие действия молча зависали или ничего не делали. Отказ запоминается, повторно программа не спрашивает.
- Автопроверка перед сборкой стала строже: формы объектов теперь открываются не только пустыми, но и на существующих объектах базы — так ловятся ошибки, которые видны только в заполненной карточке.
### fr
- Correction de l'ouverture de la fiche article depuis la partie tabulaire d'un document : la commande s'interrompait sur une erreur de requête lors de la vérification de l'utilisation du kit dans les documents.
- Dans le client web, le programme propose lui-même d'installer l'extension pour travailler avec 1C:Entreprise lorsqu'elle est nécessaire : impression sur une imprimante, enregistrement du formulaire imprimable dans un fichier, appel depuis la fiche du prospect et travail avec les images des articles. Auparavant, dans le navigateur, ces actions restaient bloquées ou sans effet. Le refus est mémorisé, le programme ne redemande plus.
- La vérification automatique avant l'assemblage est devenue plus stricte : les formulaires d'objets sont désormais ouverts non seulement vides, mais aussi sur des objets existants de la base — cela permet de détecter les erreurs visibles uniquement dans une fiche remplie.
### en
- Fixed opening the item card from a document's table: the command failed with a query error while checking whether the kit had been used in documents.
- In the web client, the application now offers to install the 1C:Enterprise extension when it is required: printing to a printer, saving a print form to a file, calling from a lead card, and working with item images. Previously such actions silently hung or did nothing in the browser. A refusal is remembered, so the application does not ask again.
- The pre-build self-check got stricter: object forms are now opened not only empty but also on existing objects from the database, which catches errors visible only in a filled-in card.
### es
- Corregida la apertura de la ficha del artículo desde la parte tabular del documento: el comando fallaba con un error de consulta al comprobar si el kit ya se había usado en documentos.
- En el cliente web, el programa propone instalar la extensión para trabajar con 1C:Empresa cuando hace falta: impresión en una impresora, guardado del formulario de impresión en un archivo, llamada desde la ficha del cliente potencial y trabajo con las imágenes de los artículos. Antes, en el navegador, esas acciones se quedaban colgadas o no hacían nada. El rechazo se recuerda y el programa no vuelve a preguntar.
- La comprobación automática antes del ensamblaje es más estricta: los formularios de objetos ahora se abren no solo vacíos, sino también sobre objetos existentes de la base, lo que detecta errores visibles solo en una ficha rellenada.
## 2.0.12.17
### ru
- Исправлена печать акта передачи в переработку и акта приёмки из переработки: подзаголовки таблиц («Передано сырьё и полуфабрикаты», «Ожидаемая продукция») были в макете обычным текстом, а не полем, и печать обрывалась с ошибкой.
- Исправлена печать табеля учёта рабочего времени: она обращалась к реквизитам, которых у документа нет, и не формировалась вовсе. Вариант учёта печатается графиком работы сотрудника; строка «Группа» в шапке остаётся пустой - такого реквизита у табеля нет.
- Печать накладной возврата от покупателя: образец возврата теперь заводится по реализации-основанию, без которого документ вообще не записывался.
### fr
- Correction de l'impression du bon de transfert en sous-traitance et du bon de réception : les sous-titres des tableaux (« Matières premières et semi-finis transférés », « Produits attendus ») étaient du texte ordinaire dans le modèle et non un champ, et l'impression s'interrompait sur une erreur.
- Correction de l'impression de la feuille de présence : elle utilisait des attributs absents du document et ne se formait pas du tout. Le mode de suivi est imprimé d'après l'horaire de travail du salarié ; la ligne « Groupe » de l'en-tête reste vide - cet attribut n'existe pas.
- Impression du bon de retour client : l'exemple de retour est désormais créé à partir de la vente d'origine, sans laquelle le document ne s'enregistrait pas du tout.
### en
- Fixed printing of the transfer-for-processing act and the acceptance act: the table subtitles ("Raw materials and semi-finished products transferred", "Expected products") were plain text in the template rather than a field, and printing broke with an error.
- Fixed printing of the timesheet: it referenced attributes the document does not have and did not print at all. The accounting mode is printed from the employee's work schedule; the "Group" line in the header stays empty - the timesheet has no such attribute.
- Customer return note printing: the sample return is now created from the sales document it is based on, without which the document would not save at all.
### es
- Corregida la impresión del acta de transferencia a procesamiento y del acta de recepción: los subtítulos de las tablas («Materias primas y semielaborados transferidos», «Productos esperados») eran texto normal en la plantilla y no un campo, y la impresión se interrumpía con error.
- Corregida la impresión del parte de horas: usaba atributos que el documento no tiene y no se generaba en absoluto. El modo de registro se imprime según el horario de trabajo del empleado; la línea «Grupo» de la cabecera queda vacía - ese atributo no existe.
- Impresión del albarán de devolución del cliente: la muestra de devolución ahora se crea a partir de la venta de origen, sin la cual el documento no se guardaba.

## 2.0.12.16
### ru
- Исправлено открытие налоговой накладной и налоговой накладной покупки: форма падала при открытии, потому что состав реквизитов документа определялся способом, который на форме не работает.
- Тестовая база теперь заполняется образцами документов автоматически: печать каждого документа конфигурации — возвратов, ордеров, ведомостей, табеля, актов — стало на чём проверять. Раньше проверка не доходила до 22 документов из 25: в базе не было ни одного такого документа.
### fr
- Correction de l'ouverture de la facture fiscale et de la facture fiscale d'achat : le formulaire s'interrompait à l'ouverture, car la composition des attributs du document était déterminée d'une manière qui ne fonctionne pas sur un formulaire.
- La base de test se remplit désormais automatiquement d'exemples de documents : l'impression de chaque document de la configuration — retours, bons de caisse, états de paie, feuille de présence, actes — peut enfin être vérifiée. Auparavant 22 documents sur 25 échappaient au contrôle, faute d'exemplaire en base.
### en
- Fixed opening the tax invoice and the purchase tax invoice: the form failed to open because the document's attribute list was determined in a way that does not work on a form.
- The test database is now filled with sample documents automatically: printing of every document in the configuration — returns, cash orders, payroll sheets, timesheet, statements — can finally be checked. Previously 22 documents out of 25 escaped the check because the database held none of them.
### es
- Corregida la apertura de la factura fiscal y de la factura fiscal de compra: el formulario fallaba al abrirse porque la composición de los atributos del documento se determinaba de un modo que no funciona en el formulario.
- La base de pruebas ahora se rellena con documentos de muestra automáticamente: la impresión de cada documento de la configuración — devoluciones, órdenes de caja, nóminas, parte de horas, actas — por fin se puede comprobar. Antes 22 documentos de 25 quedaban sin control por no haber ninguno en la base.

## 2.0.12.15
### ru
- Исправлен счёт-фактура: способ оплаты определялся по реквизиту ручной корректировки, которого у реализации нет (он есть только у налоговых накладных), и печать обрывалась. Теперь реквизит читается только там, где он есть, а у остальных документов оплаты берутся из движений по деньгам.
- Исправлена шапка печатных форм, где организация, клиент, номер и итог не выводились: товарная накладная прежней формы, чек, счёт-фактура Socassif, накладные возврата и налоговая накладная покупки. У накладной возврата печать чека на этом же месте обрывалась.
- Счёт-фактура Socassif: в накладной с товарами вместо номера документа печаталась дата, а номер не выводился совсем.
- Проверка перед сдачей стала строже: прогон печати теперь отмечает формы, в которых не нашёл номера документа, — раньше пустая шапка выглядела для него так же, как заполненная.
### fr
- Correction de la facture : le mode de règlement était déterminé par l'attribut de correction manuelle, absent de la vente (il n'existe que sur les factures fiscales), et l'impression s'interrompait. L'attribut n'est désormais lu que là où il existe ; pour les autres documents, les règlements proviennent des mouvements de trésorerie.
- Correction de l'en-tête des impressions où la société, le client, le numéro et le total n'apparaissaient pas : facture (ancien formulaire), ticket, facture Socassif, bons de retour et facture fiscale d'achat. Sur un bon de retour, l'impression du ticket s'interrompait au même endroit.
- Facture Socassif : sur un document avec marchandises, la date était imprimée à la place du numéro, et le numéro n'apparaissait pas du tout.
- Contrôle avant livraison renforcé : le test d'impression signale désormais les formulaires où le numéro du document est introuvable — auparavant un en-tête vide lui paraissait identique à un en-tête rempli.
### en
- Fixed the invoice: the payment method was determined by the manual correction attribute, which sales documents do not have (only tax invoices do), and printing broke. The attribute is now read only where it exists; for other documents payments come from cash movements.
- Fixed the header of printed forms where the company, customer, number and total were missing: invoice (former form), receipt, Socassif invoice, return notes and purchase tax invoice. On a return note, printing the receipt broke at that same place.
- Socassif invoice: on a document with goods the date was printed instead of the document number, and the number was not printed at all.
- Stricter pre-release check: the print run now flags forms in which it could not find the document number — an empty header used to look the same to it as a filled one.
### es
- Corregida la factura: la forma de pago se determinaba por el atributo de corrección manual, que la venta no tiene (solo lo tienen las facturas fiscales), y la impresión se interrumpía. Ahora el atributo se lee solo donde existe y, en los demás documentos, los pagos se toman de los movimientos de tesorería.
- Corregida la cabecera de las formas impresas donde no salían la organización, el cliente, el número y el total: albarán (formulario anterior), recibo, factura Socassif, albaranes de devolución y factura fiscal de compra. En el albarán de devolución la impresión del recibo se interrumpía en ese mismo punto.
- Factura Socassif: en el documento con mercancías se imprimía la fecha en lugar del número, y el número no salía en absoluto.
- Control previo a la entrega más estricto: la prueba de impresión ahora marca las formas en las que no encontró el número del documento — antes una cabecera vacía le parecía igual que una llena.

## 2.0.12.14
### ru
- Исправлена шапка накладных, счетов, коммерческих предложений и проформы: организация, клиент, номер, дата и итоги брались из итоговой строки запроса, где их не было, - формы либо обрывались ошибкой, либо печатались с пустой шапкой. Теперь реквизиты шапки в итоговой строке есть.
- Заказ покупателя открывается при выключенных тендерах поставщиков: кнопку и надпись тендера платформа с формы убирает, а код к ним обращался.
### fr
- Correction de l'en-tête des bons de livraison, factures, devis et proformas : l'organisation, le client, le numéro, la date et les totaux étaient lus dans la ligne de totaux de la requête, où ils n'existaient pas - les formulaires s'interrompaient ou s'imprimaient avec un en-tête vide. Les mentions de l'en-tête y figurent désormais.
- La commande client s'ouvre lorsque les appels d'offres fournisseurs sont désactivés : la plateforme retire le bouton et le libellé du formulaire, alors que le code y accédait.
### en
- Fixed the header of delivery notes, invoices, quotations and proformas: the company, customer, number, date and totals were read from the query total row where they did not exist - the forms either broke with an error or printed an empty header. The header details are now present in the total row.
- The customer order opens when supplier tenders are disabled: the platform removes the tender button and label from the form, while the code still addressed them.
### es
- Corregida la cabecera de albaranes, facturas, presupuestos y proformas: la organización, el cliente, el número, la fecha y los totales se leían de la fila de totales de la consulta, donde no existían; los formularios se interrumpían o se imprimían con la cabecera vacía. Ahora los datos de cabecera están en la fila de totales.
- El pedido de cliente se abre con las licitaciones de proveedores desactivadas: la plataforma retira el botón y el rótulo del formulario, mientras que el código seguía accediendo a ellos.

## 2.0.12.13
### ru
- Исправлена печать накладной без цен: признак «без цен» терялся, когда команда печати его не передавала, и формирование обрывалось. Заодно суммы оплат в подвале накладной приводятся к числу - пустые итоги больше не роняют печать.
- Карточка бухгалтерской операции: все колонки таблицы проводок настраиваются по наличию на форме, а не вслепую - часть колонок бухгалтерского контура в maERP просто не выводится.
### fr
- Correction de l'impression du bon de livraison sans prix : l'indicateur « sans prix » était perdu lorsque la commande d'impression ne le transmettait pas et la génération s'interrompait. De plus, les montants des règlements en pied de bon sont convertis en nombre - les totaux vides ne cassent plus l'impression.
- Fiche d'opération comptable : toutes les colonnes du tableau des écritures sont configurées selon leur présence sur le formulaire et non à l'aveugle - une partie des colonnes comptables n'est tout simplement pas affichée dans maERP.
### en
- Fixed printing the delivery note without prices: the "no prices" flag was lost when the print command did not pass it and generation broke. Payment totals in the note footer are also coerced to numbers - empty totals no longer break printing.
- Accounting operation card: every column of the entries table is configured based on whether it exists on the form instead of blindly - some accounting columns are simply not rendered in maERP.
### es
- Corregida la impresión del albarán sin precios: el indicador «sin precios» se perdía cuando el comando de impresión no lo transmitía y la generación se interrumpía. Además, los importes de los pagos en el pie del albarán se convierten a número: los totales vacíos ya no rompen la impresión.
- Ficha de operación contable: todas las columnas de la tabla de asientos se configuran según su presencia en el formulario y no a ciegas; parte de las columnas contables simplemente no se muestra en maERP.

## 2.0.12.12
### ru
- Исправлена подстановка логотипа организации в накладные, счета и коммерческие предложения: поиск рисунка в области макета шёл несуществующим методом, и печать обрывалась на одиннадцати формах реализации и заказа покупателя.
- Карточка бухгалтерской операции открывается до конца: колонки направлений деятельности и сумм управленческого учёта платформа на форму не выводит (реквизитов этих механизмов в maERP нет), настройка колонок теперь идёт по их наличию.
### fr
- Correction de l'insertion du logo de l'organisation dans les bons de livraison, les factures et les devis : la recherche de l'image dans la zone du modèle utilisait une méthode inexistante et l'impression s'interrompait sur onze formulaires de vente et de commande client.
- La fiche d'opération comptable s'ouvre jusqu'au bout : les colonnes des axes d'activité et des montants de comptabilité de gestion ne sont pas affichées par la plateforme (les attributs de ces mécanismes n'existent pas dans maERP), la configuration des colonnes tient désormais compte de leur présence.
### en
- Fixed inserting the company logo into delivery notes, invoices and quotations: looking up the picture in the template area used a non-existent method and printing broke on eleven sales and customer order forms.
- The accounting operation card now opens fully: the activity-line and management accounting amount columns are not rendered by the platform (maERP has no attributes for those mechanisms), so column setup now checks whether they exist.
### es
- Corregida la inserción del logotipo de la organización en albaranes, facturas y presupuestos: la búsqueda de la imagen en el área de la plantilla usaba un método inexistente y la impresión se interrumpía en once formularios de venta y de pedido de cliente.
- La ficha de operación contable se abre por completo: las columnas de líneas de actividad y de importes de contabilidad de gestión no las muestra la plataforma (maERP no tiene atributos de esos mecanismos), por lo que la configuración de columnas comprueba ahora su existencia.

## 2.0.12.11
### ru
- Исправлена печать накладных, счетов и заказов: если в документе не заполнена организация или контрагент удалён, печатная форма падала с ошибкой - теперь реквизиты просто остаются пустыми. Прогон нашёл это на десяти печатных формах реализации и заказа покупателя.
- Исправлен счёт Facture: номер документа не приводился к строке, и формирование обрывалось ошибкой преобразования к числу.
- Карточка бухгалтерской операции снова открывается: убраны обращения к функциональным опциям учёта по направлениям и управленческого учёта на плане счетов, которых в maERP нет.
- Прогон автотестов доведён до конца на обновлённой базе: окно печати документов исключено из проверки форм (оно открывается только с параметрами команды печати), проверка конфигурации больше не считает замечанием строку «ошибок не обнаружено», а ожидание старта клиента не зависит от того, как платформа запустила процесс.
- Сверка ссылок дополнена проверкой функциональных опций - имена в кавычках теперь тоже сверяются с конфигурацией.
### fr
- Correction de l'impression des bons de livraison, des factures et des commandes : si l'organisation n'est pas renseignée dans le document ou si le tiers a été supprimé, le formulaire imprimable tombait en erreur - les mentions restent désormais simplement vides. L'exécution l'a trouvé sur dix formulaires de vente et de commande client.
- Correction de la facture Facture : le numéro du document n'était pas converti en chaîne et la génération s'interrompait par une erreur de conversion en nombre.
- La fiche d'opération comptable s'ouvre de nouveau : suppression des appels aux options fonctionnelles de comptabilité par axe d'activité et de comptabilité de gestion sur le plan comptable, absentes de maERP.
- Les tests automatiques vont jusqu'au bout sur la base mise à jour : la fenêtre d'impression est exclue du contrôle des formulaires (elle ne s'ouvre qu'avec les paramètres de la commande d'impression), la vérification de la configuration ne considère plus la ligne « aucune erreur » comme une remarque, et l'attente du démarrage du client ne dépend plus de la façon dont la plateforme a lancé le processus.
- Le contrôle des références vérifie aussi les options fonctionnelles : les noms entre guillemets sont désormais confrontés à la configuration.
### en
- Fixed printing of delivery notes, invoices and orders: when the document has no company filled in or the counterparty was deleted, the print form failed with an error - now the details simply stay empty. The run found this on ten print forms of sales and customer orders.
- Fixed the Facture invoice: the document number was not converted to a string and generation broke with a number conversion error.
- The accounting operation card opens again: calls to functional options for activity-line accounting and management accounting on the chart of accounts, which maERP does not have, are removed.
- The automated run completes on the updated base: the print window is excluded from the form check (it only opens with print command parameters), the configuration check no longer treats the "no errors found" line as a remark, and waiting for the client start no longer depends on how the platform launched the process.
- The reference check also covers functional options: names in quotes are now verified against the configuration.
### es
- Corregida la impresión de albaranes, facturas y pedidos: si en el documento no está rellenada la organización o la contraparte se ha eliminado, el formulario de impresión fallaba con error; ahora los datos simplemente quedan vacíos. La ejecución lo encontró en diez formularios de venta y de pedido de cliente.
- Corregida la factura Facture: el número del documento no se convertía a cadena y la generación se interrumpía con un error de conversión a número.
- La ficha de operación contable vuelve a abrirse: se han eliminado las llamadas a opciones funcionales de contabilidad por líneas de actividad y de contabilidad de gestión en el plan de cuentas, que maERP no tiene.
- La ejecución automática llega hasta el final en la base actualizada: la ventana de impresión se excluye de la comprobación de formularios (solo se abre con los parámetros del comando de impresión), la comprobación de la configuración ya no considera una observación la línea «no se han encontrado errores» y la espera del arranque del cliente no depende de cómo la plataforma haya lanzado el proceso.
- El control de referencias abarca también las opciones funcionales: los nombres entre comillas se contrastan ahora con la configuración.

## 2.0.12.10
### ru
- Исправлена ошибка печати: модуль печатных форм не запускался из-за неверного обращения к типу макета, а в модуле печати лидов осталась лишняя директива области - реестр макетов и печать снова работают.
- Исправлена карточка бухгалтерской операции: форма не открывалась из-за обращения к несуществующим константам валют управленческого учёта и финансовой отчётности; в maERP валюта учёта одна.
- Прогон автотестов доведён до конца: проверка конфигурации больше не выдаёт замечаний - убраны битые ссылки в справке бухгалтерских объектов, отсутствующая картинка в справке группового изменения реквизитов и несуществующий цвет в макете накладной FactureSocassif.
- Карточка бухгалтерской операции очищена от остатков чужой библиотеки: убраны обращения к неперенесённым механизмам (управление доступом, подключаемые команды, форма редактирования комментария, учёт налоговых разниц), исправлен тип склада в подборе субконто и сообщение о незаполненном сторнируемом документе.
- Автотесты дополнены вторым проходом: после «открыть все формы» прогон формирует каждую печатную форму каждого документа - раньше печать не проверялась ничем.
- Автотесты выделены в отдельную подсистему «Автотесты»: обработка прогона и её клиентский модуль собраны в одном месте и не показываются в разделах программы.

### fr
- Correction d'une erreur d'impression : le module des formulaires imprimables ne démarrait pas à cause d'un accès incorrect au type de modèle, et le module d'impression des pistes contenait une directive de région superflue - le registre des modèles et l'impression fonctionnent de nouveau.
- Correction de la fiche d'opération comptable : le formulaire ne s'ouvrait pas à cause de constantes de devises (comptabilité de gestion et états financiers) inexistantes ; dans maERP la devise comptable est unique.
- Les tests automatiques passent jusqu'au bout : la vérification de la configuration ne signale plus rien - liens rompus dans l'aide des objets comptables, image manquante dans l'aide de la modification groupée et couleur inexistante dans le modèle FactureSocassif ont été supprimés.
- La fiche d'opération comptable est débarrassée des restes d'une bibliothèque étrangère : suppression des appels aux mécanismes non repris (gestion des accès, commandes enfichables, fenêtre d'édition du commentaire, comptabilisation des écarts fiscaux), correction du type d'entrepôt dans la sélection des sous-comptes et du message sur le document annulable non renseigné.
- Les tests automatiques reçoivent une seconde passe : après « ouvrir tous les formulaires », l'exécution génère chaque formulaire imprimable de chaque document - l'impression n'était vérifiée par rien auparavant.
- Les tests automatiques sont regroupés dans un sous-système « Tests automatiques » : le traitement d'exécution et son module client sont réunis au même endroit et n'apparaissent pas dans les sections du programme.

### en
- Fixed a printing error: the print forms module failed to start because of an incorrect reference to the template type, and the lead printing module had a stray region directive - the template registry and printing work again.
- Fixed the accounting operation card: the form did not open because of references to non-existent management and financial reporting currency constants; maERP uses a single accounting currency.
- The automated test run now completes: the configuration check reports nothing - broken links in the help of accounting objects, a missing image in the bulk attribute change help and a non-existent color in the FactureSocassif template have been removed.
- The accounting operation card is cleared of leftovers from a foreign library: calls to mechanisms that were never ported (access management, plug-in commands, the comment editing window, tax difference accounting) are removed, the warehouse type in subconto selection and the message about an empty document being cancelled are fixed.
- The automated tests get a second pass: after "open all forms" the run generates every print form of every document - printing was previously checked by nothing.
- The automated tests are extracted into a separate "Automated tests" subsystem: the run processor and its client module live in one place and are not shown in the application sections.

### es
- Corregido un error de impresión: el módulo de formularios de impresión no arrancaba por una referencia incorrecta al tipo de plantilla y el módulo de impresión de leads tenía una directiva de región sobrante - el registro de plantillas y la impresión vuelven a funcionar.
- Corregida la ficha de operación contable: el formulario no se abría por referencias a constantes de moneda de gestión y de estados financieros inexistentes; en maERP la moneda contable es única.
- La ejecución de las pruebas automáticas llega hasta el final: la comprobación de la configuración ya no informa nada - se han eliminado los enlaces rotos en la ayuda de los objetos contables, la imagen que faltaba en la ayuda del cambio masivo de atributos y el color inexistente en la plantilla FactureSocassif.
- La ficha de operación contable se ha limpiado de restos de una biblioteca ajena: se han eliminado las llamadas a mecanismos no trasladados (gestión de accesos, comandos conectables, ventana de edición del comentario, contabilidad de diferencias fiscales), se han corregido el tipo de almacén en la selección de subcuentas y el mensaje sobre el documento revertido sin rellenar.
- Las pruebas automáticas incorporan una segunda pasada: tras «abrir todos los formularios», la ejecución genera cada formulario de impresión de cada documento; antes la impresión no la comprobaba nada.
- Las pruebas automáticas se han extraído a un subsistema aparte «Pruebas automáticas»: el procesamiento de ejecución y su módulo cliente están en un solo lugar y no se muestran en las secciones del programa.

## 2.0.12.9
### ru
- Служебные помощники печати (реквизиты организации в подвале, добивка страницы пустыми строками, сумма прописью, логотип и размеры печатей-подписей, дополнение таблицы товаров) собраны в подсистеме печатных форм: печать целиком живёт в одном месте.
- ABC-классификация выделена в отдельный модуль: она нужна отчёту «ABC-анализ продаж» и к печати отношения не имеет.
- Убраны устаревшее окно предварительного просмотра и старые модули печати - все печатные формы открываются в общем окне печати.
### fr
- Les utilitaires d'impression (mentions de l'organisation en pied de page, remplissage de la page par des lignes vides, montant en toutes lettres, logo et dimensions des cachets et signatures, complément du tableau des articles) sont regroupés dans le sous-système des formulaires imprimables : l'impression vit désormais en un seul endroit.
- La classification ABC est extraite dans un module distinct : elle sert au rapport « Analyse ABC des ventes » et n'a rien à voir avec l'impression.
- L'ancienne fenêtre d'aperçu et les anciens modules d'impression sont supprimés - tous les formulaires imprimables s'ouvrent dans la fenêtre d'impression commune.
### en
- The printing utilities (company details in the footer, filling the page with empty rows, amount in words, logo and the size of stamps and signatures, extending the goods table) are gathered in the print forms subsystem: printing now lives in one place.
- The ABC classification is extracted into a separate module: it serves the "ABC sales analysis" report and has nothing to do with printing.
- The obsolete preview window and the old printing modules are removed - all print forms open in the common print window.
### es
- Las utilidades de impresión (datos de la organización en el pie, relleno de la página con líneas vacías, importe en letras, logotipo y tamaño de sellos y firmas, complemento de la tabla de artículos) se reúnen en el subsistema de formularios de impresión: la impresión vive ahora en un solo lugar.
- La clasificación ABC se ha extraído a un módulo aparte: sirve al informe «Análisis ABC de ventas» y no tiene relación con la impresión.
- Se han eliminado la antigua ventana de vista previa y los módulos de impresión antiguos: todos los formularios de impresión se abren en la ventana común.

## 2.0.12.8
### ru
- Рабочее место кассира печатает через общее окно печати: чек уходит на чековый принтер или показывается перед печатью, накладная и возврат открываются в окне печати, Z-отчёт кассовой смены печатается одной командой.
- В режиме ПДВ накладная из кассы по-прежнему печатается без цен.
- Этикетки: макет стикера теперь виден в реестре макетов и правится как остальные печатные формы, печать на принтер этикеток перенесена в подсистему печати и сообщает об отсутствующем принтере понятным текстом на четырёх языках.
- Лиды интернет-магазина: заказ покупателя и накладная на доставку печатаются через общее окно, телефон и почта покупателя подставляются в форму как раньше.
- При сохранении из окна печати имя файла берётся из печатной формы - например, «Bon de livraison № 5 du 26.08.2026».
### fr
- Le poste de caisse imprime via la fenêtre d'impression commune : le ticket part sur l'imprimante à tickets ou s'affiche avant l'impression, le bon de livraison et l'avoir s'ouvrent dans la fenêtre d'impression, l'état Z de la session de caisse s'imprime en une commande.
- En mode PDV, le bon de livraison de la caisse s'imprime toujours sans les prix.
- Étiquettes : le modèle d'étiquette apparaît désormais dans le registre des modèles et se modifie comme les autres formulaires imprimables ; l'impression sur l'imprimante d'étiquettes est passée dans le sous-système d'impression et signale l'imprimante manquante dans les quatre langues.
- Prospects de la boutique en ligne : la commande client et le bon de livraison s'impriment via la fenêtre commune, le téléphone et l'e-mail de l'acheteur sont repris comme avant.
- Lors de l'enregistrement depuis la fenêtre d'impression, le nom du fichier provient du formulaire imprimable - par exemple « Bon de livraison № 5 du 26.08.2026 ».
### en
- The cashier workplace prints through the common print window: the receipt goes to the receipt printer or is shown before printing, the delivery note and the credit note open in the print window, and the cash session Z-report is printed by a single command.
- In POS mode the delivery note from the cash desk is still printed without prices.
- Labels: the sticker template now appears in the template registry and is edited like other print forms; printing to the label printer moved into the print subsystem and reports a missing printer in all four languages.
- Online store leads: the customer order and the delivery note are printed through the common window, the buyer's phone and e-mail are filled in as before.
- When saving from the print window, the file name comes from the print form - for example, "Bon de livraison № 5 du 26.08.2026".
### es
- El puesto de caja imprime a través de la ventana de impresión común: el recibo se envía a la impresora de tickets o se muestra antes de imprimir, el albarán y la devolución se abren en la ventana de impresión, y el informe Z de la sesión de caja se imprime con un solo comando.
- En modo TPV el albarán de la caja se sigue imprimiendo sin precios.
- Etiquetas: la plantilla del adhesivo ahora aparece en el registro de plantillas y se edita como los demás formularios de impresión; la impresión en la impresora de etiquetas pasó al subsistema de impresión e informa de la impresora ausente en los cuatro idiomas.
- Prospectos de la tienda en línea: el pedido de cliente y el albarán de entrega se imprimen por la ventana común, el teléfono y el correo del comprador se rellenan como antes.
- Al guardar desde la ventana de impresión, el nombre del archivo procede del formulario de impresión, por ejemplo «Bon de livraison № 5 du 26.08.2026».

## 2.0.12.7
### ru
- На общее окно печати переведены все оставшиеся документы: реализация товаров и услуг с её накладными, счётом, чеком и актом, заказ покупателя с коммерческими предложениями и проформой, налоговая накладная, отгрузка товара, возвраты от покупателя, приходный и расходный кассовые ордера, кассовая смена, сверка взаиморасчётов, предложение поставщика, табель и прайс-лист.
- В окне печати любого из этих документов можно отметить сразу несколько форм, задать число копий, сохранить в файл и поправить макет под себя.
- Печать чека на чековый принтер осталась в одну команду, а настройки страницы чека теперь заданы в самой печатной форме и одинаковы при просмотре и при печати.
- Прайс-лист, как и раньше, спрашивает перед печатью иерархию и НДС, а табель формируется документом, и сокращения дней недели переведены на все языки программы.
### fr
- Tous les documents restants passent à la fenêtre d'impression commune : vente de biens et services avec ses bons de livraison, sa facture proforma, son ticket et son acte, commande client avec devis et proforma, facture de vente, bon de livraison, retours client, bons d'encaissement et de décaissement, session de caisse, acte de rapprochement, offre du fournisseur, feuille de temps et liste de prix.
- Dans la fenêtre d'impression de ces documents, on peut cocher plusieurs formulaires à la fois, indiquer le nombre de copies, enregistrer dans un fichier et adapter le modèle.
- L'impression du ticket sur l'imprimante à tickets reste en une seule commande, et la mise en page du ticket est désormais définie dans le formulaire imprimable : elle est identique à l'aperçu et à l'impression.
- La liste de prix demande toujours la hiérarchie et la TVA avant l'impression, la feuille de temps est produite par le document lui-même et les abréviations des jours de la semaine sont traduites dans toutes les langues du programme.
### en
- All remaining documents are switched to the common print window: sales of goods and services with its delivery notes, invoice for payment, receipt and act, customer order with quotations and proforma, tax invoice, goods shipment, customer returns, cash receipt and payment orders, cash session, reconciliation act, supplier offer, timesheet and price list.
- In the print window of these documents you can select several forms at once, set the number of copies, save to a file and adjust the template.
- Printing a receipt on the receipt printer is still a single command, and the receipt page setup now lives in the print form itself, so it is the same in preview and in printing.
- The price list still asks for hierarchy and VAT before printing, the timesheet is produced by the document itself, and the weekday abbreviations are translated into all languages of the application.
### es
- Todos los documentos restantes pasan a la ventana de impresión común: venta de bienes y servicios con sus albaranes, factura para pago, recibo y acta, pedido de cliente con presupuestos y proforma, factura de venta, albarán de salida, devoluciones de cliente, órdenes de ingreso y de pago de caja, sesión de caja, acta de conciliación, oferta del proveedor, hoja de horas y lista de precios.
- En la ventana de impresión de estos documentos se pueden marcar varios formularios a la vez, indicar el número de copias, guardar en un archivo y ajustar la plantilla.
- La impresión del recibo en la impresora de tickets sigue siendo un solo comando, y la configuración de página del recibo ahora está en el propio formulario de impresión: es la misma en la vista previa y en la impresión.
- La lista de precios sigue preguntando la jerarquía y el IVA antes de imprimir, la hoja de horas la genera el propio documento y las abreviaturas de los días de la semana están traducidas a todos los idiomas del programa.

## 2.0.12.6
### ru
- Исправлено проведение поступления товаров и услуг, оприходования товаров и налоговой накладной покупки: документы падали с ошибкой «Неверное имя колонки» из-за повторного добавления колонки партии, появившейся вместе со списанием по указанной партии.
### fr
- Correction de la validation de la réception de biens et services, de l'entrée de marchandises et de la facture d'achat : les documents échouaient avec l'erreur « Nom de colonne incorrect » à cause de l'ajout en double de la colonne de lot apparue avec la sortie par lot désigné.
### en
- Fixed posting of the receipt of goods and services, goods receipt and purchase tax invoice: the documents failed with the "Invalid column name" error because the batch column, introduced together with write-off by a chosen batch, was added twice.
### es
- Corregida la contabilización de la recepción de bienes y servicios, del alta de mercancías y de la factura de compra: los documentos fallaban con el error «Nombre de columna incorrecto» por añadir dos veces la columna de lote, aparecida junto con la baja por lote indicado.

## 2.0.12.5
### ru
- Исправлена ошибка при входе в программу: окно «Что нового» с закладками языков не открывалось из-за неверного имени свойства формы.
- Сбой окна «Что нового» больше не мешает начать работу: программа запускается, а окно можно открыть вручную в разделе Сервис.
### fr
- Correction d'une erreur à la connexion : la fenêtre « Nouveautés » avec les onglets de langue ne s'ouvrait pas à cause d'un nom de propriété de formulaire incorrect.
- Une défaillance de la fenêtre « Nouveautés » n'empêche plus de commencer le travail : le programme démarre et la fenêtre peut être ouverte manuellement dans la section Service.
### en
- Fixed an error at sign-in: the "What's new" window with language tabs did not open because of an incorrect form property name.
- A failure of the "What's new" window no longer prevents starting work: the application starts and the window can be opened manually in the Service section.
### es
- Corregido un error al iniciar sesión: la ventana «Novedades» con pestañas de idioma no se abría por un nombre incorrecto de propiedad del formulario.
- Un fallo de la ventana «Novedades» ya no impide empezar a trabajar: el programa arranca y la ventana se puede abrir manualmente en la sección Servicio.

## 2.0.12.4
### ru
- В окне «Что нового» появились закладки по языкам: список изменений ведётся и показывается на русском, французском, английском и испанском.
- При открытии окна сразу выбирается закладка языка текущего сеанса.
### fr
- La fenêtre « Nouveautés » comporte désormais des onglets de langue : la liste des modifications est tenue et affichée en russe, français, anglais et espagnol.
- À l'ouverture de la fenêtre, l'onglet de la langue de la session en cours est sélectionné automatiquement.
### en
- The "What's new" window now has language tabs: the list of changes is maintained and shown in Russian, French, English and Spanish.
- When the window opens, the tab of the current session language is selected automatically.
### es
- La ventana «Novedades» ahora tiene pestañas de idioma: la lista de cambios se mantiene y se muestra en ruso, francés, inglés y español.
- Al abrir la ventana se selecciona automáticamente la pestaña del idioma de la sesión actual.

## 2.0.12.3
### ru
- Окно «Что нового» открывалось пустым: текст переведён на HTML-документ, как в типовых конфигурациях, и теперь показывается со списком пунктов по каждой версии.
- Окно «Что нового» показывает все изменения, накопленные с прошлой публикации программы, а не только последнюю правку: список версий виден целиком, заголовок окна называет текущую версию.
### fr
- La fenêtre « Nouveautés » s'ouvrait vide : le texte est désormais affiché comme un document HTML, comme dans les configurations standard, avec la liste des points de chaque version.
- La fenêtre « Nouveautés » affiche toutes les modifications accumulées depuis la publication précédente du programme, et non seulement la dernière correction : la liste des versions est visible en entier et le titre de la fenêtre indique la version actuelle.
### en
- The "What's new" window opened empty: the text is now shown as an HTML document, as in standard configurations, with the list of items for each version.
- The "What's new" window shows all changes accumulated since the previous release of the application, not only the latest fix: the whole list of versions is visible and the window title names the current version.
### es
- La ventana «Novedades» se abría vacía: ahora el texto se muestra como un documento HTML, igual que en las configuraciones estándar, con la lista de puntos de cada versión.
- La ventana «Novedades» muestra todos los cambios acumulados desde la publicación anterior del programa, y no solo la última corrección: la lista de versiones se ve completa y el título de la ventana indica la versión actual.

## 2.0.12.2
### ru
- Печать документов переведена на общее окно: слева список печатных форм документа с флажками, справа просмотр, число копий, сохранение в PDF, Excel или табличный документ.
- Макет любой печатной формы можно изменить под себя: реестр макетов открывается в разделе Сервис — Управление данными, там же видно, какие макеты изменены и в какой версии программы, и одной командой возвращается поставляемый макет.
- Логотип и печать организации подставляются в печатные формы автоматически из карточки организации.
- На новое окно печати переведены: перемещение, списание и оприходование товаров, передача в переработку и поступление из переработки, корректировка долга, платёжная ведомость на аванс, поступление товаров и услуг, выплата зарплаты, заказ поставщику, налоговая накладная покупки.
- Окно «Что нового»: исправлен пустой отступ в начале текста.
- Новая схема нумерации версий: линейка 2.0, номер сборки растёт при каждой передаче на проверку, и все изменения сборки перечисляются в этом окне.
### fr
- L'impression des documents passe par une fenêtre commune : à gauche la liste des formulaires imprimables du document avec des cases à cocher, à droite l'aperçu, le nombre de copies et l'enregistrement en PDF, Excel ou document tabulaire.
- Le modèle de tout formulaire imprimable peut être adapté : le registre des modèles s'ouvre dans la section Service — Gestion de données, on y voit quels modèles ont été modifiés et dans quelle version du programme, et une seule commande restaure le modèle fourni.
- Le logo et le cachet de l'organisation sont insérés automatiquement dans les formulaires imprimables depuis la fiche de l'organisation.
- Sont passés à la nouvelle fenêtre d'impression : transfert, sortie et entrée de marchandises, transfert en sous-traitance et réception de sous-traitance, correction de dette, paiement anticipé, bon de réception, paiement des salaires, commande au fournisseur, facture d'achat.
- Fenêtre « Nouveautés » : le retrait vide en début de texte est corrigé.
- Nouveau schéma de numérotation des versions : ligne 2.0, le numéro de build augmente à chaque remise pour vérification et toutes les modifications du build sont listées dans cette fenêtre.
### en
- Document printing now goes through a common window: the list of the document's print forms with check boxes on the left, preview, number of copies and saving to PDF, Excel or a spreadsheet document on the right.
- The template of any print form can be customized: the template registry opens in the Service — Data management section, it shows which templates were changed and in which version of the application, and a single command restores the supplied template.
- The company logo and stamp are inserted into print forms automatically from the company card.
- Switched to the new print window: transfer, write-off and receipt of goods, transfer for processing and receipt from processing, debt adjustment, advance payroll sheet, receipt of goods and services, salary payment, order to supplier, purchase tax invoice.
- "What's new" window: the empty indent at the beginning of the text is fixed.
- New version numbering scheme: line 2.0, the build number increases with every handover for testing, and all changes of the build are listed in this window.
### es
- La impresión de documentos pasa por una ventana común: a la izquierda la lista de formularios de impresión del documento con casillas, a la derecha la vista previa, el número de copias y el guardado en PDF, Excel o documento tabular.
- La plantilla de cualquier formulario de impresión se puede adaptar: el registro de plantillas se abre en la sección Servicio — Gestión de datos, allí se ve qué plantillas se han modificado y en qué versión del programa, y un solo comando restaura la plantilla suministrada.
- El logotipo y el sello de la organización se insertan automáticamente en los formularios de impresión desde la ficha de la organización.
- Pasan a la nueva ventana de impresión: traslado, baja y alta de mercancías, transferencia a procesamiento y recepción de procesamiento, corrección de deuda, pago anticipado, recepción de bienes y servicios, pago de salarios, pedido al proveedor y factura de compra.
- Ventana «Novedades»: se ha corregido el espacio vacío al inicio del texto.
- Nuevo esquema de numeración de versiones: línea 2.0, el número de compilación aumenta en cada entrega para revisión y todos los cambios de la compilación se enumeran en esta ventana.

## 1.0.12.1
### ru
- Производственный контур: статусы заказов «В производстве», «Передан субподрядчику» и «Получен от субподрядчика» пересчитываются по связанным документам.
- Выпуск продукции: несколько позиций готовой продукции в одном документе, себестоимость и НДС распределяются по весам технологических карт.
- Поступление из переработки: стоимость услуг переработчика капитализируется в себестоимость продукции, долг переработчику попадает во взаиморасчёты.
- Товары в переработке ведутся в разрезе заказа покупателя, в отчёте появился отбор по заказу.
- Рабочее место «Заказы в производстве»: заказы со статусами, товары заказа и связанные документы в одном окне.
- Начальная страница: дашборды продаж, склада и производства с показателями дня, месяца и рекордами.
- Роль «Оператор производства» больше не видит цены и суммы в документах товародвижения и производства.
- По одному заказу покупателя допускается несколько реализаций (частичные отгрузки).
- Меню перегруппировано по бизнес-процессам: главные документы раздела выделены в «Важное», второстепенные команды убраны в «См. также».
- Элементы меню переведены на французский, английский и испанский языки.
- Механизм обновления данных: версия базы, обработчики обновления и окно «Что нового» с описанием изменений.
- Исправлено падение при открытии реализации товаров и услуг, а также ряд ошибок в запросах и печатных формах.
### fr
- Circuit de production : les statuts des commandes « En production », « Transmis au sous-traitant » et « Reçu du sous-traitant » sont recalculés d'après les documents liés.
- Fabrication : plusieurs articles de produits finis dans un même document, le coût de revient et la TVA sont répartis selon les poids des fiches techniques.
- Réception de sous-traitance : le coût des services du sous-traitant est capitalisé dans le coût de revient des produits, la dette envers le sous-traitant entre dans les règlements mutuels.
- Les marchandises en sous-traitance sont suivies par commande client, et le rapport dispose d'un filtre par commande.
- Poste de travail « Commandes en production » : les commandes avec leurs statuts, les articles de la commande et les documents liés dans une seule fenêtre.
- Page d'accueil : tableaux de bord des ventes, du stock et de la production avec les indicateurs du jour, du mois et les records.
- Le rôle « Opérateur de production » ne voit plus les prix ni les montants dans les documents de mouvement de marchandises et de production.
- Une même commande client peut donner lieu à plusieurs ventes (livraisons partielles).
- Le menu est réorganisé par processus métier : les documents principaux de chaque section sont placés dans « Important », les commandes secondaires dans « Voir aussi ».
- Les éléments de menu sont traduits en français, en anglais et en espagnol.
- Mécanisme de mise à jour des données : version de la base, gestionnaires de mise à jour et fenêtre « Nouveautés » avec la description des modifications.
- Correction du plantage à l'ouverture de la vente de biens et services, ainsi que de plusieurs erreurs dans les requêtes et les formulaires imprimables.
### en
- Production circuit: the order statuses "In production", "Transferred to subcontractor" and "Received from subcontractor" are recalculated from the related documents.
- Production output: several finished product items in one document, cost and VAT are distributed by the weights of the technological charts.
- Receipt from processing: the processor's service cost is capitalized into the product cost, and the debt to the processor goes into mutual settlements.
- Goods in processing are tracked by customer order, and the report now has a filter by order.
- "Orders in production" workplace: orders with statuses, order items and related documents in one window.
- Home page: sales, warehouse and production dashboards with daily and monthly indicators and records.
- The "Production operator" role no longer sees prices and amounts in goods movement and production documents.
- One customer order can have several sales documents (partial shipments).
- The menu is regrouped by business processes: the main documents of each section are placed in "Important", secondary commands in "See also".
- Menu items are translated into French, English and Spanish.
- Data update mechanism: infobase version, update handlers and the "What's new" window with the description of changes.
- Fixed the crash when opening a sales document, as well as a number of errors in queries and print forms.
### es
- Circuito de producción: los estados de los pedidos «En producción», «Transferido al subcontratista» y «Recibido del subcontratista» se recalculan según los documentos vinculados.
- Fabricación: varias posiciones de productos terminados en un mismo documento, el coste y el IVA se distribuyen según los pesos de las fichas técnicas.
- Recepción de procesamiento: el coste de los servicios del procesador se capitaliza en el coste del producto y la deuda con el procesador entra en las liquidaciones mutuas.
- Las mercancías en procesamiento se llevan por pedido de cliente y el informe tiene un filtro por pedido.
- Puesto de trabajo «Pedidos en producción»: pedidos con sus estados, artículos del pedido y documentos vinculados en una sola ventana.
- Página de inicio: paneles de ventas, almacén y producción con indicadores del día, del mes y récords.
- El rol «Operador de producción» ya no ve precios ni importes en los documentos de movimiento de mercancías y de producción.
- Un mismo pedido de cliente admite varias ventas (envíos parciales).
- El menú se ha reagrupado por procesos de negocio: los documentos principales de cada sección están en «Importante» y los comandos secundarios en «Véase también».
- Los elementos del menú están traducidos al francés, inglés y español.
- Mecanismo de actualización de datos: versión de la base, controladores de actualización y ventana «Novedades» con la descripción de los cambios.
- Corregido el fallo al abrir la venta de bienes y servicios, así como varios errores en consultas y formularios de impresión.

## 1.0.11.1
### ru
- Первый релиз maERP: продажи, закупки, склад, производство, казначейство, зарплата и кадры, бухгалтерия.
### fr
- Première version de maERP : ventes, achats, stock, production, trésorerie, paie et RH, comptabilité.
### en
- First maERP release: sales, purchases, warehouse, production, treasury, payroll and HR, accounting.
### es
- Primera versión de maERP: ventas, compras, almacén, producción, tesorería, nóminas y RR. HH., contabilidad.
