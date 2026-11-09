# Список изменений maERP

Секции переносятся сюда из общего макета `ОписаниеИзменений` при публикации CF
(правило в `docs/RELEASING.md`). Внутри релиза секции идут по сборкам, от новых
к старым, на всех языках конфигурации — ровно так, как их видел владелец в окне
«Что нового».

# Релиз 2.0.16.150 (2026-11-09)

Поставка: `maERP-2.0.16.150.cf`; обновление с опубликованных релизов 1.0.11.1 … 2.0.15.71 — `maERP-2.0.16.150.cfu`.
Станки, ордерные склады, валюта и фирменная печать: рабочие места производства, закупок и управления станками, ордерные склады, переработка по нескольким
заказам, себестоимость и маржа по партиям, документы в валюте, раздельный управленческий и налоговый учёт, фирменные
печатные формы с предпросмотром, перестроенное меню, отчёты и список товаров.

## 2.0.16.150
### ru
- Предпросмотр в окне печати больше не искажает печатные формы с арабским текстом и шрифтами, которых нет на сервере 1С. Раньше такой текст вылезал из ячеек и наезжал на соседний: просмотр собирался шрифтами сервера. Теперь в приложении 1С он собирается шрифтами компьютера пользователя — теми же, которыми печатает принтер. В браузере просмотр, как и раньше, собирается на сервере.
### fr
- L'aperçu de la fenêtre d'impression ne déforme plus les formulaires imprimables contenant du texte arabe ou des polices absentes du serveur 1C. Auparavant, ce texte débordait des cellules et chevauchait le texte voisin, car l'aperçu était généré avec les polices du serveur. Dans l'application 1C, il est désormais généré avec les polices de l'ordinateur de l'utilisateur, les mêmes que celles utilisées par l'imprimante. Dans le navigateur, l'aperçu reste généré sur le serveur.
### en
- The print window preview no longer distorts print forms with Arabic text or with fonts that are missing on the 1C server. Previously such text spilled out of its cells and overlapped neighbouring text because the preview was built with the server's fonts. In the 1C application it is now built with the fonts of the user's computer, the same ones the printer uses. In a browser the preview is still built on the server.
### es
- La vista previa de la ventana de impresión ya no deforma los formularios de impresión con texto árabe o con fuentes que no están en el servidor 1C. Antes ese texto se salía de las celdas y se superponía al texto vecino, porque la vista previa se generaba con las fuentes del servidor. En la aplicación 1C ahora se genera con las fuentes del ordenador del usuario, las mismas que usa la impresora. En el navegador la vista previa sigue generándose en el servidor.

## 2.0.16.149
### ru
- В задании на пересчёт в строки товаров теперь можно выбрать не только товары, но и продукцию, полуфабрикаты и сырьё. Услуги и комплекты в выборе по-прежнему не предлагаются: складских остатков у них нет.
### fr
- Dans la tâche d'inventaire, les lignes d'articles acceptent désormais non seulement les marchandises, mais aussi les produits finis, les produits semi-finis et les matières premières. Les services et les kits ne sont toujours pas proposés : ils n'ont pas de stock.
### en
- In the stocktaking task, the goods lines now accept not only goods but also finished products, semi-finished products and raw materials. Services and kits are still not offered for selection: they have no stock balances.
### es
- En la tarea de recuento, las líneas de artículos ahora admiten no solo mercancías, sino también productos terminados, semielaborados y materias primas. Los servicios y los kits siguen sin ofrecerse: no tienen existencias.

## 2.0.16.148
### ru
- Групповое изменение реквизитов (Настройки программы → Обслуживание) снова открывается. Раньше обработка останавливалась с сообщением, что она предназначена для платформы 8.3, и не запускалась вовсе.
### fr
- La modification groupée des attributs (Paramètres du programme → Maintenance) s'ouvre de nouveau. Auparavant, le traitement s'arrêtait avec un message indiquant qu'il était conçu pour la plate-forme 8.3 et ne démarrait pas du tout.
### en
- Bulk attribute editing (Application settings → Maintenance) opens again. Previously the data processor stopped with a message that it was intended for platform 8.3 and did not start at all.
### es
- La modificación masiva de atributos (Ajustes del programa → Mantenimiento) vuelve a abrirse. Antes el procesamiento se detenía con un mensaje de que estaba diseñado para la plataforma 8.3 y no se iniciaba.

## 2.0.16.147
### ru
- Настройки «Компания и учёт» и производственный календарь: страна календаря выбирается из списка стран, для которых в программе есть праздничные дни, например «Марокко (MA)». Раньше код страны вписывался вручную двумя буквами, и опечатка оставляла календарь без праздников.
### fr
- Paramètres « Entreprise et comptabilité » et calendrier de production : le pays du calendrier se choisit dans la liste des pays dont les jours fériés sont fournis par le programme, par exemple « Maroc (MA) ». Auparavant, le code du pays se saisissait à la main en deux lettres, et une faute de frappe laissait le calendrier sans jours fériés.
### en
- "Company and accounting" settings and production calendar: the calendar country is chosen from the list of countries whose public holidays the application provides, for example "Morocco (MA)". Previously the two-letter country code was typed by hand, and a typo left the calendar without holidays.
### es
- Ajustes «Empresa y contabilidad» y calendario de producción: el país del calendario se elige de la lista de países cuyos días festivos incluye el programa, por ejemplo «Marruecos (MA)». Antes el código del país se escribía a mano con dos letras, y un error de escritura dejaba el calendario sin festivos.

## 2.0.16.146
### ru
- Рабочие места производства и закупок: после закрытия документа, открытого из таблицы, курсор остаётся на той строке, с которой документ открывали. Раньше таблицы перечитывались, и курсор уходил на первую строку — на закладке «Продукция» производства вместе с ним менялся и заказ нижних закладок.
### fr
- Postes de production et d'achats : après la fermeture d'un document ouvert depuis un tableau, le curseur reste sur la ligne d'où il a été ouvert. Auparavant, les tableaux étaient relus et le curseur revenait à la première ligne — dans l'onglet « Production » du poste de production, la commande des onglets inférieurs changeait avec lui.
### en
- Production and purchasing workstations: after closing a document opened from a table, the cursor stays on the line it was opened from. Previously the tables were reloaded and the cursor jumped to the first line — on the "Products" tab of the production workstation, the order shown on the lower tabs changed along with it.
### es
- Puestos de producción y de compras: al cerrar un documento abierto desde una tabla, el cursor permanece en la línea desde la que se abrió. Antes las tablas se releían y el cursor volvía a la primera línea; en la pestaña «Producción» del puesto de producción, con él cambiaba también el pedido de las pestañas inferiores.

## 2.0.16.145
### ru
- Поступление из переработки: новый документ, заполненный по передаче, проведённой сегодня, больше не сообщает, что сырья у подрядчика нет. Раньше остатки у подрядчика брались на начало дня, и помогала только смена даты документа.
### fr
- Réception de sous-traitance : un nouveau document rempli à partir d'un transfert validé aujourd'hui n'indique plus qu'il n'y a pas de matières chez le sous-traitant. Auparavant, le stock chez le sous-traitant était lu au début de la journée, et seul un changement de date du document aidait.
### en
- Subcontracting receipt: a new document filled from a transfer posted today no longer reports that the subcontractor holds no materials. Previously the subcontractor's stock was read as of the start of the day, and only changing the document date helped.
### es
- Recepción de subcontratación: un documento nuevo rellenado desde un envío contabilizado hoy ya no indica que el subcontratista no tiene materias. Antes el stock del subcontratista se leía al inicio del día, y solo ayudaba cambiar la fecha del documento.

## 2.0.16.144
### ru
- Рабочее место производства: новая верхняя закладка «Документы» рядом с «Заказами» и «Продукцией». На ней одна таблица на всю высоту окна, сверху — вид, режим показа и отборы: подрядчик, склад, период (по умолчанию — текущий месяц), «Только незакрытые». Документы — от новых к старым, по 50 на странице.
- Вид «Переработка», режим «Документы»: передачи в переработку и поступления из переработки с подрядчиком, складом, заказами (у документа нескольких заказов — все его заказы), количеством продукции, которую ещё ждут от подрядчика, суммой услуг и статусом. «Только незакрытые» — передачи, по которым ждут продукцию, и черновики (период — не больше трёх месяцев).
- Режим «Строки» — строки сырья передач и продукции поступлений текущей страницы с заказом и клиентом каждой строки. Режим «У подрядчиков (на сейчас)» — что сейчас лежит у подрядчиков по передачам и заказам и какая продукция ожидается к приёму.
- Команды закладки: «Провести» и «Отменить проведение» выделенных документов (документ нескольких заказов — в его форме), «Поступление из переработки» по передаче текущей строки, «Печать» документа строки; двойной щелчок открывает документ. Суммы видны по праву «Видеть суммы (производство)».
- Вид «Выпуски»: ручные выпуски и автовыпуски периода с основанием и продукцией. В режиме «Строки» можно ввести выпуск без заказа прямо строкой: продукция и количество (склад — из отбора закладки, без него — склад выпуска по умолчанию) — создаётся и проводится выпуск без основания на основную организацию пользователя; его строку можно поправить или удалить там же.
- Вид «Требования-накладные» (виден, если не включён автовыпуск при отгрузке): требования периода со станком, заказом, планом и фактом, статусом и выпусками по ним; в режиме «Строки» — материалы требований. Команда «Статус»: «Запустить», «Завершить» (с вводом выпущенного количества), «Отменить», «Вернуть в работу» — как в рабочем месте станков.
### fr
- Poste de production : nouvel onglet supérieur « Documents » à côté de « Commandes » et « Production ». Il affiche un seul tableau sur toute la hauteur, avec en haut le type, le mode d'affichage et les filtres : sous-traitant, entrepôt, période (par défaut le mois en cours), « Non clôturés seulement ». Documents du plus récent au plus ancien, 50 par page.
- Type « Sous-traitance », mode « Documents » : transferts et réceptions de sous-traitance avec sous-traitant, entrepôt, commandes (toutes les commandes d'un document de plusieurs commandes), quantité de produits encore attendue du sous-traitant, montant des services et statut. « Non clôturés seulement » : transferts avec des produits attendus et brouillons (période de trois mois au plus).
- Mode « Lignes » : lignes de matières des transferts et de produits des réceptions de la page, avec la commande et le client de chaque ligne. Mode « Chez les sous-traitants (maintenant) » : ce qui se trouve actuellement chez les sous-traitants par transfert et commande, et les produits attendus à la réception.
- Commandes de l'onglet : « Valider » et « Annuler la validation » des documents sélectionnés (un document de plusieurs commandes se valide dans son formulaire), « Réception de sous-traitance » selon le transfert de la ligne, « Impression » du document de la ligne ; un double clic ouvre le document. Les montants sont visibles selon le droit « Voir les montants (production) ».
- Type « Productions » : productions manuelles et automatiques de la période avec leur base et leurs produits. En mode « Lignes », une production sans commande se saisit directement en ligne : produit et quantité (entrepôt du filtre de l'onglet, sinon l'entrepôt de production par défaut) — une production sans base est créée et validée pour l'organisation principale de l'utilisateur ; sa ligne se modifie ou se supprime au même endroit.
- Type « Bons de consommation » (visible si la production automatique à l'expédition n'est pas activée) : bons de la période avec machine, commande, prévu et réel, statut et productions associées ; en mode « Lignes », matières des bons. Commande « Statut » : « Lancer », « Terminer » (avec saisie de la quantité produite), « Annuler », « Remettre en cours » — comme dans le poste des machines.
### en
- Production workstation: new top tab "Documents" next to "Orders" and "Products". It shows one full-height table with the kind, display mode and filters on top: subcontractor, warehouse, period (current month by default), "Open only". Documents are listed newest first, 50 per page.
- Kind "Subcontracting", mode "Documents": subcontracting transfers and receipts with subcontractor, warehouse, orders (all orders of a several-orders document), quantity of products still expected from the subcontractor, services amount and status. "Open only" shows transfers with expected products and drafts (period of three months at most).
- Mode "Lines": material lines of transfers and product lines of receipts on the page, with the order and customer of each line. Mode "At subcontractors (now)": what is currently held by subcontractors per transfer and order, and the products expected to be received.
- Tab commands: "Post" and "Unpost" for the selected documents (a several-orders document is posted in its form), "Subcontract receipt" for the transfer of the current line, "Print" for the line document; a double click opens the document. Amounts are shown according to the "See amounts (production)" right.
- Kind "Outputs": manual and automatic outputs of the period with their basis and products. In mode "Lines" an output without an order can be entered right as a line: product and quantity (warehouse from the tab filter, otherwise the default output warehouse) — an output without a basis is created and posted for the user's main company; its line can be edited or deleted in the same place.
- Kind "Requisitions" (shown when automatic output on shipment is off): requisitions of the period with machine, order, planned and actual quantity, status and related outputs; in mode "Lines", requisition materials. "Status" command: "Start", "Complete" (entering the produced quantity), "Cancel", "Return to work" — as in the machines workstation.
### es
- Puesto de producción: nueva pestaña superior «Documentos» junto a «Pedidos» y «Producción». Muestra una sola tabla a toda la altura, con el tipo, el modo de visualización y los filtros arriba: subcontratista, almacén, período (por defecto el mes en curso), «Solo abiertos». Documentos de más reciente a más antiguo, 50 por página.
- Tipo «Subcontratación», modo «Documentos»: envíos y recepciones de subcontratación con subcontratista, almacén, pedidos (todos los pedidos de un documento de varios pedidos), cantidad de productos aún pendiente del subcontratista, importe de servicios y estado. «Solo abiertos»: envíos con productos pendientes y borradores (período de tres meses como máximo).
- Modo «Líneas»: líneas de materias de los envíos y de productos de las recepciones de la página, con el pedido y el cliente de cada línea. Modo «En subcontratistas (ahora)»: lo que tienen ahora los subcontratistas por envío y pedido, y los productos pendientes de recibir.
- Comandos de la pestaña: «Contabilizar» y «Anular contabilización» de los documentos seleccionados (un documento de varios pedidos se contabiliza en su formulario), «Recepción de subcontratación» según el envío de la línea, «Impresión» del documento de la línea; un doble clic abre el documento. Los importes se ven según el derecho «Ver importes (producción)».
- Tipo «Producciones»: producciones manuales y automáticas del período con su base y productos. En el modo «Líneas», una producción sin pedido se introduce directamente como línea: producto y cantidad (almacén del filtro de la pestaña o, si no hay, el almacén de producción por defecto) — se crea y contabiliza una producción sin base para la organización principal del usuario; su línea se corrige o elimina en el mismo lugar.
- Tipo «Vales de consumo» (visible si la producción automática al enviar no está activada): vales del período con máquina, pedido, plan y real, estado y producciones asociadas; en el modo «Líneas», las materias de los vales. Comando «Estado»: «Iniciar», «Terminar» (indicando la cantidad producida), «Cancelar», «Devolver a producción» — como en el puesto de máquinas.

## 2.0.16.143
### ru
- Рабочее место производства, режим нескольких заказов: выделите в «Заказах» или в «Продукции» больше одного заказа — закладки «Передача в переработку» и «Поступления из переработки» покажут строки всех выделенных заказов с колонкой «Заказ», в заголовке закладки — число заказов.
- Новая строка передачи в этом режиме идёт в общую передачу подрядчику (документ нескольких заказов): заказ строки выбирается из выделенных, следующие строки того же подрядчика за сегодня дописываются в ту же передачу. В передачу одного заказа такие строки не попадают.
- Команда «Заполнить по потребностям» на закладке «Передача в переработку» (видна в режиме нескольких заказов): подрядчик, склад и способ — по этапам переработчика (сырьё ПФ подрядчика, ещё не переданное), по выпущенным ПФ (свои выпущенные ПФ для подрядчика) или пустая (строки вручную). Строки предпросмотра можно снять или поправить количество; «Заполнить» создаёт и проводит общую передачу. Если пока окно было открыто данные изменились, передача не создаётся и предпросмотр пересчитывается.
- Поступление из переработки в режиме нескольких заказов: в колонке «Передача» — передачи всех выделенных заказов, включая общие; продукция общей передачи выбирается с её заказом.
- В быстром выборе передачи в переработку (например, в поле «Основание» поступления из переработки) рядом с номером и датой виден подрядчик.
### fr
- Poste de production, mode plusieurs commandes : sélectionnez plus d'une commande dans « Commandes » ou « Production » : les onglets « Transfert en sous-traitance » et « Réceptions de sous-traitance » affichent les lignes de toutes les commandes sélectionnées avec une colonne « Commande », et le titre de l'onglet indique le nombre de commandes.
- Dans ce mode, une nouvelle ligne de transfert va dans un transfert commun au sous-traitant (document de plusieurs commandes) : la commande de la ligne se choisit parmi les commandes sélectionnées, les lignes suivantes du même sous-traitant du jour s'ajoutent au même transfert. Elles ne vont jamais dans un transfert d'une seule commande.
- Commande « Remplir selon les besoins » dans l'onglet « Transfert en sous-traitance » (visible en mode plusieurs commandes) : sous-traitant, entrepôt et mode — par étapes du sous-traitant (matières des semi-finis du sous-traitant non encore transférées), par semi-finis produits (vos semi-finis produits pour le sous-traitant) ou vide (lignes à la main). On peut décocher des lignes de l'aperçu ou corriger les quantités ; « Remplir » crée et valide le transfert commun. Si les données ont changé pendant que la fenêtre était ouverte, le transfert n'est pas créé et l'aperçu est recalculé.
- Réception de sous-traitance en mode plusieurs commandes : la colonne « Transfert » propose les transferts de toutes les commandes sélectionnées, y compris les transferts communs ; les produits d'un transfert commun se choisissent avec leur commande.
- Dans le choix rapide d'un transfert en sous-traitance (par exemple, le champ « Base » d'une réception de sous-traitance), le sous-traitant s'affiche à côté du numéro et de la date.
### en
- Production workstation, several-orders mode: select more than one order in "Orders" or "Products": the "Subcontracting transfer" and "Subcontracting receipts" tabs show the lines of all selected orders with an "Order" column, and the tab title shows the number of orders.
- In this mode a new transfer line goes to a shared transfer to the subcontractor (a several-orders document): the line order is chosen from the selected orders, and the next lines of the same subcontractor for today are added to the same transfer. Such lines never go to a single-order transfer.
- "Fill by requirements" command on the "Subcontracting transfer" tab (visible in several-orders mode): subcontractor, warehouse and method — by subcontractor stages (materials of the subcontractor's semi-finished goods not yet transferred), by produced semi-finished goods (your own semi-finished goods produced for the subcontractor) or empty (lines by hand). Preview lines can be unticked or their quantities corrected; "Fill" creates and posts the shared transfer. If the data changed while the window was open, the transfer is not created and the preview is recalculated.
- Subcontracting receipt in several-orders mode: the "Transfer" column offers the transfers of all selected orders, including shared ones; products of a shared transfer are chosen with their order.
- In the quick choice of a subcontracting transfer (for example, the "Basis" field of a subcontracting receipt) the subcontractor is shown next to the number and date.
### es
- Puesto de producción, modo de varios pedidos: seleccione más de un pedido en «Pedidos» o «Producción»: las pestañas «Envío a subcontratación» y «Recepciones de subcontratación» muestran las líneas de todos los pedidos seleccionados con una columna «Pedido», y el título de la pestaña indica el número de pedidos.
- En este modo, una línea nueva de envío va a un envío común al subcontratista (documento de varios pedidos): el pedido de la línea se elige entre los seleccionados y las líneas siguientes del mismo subcontratista del día se añaden al mismo envío. Nunca van a un envío de un solo pedido.
- Comando «Rellenar según necesidades» en la pestaña «Envío a subcontratación» (visible en modo de varios pedidos): subcontratista, almacén y modo — por etapas del subcontratista (materias de los semielaborados del subcontratista aún no enviadas), por semielaborados producidos (sus semielaborados producidos para el subcontratista) o vacío (líneas a mano). Las líneas de la vista previa se pueden desmarcar o corregir; «Rellenar» crea y contabiliza el envío común. Si los datos cambiaron mientras la ventana estaba abierta, el envío no se crea y la vista previa se recalcula.
- Recepción de subcontratación en modo de varios pedidos: la columna «Envío» ofrece los envíos de todos los pedidos seleccionados, incluidos los comunes; los productos de un envío común se eligen con su pedido.
- En la selección rápida de un envío a subcontratación (por ejemplo, el campo «Base» de una recepción de subcontratación) se muestra el subcontratista junto al número y la fecha.

## 2.0.16.142
### ru
- Передача в переработку по нескольким заказам: одним документом подрядчику можно передать материалы разных заказов и разных клиентов. В форме передачи отметьте «Несколько заказов» — у строк товаров и ожидаемой продукции появится колонка «Заказ». Без флажка документ работает как раньше, по одному заказу.
- Поступление из переработки по такой передаче принимает продукцию всех её заказов одним документом: заказ каждой строки берётся из передачи, сырьё списывается отдельно по каждому заказу, себестоимость продукции заказа складывается только из его сырья. Если сырья одного заказа не хватает, недостающее не берётся из сырья другого заказа — документ не проводится и называет заказ.
- Акт передачи и акт приёмки по нескольким заказам печатают список заказов с клиентами и группируют строки по заказу.
- Стадии заказов, потребности производства, связанные документы, отчёт по переработке и прослеживаемость партий учитывают заказ каждой строки.
- Проведённую передачу нельзя перенести на другой заказ или подрядчика простой записью — только перепроведением; после поступления продукции по ней заказ, подрядчик и дата не меняются, а отмена проведения и удаление запрещены.
- В рабочем месте производства строки документов по нескольким заказам видны на закладке каждого заказа; правятся они в форме документа.
- При обновлении заказ строк существующих передач и поступлений заполняется по их движениям; документы, у которых заказ шапки расходился с движениями, записываются в журнал регистрации.
- Заказ, продукция которого принята поступлением из переработки по передаче, теперь получает стадию «Получен от субподрядчика» — раньше оставался «Передан субподрядчику».
### fr
- Transfert en sous-traitance pour plusieurs commandes : un seul document peut envoyer au sous-traitant les matières de commandes et de clients différents. Dans le transfert, cochez « Plusieurs commandes » : une colonne « Commande » apparaît dans les lignes d'articles et de produits attendus. Sans la case, le document fonctionne comme avant, pour une seule commande.
- La réception de sous-traitance d'un tel transfert reçoit les produits de toutes ses commandes en un seul document : la commande de chaque ligne vient du transfert, les matières sont sorties séparément par commande, et le coût des produits d'une commande ne comprend que ses propres matières. S'il manque des matières pour une commande, elles ne sont pas prises sur une autre commande : le document n'est pas validé et indique la commande.
- Le bon de transfert et le procès-verbal de réception pour plusieurs commandes impriment la liste des commandes avec les clients et regroupent les lignes par commande.
- Les étapes des commandes, les besoins de production, les documents liés, le rapport de sous-traitance et la traçabilité des lots tiennent compte de la commande de chaque ligne.
- Un transfert validé ne peut plus être rattaché à une autre commande ou à un autre sous-traitant par un simple enregistrement, seulement en le revalidant ; après une réception sur ce transfert, la commande, le sous-traitant et la date ne changent plus, l'annulation et la suppression sont interdites.
- Dans le poste de production, les lignes des documents à plusieurs commandes s'affichent dans l'onglet de chaque commande ; elles se modifient dans le formulaire du document.
- Lors de la mise à jour, la commande des lignes des transferts et réceptions existants est remplie d'après leurs mouvements ; les documents dont la commande d'en-tête divergeait des mouvements sont inscrits au journal.
- Une commande dont les produits sont reçus par une réception de sous-traitance sur un transfert passe désormais au statut « Reçue du sous-traitant » ; avant, elle restait « Transmise au sous-traitant ».
### en
- Subcontracting transfer for several orders: one document can send the subcontractor materials of different orders and different customers. In the transfer, check "Several orders": an "Order" column appears in the item and expected product lines. Without the flag the document works as before, for one order.
- A subcontracting receipt for such a transfer receives the products of all its orders in one document: each line's order comes from the transfer, materials are written off separately per order, and the cost of an order's products includes only its own materials. If one order lacks materials, they are not taken from another order: the document is not posted and names the order.
- The transfer note and the acceptance report for several orders print the list of orders with customers and group lines by order.
- Order stages, production requirements, related documents, the subcontracting report and lot traceability take each line's order into account.
- A posted transfer can no longer be moved to another order or subcontractor by a plain save, only by reposting; once products have been received against it, the order, subcontractor and date cannot change, and unposting and deletion are blocked.
- In the production workstation, lines of multi-order documents are shown on each order's tab; they are edited in the document form.
- During the update, the line order of existing transfers and receipts is filled from their movements; documents whose header order differed from the movements are written to the event log.
- An order whose products are received by a subcontracting receipt against a transfer now gets the "Received from subcontractor" status; before, it stayed "Sent to subcontractor".
### es
- Envío a subcontratación para varios pedidos: un solo documento puede enviar al subcontratista materiales de pedidos y clientes distintos. En el envío, marque «Varios pedidos»: aparece una columna «Pedido» en las líneas de artículos y de productos esperados. Sin la casilla, el documento funciona como antes, para un solo pedido.
- La recepción de subcontratación de ese envío recibe los productos de todos sus pedidos en un solo documento: el pedido de cada línea viene del envío, las materias se dan de baja por separado por pedido y el coste de los productos de un pedido incluye solo sus propias materias. Si faltan materias de un pedido, no se toman de otro: el documento no se contabiliza e indica el pedido.
- El albarán de envío y el acta de recepción de varios pedidos imprimen la lista de pedidos con sus clientes y agrupan las líneas por pedido.
- Las etapas de los pedidos, las necesidades de producción, los documentos relacionados, el informe de subcontratación y la trazabilidad de lotes tienen en cuenta el pedido de cada línea.
- Un envío contabilizado ya no puede pasar a otro pedido o subcontratista con un simple guardado, solo volviendo a contabilizarlo; tras una recepción por él, el pedido, el subcontratista y la fecha no cambian, y la anulación y la eliminación están bloqueadas.
- En el puesto de producción, las líneas de documentos de varios pedidos se muestran en la pestaña de cada pedido; se editan en el formulario del documento.
- Durante la actualización, el pedido de las líneas de envíos y recepciones existentes se rellena según sus movimientos; los documentos cuyo pedido de cabecera difería de los movimientos se anotan en el registro de eventos.
- Un pedido cuyos productos se reciben con una recepción de subcontratación por un envío pasa ahora al estado «Recibido del subcontratista»; antes se quedaba en «Enviado al subcontratista».

## 2.0.16.141
### ru
- Карточка товара перестроена. Вверху — небольшое фото и шапка: тип товара (первым — от него зависит вид карточки), наименование и артикул, категория и способ пополнения, остаток и цены. Смена типа больше не сдвигает поля шапки.
- Карточка всегда открывается на закладке «Описание и свойства»: описание товара, бренд, качество, товарная группа и дополнительные свойства. Единицы, вес, ставка НДС, поставщик, производитель и упаковки — на закладке «Учёт», код и прочее служебное — на «Служебном».
- На закладках «Склад» и «Производство» каждая таблица — на своей вкладке: остатки, минимумы и максимумы по складам, ячейки и условия хранения, материалы на станках; техкарта, станки, выработка станков, «где используется». Короткие поля с близким смыслом стоят в одну строку.
- Цены, техкарта, остатки и штрихкоды снова загружаются при переходе на свою закладку.
### fr
- La fiche article a été réorganisée. En haut : une petite photo et l'en-tête : le type d'article (en premier, car il détermine l'aspect de la fiche), la désignation et la référence, la catégorie et le mode de réapprovisionnement, le stock et les prix. Changer le type ne décale plus les champs de l'en-tête.
- La fiche s'ouvre toujours sur l'onglet « Description et propriétés » : description de l'article, marque, qualité, groupe d'articles et propriétés supplémentaires. Unités, poids, taux de TVA, fournisseur, fabricant et conditionnements sont dans l'onglet « Gestion », le code et les autres données techniques dans « Service ».
- Dans les onglets « Stock » et « Production », chaque tableau a son propre sous-onglet : stocks, minimums et maximums par entrepôt, emplacements et conditions de stockage, matières sur les machines ; gamme de fabrication, machines, rendement des machines, « où est utilisé ». Les champs courts de sens proche sont sur une même ligne.
- Les prix, la gamme de fabrication, les stocks et les codes-barres se chargent de nouveau à l'ouverture de leur onglet.
### en
- The item card has been reorganized. At the top: a small photo and the header: item type (first, as it defines how the card looks), name and SKU, category and replenishment method, stock and prices. Changing the type no longer shifts the header fields.
- The card always opens on the "Description and properties" tab: item description, brand, quality, product group and additional properties. Units, weight, VAT rate, supplier, manufacturer and packaging are on the "Accounting" tab; the code and other technical data are on "Service".
- On the "Stock" and "Production" tabs, each table has its own sub-tab: stock, minimums and maximums by warehouse, bins and storage conditions, materials on machines; production routing, machines, machine output, "where used". Short fields with related meaning share one line.
- Prices, production routing, stock and barcodes load again when their tab is opened.
### es
- Se ha reorganizado la ficha del artículo. Arriba: una foto pequeña y la cabecera: el tipo de artículo (primero, ya que define el aspecto de la ficha), nombre y referencia, categoría y forma de reposición, existencias y precios. Cambiar el tipo ya no desplaza los campos de la cabecera.
- La ficha se abre siempre en la pestaña «Descripción y propiedades»: descripción del artículo, marca, calidad, grupo de artículos y propiedades adicionales. Unidades, peso, tipo de IVA, proveedor, fabricante y embalajes están en la pestaña «Gestión»; el código y otros datos técnicos, en «Servicio».
- En las pestañas «Almacén» y «Producción», cada tabla tiene su propia subpestaña: existencias, mínimos y máximos por almacén, ubicaciones y condiciones de almacenamiento, materiales en máquinas; ruta de fabricación, máquinas, rendimiento de máquinas, «dónde se usa». Los campos cortos de sentido parecido están en una misma línea.
- Los precios, la ruta de fabricación, las existencias y los códigos de barras vuelven a cargarse al abrir su pestaña.

## 2.0.16.140
### ru
- Рабочее место производства, закладка «Передача в переработку»: исправлена ошибка «Поле объекта не обнаружено (Продукция)» при завершении редактирования уже записанной строки.
### fr
- Poste de production, onglet « Transfert en sous-traitance » : correction de l'erreur « Le champ de l'objet n'est pas défini (Продукция) » à la fin de la modification d'une ligne déjà enregistrée.
### en
- Production workplace, "Subcontracting transfer" tab: fixed the "Object field not found (Продукция)" error when finishing editing a line that was already saved.
### es
- Puesto de producción, pestaña «Envío a subcontratación»: corregido el error «Campo del objeto no encontrado (Продукция)» al terminar de editar una línea ya guardada.

## 2.0.16.139
### ru
- Рабочее место производства, закладка «Передача в переработку»: панель «Свойства ПФ/ГП» показывает свойства и тогда, когда в строке не выбран ПФ/ГП, — берётся изделие заказа, в которое входит переданный материал (для переданного полуфабриката — готовая продукция). В заголовке панели указано, чьи это свойства; править их можно там же. Раньше без выбранного ПФ/ГП панель была пустой.
### fr
- Poste de production, onglet « Transfert en sous-traitance » : le panneau « Propriétés SF/PF » affiche les propriétés même si aucun SF/PF n'est choisi dans la ligne : il prend l'article de la commande dans lequel entre la matière transférée (pour un semi-fini transféré, le produit fini). Le titre du panneau indique à quel article elles appartiennent ; elles se modifient au même endroit. Auparavant, sans SF/PF choisi, le panneau restait vide.
### en
- Production workplace, "Subcontracting transfer" tab: the "SFG/FG properties" panel now shows properties even when no SFG/FG is selected in the line: it takes the order item the transferred material goes into (for a transferred semi-finished good, the finished product). The panel title shows whose properties they are; they can be edited there. Before, the panel stayed empty without a selected SFG/FG.
### es
- Puesto de producción, pestaña «Envío a subcontratación»: el panel «Propiedades SE/PT» muestra las propiedades aunque no se haya elegido SE/PT en la línea: toma el artículo del pedido en el que entra el material enviado (para un semielaborado enviado, el producto terminado). El título del panel indica de qué artículo son; se editan allí mismo. Antes, sin SE/PT elegido, el panel quedaba vacío.

## 2.0.16.138
### ru
- Рабочее место производства, закладка «Поступления из переработки»: после частичной приёмки новая строка по той же передаче предлагает в колонке «Продукция» только оставшееся количество. Раньше строка, введённая в тот же день, попадала в сегодняшний документ приёмки и снова предлагала всё ожидаемое количество.
### fr
- Poste de production, onglet « Réceptions de sous-traitance » : après une réception partielle, une nouvelle ligne du même transfert ne propose dans la colonne « Produit » que la quantité restante. Auparavant, une ligne saisie le même jour allait dans la réception du jour et proposait de nouveau toute la quantité attendue.
### en
- Production workplace, "Subcontracting receipts" tab: after a partial receipt, a new line for the same transfer offers only the remaining quantity in the "Product" column. Before, a line entered on the same day went into that day's receipt and offered the full expected quantity again.
### es
- Puesto de producción, pestaña «Recepciones de subcontratación»: tras una recepción parcial, una nueva línea del mismo envío solo propone en la columna «Producto» la cantidad restante. Antes, una línea introducida el mismo día iba a la recepción del día y volvía a proponer toda la cantidad esperada.

## 2.0.16.137
### ru
- Печатная форма коммерческого предложения обновлена по образцу: в строке номера — дата редакции; у клиента вместо договора — адрес и ICE; под именем вашего контакта — его телефон, e-mail и дата отгрузки; артикул больше не добавляется к наименованию товара; строка «Цены без НДС» и подпись «С уважением» убраны. Уже отправленные редакции печатаются с прежним содержанием (товары, цены, реквизиты на дату отправки), но в новом оформлении и с датой своей редакции.
- В итогах предложения появилась строка скидки, если в предложении есть скидка.
- В коммерческом предложении новые поля: «Действует до» (по умолчанию — месяц от даты создания), условия поставки Incoterms с местом и срок поставки. Внизу печатной формы — блок условий: срок действия, условия оплаты из карточки клиента, условия и срок поставки.
- Новая печать «Коммерческое предложение с вложениями»: картинки, прикреплённые к предложению кнопкой «Вложения», печатаются после него с новой страницы, по две на страницу. Прикреплять и удалять файлы предложения может тот, кто вправе изменять само предложение.
### fr
- Le devis imprimé est mis à jour selon le modèle : la ligne du numéro porte la date de la révision ; pour le client, l'adresse et l'ICE remplacent le contrat ; sous le nom de votre contact figurent son téléphone, son e-mail et la date d'expédition ; la référence n'est plus ajoutée à la désignation de l'article ; la ligne « Prix HT » et la formule « Cordialement » sont supprimées. Les révisions déjà envoyées gardent leur contenu (articles, prix, coordonnées à la date d'envoi) mais s'impriment dans la nouvelle présentation, avec la date de leur révision.
- Les totaux du devis affichent une ligne de remise lorsque le devis comporte une remise.
- Nouveaux champs dans le devis : date de validité (par défaut un mois après la création), conditions de livraison Incoterms avec le lieu et délais de livraison. En bas du devis imprimé, un bloc de conditions : validité, conditions de paiement de la fiche client, conditions et délais de livraison.
- Nouvelle impression « Devis avec pièces jointes » : les images jointes au devis par le bouton « Pièces jointes » s'impriment après le devis, sur une nouvelle page, deux par page. Seul un utilisateur autorisé à modifier le devis peut y joindre ou en supprimer des fichiers.
### en
- The printed quotation now follows the sample: the number line shows the revision date; the customer block shows the address and ICE instead of the contract; your contact's phone, e-mail and the shipping date appear under the contact name; the item code is no longer added to the item name; the "Prices exclude VAT" line and the "Kind regards" signature are removed. Revisions already sent keep their content (items, prices, details as of sending) but print in the new layout with their revision date.
- Quotation totals show a discount line when the quotation has a discount.
- New quotation fields: valid until (one month after creation by default), Incoterms delivery terms with the place, and delivery lead time. A terms block at the bottom of the printed quotation shows validity, payment terms from the customer card, and delivery terms and lead time.
- New print "Quotation with attachments": images attached to the quotation with the "Attachments" button are printed after it on a new page, two per page. Only a user allowed to change the quotation can attach or delete its files.
### es
- El presupuesto impreso sigue ahora el modelo: la línea del número muestra la fecha de la revisión; el bloque del cliente muestra la dirección y el ICE en lugar del contrato; bajo el nombre de su contacto aparecen su teléfono, su e-mail y la fecha de envío; la referencia ya no se añade al nombre del artículo; se eliminan la línea «Precios sin IVA» y la firma «Atentamente». Las revisiones ya enviadas conservan su contenido (artículos, precios, datos a la fecha de envío), pero se imprimen con el nuevo diseño y la fecha de su revisión.
- Los totales del presupuesto muestran una línea de descuento cuando el presupuesto tiene descuento.
- Nuevos campos del presupuesto: válido hasta (por defecto, un mes desde la creación), condiciones de entrega Incoterms con el lugar y plazo de entrega. Al pie del presupuesto impreso, un bloque de condiciones: validez, condiciones de pago de la ficha del cliente, condiciones y plazo de entrega.
- Nueva impresión «Presupuesto con adjuntos»: las imágenes adjuntadas al presupuesto con el botón «Adjuntos» se imprimen después de él, en una página nueva, dos por página. Solo un usuario autorizado a modificar el presupuesto puede adjuntar o eliminar sus archivos.

## 2.0.16.136
### ru
- Печать доступна всем пользователям, которые видят документ: раньше у кладовщика, менеджеров, кассира, логиста, оператора и других ролей часть печатных форм в меню «Печать» не появлялась, а у администратора была (счета, накладные, чеки, акты сверки, кассовые ордера, прайс, перемещение, списание, оприходование и другие).
- Оператору производства в рабочем месте доступны бланк заказа и накладные BL — без цен, как и другие суммы, скрытые от его роли. Формы, в которых цены — суть документа (счёт-проформа, счёт-фактура, чек, поступление товаров), ему по-прежнему недоступны.
- Пользователь, от которого скрыты суммы (оператор производства, в том числе вместе с другими ролями), печатает акт списания и накладную на оприходование без цен и сумм. Формы с ценами ему не печатаются и не показываются в меню рабочих мест, даже если право на них дала другая роль.
### fr
- L'impression est disponible pour tous les utilisateurs qui voient le document : auparavant, pour le magasinier, les commerciaux, le caissier, le logisticien, l'opérateur et d'autres rôles, une partie des formulaires n'apparaissait pas dans le menu « Impression », alors qu'elle apparaissait pour l'administrateur (factures, bons de livraison, tickets, rapprochements, pièces de caisse, liste de prix, transferts, mises au rebut, entrées en stock, etc.).
- L'opérateur de production peut imprimer le bon de commande et les bons de livraison BL sans prix, comme les autres montants masqués pour son rôle. Les formulaires dont les prix sont l'essentiel (facture proforma, facture, ticket, réception de marchandises) lui restent inaccessibles.
- L'utilisateur pour qui les montants sont masqués (opérateur de production, y compris avec d'autres rôles) imprime la sortie de marchandises et l'entrée des marchandises sans prix ni montants. Les formulaires avec prix ne lui sont ni imprimés ni proposés dans les menus des postes, même si un autre rôle en donne le droit.
### en
- Printing is available to every user who can see the document: previously, for the storekeeper, managers, cashier, logistician, operator and other roles, some print forms did not appear in the "Print" menu, while they did for the administrator (invoices, delivery notes, receipts, reconciliation statements, cash documents, price list, transfers, write-offs, stock receipts and others).
- The production operator can print the order form and BL delivery notes without prices, like other amounts hidden from this role. Forms where prices are the essence of the document (proforma invoice, invoice, receipt, goods receipt) remain unavailable to the operator.
- A user whose amounts are hidden (production operator, including together with other roles) prints the write-off act and the stock receipt note without prices and amounts. Forms with prices are neither printed for this user nor shown in workplace menus, even when another role grants the right.
### es
- La impresión está disponible para todos los usuarios que ven el documento: antes, para el almacenero, los comerciales, el cajero, el logístico, el operador y otros roles, parte de los formularios no aparecía en el menú «Impresión», mientras que para el administrador sí (facturas, albaranes, tickets, conciliaciones, documentos de caja, lista de precios, traslados, bajas, entradas de stock y otros).
- El operador de producción puede imprimir la hoja de pedido y los albaranes BL sin precios, como los demás importes ocultos para su rol. Los formularios cuyo contenido son los precios (factura proforma, factura, ticket, recepción de mercancías) siguen sin estar disponibles para él.
- El usuario para quien los importes están ocultos (operador de producción, también junto con otros roles) imprime el acta de baja y la entrada de mercancías sin precios ni importes. Los formularios con precios no se le imprimen ni se muestran en los menús de los puestos, aunque otro rol dé el derecho.

## 2.0.16.135
### ru
- Оператору производства доступна печать на закладках «Передача в переработку» и «Поступления из переработки» рабочего места производства (акт передачи и акт приёмки): раньше меню «Печать» там было только у администратора. Акт приёмки печатается оператору без себестоимости и стоимости услуг, как и другие суммы, скрытые от его роли.
### fr
- L'opérateur de production peut imprimer depuis les onglets « Transfert en sous-traitance » et « Réceptions de sous-traitance » du poste de production (bon de transfert et bon de réception) : auparavant le menu « Impression » n'y était disponible que pour l'administrateur. Le bon de réception est imprimé pour l'opérateur sans coût de revient ni coût des services, comme les autres montants masqués pour son rôle.
### en
- The production operator can print from the "Subcontracting transfer" and "Subcontracting receipts" tabs of the production workplace (transfer act and receipt act): previously the "Print" menu there was available only to the administrator. The receipt act is printed for the operator without cost and service amounts, like other amounts hidden from this role.
### es
- El operador de producción puede imprimir desde las pestañas «Envío a subcontratación» y «Recepciones de subcontratación» del puesto de producción (acta de transferencia y acta de recepción): antes el menú «Impresión» solo estaba disponible para el administrador. El acta de recepción se imprime para el operador sin coste ni importe de los servicios, como los demás importes ocultos para su rol.

## 2.0.16.134
### ru
- У пользователей без полных прав снова работает подбор по набранному тексту в полях выбора (клиент, товар и другие справочники): раньше такое поле показывало только недавно выбранные значения, у администратора всё работало. Исправлено во всех ролях.
### fr
- La saisie semi-automatique dans les champs de sélection (client, produit et autres référentiels) fonctionne de nouveau pour les utilisateurs sans droits complets : auparavant le champ ne proposait que les valeurs choisies récemment, alors que tout fonctionnait pour l'administrateur. Corrigé dans tous les rôles.
### en
- Typing to search in selection fields (customer, product and other catalogs) works again for users without full rights: previously such a field offered only recently selected values, while everything worked for the administrator. Fixed in all roles.
### es
- La búsqueda al escribir en los campos de selección (cliente, producto y otros catálogos) vuelve a funcionar para los usuarios sin derechos completos: antes el campo solo ofrecía los valores elegidos recientemente, mientras que para el administrador todo funcionaba. Corregido en todos los roles.

## 2.0.16.133
### ru
- Рабочие места производства, закупок и управления станками можно открывать автоматически при запуске программы: меню «Настройки» (шестерёнка) в самом рабочем месте → флажок «Открывать при запуске».
- В карточке пользователя новая закладка «При запуске»: список рабочих мест, которые у него открываются при запуске; лишнее можно удалить.
- Новая роль «Складские ордера». Вместе с «Оператором производства» она открывает рабочее место закупок в режиме приёмки: заказы поставщикам видны без цен и сумм, выбранные заказы принимаются приходными ордерами (кнопка «Создать поступление» на ордерном складе). Заказы, статусы, потребность, оплаты и документы с ценами в этом режиме недоступны. Рабочее место закупок у такого пользователя — в разделе «Производство».
- Рабочее место закупок больше не падает с ошибкой прав у пользователей без доступа к документам оплат: закладки «Оплаты» и «Документы» у них просто скрыты.
### fr
- Les postes de production, des achats et des machines peuvent s'ouvrir automatiquement au démarrage : menu « Paramètres » (roue dentée) du poste → case « Ouvrir au démarrage ».
- Nouvel onglet « Au démarrage » dans la fiche utilisateur : la liste des postes ouverts au démarrage ; on peut en retirer.
- Nouveau rôle « Bons d'entrepôt ». Avec « Opérateur de production », il ouvre le poste des achats en mode réception : les commandes fournisseurs sont visibles sans prix ni montants, les commandes sélectionnées sont reçues par bons d'entrée (bouton « Créer une réception » sur un entrepôt à bons). Commandes, statuts, besoins, paiements et documents avec prix ne sont pas accessibles dans ce mode. Pour cet utilisateur, le poste des achats est dans la section « Production ».
- Le poste des achats ne s'arrête plus sur une erreur de droits chez les utilisateurs sans accès aux documents de paiement : les onglets « Paiements » et « Documents » sont simplement masqués.
### en
- The production, purchasing and machine workplaces can open automatically at startup: the "Settings" menu (gear) of the workplace → "Open at startup".
- New "At startup" tab in the user card: the list of workplaces opened at startup; entries can be removed.
- New "Warehouse orders" role. Together with "Production operator" it opens the purchasing workplace in receiving mode: purchase orders are shown without prices and amounts, selected orders are received with receiving orders (the "Create receipt" button on a warehouse that uses receiving orders). Orders, statuses, demand, payments and documents with prices are not available in this mode. For such a user the purchasing workplace is in the "Production" section.
- The purchasing workplace no longer fails with an access error for users without access to payment documents: the "Payments" and "Documents" tabs are simply hidden.
### es
- Los puestos de producción, compras y máquinas pueden abrirse automáticamente al iniciar: menú «Configuración» (engranaje) del puesto → casilla «Abrir al iniciar».
- Nueva pestaña «Al iniciar» en la ficha del usuario: la lista de puestos que se abren al iniciar; se pueden quitar.
- Nuevo rol «Órdenes de almacén». Junto con «Operador de producción» abre el puesto de compras en modo de recepción: los pedidos a proveedores se ven sin precios ni importes, los pedidos seleccionados se reciben con órdenes de entrada (botón «Crear recepción» en un almacén con órdenes). Pedidos, estados, necesidades, pagos y documentos con precios no están disponibles en este modo. Para este usuario, el puesto de compras está en la sección «Producción».
- El puesto de compras ya no falla con un error de derechos para usuarios sin acceso a los documentos de pago: las pestañas «Pagos» y «Documentos» simplemente se ocultan.

## 2.0.16.132
### ru
- Приходный и расходный ордер: под таблицей — итог количества по каждой единице измерения (килограммы и метры считаются отдельно).
- Расходный ордер: стороны в шапке называются «Отправитель» и «Получатель» вместо «Продавец» и «Покупатель».
- Основание в печатной форме ордеров — «Заказ клиента № 5 от 27.10.2026» на языке печати, без времени документа.
- Меню «Печать» реализации сокращено: остались накладные BL (обычная, A4, A4 без НДС, A4 без цен) и чеки. Facture, Facture proforma, акт об оказании услуг, заказ и коммерческое предложение из меню убраны.
### fr
- Bon de réception et bon de sortie : sous le tableau, le total des quantités par unité de mesure (kilogrammes et mètres sont comptés séparément).
- Bon de sortie : les parties de l'en-tête s'appellent « Expéditeur » et « Destinataire » au lieu de « Vendeur » et « Acheteur ».
- Le document de base dans l'impression des bons s'affiche comme « Commande client n° 5 du 27/10/2026 » dans la langue d'impression, sans l'heure du document.
- Le menu « Impression » du bon de livraison est réduit : restent les bons de livraison (normal, A4, A4 HT, A4 sans prix) et les tickets. Facture, Facture proforma, acte de prestation de services, commande et devis sont retirés du menu.
### en
- Goods receipt and goods issue notes: below the table, the total quantity for each unit of measure (kilograms and metres are counted separately).
- Goods issue note: the parties in the header are called "Sender" and "Recipient" instead of "Seller" and "Buyer".
- The basis document in the printed notes reads "Customer order No. 5 dated 10/27/2026" in the print language, without the document time.
- The "Print" menu of the sales document is shortened: delivery notes (standard, A4, A4 without VAT, A4 without prices) and receipts remain. Invoice, proforma invoice, act of provision of services, order and quotation are removed from the menu.
### es
- Orden de entrada y orden de salida: debajo de la tabla, el total de cantidades por unidad de medida (kilogramos y metros se cuentan por separado).
- Orden de salida: las partes del encabezado se llaman «Remitente» y «Destinatario» en lugar de «Vendedor» y «Comprador».
- El documento base en la impresión de las órdenes aparece como «Pedido del cliente n.º 5 del 27/10/2026» en el idioma de impresión, sin la hora del documento.
- El menú «Impresión» del albarán se reduce: quedan los albaranes de entrega (normal, A4, A4 sin IVA, A4 sin precios) y los tickets. Factura, factura proforma, acta de prestación de servicios, pedido y presupuesto se quitan del menú.

## 2.0.16.131
### ru
- Начальное заполнение базы заполняет у дирхама, евро, доллара США и рубля параметры суммы прописью на всех языках (русский, английский, французский): единицы целой и дробной части и род. Таблицу «Параметры исчисления» в карточке валюты больше не нужно заполнять вручную, её можно поправить — повторное заполнение исправленные строки не меняет.
- Сумма прописью по-русски учитывает род, указанный в карточке валюты: «один сантим», а не «одна сантим».
### fr
- Le remplissage initial de la base renseigne pour le dirham, l'euro, le dollar US et le rouble les paramètres du montant en toutes lettres dans toutes les langues (russe, anglais, français) : unités de la partie entière et fractionnaire et genre. Le tableau « Paramètres de calcul » de la fiche devise n'est plus à remplir à la main ; il peut être corrigé, un nouveau remplissage ne modifie pas les lignes corrigées.
- Le montant en toutes lettres en russe tient compte du genre indiqué dans la fiche devise.
### en
- Initial database filling now sets the amount-in-words parameters for the dirham, euro, US dollar and ruble in all languages (Russian, English, French): units of the integer and fractional parts and gender. The "Calculation parameters" table in the currency card no longer has to be filled in by hand; it can be edited, and filling again does not change edited rows.
- The amount in words in Russian takes into account the gender set in the currency card.
### es
- El llenado inicial de la base completa para el dírham, el euro, el dólar estadounidense y el rublo los parámetros del importe en letras en todos los idiomas (ruso, inglés, francés): unidades de la parte entera y fraccionaria y género. La tabla «Parámetros de cálculo» de la ficha de la moneda ya no se rellena a mano; se puede corregir y un nuevo llenado no cambia las filas corregidas.
- El importe en letras en ruso tiene en cuenta el género indicado en la ficha de la moneda.

## 2.0.16.130
### ru
- Новый отчёт «Деньги и статусы заказов клиентов» (раздел «Продажи»): по каждому заказу — сумма заказа, отгружено, оплачено, долг, сколько осталось оплатить, выручка без НДС, себестоимость, маржа и маржинальность.
- Вариант «Деньги по заказам» группирует заказы по заказчику и показывает его общий долг и строку «Не распределено по заказам» — авансы и долги, не привязанные к заказам, чтобы итог по заказчику сходился с его долгом.
- Вариант «Статусы заказов» — таблица заказов с текущим статусом, плановой датой отгрузки, процентом отгруженного и просрочкой отгрузки в днях; просроченные заказы выделены цветом.
- Процент отгруженного считается по каждой позиции: перегруз одной позиции не закрывает недогруз другой. Учитываются отгрузки со склада расходными ордерами и возвраты.
- В отчёт попадают заказы, созданные в периоде, и все незакрытые на конец периода: не отгруженные полностью, не реализованные полностью или с долгом.
### fr
- Nouveau rapport « Argent et statuts des commandes clients » (section « Ventes ») : pour chaque commande — montant, expédié, payé, dette, reste à payer, chiffre d'affaires HT, coût de revient, marge et taux de marge.
- La variante « Argent par commandes » regroupe les commandes par client et montre sa dette totale ainsi que la ligne « Non réparti par commandes » — avances et dettes non liées à une commande, pour que le total du client corresponde à sa dette.
- La variante « Statuts des commandes » est un tableau des commandes avec le statut actuel, la date d'expédition prévue, le pourcentage expédié et le retard d'expédition en jours ; les commandes en retard sont mises en couleur.
- Le pourcentage expédié est calculé par article : l'excédent d'un article ne compense pas le manque d'un autre. Les sorties de stock par bons de sortie et les retours sont pris en compte.
- Le rapport contient les commandes créées dans la période et toutes celles non clôturées à la fin de la période : pas entièrement expédiées, pas entièrement facturées ou avec une dette.
### en
- New report "Customer order money and statuses" ("Sales" section): for each order — order amount, shipped, paid, debt, left to pay, revenue excl. VAT, cost, margin and margin rate.
- The "Money by orders" variant groups orders by customer and shows the customer's total debt and a "Not allocated to orders" line — advances and debts not linked to an order, so that the customer total matches the customer's debt.
- The "Order statuses" variant is a table of orders with the current status, planned shipment date, percent shipped and shipment delay in days; overdue orders are highlighted.
- Percent shipped is calculated per item: overshipping one item does not cover a shortfall of another. Shipments by goods issue notes and returns are taken into account.
- The report includes orders created in the period and all orders still open at the end of the period: not fully shipped, not fully invoiced or with a debt.
### es
- Nuevo informe «Dinero y estados de pedidos de clientes» (sección «Ventas»): para cada pedido — importe, enviado, pagado, deuda, pendiente de pago, ingresos sin IVA, coste, margen y porcentaje de margen.
- La variante «Dinero por pedidos» agrupa los pedidos por cliente y muestra su deuda total y la línea «No asignado a pedidos» — anticipos y deudas no vinculados a un pedido, para que el total del cliente coincida con su deuda.
- La variante «Estados de los pedidos» es una tabla de pedidos con el estado actual, la fecha de envío prevista, el porcentaje enviado y el retraso del envío en días; los pedidos atrasados se resaltan en color.
- El porcentaje enviado se calcula por artículo: el exceso de un artículo no compensa la falta de otro. Se tienen en cuenta las salidas por órdenes de salida y las devoluciones.
- El informe incluye los pedidos creados en el período y todos los no cerrados al final del período: no enviados por completo, no facturados por completo o con deuda.

## 2.0.16.129
### ru
- Новый отчёт «Переработка по переработчикам» (раздел «Производство»): по каждому переработчику — что передано, что принято и что ещё у него лежит, с разбивкой по заказам клиентов. В каждом заказе три колонки: передачи, приёмы продукции и остаток у переработчика с датой самой старой передачи.
- В шапке переработчика и заказа — итоги по единицам измерения, средний срок переработки (от передачи до приёма) и сколько дней лежит самая старая незакрытая передача.
- Если одно поступление из переработки закрыло сырьё нескольких заказов, его продукция показана в каждом заказе с пометкой «◐», а в итог переработчика входит один раз. Приём продукции без сырья помечается «хвост без сырья».
- Отчёт можно отобрать по переработчику, клиенту или заказу и добавить в «Избранные отчёты».
### fr
- Nouveau rapport « Sous-traitance par sous-traitant » (section « Production ») : pour chaque sous-traitant — ce qui a été envoyé, reçu et ce qui reste chez lui, par commande client. Dans chaque commande, trois colonnes : envois, réceptions de produits et solde chez le sous-traitant avec la date de l'envoi le plus ancien.
- Dans l'en-tête du sous-traitant et de la commande : totaux par unité de mesure, délai moyen de traitement (de l'envoi à la réception) et nombre de jours de l'envoi ouvert le plus ancien.
- Si une réception de sous-traitance a soldé la matière de plusieurs commandes, son produit est montré dans chacune avec la marque « ◐ » et compte une seule fois dans le total du sous-traitant. Une réception de produit sans matière est marquée « reliquat sans matière ».
- Le rapport se filtre par sous-traitant, client ou commande et peut être ajouté aux « Rapports favoris ».
### en
- New report "Processing by processor" ("Production" section): for each processor — what was sent, what was received and what is still at the processor, broken down by customer order. Each order has three columns: transfers, product receipts and the balance at the processor with the date of the oldest transfer.
- The processor and order headers show totals per unit of measure, the average processing time (from transfer to receipt) and how many days the oldest open transfer has been waiting.
- If one receipt from processing closed raw material of several orders, its product is shown in each order marked "◐" and counts once in the processor total. A product receipt without raw material is marked "tail without raw material".
- The report can be filtered by processor, customer or order and added to "Favourite reports".
### es
- Nuevo informe «Procesamiento por procesador» (sección «Producción»): para cada procesador — lo enviado, lo recibido y lo que aún tiene, desglosado por pedido de cliente. En cada pedido, tres columnas: envíos, recepciones de producto y saldo en el procesador con la fecha del envío más antiguo.
- En la cabecera del procesador y del pedido: totales por unidad de medida, plazo medio de procesamiento (del envío a la recepción) y días que lleva abierto el envío más antiguo.
- Si una recepción de procesamiento cerró materia prima de varios pedidos, su producto se muestra en cada pedido con la marca «◐» y cuenta una sola vez en el total del procesador. Una recepción de producto sin materia prima se marca «remanente sin materia prima».
- El informe se puede filtrar por procesador, cliente o pedido y añadir a «Informes favoritos».

## 2.0.16.128
### ru
- Новый отчёт «Прослеживаемость партий материала» (раздел «Производство»): по каждой партии материала — дата прихода, лот (номер документа поставщика), приход и остаток, а рядом четыре колонки воронки: выпуск полуфабриката из партии, передача полуфабриката переработчику, отгрузка готовой продукции клиенту. Внизу колонки отгрузки — остаток продукции на складе.
- Документы в отчёте открываются щелчком; возврат покупателя показывается строкой с минусом, списание — отдельной строкой «прочее выбытие».
- Если выпуск или поступление из переработки собраны из нескольких партий, строка помечается «◐»: количество относится ко всем этим партиям сразу и долями не делится.
- Отбор по клиенту оставляет только выпуски, передачи и отгрузки его заказов; поиск по лоту — по части номера документа поставщика. Отчёт можно добавить в «Избранные отчёты».
### fr
- Nouveau rapport « Traçabilité des lots de matière » (section « Production ») : pour chaque lot de matière — date de réception, lot (n° du document fournisseur), entrée et stock, et à côté quatre colonnes : fabrication du semi-fini à partir du lot, envoi du semi-fini au sous-traitant, livraison du produit fini au client. En bas de la colonne livraison — le stock de produit restant.
- Les documents du rapport s'ouvrent d'un clic ; un retour client apparaît en ligne négative, une mise au rebut en ligne « autre sortie ».
- Si une fabrication ou une réception de sous-traitance regroupe plusieurs lots, la ligne est marquée « ◐ » : la quantité concerne tous ces lots à la fois et n'est pas répartie.
- Le filtre client ne garde que les fabrications, envois et livraisons de ses commandes ; la recherche par lot se fait sur une partie du n° fournisseur. Le rapport peut être ajouté aux « Rapports favoris ».
### en
- New report "Material lot traceability" ("Production" section): for each material lot — receipt date, lot (supplier document number), quantity received and balance, and next to it four columns: semi-finished output from the lot, transfer of the semi-finished goods to the processor, shipment of the finished product to the customer. At the bottom of the shipment column — product still in stock.
- Documents in the report open with a click; a customer return is shown as a negative line, a write-off as a separate "other disposal" line.
- If an output or a receipt from processing combines several lots, the line is marked "◐": the quantity covers all those lots together and is not split.
- The customer filter keeps only the outputs, transfers and shipments of that customer's orders; the lot search matches part of the supplier document number. The report can be added to "Favourite reports".
### es
- Nuevo informe «Trazabilidad de lotes de material» (sección «Producción»): para cada lote de material — fecha de entrada, lote (n.º del documento del proveedor), entrada y saldo, y al lado cuatro columnas: producción del semielaborado a partir del lote, envío del semielaborado al procesador, expedición del producto terminado al cliente. Al final de la columna de expedición — el producto que queda en almacén.
- Los documentos del informe se abren con un clic; una devolución del cliente aparece como línea negativa y una baja como línea aparte «otra salida».
- Si una producción o una recepción de procesamiento reúne varios lotes, la línea se marca con «◐»: la cantidad corresponde a todos esos lotes a la vez y no se reparte.
- El filtro por cliente deja solo las producciones, envíos y expediciones de sus pedidos; la búsqueda por lote coincide con parte del n.º del proveedor. El informe se puede añadir a «Informes favoritos».

## 2.0.16.127
### ru
- В отчётах можно сохранять свои именованные варианты: «Ещё» → «Сохранить вариант…», «Выбрать вариант…» и «Изменить вариант…» (поля, группировки, отборы). Сохранённые варианты видны в «Все отчёты» с пометкой «(мой)», их можно открыть, добавить в избранное или удалить.
### fr
- Les rapports permettent d'enregistrer vos propres variantes nommées : « Plus » → « Enregistrer la variante… », « Choisir la variante… » et « Modifier la variante… » (champs, regroupements, filtres). Les variantes enregistrées apparaissent dans « Tous les rapports » avec la mention « (le mien) » ; on peut les ouvrir, les ajouter aux favoris ou les supprimer.
### en
- Reports can now save your own named variants: "More" → "Save variant…", "Select variant…" and "Change variant…" (fields, groupings, filters). Saved variants appear in "All reports" marked "(mine)" and can be opened, added to favourites or deleted.
### es
- Los informes permiten guardar sus propias variantes con nombre: «Más» → «Guardar variante…», «Seleccionar variante…» y «Modificar variante…» (campos, agrupaciones, filtros). Las variantes guardadas aparecen en «Todos los informes» con la marca «(mío)» y se pueden abrir, añadir a favoritos o eliminar.

## 2.0.16.126
### ru
- В разделе «Главное» появились «Избранные отчёты»: панель с уменьшенными образами ваших любимых отчётов. Щелчок по образу или заголовку открывает отчёт с теми же отборами и настройками. Образы обновляются сами, если им больше часа, или по кнопке; плитки можно переименовать, переставить и убрать.
- «Все отчёты» в разделе «Главное»: все доступные вам отчёты по разделам с быстрым поиском по названию и описанию. Отчёт открывается двойным щелчком, кнопка «В избранное» добавляет его на панель.
- В открытом отчёте появилась кнопка «В избранное»: настройте отборы и добавьте отчёт на панель — он откроется именно с этими настройками. Бухгалтерские и зарплатные отчёты со своими формами добавляются ярлыком, без образа.
- У каждого пользователя своё избранное; отчёт, к которому у пользователя нет доступа, на панели не показывается.
### fr
- La section « Principal » propose désormais les « Rapports favoris » : un panneau avec des aperçus réduits de vos rapports préférés. Un clic sur l'aperçu ou le titre ouvre le rapport avec les mêmes filtres et paramètres. Les aperçus se mettent à jour d'eux-mêmes s'ils datent de plus d'une heure, ou par un bouton ; les tuiles peuvent être renommées, déplacées et retirées.
- « Tous les rapports » dans la section « Principal » : tous les rapports auxquels vous avez accès, par section, avec une recherche rapide par nom et description. Un double clic ouvre le rapport, le bouton « Ajouter aux favoris » l'ajoute au panneau.
- Un rapport ouvert propose le bouton « Ajouter aux favoris » : réglez les filtres et ajoutez le rapport au panneau — il s'ouvrira avec exactement ces paramètres. Les rapports comptables et de paie ayant leurs propres formulaires sont ajoutés comme raccourci, sans aperçu.
- Chaque utilisateur a ses propres favoris ; un rapport auquel l'utilisateur n'a pas accès n'est pas affiché dans le panneau.
### en
- The "Main" section now has "Favourite reports": a panel with reduced snapshots of your favourite reports. Clicking a snapshot or title opens the report with the same filters and settings. Snapshots refresh by themselves when older than an hour, or with a button; tiles can be renamed, reordered and removed.
- "All reports" in the "Main" section: all reports available to you, by section, with a quick search by name and description. Double-click opens a report, the "Add to favourites" button adds it to the panel.
- An open report now has an "Add to favourites" button: set the filters and add the report to the panel — it will open with exactly these settings. Accounting and payroll reports with their own forms are added as a shortcut, without a snapshot.
- Each user has their own favourites; a report the user has no access to is not shown on the panel.
### es
- La sección «Principal» ahora tiene «Informes favoritos»: un panel con vistas reducidas de sus informes preferidos. Un clic en la vista o el título abre el informe con los mismos filtros y ajustes. Las vistas se actualizan solas si tienen más de una hora, o con un botón; los mosaicos se pueden renombrar, reordenar y quitar.
- «Todos los informes» en la sección «Principal»: todos los informes a los que tiene acceso, por sección, con búsqueda rápida por nombre y descripción. Un doble clic abre el informe, el botón «Añadir a favoritos» lo añade al panel.
- Un informe abierto tiene ahora el botón «Añadir a favoritos»: ajuste los filtros y añada el informe al panel; se abrirá exactamente con esos ajustes. Los informes contables y de nómina con formularios propios se añaden como acceso directo, sin vista.
- Cada usuario tiene sus propios favoritos; un informe al que el usuario no tiene acceso no se muestra en el panel.

## 2.0.16.125
### ru
- Акт передачи в переработку: в шапке рядом с заказом печатается клиент заказа.
- Акт передачи в переработку, накладная BL и расходный ордер: под строкой товара отдельными строками печатаются его вес и заполненные дополнительные реквизиты (например, материал, цвет, ширина, тип обработки). Вес не повторяется, если количество строки уже указано в весовой единице.
### fr
- Bon de transfert en sous-traitance : le client de la commande est imprimé dans l'en-tête, à côté de la commande.
- Bon de transfert en sous-traitance, bon de livraison et bon de sortie : sous la ligne d'article, son poids et ses attributs supplémentaires renseignés (par exemple matière, couleur, largeur, type de traitement) sont imprimés chacun sur sa propre ligne. Le poids n'est pas répété si la quantité de la ligne est déjà exprimée dans une unité de poids.
### en
- Transfer for processing act: the order's customer is printed in the header, next to the order.
- Transfer for processing act, delivery note and goods issue order: below the item line, its weight and filled-in additional attributes (for example material, colour, width, processing type) are printed, each on its own line. The weight is not repeated if the line quantity is already in a unit of weight.
### es
- Acta de transferencia a procesamiento: el cliente del pedido se imprime en el encabezado, junto al pedido.
- Acta de transferencia a procesamiento, albarán de entrega y orden de salida: bajo la línea del artículo se imprimen su peso y sus atributos adicionales rellenados (por ejemplo material, color, ancho, tipo de tratamiento), cada uno en su propia línea. El peso no se repite si la cantidad de la línea ya está en una unidad de peso.

## 2.0.16.124
### ru
- Остатки на складах ведутся одним регистром — партиями «Товаров в наличии»: физический остаток, остатки в подборе, в документах, отчётах и на дашборде — это сумма партий позиции. Цифры не меняются, но отдельной копии остатков больше нет, и расходиться им не с чем.
- При обновлении ордера, проведённые до перехода на партии и ещё не переведённые, переводятся автоматически.
- Оповещение о минимальном остатке работает как прежде; налоговые документы на основаниях его не вызывают.
### fr
- Les stocks des entrepôts sont tenus dans un seul registre — les lots des « Produits en stock » : le stock physique, les stocks dans la sélection, les documents, les rapports et le tableau de bord sont la somme des lots de l'article. Les chiffres ne changent pas, mais il n'y a plus de copie séparée des stocks qui pourrait diverger.
- Lors de la mise à jour, les bons validés avant le passage aux lots et pas encore convertis sont convertis automatiquement.
- La notification de stock minimum fonctionne comme avant ; les documents fiscaux sur bases ne la déclenchent pas.
### en
- Warehouse stock is kept in a single register — the batches of «Products in stock»: physical stock, stock in selection, documents, reports and the dashboard are the sum of the item's batches. The figures do not change, but there is no separate copy of stock left to diverge.
- On update, orders posted before the move to batches and not yet converted are converted automatically.
- The minimum stock notification works as before; tax documents on bases do not trigger it.
### es
- Las existencias de los almacenes se llevan en un solo registro — los lotes de «Productos en stock»: las existencias físicas, en la selección, en documentos, informes y el panel son la suma de los lotes del artículo. Las cifras no cambian, pero ya no hay una copia aparte de existencias que pueda divergir.
- Al actualizar, las órdenes contabilizadas antes del paso a lotes y aún no convertidas se convierten automáticamente.
- La notificación de existencias mínimas funciona como antes; los documentos fiscales sobre bases no la activan.

## 2.0.16.123
### ru
- Ордерный склад: поступление и реализацию можно провести и без ордера — документ первым. Товар ждёт приёмки или отгрузки, а кладовщик вводит приходный или расходный ордер на основании документа: строки заполняются тем, что ещё не принято или не отгружено.
- В одном документе можно сочетать строки по ордерам и строки без ордера.
- Партия, принятая по поступлению частями, получает стоимость по своей доле строки; изменение цены поступления сразу пересчитывает партии всех его приёмок.
- Себестоимость реализации, проведённой раньше отгрузки, появляется по мере отгрузки расходными ордерами. В отчётах стоимости и маржи видно, сколько реализаций ещё не отгружено полностью.
- Вернуть по реализации ордерного склада можно только то, что уже отгружено; отменить отгрузку, которую покупатель вернул, нельзя.
- Дополнительные расходы на поступление, ещё не принятое полностью, распределяются по мере приёмки; программа сообщает, какая часть ждёт приёмки.
- Поступление, принятое ордером, и строки, по которым принят товар, защищены от отмены и удаления: сначала отменяется ордер.
- В отчёте «Остатки на складах» — колонки «Ожидает приёмки» и «Ожидает отгрузки». Раз в сутки приходит оповещение, если ордера или документы ждут оформления дольше трёх дней (порог настраивается).
- При выпуске из материала, стоимость которого ещё не подтверждена поступлением, программа предупреждает об этом.
### fr
- Entrepôt à bons : la réception et la vente peuvent être validées sans bon — le document d'abord. La marchandise attend la réception ou l'expédition, et le magasinier saisit un bon d'entrée ou de sortie à partir du document : les lignes reprennent ce qui n'est pas encore reçu ou expédié.
- Un même document peut combiner des lignes sur bons et des lignes sans bon.
- Un lot reçu en plusieurs fois reçoit le coût de sa part de ligne ; un changement de prix de la réception recalcule aussitôt les lots de toutes ses réceptions.
- Le coût d'une vente validée avant l'expédition apparaît au fur et à mesure des bons de sortie. Les rapports de coût et de marge indiquent combien de ventes ne sont pas encore entièrement expédiées.
- Pour une vente d'entrepôt à bons, seul l'expédié peut être retourné ; une expédition retournée par le client ne peut pas être annulée.
- Les frais d'une réception pas encore entièrement reçue sont répartis au fil des réceptions ; le programme indique la part en attente.
- Une réception reçue par bon et ses lignes reçues sont protégées contre l'annulation et la suppression : il faut d'abord annuler le bon.
- Le rapport « Stocks des entrepôts » a les colonnes « En attente de réception » et « En attente d'expédition ». Une notification quotidienne signale les bons ou documents en attente depuis plus de trois jours (seuil réglable).
- Lors d'une fabrication à partir d'un matériau dont le coût n'est pas encore confirmé par une réception, le programme le signale.
### en
- Order-based warehouse: a receipt or a sale can now be posted without an order — document first. The goods wait for receipt or shipment, and the storekeeper enters a receipt or issue order based on the document: the lines are filled with what is not yet received or shipped.
- One document can combine lines on orders and lines without an order.
- A batch received in parts gets the cost of its share of the line; a change of the receipt price immediately recalculates the batches of all its receipts.
- The cost of a sale posted before shipment appears as issue orders ship it. Cost and margin reports show how many sales are not yet fully shipped.
- For an order-based warehouse sale only goods already shipped can be returned; a shipment returned by the customer cannot be cancelled.
- Additional costs of a receipt not yet fully received are allocated as goods are received; the program shows the part still waiting.
- A receipt received by order and its received lines are protected from unposting and deletion: cancel the order first.
- The «Warehouse stock» report has «Awaiting receipt» and «Awaiting shipment» columns. A daily notification warns when orders or documents have waited more than three days (configurable threshold).
- When production uses a material whose cost is not yet confirmed by a receipt, the program warns about it.
### es
- Almacén con órdenes: la recepción y la venta pueden contabilizarse sin orden — el documento primero. La mercancía espera la recepción o el envío, y el almacenero introduce una orden de entrada o de salida a partir del documento: las líneas se rellenan con lo que aún no se ha recibido o enviado.
- Un mismo documento puede combinar líneas por órdenes y líneas sin orden.
- Un lote recibido por partes recibe el coste de su parte de la línea; un cambio de precio de la recepción recalcula al instante los lotes de todas sus recepciones.
- El coste de una venta contabilizada antes del envío aparece a medida que lo envían las órdenes de salida. Los informes de coste y margen muestran cuántas ventas aún no se han enviado por completo.
- En una venta de almacén con órdenes solo se devuelve lo ya enviado; un envío devuelto por el cliente no se puede anular.
- Los gastos de una recepción aún no recibida por completo se reparten a medida que se recibe; el programa indica la parte pendiente.
- Una recepción recibida por orden y sus líneas recibidas están protegidas contra la anulación y la eliminación: primero se anula la orden.
- El informe «Existencias en almacenes» tiene las columnas «Pendiente de recepción» y «Pendiente de envío». Una notificación diaria avisa cuando órdenes o documentos esperan más de tres días (umbral configurable).
- Al fabricar con un material cuyo coste aún no está confirmado por una recepción, el programa lo advierte.

## 2.0.16.122
### ru
- Ордерный склад: приходный ордер сразу создаёт партию — материал, принятый кладовщиком, можно списывать в производство, перемещать и отгружать до того, как менеджер оформит поступление.
- Стоимость такой партии — 0 до оформления поступления, без оценки. Когда поступление оформлено, стоимость партии пересчитывается сразу, а себестоимость выпуска, списаний и продаж из неё — при пересчёте себестоимости («Сервис — Перепроведение документов» или по расписанию).
- Расходный ордер списывает партии со склада сам; реализация по ордеру получает себестоимость из этого списания — по своей части отгрузки. Если партий на складе не хватает, расходный ордер не проводится.
- Пока у партии ордерного склада есть неоформленный остаток или её расходы ещё не пересчитаны, её стоимость в расчёт цен не попадает: средняя себестоимость для цен и правила ценообразования берут только подтверждённые партии. В отчётах стоимости и маржи видно, сколько партий со стоимостью, не подтверждённой поступлением.
- Дополнительные расходы поступления ордерного склада и документ дополнительных расходов по такому поступлению ложатся на партии ордеров. Дополнительный расход партии с нулевой стоимостью списывается пропорционально количеству.
- Документ, оформивший ордер, нельзя удалить, не отменив сначала его проведение; ордер должен быть раньше оформляющего документа. Налоговый документ на основаниях с ордерного склада не оформляется.
- Ордера, проведённые до обновления, переходят на партии при повторном проведении ордера или при пересчёте себестоимости; ордера, оформленные одним документом, переводятся вместе. До этого документы, оформившие такой ордер, повторно не проводятся — программа подскажет, что сделать.
- Поступление ордерного склада, на которое распределены дополнительные расходы отдельным документом, нельзя отменить, пока не отменён этот документ.
### fr
- Entrepôt à bons : le bon d'entrée crée immédiatement le lot — la matière reçue par le magasinier peut être consommée en production, transférée et expédiée avant que le gestionnaire n'enregistre la réception.
- Le coût d'un tel lot est 0 tant que la réception n'est pas enregistrée, sans estimation. Une fois la réception enregistrée, le coût du lot est recalculé aussitôt, et le coût de la production, des sorties et des ventes qui en proviennent — lors du recalcul du coût (« Service — Repasser les documents » ou selon la planification).
- Le bon de sortie consomme lui-même les lots de l'entrepôt ; la vente sur bon reçoit son coût de cette sortie, pour sa part de l'expédition. Si les lots de l'entrepôt ne suffisent pas, le bon de sortie n'est pas validé.
- Tant qu'un lot de l'entrepôt à bons a un reste non régularisé ou que ses sorties ne sont pas recalculées, son coût n'entre pas dans le calcul des prix : le coût moyen pour les prix et les règles de tarification ne prennent que les lots confirmés. Les rapports de coût et de marge indiquent le nombre de lots au coût non confirmé par une réception.
- Les frais supplémentaires d'une réception de l'entrepôt à bons et le document de frais supplémentaires sur une telle réception sont imputés aux lots des bons. Les frais supplémentaires d'un lot à coût nul sont sortis au prorata de la quantité.
- Un document qui a régularisé un bon ne peut pas être supprimé sans être d'abord dévalidé ; le bon doit précéder le document de régularisation. Aucun document fiscal sur bases n'est établi depuis un entrepôt à bons.
- Les bons validés avant la mise à jour passent aux lots lors d'une nouvelle validation du bon ou du recalcul du coût ; les bons régularisés par un même document sont convertis ensemble. D'ici là, les documents qui ont régularisé un tel bon ne sont pas revalidés — le programme indique quoi faire.
- Une réception d'entrepôt à bons sur laquelle des frais sont répartis par un document séparé ne peut pas être dévalidée tant que ce document n'est pas dévalidé.
### en
- Order-based warehouse: a receipt order creates the batch right away — material accepted by the storekeeper can be consumed in production, transferred and shipped before the manager documents the purchase receipt.
- The cost of such a batch is 0 until the receipt is documented, with no estimate. Once the receipt is documented, the batch cost is recalculated at once, and the cost of production, write-offs and sales made from it — during cost recalculation ("Service — Document reposting" or on schedule).
- An issue order writes off batches from the warehouse itself; a sale documenting the order gets its cost from that write-off, for its share of the shipment. If the warehouse lacks batches, the issue order is not posted.
- While a batch of an order-based warehouse has an undocumented remainder or its write-offs are not yet recalculated, its cost stays out of pricing: the average cost for prices and the pricing rules use confirmed batches only. Cost and margin reports show how many batches have a cost not confirmed by a receipt.
- Additional costs of a receipt at an order-based warehouse and an additional cost document for such a receipt go to the order batches. The additional cost of a zero-cost batch is written off in proportion to quantity.
- A document that documented an order cannot be deleted without being unposted first; the order must be earlier than the documenting document. A tax document on bases is not issued from an order-based warehouse.
- Orders posted before the update move to batches when the order is posted again or during cost recalculation; orders documented by the same document are converted together. Until then, documents that documented such an order are not reposted — the program tells you what to do.
- An order-based warehouse receipt with additional costs allocated by a separate document cannot be unposted until that document is unposted.
### es
- Almacén por órdenes: la orden de entrada crea el lote al momento — el material recibido por el almacenero puede consumirse en producción, trasladarse y enviarse antes de que el gestor registre la recepción.
- El coste de ese lote es 0 hasta que se registra la recepción, sin estimación. Al registrar la recepción, el coste del lote se recalcula en el acto, y el coste de la producción, las bajas y las ventas que salen de él — en el recálculo del coste («Servicio — Volver a contabilizar documentos» o según la programación).
- La orden de salida da de baja los lotes del almacén por sí misma; la venta que formaliza la orden recibe su coste de esa baja, por su parte del envío. Si faltan lotes en el almacén, la orden de salida no se contabiliza.
- Mientras un lote del almacén por órdenes tenga un resto sin formalizar o sus salidas no estén recalculadas, su coste no entra en el cálculo de precios: el coste medio para precios y las reglas de tarificación toman solo lotes confirmados. Los informes de coste y margen muestran cuántos lotes tienen un coste no confirmado por una recepción.
- Los gastos adicionales de una recepción del almacén por órdenes y el documento de gastos adicionales sobre esa recepción se imputan a los lotes de las órdenes. El gasto adicional de un lote de coste cero se da de baja en proporción a la cantidad.
- Un documento que formalizó una orden no puede eliminarse sin anular antes su contabilización; la orden debe ser anterior al documento que la formaliza. No se emite documento fiscal sobre bases desde un almacén por órdenes.
- Las órdenes contabilizadas antes de la actualización pasan a lotes al volver a contabilizar la orden o al recalcular el coste; las órdenes formalizadas por un mismo documento se convierten juntas. Hasta entonces, los documentos que formalizaron esa orden no se vuelven a contabilizar — el programa indica qué hacer.
- Una recepción de almacén con órdenes con gastos repartidos por un documento aparte no se puede anular mientras ese documento no se anule.

## 2.0.16.121
### ru
- Маржа считается по партиям и статьям дополнительных расходов: себестоимость проданного товара хранится отдельно от выручки — по каждой партии, из которой товар ушёл со склада, и по каждой статье дополнительных расходов (доставка, таможня и другие). Отчёты «Ведомость по продажам», «Финансовый результат», «ABC-анализ продаж», «Проданный товар без накладной», дашборд продаж и расчёт зарплаты от прибыли берут себестоимость оттуда.
- История продаж перенесена: при обновлении себестоимость всех прежних продаж и возвратов переносится автоматически и сверяется с прежними данными по каждому документу; маржа в отчётах за прошлые периоды не меняется. Если в истории найдутся возвраты, вернувшие больше, чем было продано из партии, обновление остановится и назовёт эти документы.
- Возврат от покупателя: второй и следующие частичные возвраты по одной продаже возвращают на склад оставшиеся партии, а не первые снова; несколько строк одного товара в возврате тоже не возвращают одну партию дважды. Выручка возврата считается от ещё не возвращённой части продажи — после полного возврата продажа обнуляется точно.
- «Финансовый результат»: дополнительные расходы в закупочной стоимости проданного теперь вычитаются, а не прибавляются.
- Продажи, покрытые налоговым документом на основаниях с возвратами, теперь тоже пересчитываются при пересчёте себестоимости вместе с налоговым документом и возвратами по нему.
- В отчётах «ABC-анализ продаж» и «Проданный товар без накладной» видно, на какой момент себестоимость актуальна. В карточке продажи пользователь личного кабинета не видит себестоимость, прибыль и наценку.
### fr
- La marge est calculée par lot et par poste de frais supplémentaires : le coût des marchandises vendues est conservé séparément du chiffre d'affaires — pour chaque lot dont la marchandise est sortie de l'entrepôt et pour chaque poste de frais supplémentaires (transport, douane, etc.). Les rapports « État des ventes », « Résultat financier », « Analyse ABC des ventes », « Produits vendus sans facture », le tableau de bord des ventes et le calcul des salaires sur la marge en tirent le coût.
- L'historique des ventes est transféré : lors de la mise à jour, le coût de toutes les ventes et de tous les retours passés est transféré automatiquement et rapproché des anciennes données document par document ; la marge des rapports des périodes passées ne change pas. Si l'historique contient des retours ayant restitué plus que ce qui avait été vendu d'un lot, la mise à jour s'arrête et nomme ces documents.
- Retour client : le deuxième retour partiel et les suivants sur une même vente restituent les lots restants, et non les premiers à nouveau ; plusieurs lignes d'un même article dans un retour ne restituent pas non plus le même lot deux fois. Le chiffre d'affaires du retour est calculé sur la partie de la vente pas encore retournée — après un retour complet, la vente revient exactement à zéro.
- « Résultat financier » : les frais supplémentaires du coût d'achat des produits vendus sont désormais déduits et non plus ajoutés.
- Les ventes couvertes par un document fiscal sur bases avec des retours sont désormais elles aussi recalculées lors du recalcul du coût, avec le document fiscal et ses retours.
- Les rapports « Analyse ABC des ventes » et « Produits vendus sans facture » indiquent à quelle date le coût est à jour. Dans la fiche de vente, l'utilisateur de l'espace client ne voit ni le coût, ni la marge, ni la majoration.
### en
- Margin is calculated by batch and by additional cost item: the cost of goods sold is kept separately from revenue — for each batch the goods left the warehouse from and for each additional cost item (delivery, customs and others). The "Sales status", "Financial result", "ABC sales analysis", "Products sold without invoice" reports, the sales dashboard and profit-based payroll take the cost from there.
- Sales history is transferred: during the update, the cost of all past sales and returns is transferred automatically and reconciled with the previous data document by document; the margin in reports for past periods does not change. If the history contains returns that brought back more than was sold from a batch, the update stops and names those documents.
- Customer return: the second and further partial returns of the same sale bring back the remaining batches, not the first ones again; several lines of the same item in a return do not bring back one batch twice either. Return revenue is calculated from the part of the sale not yet returned — after a full return the sale comes to exactly zero.
- "Financial result": additional costs in the purchase cost of goods sold are now subtracted instead of added.
- Sales covered by a tax document on bases with returns are now also recalculated during cost recalculation, together with the tax document and its returns.
- The "ABC sales analysis" and "Products sold without invoice" reports show up to which moment the cost is current. In the sale form, a customer portal user does not see the cost, profit and markup.
### es
- El margen se calcula por lote y por partida de gastos adicionales: el coste de la mercancía vendida se guarda aparte de los ingresos — por cada lote del que la mercancía salió del almacén y por cada partida de gastos adicionales (transporte, aduana y otras). Los informes «Estado de ventas», «Resultado financiero», «Análisis ABC de ventas», «Productos vendidos sin factura», el panel de ventas y el cálculo de la nómina sobre el beneficio toman el coste de ahí.
- El historial de ventas se ha trasladado: en la actualización, el coste de todas las ventas y devoluciones anteriores se traslada automáticamente y se concilia con los datos anteriores documento por documento; el margen de los informes de periodos pasados no cambia. Si el historial contiene devoluciones que restituyeron más de lo vendido de un lote, la actualización se detiene y nombra esos documentos.
- Devolución del cliente: la segunda devolución parcial y las siguientes de una misma venta restituyen los lotes restantes y no los primeros de nuevo; varias líneas de un mismo artículo en una devolución tampoco restituyen un lote dos veces. Los ingresos de la devolución se calculan sobre la parte de la venta aún no devuelta — tras una devolución completa, la venta queda exactamente en cero.
- «Resultado financiero»: los gastos adicionales del coste de compra de lo vendido ahora se restan en vez de sumarse.
- Las ventas cubiertas por un documento fiscal sobre bases con devoluciones ahora también se recalculan en el recálculo del coste, junto con el documento fiscal y sus devoluciones.
- Los informes «Análisis ABC de ventas» y «Productos vendidos sin factura» muestran hasta qué momento el coste está al día. En la ficha de venta, el usuario del área de cliente no ve el coste, el beneficio ni el margen.

## 2.0.16.120
### ru
- Себестоимость выпуска продукции, требований-накладных и передачи в переработку теперь пересчитывается вместе с остальными документами: если задним числом провели поступление материала или изменили его цену, себестоимость выпуска и проданной продукции догонит это при пересчёте. Автовыпуск, «из остатка», стадии заказов, загрузка станков и закрепление материалов при пересчёте не меняются.
- Пересчёт себестоимости теперь идёт сам каждые 30 минут (если администратор не задал своё расписание) и только по документам, которые его ждут. Кнопка «Выполнить» в «Перепроведении документов» начинает с последнего пересчитанного документа; второй пересчёт одновременно не запускается. При ошибке документа пересчёт останавливается на нём — список в «Непроведенных документах».
- В отчётах «Стоимость склада», «Ведомость по товарам на складах», «Ведомость по продажам», «Финансовый результат», «Себестоимость продукции» видно, на какой момент себестоимость актуальна: пока пересчёт не догнал документы, над отчётом — строка «Себестоимость пересчитана по…». На дашборде продаж — карточка «Себестоимость» со ссылкой «Пересчитать».
- После обновления первый пересчёт пройдёт и по прежним выпускам и переработке — это может занять время на базе с длинной историей.
### fr
- Le coût de revient des productions, des bons de consommation et des transferts en sous-traitance est désormais recalculé avec les autres documents : si une réception de matière a été validée à une date antérieure ou si son prix a changé, le coût de la production et des produits vendus est mis à jour lors du recalcul. La fabrication automatique, le « depuis le stock », les étapes des commandes, la charge des machines et les matières réservées ne changent pas lors du recalcul.
- Le recalcul du coût s'exécute maintenant automatiquement toutes les 30 minutes (sauf si l'administrateur a défini son propre planning) et uniquement pour les documents qui l'attendent. Le bouton « Exécuter » de « Repasser les documents » commence au dernier document recalculé ; un second recalcul simultané ne démarre pas. En cas d'erreur sur un document, le recalcul s'arrête sur celui-ci — liste dans « Documents non reportés ».
- Les rapports « Valeur du stock », « État des stocks », « État des ventes », « Résultat financier » et « Coût de revient des produits » indiquent à quelle date le coût est à jour : tant que le recalcul n'a pas rattrapé les documents, une ligne « Coût de revient recalculé jusqu'au… » s'affiche au-dessus du rapport. Le tableau de bord des ventes a une carte « Coût de revient » avec le lien « Recalculer ».
- Après la mise à jour, le premier recalcul passera aussi sur les productions et la sous-traitance existantes — cela peut prendre du temps sur une base avec un long historique.
### en
- The cost of production output, requisitions and transfers for subcontracting is now recalculated together with the other documents: if a material receipt was posted backdated or its price changed, the cost of the output and of the products sold catches up during recalculation. Automatic output, "from stock", order stages, machine load and reserved materials do not change during recalculation.
- Cost recalculation now runs by itself every 30 minutes (unless the administrator set a schedule of their own) and only for the documents waiting for it. The "Run" button in "Document reposting" starts from the last recalculated document; a second recalculation does not start at the same time. If a document fails, recalculation stops on it — see the list in "Documents not postponed".
- The "Warehouse value", "Inventory status", "Sales status", "Financial result" and "Product cost" reports show up to which moment the cost is current: while recalculation has not caught up with the documents, a "Cost recalculated up to…" line is shown above the report. The sales dashboard has a "Cost" card with a "Recalculate" link.
- After the update, the first recalculation also goes through existing production output and subcontracting — it may take a while on a database with a long history.
### es
- El coste de la producción, de los vales de consumo y de las transferencias a subcontratación ahora se recalcula junto con los demás documentos: si una recepción de materia se contabilizó con fecha anterior o cambió su precio, el coste de la producción y de los productos vendidos se pone al día en el recálculo. La fabricación automática, el «desde el stock», las etapas de los pedidos, la carga de las máquinas y los materiales reservados no cambian en el recálculo.
- El recálculo del coste ahora se ejecuta solo cada 30 minutos (salvo que el administrador haya fijado su propia programación) y solo para los documentos que lo esperan. El botón «Ejecutar» de «Volver a contabilizar documentos» empieza por el último documento recalculado; un segundo recálculo no se inicia a la vez. Si un documento falla, el recálculo se detiene en él — lista en «Documentos no aplazados».
- Los informes «Valor del almacén», «Estado del inventario», «Estado de ventas», «Resultado financiero» y «Coste de los productos» muestran hasta qué momento el coste está al día: mientras el recálculo no alcanza a los documentos, sobre el informe aparece la línea «Coste recalculado hasta…». El panel de ventas tiene una tarjeta «Coste» con el enlace «Recalcular».
- Tras la actualización, el primer recálculo pasará también por las producciones y subcontrataciones existentes; puede tardar en una base con un historial largo.

## 2.0.16.119
### ru
- Отгрузка продукции, полученной от переработчика: если отгрузку (например, расходный ордер) создали заранее, а продукция пришла позже её даты, программа больше не пытается произвести эту продукцию заново и не пишет о нехватке сырья. Вместо этого она называет поступление из переработки и подсказывает, на какую дату перенести отгрузку, чтобы её провести.
### fr
- Expédition d'un produit reçu du sous-traitant : si l'expédition (par exemple un bon de sortie) a été créée à l'avance et que le produit est arrivé après sa date, le programme n'essaie plus de refabriquer ce produit et n'annonce plus un manque de matières. Il indique la réception de sous-traitance et la date à laquelle reporter l'expédition pour la valider.
### en
- Shipping a product received from the subcontractor: if the shipment (for example, a goods issue order) was created in advance and the product arrived after its date, the program no longer tries to produce the product again or reports missing materials. Instead, it names the subcontracting receipt and suggests the date to move the shipment to so that it can be posted.
### es
- Envío de un producto recibido del subcontratista: si el envío (por ejemplo, una orden de salida) se creó de antemano y el producto llegó después de su fecha, el programa ya no intenta volver a fabricarlo ni informa de falta de materias. En su lugar, indica la recepción de subcontratación y la fecha a la que mover el envío para contabilizarlo.

## 2.0.16.118
### ru
- Кнопки, которые работают с выделенными строками, теперь действительно остаются в панели, когда строки отмечены флажками: «Оформить поступлением» и «Оформить реализацией» в списках приходных и расходных ордеров и остальные кнопки из сборки 2.0.16.117.
- Списки приходных и расходных ордеров: снова видны дата и номер ордера, появились колонки «Наша компания» и «Количество» (сколько товара в ордере всего), колонка места хранения называется «Склад».
### fr
- Les boutons qui agissent sur les lignes sélectionnées restent maintenant vraiment dans la barre quand des lignes sont cochées : « Régulariser par une réception » et « Régulariser par une vente » dans les listes des bons de réception et de sortie, ainsi que les autres boutons de la version 2.0.16.117.
- Listes des bons de réception et de sortie : la date et le numéro du bon sont de nouveau affichés, les colonnes « Notre société » et « Quantité » (quantité totale d'articles du bon) sont ajoutées, la colonne du lieu de stockage s'appelle « Entrepôt ».
### en
- Buttons that act on the selected lines now really stay in the bar when lines are checked: "Document with a receipt" and "Document with a sale" in the goods receipt and goods issue order lists, and the other buttons from build 2.0.16.117.
- Goods receipt and goods issue order lists: the order date and number are shown again, the "Our company" and "Quantity" (total quantity of goods in the order) columns are added, and the storage place column is now called "Warehouse".
### es
- Los botones que actúan sobre las líneas seleccionadas ahora sí permanecen en la barra cuando las líneas están marcadas: «Formalizar con una recepción» y «Formalizar con una venta» en las listas de órdenes de entrada y de salida, y los demás botones de la versión 2.0.16.117.
- Listas de órdenes de entrada y de salida: vuelven a mostrarse la fecha y el número de la orden, se añaden las columnas «Nuestra empresa» y «Cantidad» (cantidad total de artículos de la orden) y la columna del lugar de almacenamiento se llama «Almacén».

## 2.0.16.117
### ru
- Кнопки, которые работают с выделенными строками, теперь остаются в панели и тогда, когда строки отмечены флажками: «Оформить реализацию» и печать «Коммерческое предложение» в списке реализаций, «Оформить поступление» в списке поступлений, «Изменить выделенные» в бухгалтерских операциях, «Сохранить на диск» в присоединённых файлах, фискализация в очереди чеков, «Создать поступление» по заказам в рабочем месте закупок, а также команды служебных обработок регламентных заданий и регистрации изменений для обмена.
### fr
- Les boutons qui agissent sur les lignes sélectionnées restent désormais dans la barre quand des lignes sont cochées : « Créer la vente » et l'impression « Devis » dans la liste des ventes, « Créer la réception » dans la liste des réceptions, « Modifier la sélection » dans les opérations comptables, « Enregistrer sur le disque » dans les fichiers joints, la fiscalisation dans la file des tickets, « Créer une réception » par commandes au poste des achats, ainsi que les commandes des traitements de service des tâches planifiées et de l'enregistrement des modifications pour l'échange.
### en
- Buttons that act on the selected lines now stay in the bar when lines are checked: "Create sale" and the "Quotation" print in the sales list, "Create receipt" in the receipts list, "Edit the selection" in accounting operations, "Save to disk" in attached files, fiscalization in the receipt queue, "Create receipt" by orders in the purchasing workplace, and the commands of the scheduled jobs and exchange change registration service tools.
### es
- Los botones que actúan sobre las líneas seleccionadas ahora permanecen en la barra cuando las líneas están marcadas: «Crear la venta» y la impresión «Presupuesto» en la lista de ventas, «Crear la recepción» en la lista de recepciones, «Edite la selección» en las operaciones contables, «Guardar en disco» en los archivos adjuntos, la fiscalización en la cola de tickets, «Crear recepción» por pedidos en el puesto de compras, y los comandos de los procesamientos de servicio de tareas programadas y del registro de cambios para el intercambio.

## 2.0.16.116
### ru
- Списки приходных и расходных ордеров: кнопки «Оформить поступлением» и «Оформить реализацией» больше не пропадают, когда строки отмечены флажками, — отмеченные ордера оформляются одним документом прямо из панели отмеченных строк.
### fr
- Listes des bons de réception et de sortie : les boutons « Régulariser par une réception » et « Régulariser par une vente » ne disparaissent plus quand des lignes sont cochées — les bons cochés se régularisent en un seul document directement depuis la barre des lignes cochées.
### en
- Goods receipt and goods issue order lists: the "Document with a receipt" and "Document with a sale" buttons no longer disappear when lines are checked — the checked orders are documented with one document right from the checked-lines bar.
### es
- Listas de órdenes de entrada y de salida: los botones «Formalizar con una recepción» y «Formalizar con una venta» ya no desaparecen al marcar líneas — las órdenes marcadas se formalizan en un solo documento directamente desde la barra de líneas marcadas.

## 2.0.16.115
### ru
- Рабочее место закупок, «Поступления», режим «Товары»: новая строка добавляется сверху, строки идут по документам — свежие сверху, внутри документа последняя добавленная строка первой.
- Записанную строку теперь можно править как в рабочем месте производства: двойной щелчок по количеству, товару или цене начинает правку, а форму документа открывает щелчок по колонке «Документ» или «Статус». После закрытия документа курсор остаётся на той же строке. Если правку записать нельзя, появляется сообщение и строке возвращаются записанные значения.
- Новое меню «Изменить статус» — провести, вернуть в черновик или пометить на удаление документы выделенных строк.
### fr
- Poste des achats, « Réceptions », mode « Articles » : la nouvelle ligne s'ajoute en haut, les lignes suivent les documents — les plus récents en haut, et dans un document la dernière ligne ajoutée en premier.
- Une ligne enregistrée se modifie maintenant comme au poste de production : un double-clic sur la quantité, l'article ou le prix lance la modification, et le formulaire du document s'ouvre par un clic sur la colonne « Document » ou « Statut ». Après la fermeture du document, le curseur reste sur la même ligne. Si la modification ne peut pas être enregistrée, un message s'affiche et la ligne reprend ses valeurs enregistrées.
- Nouveau menu « Changer le statut » : valider, remettre en brouillon ou marquer pour suppression les documents des lignes sélectionnées.
### en
- Purchasing workplace, "Receipts", "Items" mode: a new line is added at the top; lines follow documents — newest at the top, and within a document the last added line comes first.
- A saved line can now be edited as in the production workplace: double-clicking the quantity, item or price starts editing, while clicking the "Document" or "Status" column opens the document form. After the document is closed, the cursor stays on the same line. If a change cannot be saved, a message appears and the line gets its saved values back.
- New "Change status" menu: post, return to draft, or mark for deletion the documents of the selected lines.
### es
- Puesto de compras, «Recepciones», modo «Artículos»: la línea nueva se añade arriba; las líneas siguen los documentos — los más recientes arriba y, dentro de un documento, la última línea añadida primero.
- Una línea guardada ahora se edita como en el puesto de producción: un doble clic en la cantidad, el artículo o el precio inicia la edición, y el formulario del documento se abre con un clic en la columna «Documento» o «Estado». Al cerrar el documento, el cursor queda en la misma línea. Si el cambio no se puede guardar, aparece un mensaje y la línea recupera sus valores guardados.
- Nuevo menú «Cambiar estado»: contabilizar, devolver a borrador o marcar para eliminar los documentos de las líneas seleccionadas.

## 2.0.16.114
### ru
- Рабочее место производства, закладка «Выпуск»: в списке выбора поля «Продукция» теперь есть каждый полуфабрикат из материалов заказа, а не только тот, под которым в заказе лежит его сырьё. Полуфабрикатом считается материал со способом изготовления «Наше производство» или «Оба», а если способ не указан — позиция, которая производится по техкарте. Закупаемые материалы и материалы переработчика в список не попадают. Чтобы выпуск полуфабриката провёлся, у него должна быть техкарта.
### fr
- Poste de production, onglet « Production » : la liste de choix du champ « Produit » propose désormais chaque semi-fini des matières de la commande, et pas seulement celui sous lequel la commande contient ses matières. Est un semi-fini une matière en mode de fabrication « Notre fabrication » ou « Les deux », ou, sans mode indiqué, un article fabriqué selon une gamme. Les matières achetées et celles du sous-traitant n'y figurent pas. Pour que la production du semi-fini soit validée, il lui faut une gamme.
### en
- Production workplace, "Output" tab: the choice list of the "Product" field now offers every semi-finished item from the order materials, not only one with its own materials under it in the order. A semi-finished item is a material with the "Our production" or "Both" manufacturing method or, with no method set, an item produced by a routing. Purchased materials and subcontractor materials are not listed. The semi-finished item needs a routing for its output to be posted.
### es
- Puesto de producción, pestaña «Producción»: la lista de selección del campo «Producto» ofrece ahora cada semielaborado de los materiales del pedido, no solo el que tiene sus materias debajo en el pedido. Es semielaborado un material con el modo de fabricación «Producción propia» o «Ambos» o, sin modo indicado, un artículo fabricado según una ruta. Los materiales comprados y los del subcontratista no aparecen. Para contabilizar la producción del semielaborado, este necesita una ruta.

## 2.0.16.113
### ru
- Полуфабрикат, у которого в карточке способ пополнения «Оба» (делаем и покупаем), теперь производится, если в строке техкарты изделия стоит «Наше производство»: он попадает в дерево материалов заказа со своим сырьём. После обновления проверьте строки таких полуфабрикатов в техкартах — обновление 2.0.16.103 поставило им «Закупка» — и в открытых заказах заполните материалы по техкарте заново.
- При включённом «Автовыпуске при отгрузке» полуфабрикат снова можно выпустить вручную на закладке «Выпуск» рабочего места производства. Автовыпуск изделия при отгрузке берёт уже выпущенный по заказу полуфабрикат, а его сырьё списывает только на остальное количество — сырьё не списывается дважды.
### fr
- Un semi-fini dont la fiche indique le mode d'approvisionnement « Les deux » (fabriqué et acheté) est désormais fabriqué si la ligne de la gamme du produit indique « Notre fabrication » : il entre dans l'arbre des matières de la commande avec ses matières. Après la mise à jour, vérifiez les lignes de ces semi-finis dans les gammes — la mise à jour 2.0.16.103 leur a mis « Achat » — et remplissez à nouveau les matières des commandes ouvertes selon la gamme.
- Avec la « Production automatique à l'expédition », le semi-fini peut de nouveau être produit manuellement dans l'onglet « Production » du poste de production. La production automatique du produit à l'expédition prend le semi-fini déjà produit pour la commande et ne consomme ses matières que pour le reste — les matières ne sont pas consommées deux fois.
### en
- A semi-finished item whose card has the "Both" replenishment method (made and bought) is now produced when the product's routing line says "Our production": it enters the order's material tree with its materials. After the update, check these semi-finished lines in routings — update 2.0.16.103 set them to "Purchase" — and refill materials of open orders from the routing.
- With "Automatic output on shipment" on, semi-finished items can again be produced manually on the "Output" tab of the production workplace. Automatic output of the product on shipment takes the semi-finished item already produced for the order and consumes its materials only for the rest — materials are not consumed twice.
### es
- Un semielaborado con el modo de reposición «Ambos» (se fabrica y se compra) en su ficha ahora se fabrica si la línea de la ruta del producto indica «Producción propia»: entra en el árbol de materiales del pedido con sus materias. Tras la actualización, revise esas líneas en las rutas — la actualización 2.0.16.103 les puso «Compra» — y vuelva a llenar los materiales de los pedidos abiertos según la ruta.
- Con la «Producción automática al enviar», el semielaborado se puede producir de nuevo a mano en la pestaña «Producción» del puesto de producción. La producción automática del producto al enviar toma el semielaborado ya producido para el pedido y consume sus materias solo para el resto — las materias no se consumen dos veces.

## 2.0.16.112
### ru
- Рабочее место закупок, «Поступления», режим «Товары»: колонки «№ накл.» и «Дата накл.» — номер и дата накладной поставщика вводятся прямо в строке и попадают в новое поступление. Строки с тем же номером накладной того же поставщика на том же складе сами попадают в одно сегодняшнее поступление, как в рабочем месте производства.
### fr
- Poste des achats, « Réceptions », mode « Articles » : colonnes « N° fact. » et « Date fact. » — le numéro et la date de la facture du fournisseur se saisissent dans la ligne et passent dans la nouvelle réception. Les lignes avec le même numéro de facture du même fournisseur sur le même entrepôt vont d'elles-mêmes dans une seule réception du jour, comme au poste de production.
### en
- Purchasing workplace, "Receipts", "Items" mode: "Invoice No." and "Invoice date" columns — the supplier invoice number and date are entered in the line and go into the new receipt. Lines with the same invoice number of the same supplier on the same warehouse go into one receipt of the day, as in the production workplace.
### es
- Puesto de compras, «Recepciones», modo «Artículos»: columnas «N.º fact.» y «Fecha fact.» — el número y la fecha de la factura del proveedor se introducen en la línea y pasan a la nueva recepción. Las líneas con el mismo número de factura del mismo proveedor en el mismo almacén van solas a una recepción del día, como en el puesto de producción.

## 2.0.16.111
### ru
- Рабочее место закупок, «Поступления», режим «Товары»: новая колонка «Склад». По складу строки программа сама выбирает документ — на ордерном складе приходный ордер, на обычном поступление, как в рабочем месте производства. По умолчанию подставляется склад поступлений из настроек пользователя.
- При выборе товара в новой строке сразу заполняется единица из карточки товара и видно, к какому заказу поставщику строка будет привязана.
- Колонка «Характеристика» показывается только при включённом учёте характеристик, «Цена» и «Сумма» — только пользователю, которому в дополнительных настройках разрешён просмотр сумм.
### fr
- Poste des achats, « Réceptions », mode « Articles » : nouvelle colonne « Entrepôt ». Selon l'entrepôt de la ligne, le programme choisit le document — bon de réception sur un entrepôt à bons, réception sinon, comme au poste de production. Par défaut, l'entrepôt de réception des paramètres de l'utilisateur.
- Au choix de l'article dans une nouvelle ligne, l'unité de la fiche article est remplie aussitôt et la commande fournisseur à laquelle la ligne sera rattachée est visible.
- La colonne « Caractéristique » n'apparaît que si les caractéristiques sont utilisées ; « Prix » et « Montant » seulement pour l'utilisateur autorisé à voir les montants dans ses paramètres supplémentaires.
### en
- Purchasing workplace, "Receipts", "Items" mode: new "Warehouse" column. The line's warehouse decides the document — a goods receipt note on an order-based warehouse, a receipt otherwise, as in the production workplace. By default, the receipt warehouse from the user settings.
- When an item is chosen in a new line, the unit from the item card is filled at once and the supplier order the line will be linked to is shown.
- The "Characteristic" column is shown only when characteristics are used; "Price" and "Amount" only for users allowed to see amounts in their additional settings.
### es
- Puesto de compras, «Recepciones», modo «Artículos»: nueva columna «Almacén». Según el almacén de la línea, el programa elige el documento — orden de entrada en un almacén por órdenes, recepción en otro caso, como en el puesto de producción. Por defecto, el almacén de recepciones de la configuración del usuario.
- Al elegir el artículo en una línea nueva, la unidad de la ficha se rellena enseguida y se ve el pedido al proveedor al que se vinculará la línea.
- La columna «Característica» se muestra solo si se usan características; «Precio» e «Importe», solo al usuario con permiso para ver importes en su configuración adicional.

## 2.0.16.110
### ru
- Акт передачи в переработку печатается в фирменном оформлении, как наши накладные: логотип, шрифты и цвета, заказчик и переработчик в шапке, переданное сырьё и ожидаемая продукция — разделами одной таблицы, подписи «Отпустил» и «Получил». Если вы меняли прежний макет акта, правка больше не действует (запись в журнале регистрации).
### fr
- Le bon de transfert en sous-traitance s'imprime dans la mise en page à en-tête, comme nos bons de livraison : logo, polices et couleurs, donneur d'ordre et sous-traitant en en-tête, matières transférées et produits attendus en sections d'un même tableau, signatures « Remis par » et « Reçu par ». Si vous aviez modifié l'ancien modèle du bon, la modification ne s'applique plus (entrée dans le journal).
### en
- The transfer for processing act is printed in the branded layout, like our delivery notes: logo, fonts and colours, customer and processor in the header, transferred materials and expected products as sections of one table, "Issued by" and "Received by" signatures. If you had changed the old act template, the change no longer applies (event log entry).
### es
- El acta de transferencia a procesamiento se imprime con el diseño corporativo, como nuestros albaranes: logotipo, fuentes y colores, cliente y subcontratista en la cabecera, materias transferidas y productos esperados como secciones de una misma tabla, firmas «Despachado por» y «Recibido por». Si había modificado la plantilla anterior del acta, el cambio ya no se aplica (entrada en el registro).

## 2.0.16.109
### ru
- Ручной выпуск по заказу на производство (строкой рабочего места производства) теперь уменьшает дефицит сырья: материалы, взятые со свободного склада, больше не предлагаются к закупке на закладке «Потребность» рабочего места закупок. Выпуск, проведённый до обновления, этого не делает — если «Потребность» предлагает докупить уже израсходованное сырьё, перепроведите такой выпуск.
- При включённом «Автовыпуске при отгрузке» рабочее место производства не предлагает вручную выпускать полуфабрикаты: изделие при отгрузке само спишет их сырьё.
- Рабочее место закупок, открытое на закладке «Поступления», сразу показывает подменю «Создать» (при ордерных складах) — раньше до смены закладки была видна простая кнопка.
- Исправлен запуск длительных операций в фоне.
### fr
- La production manuelle sur commande de fabrication (ligne du poste de production) réduit désormais le manque de matières : les matières prises sur le stock libre ne sont plus proposées à l'achat dans l'onglet « Besoin » du poste des achats. Une production validée avant la mise à jour ne le fait pas : si « Besoin » propose de racheter des matières déjà consommées, revalidez cette production.
- Avec la « Production automatique à l'expédition », le poste de production ne propose plus de produire manuellement les semi-finis : le produit consommera leurs matières à l'expédition.
- Le poste des achats ouvert sur l'onglet « Réceptions » affiche tout de suite le sous-menu « Créer » (avec entrepôts à bons) — auparavant, un simple bouton s'affichait jusqu'au changement d'onglet.
- Correction du lancement des opérations longues en arrière-plan.
### en
- Manual output for a production order (a line of the production workplace) now reduces the material shortage: materials taken from free stock are no longer offered for purchase on the "Requirement" tab of the purchasing workplace. Output posted before the update does not do this — if "Requirement" offers to buy materials already consumed, repost that output.
- With "Automatic output on shipment" enabled, the production workplace no longer offers manual output of semi-finished goods: the product consumes their materials on shipment.
- The purchasing workplace opened on the "Receipts" tab shows the "Create" submenu right away (with order-based warehouses) — before, a plain button was shown until the tab changed.
- Fixed starting long-running operations in the background.
### es
- La producción manual por pedido de fabricación (línea del puesto de producción) ahora reduce el déficit de materias primas: las tomadas del stock libre ya no se proponen para compra en la pestaña «Necesidad» del puesto de compras. Una producción contabilizada antes de la actualización no lo hace: si «Necesidad» propone comprar materias ya consumidas, vuelva a contabilizar esa producción.
- Con la «Producción automática al enviar», el puesto de producción ya no propone producir semielaborados a mano: el producto consumirá sus materias al enviar.
- El puesto de compras abierto en la pestaña «Recepciones» muestra enseguida el submenú «Crear» (con almacenes por órdenes); antes se veía un botón simple hasta cambiar de pestaña.
- Corregido el inicio de operaciones largas en segundo plano.

## 2.0.16.108
### ru
- Рабочее место закупок, закладка «Поступления»: новый переключатель «Документы / Товары». В режиме «Товары» строки поступлений вводятся прямо в таблице: укажите поставщика, товар и количество — при выходе из строки программа сама создаст и проведёт поступление.
- В колонке «Документ» следующей строки можно выбрать уже созданное сегодня поступление этого поставщика — строка добавится в него. Если ничего не выбирать, создаётся новое поступление.
- Если у поставщика есть открытый заказ на этот товар, строка сама привязывается к строке заказа и поступление оформляется по заказу. Иначе — поступление без заказа. Одно поступление относится либо к одному заказу, либо ни к какому: программа подскажет, если товар нужно ввести новым поступлением.
- На ордерном складе вместо поступления создаётся приходный ордер. Строки документов, которые правятся только в форме (с сериями, услугами, оформленные по ордеру), показываются для просмотра.
### fr
- Poste de travail des achats, onglet « Réceptions » : nouveau sélecteur « Documents / Articles ». En mode « Articles », les lignes de réception se saisissent directement dans le tableau : indiquez le fournisseur, l'article et la quantité — en quittant la ligne, le programme crée et valide la réception.
- Dans la colonne « Document » de la ligne suivante, vous pouvez choisir une réception déjà créée aujourd'hui pour ce fournisseur — la ligne y est ajoutée. Sans choix, une nouvelle réception est créée.
- Si le fournisseur a une commande ouverte pour cet article, la ligne se rattache à la ligne de commande et la réception suit la commande. Sinon, la réception est sans commande. Une réception concerne une seule commande ou aucune : le programme indique quand l'article doit passer par une nouvelle réception.
- Sur un entrepôt à bons, un bon d'entrée est créé à la place de la réception. Les lignes des documents qui ne se modifient que dans le formulaire (avec séries, services, régularisées par bon) sont affichées en lecture seule.
### en
- Purchasing workplace, "Receipts" tab: new "Documents / Items" switch. In "Items" mode, receipt lines are entered directly in the table: specify the supplier, item and quantity — when you leave the line, the program creates and posts the receipt.
- In the "Document" column of the next line you can select a receipt already created today for this supplier — the line is added to it. Without a choice, a new receipt is created.
- If the supplier has an open order for this item, the line is linked to the order line and the receipt follows the order. Otherwise the receipt has no order. A receipt belongs to one order or to none: the program tells you when the item must go into a new receipt.
- On an order-based warehouse a receiving order is created instead of the receipt. Lines of documents that are edited only in the form (with series, services, or settled by an order) are shown read-only.
### es
- Puesto de compras, pestaña «Recepciones»: nuevo selector «Documentos / Artículos». En el modo «Artículos», las líneas de recepción se introducen directamente en la tabla: indique el proveedor, el artículo y la cantidad; al salir de la línea, el programa crea y contabiliza la recepción.
- En la columna «Documento» de la línea siguiente puede elegir una recepción ya creada hoy para este proveedor: la línea se añade a ella. Sin elegir, se crea una recepción nueva.
- Si el proveedor tiene un pedido abierto de este artículo, la línea se vincula a la línea del pedido y la recepción sigue el pedido. Si no, la recepción va sin pedido. Una recepción pertenece a un solo pedido o a ninguno: el programa avisa cuando el artículo debe ir en una recepción nueva.
- En un almacén por órdenes se crea una orden de entrada en lugar de la recepción. Las líneas de documentos que solo se editan en el formulario (con series, servicios o regularizadas por orden) se muestran solo para consulta.

## 2.0.16.107
### ru
- Новая настройка «Ордерные склады» (настройки программы, раздел «Склад»). Пока она выключена, флажок «Ордерный склад» в карточке склада, приходные и расходные ордера в меню скрыты — программа выглядит проще для тех, кто ордерами не пользуется.
- В базах, где уже есть ордерные склады или ордера, настройка включается сама при обновлении — ничего не меняется. Выключить её нельзя, пока есть ордерные склады или ордера: программа подскажет, что мешает.
- Рабочее место закупок, закладка «Поступления»: при включённых ордерных складах кнопка «Создать» открывает меню «Создать поступление» и «Создать приходный ордер». На остальных закладках «Создать» по-прежнему создаёт заказ поставщику.
### fr
- Nouveau paramètre « Entrepôts à bons » (paramètres du programme, section « Entrepôt »). Tant qu'il est désactivé, la case « Entrepôt à bons » de la fiche entrepôt ainsi que les bons d'entrée et de sortie du menu sont masqués : le programme est plus simple pour ceux qui n'utilisent pas les bons.
- Dans les bases qui ont déjà des entrepôts à bons ou des bons, le paramètre s'active tout seul à la mise à jour : rien ne change. Il ne peut pas être désactivé tant qu'il existe des entrepôts à bons ou des bons : le programme indique ce qui l'empêche.
- Poste de travail des achats, onglet « Réceptions » : avec les entrepôts à bons activés, le bouton « Créer » ouvre le menu « Créer une réception » et « Créer un bon d'entrée ». Sur les autres onglets, « Créer » crée toujours une commande fournisseur.
### en
- New "Order-based warehouses" setting (program settings, "Warehouse" section). While it is off, the "Order-based warehouse" flag on the warehouse card and the receiving and goods issue orders in the menu are hidden, so the program is simpler for those who do not use orders.
- In databases that already have order-based warehouses or orders, the setting turns on by itself during the update, so nothing changes. It cannot be turned off while order-based warehouses or orders exist; the program shows what prevents it.
- Purchasing workplace, "Receipts" tab: with order-based warehouses on, the "Create" button opens a menu with "Create receipt" and "Create receiving order". On the other tabs, "Create" still creates a supplier order.
### es
- Nuevo ajuste «Almacenes con órdenes» (ajustes del programa, sección «Almacén»). Mientras está desactivado, la casilla «Almacén por órdenes» de la ficha del almacén y las órdenes de entrada y salida del menú se ocultan: el programa es más sencillo para quien no usa órdenes.
- En las bases que ya tienen almacenes por órdenes u órdenes, el ajuste se activa solo al actualizar: no cambia nada. No se puede desactivar mientras existan almacenes por órdenes u órdenes; el programa indica qué lo impide.
- Puesto de compras, pestaña «Recepciones»: con los almacenes por órdenes activados, el botón «Crear» abre el menú «Crear recepción» y «Crear orden de entrada». En las demás pestañas, «Crear» sigue creando un pedido a proveedor.

## 2.0.16.106
### ru
- Карточка товара, закладка «Производство»: смена способа изготовления в строке технологической карты больше не закрывает программу. Если сразу после правки строки записать карточку, правка сохраняется.
- Расходный ордер на товары и поступление товаров и услуг (строки товаров и дополнительных расходов): можно выбрать любую номенклатуру, а не только товары. Строки услуг по-прежнему принимают только услуги.
- Рабочее место «Управление станками»: при переходе на закладку «Под риском» риски снова рассчитываются сразу, без нажатия «Обновить».
### fr
- Fiche article, onglet « Production » : changer le mode de fabrication d'une ligne de la gamme ne ferme plus l'application. Si la fiche est enregistrée juste après la modification de la ligne, la modification est conservée.
- Bon de sortie et achat (lignes de marchandises et de dépenses supplémentaires) : tout article peut être choisi, et pas seulement les marchandises. Les lignes de services n'acceptent toujours que des services.
- Poste « Gestion des machines » : en ouvrant l'onglet « À risque », les risques sont de nouveau calculés aussitôt, sans cliquer sur « Actualiser ».
### en
- Item card, "Production" tab: changing the manufacturing method in a routing line no longer closes the application. If the card is saved right after editing the line, the change is kept.
- Goods issue order and purchase (goods and additional expense lines): any item can be selected, not only goods. Service lines still accept services only.
- "Machine management" workplace: opening the "At risk" tab again calculates the risks straight away, without clicking "Refresh".
### es
- Ficha del artículo, pestaña «Producción»: cambiar el modo de fabricación en una línea de la ruta ya no cierra el programa. Si la ficha se guarda justo después de editar la línea, el cambio se conserva.
- Orden de salida de mercancías y compra (líneas de mercancías y de gastos adicionales): se puede elegir cualquier artículo, no solo mercancías. Las líneas de servicios siguen admitiendo solo servicios.
- Puesto «Gestión de máquinas»: al abrir la pestaña «En riesgo», los riesgos vuelven a calcularse en el acto, sin pulsar «Actualizar».

## 2.0.16.105
### ru
- Рабочее место закупок: при переключении закладок «Потребность», «Заказы поставщикам» и «Поступления» снова перестраивается нижняя панель и обновляются данные закладки. Раньше нижняя панель могла пропасть и не возвращалась.
- Карточка товара: при переходе на закладки «Цена», «Склад», «Производство» и «Служебное» снова загружаются цены, технологическая карта и сведения закладки — они не заполнялись с 2.0.16.62.

- Рабочее место производства, закладка «Выпуск»: выпуск полуфабриката, созданный автоматически при передаче в переработку, теперь виден в списке, как автовыпуск при отгрузке.
- Приходный ордер: в строках можно выбрать любую номенклатуру, а не только товары.
- Рабочее место производства: легенда индикатора стадий выведена бледным цветом.
### fr
- Poste de travail des achats : en changeant d'onglet entre « Besoin », « Commandes fournisseurs » et « Réceptions », le panneau inférieur est de nouveau reconstruit et les données de l'onglet actualisées. Auparavant, le panneau inférieur pouvait disparaître sans revenir.
- Fiche article : en passant aux onglets « Prix », « Stock », « Production » et « Service », les prix, la gamme et les informations de l'onglet sont de nouveau chargés — ils ne l'étaient plus depuis 2.0.16.62.

- Poste de travail de production, onglet « Production » : la production du semi-fini créée automatiquement au transfert en sous-traitance apparaît désormais dans la liste, comme la production automatique à l'expédition.
- Bon d'entrée : les lignes acceptent tout article, et pas seulement les marchandises.
- Poste de travail de production : la légende de l'indicateur d'étapes est affichée en couleur atténuée.
### en
- Purchasing workplace: switching between the "Need", "Supplier orders" and "Receipts" tabs again rebuilds the bottom panel and refreshes the tab data. Previously the bottom panel could disappear and not come back.
- Item card: opening the "Price", "Stock", "Production" and "Service" tabs again loads prices, the routing and the tab details — they had not been filled since 2.0.16.62.

- Production workplace, "Output" tab: the semi-finished output created automatically on transfer for processing is now shown in the list, like the automatic output on shipment.
- Receiving order: lines accept any item, not only goods.
- Production workplace: the stage indicator legend is shown in a muted colour.
### es
- Puesto de compras: al cambiar entre las pestañas «Necesidad», «Pedidos a proveedores» y «Recepciones», el panel inferior vuelve a reconstruirse y los datos de la pestaña se actualizan. Antes el panel inferior podía desaparecer y no volvía.
- Ficha del artículo: al pasar a las pestañas «Precio», «Stock», «Producción» y «Servicio» vuelven a cargarse los precios, la ruta y los datos de la pestaña; no se rellenaban desde 2.0.16.62.
- Puesto de producción, pestaña «Producción»: la producción del semielaborado creada automáticamente al transferir a procesamiento ahora aparece en la lista, como la producción automática al expedir.
- Orden de entrada: las líneas admiten cualquier artículo, no solo mercancías.
- Puesto de producción: la leyenda del indicador de etapas se muestra en un color atenuado.

## 2.0.16.104
### ru
- Рабочее место производства, закладка «Выпуск»: в выборе продукции теперь есть и полуфабрикаты собственного производства из материалов заказа, с количеством, которое ещё осталось выпустить. Выпуск полуфабриката списывает его сырьё по его технологической карте и приходует полуфабрикат на склад; выпуск изделия затем списывает уже выпущенный полуфабрикат.

### fr
- Poste de travail de production, onglet « Production » : le choix du produit propose désormais aussi les produits semi-finis de notre production issus des matières de la commande, avec la quantité restant à produire. La production d'un semi-fini consomme ses matières selon sa gamme et entre le semi-fini en stock ; la production du produit consomme ensuite le semi-fini déjà produit.

### en
- Production workplace, "Output" tab: the product choice now also offers in-house semi-finished products from the order's materials, with the quantity still to be produced. Producing a semi-finished product consumes its materials by its routing and puts it in stock; producing the product then consumes the semi-finished product already produced.

### es
- Puesto de producción, pestaña «Producción»: la elección del producto ahora también ofrece los semielaborados de producción propia de los materiales del pedido, con la cantidad que queda por producir. Producir un semielaborado consume sus materiales según su ruta y lo da de alta en stock; producir el producto consume después el semielaborado ya producido.

## 2.0.16.103
### ru
- Технологическая карта: новый способ изготовления «Закупка». У закупаемых материалов он ставится сам, у производимых — «Наше производство»; при смене материала в строке способ подставляется заново, а выбор «Переработчик» или «Оба» сохраняется. Существующие карты переведены обновлением.
- Полуфабрикат, который делает переработчик из вашего сырья, теперь раскрывается, если его собственная карта — только из закупаемого сырья и этот полуфабрикат больше нигде в заказе не встречается (отдельной строкой или своим производством); иначе он считается, как раньше. Его сырьё попадает в «Материалы» заказа, в потребность и в рабочее место закупок. Сам полуфабрикат не закупается — его приносит поступление из переработки. Сырьё, переданное переработчику по заказу, считается обеспеченным.
- При отгрузке изделия программа списывает полуфабрикат, полученный от переработчика, а не его сырьё.
- Рабочее место производства, закладка «Материалы»: колонка «Способ изготовления» стоит сразу за «Продукцией» и заполнена на всех уровнях.
- В уже созданных заказах сырьё полуфабриката переработчика появится после команды «Заполнить по техкарте» в заказе.

### fr
- Gamme de fabrication : nouveau mode de fabrication « Achat ». Il s'applique automatiquement aux matières achetées, « Notre production » aux articles fabriqués ; en changeant la matière d'une ligne, le mode est proposé à nouveau, tandis qu'un choix « Sous-traitant » ou « Les deux » est conservé. Les gammes existantes sont mises à jour.
- Le produit semi-fini fabriqué par un sous-traitant à partir de vos matières est désormais détaillé, si sa propre gamme ne contient que des matières achetées et qu'il ne figure nulle part ailleurs dans la commande (ligne à part ou notre production) ; sinon, il est compté comme avant. Ses matières apparaissent dans les « Matières » de la commande, dans les besoins et dans le poste de travail des achats. Le semi-fini lui-même n'est pas acheté — il arrive par la réception de sous-traitance. Les matières transférées au sous-traitant pour la commande sont considérées comme couvertes.
- À l'expédition du produit, le programme sort le semi-fini reçu du sous-traitant, et non ses matières.
- Poste de travail de production, onglet « Matières » : la colonne « Mode de fabrication » suit directement « Produit » et est renseignée à tous les niveaux.
- Dans les commandes déjà créées, les matières du semi-fini du sous-traitant apparaissent après la commande « Remplir selon la gamme de fabrication » de la commande.

### en
- Production routing: new manufacturing method "Purchase". It is set automatically for purchased materials, "In-house production" for manufactured items; when the material of a line changes, the method is suggested again, while a "Subcontractor" or "Both" choice is kept. Existing routings are updated.
- A semi-finished product made by a subcontractor from your materials is now expanded, if its own routing contains only purchased materials and it appears nowhere else in the order (as a separate line or in-house production); otherwise it is counted as before. Its materials appear in the order's "Materials", in the requirements and in the purchasing workplace. The semi-finished product itself is not purchased — it comes in with the receipt from processing. Materials transferred to the subcontractor for the order count as covered.
- When the product is shipped, the program writes off the semi-finished product received from the subcontractor, not its materials.
- Production workplace, "Materials" tab: the "Manufacturing method" column follows "Product" and is filled at every level.
- In orders created earlier, the subcontracted semi-finished product's materials appear after the order's "Fill from production routing" command.

### es
- Ruta de fabricación: nuevo método de fabricación «Compra». Se asigna solo a los materiales comprados, «Producción propia» a los fabricados; al cambiar el material de una línea, el método se propone de nuevo, y una elección «Subcontratista» o «Ambos» se conserva. Las rutas existentes se actualizan.
- El semielaborado que fabrica un subcontratista con sus materiales ahora se despliega, si su propia ruta solo contiene materiales comprados y no aparece en ninguna otra parte del pedido (línea aparte o producción propia); si no, se cuenta como antes. Sus materiales aparecen en los «Materiales» del pedido, en las necesidades y en el puesto de compras. El semielaborado en sí no se compra: llega con la recepción de procesamiento. Los materiales transferidos al subcontratista para el pedido cuentan como cubiertos.
- Al expedir el producto, el programa da de baja el semielaborado recibido del subcontratista, no sus materiales.
- Puesto de producción, pestaña «Materiales»: la columna «Método de fabricación» sigue a «Producto» y se rellena en todos los niveles.
- En los pedidos ya creados, los materiales del semielaborado del subcontratista aparecen tras el comando «Rellenar según ruta de fabricación» del pedido.

## 2.0.16.102
### ru
- Карточка товара, закладка «Производство»: смена способа изготовления в строке технологической карты больше не закрывает программу с ошибкой.

### fr
- Fiche article, onglet « Production » : changer le mode de fabrication d'une ligne de la gamme ne fait plus planter l'application.

### en
- Item card, "Production" tab: changing the manufacturing method of a routing line no longer crashes the application.

### es
- Ficha del artículo, pestaña «Producción»: cambiar el modo de fabricación de una línea de la ruta ya no cierra la aplicación con un error.

## 2.0.16.101
### ru
- Ордерный склад: товар, принятый приходным ордером, сразу виден в остатке и при подборе товара в рабочем месте кассира — не нужно ждать, пока менеджер оформит поступление. Раньше подбор показывал товар только после поступления.
- Отчёт «Движения товара»: количество теперь считается по приходным и расходным ордерам (показатели «Поступило» и «Продано»), а сумма — по поступлениям и реализациям, как и раньше.
- Отчёт «Проданный товар без накладной»: остатки складов — по товару на полке. Строка товара больше не повторяется по числу партий на складе.

- Рабочее место закупок: кнопка «Создать» снова работает — на закладке «Поступления» она открывает новое поступление, а если ваш склад поступлений ордерный — приходный ордер: товар сразу принимается на склад, поступление менеджер оформит потом. На остальных закладках — новый заказ поставщику. Раньше кнопка выдавала ошибку.
### fr
- Entrepôt à bons : la marchandise reçue par un bon d'entrée apparaît immédiatement dans le stock et dans la sélection de produits du poste de caisse, sans attendre que le gestionnaire saisisse la réception. Auparavant, la sélection ne la montrait qu'après la réception.
- Rapport « Mouvement de marchandises » : la quantité est désormais calculée d'après les bons d'entrée et de sortie (indicateurs « Reçu » et « Vendu »), le montant d'après les réceptions et les ventes, comme avant.
- Rapport « Stock vendu non facturé » : les stocks des entrepôts reflètent la marchandise en rayon. La ligne d'un produit n'est plus répétée autant de fois qu'il y a de lots en stock.

- Poste de travail des achats : le bouton « Créer » fonctionne à nouveau — sur l'onglet « Réceptions », il ouvre une nouvelle réception, ou un bon d'entrée si votre entrepôt de réception fonctionne par bons : la marchandise entre tout de suite en stock, le gestionnaire saisira la réception plus tard. Sur les autres onglets — une nouvelle commande fournisseur. Auparavant, le bouton renvoyait une erreur.
### en
- Warehouse with warehouse orders: goods taken in by a receiving order show up in the stock and in the cashier workplace product selection right away, without waiting for the manager to register the receipt. Previously the selection showed them only after the receipt.
- "Movement of goods" report: the quantity now follows receiving and issuing orders ("Received" and "Sold" indicators), while the amount follows receipts and sales, as before.
- "Stock sold not invoiced" report: warehouse balances reflect the goods on the shelf. A product line is no longer repeated once per stock batch.

- Purchasing workplace: the "Create" button works again — on the "Receipts" tab it opens a new receipt, or a receiving order if your receiving warehouse works with warehouse orders: the goods enter the stock right away and the manager registers the receipt later. On the other tabs — a new supplier order. Previously the button raised an error.
### es
- Almacén con órdenes: la mercancía recibida con una orden de entrada aparece de inmediato en el stock y en la selección de productos del puesto de caja, sin esperar a que el gestor registre la recepción. Antes la selección la mostraba solo después de la recepción.
- Informe «Circulación de mercancías»: la cantidad se calcula ahora por las órdenes de entrada y de salida (indicadores «Recibido» y «Vendido»), y el importe por las recepciones y ventas, como antes.
- Informe «Stock vendido no facturado»: los stocks de los almacenes reflejan la mercancía en estantería. La línea de un producto ya no se repite tantas veces como lotes hay en stock.
- Puesto de trabajo de compras: el botón «Crear» vuelve a funcionar: en la pestaña «Recepciones» abre una nueva recepción, o una orden de entrada si su almacén de recepción funciona con órdenes: la mercancía entra en stock de inmediato y el gestor registra la recepción después. En las demás pestañas, un nuevo pedido a proveedor. Antes el botón daba un error.

## 2.0.16.100
### ru
- Рабочее место производства: на закладках с документами — заказы поставщику, поступления, передача в переработку, поступления из переработки, отгрузки — появилась кнопка «Печать». Встаньте на строку документа и нажмите её: печатается весь документ этой строки, со всеми его строками.
- В «Печати» те же печатные формы, что и в самом документе. Если форм несколько, кнопка открывает список для выбора; формы, на которые у пользователя нет прав, в списке не показываются.
- На ордерном складе строка поступления или отгрузки может быть приходным или расходным ордером — тогда «Печать» предлагает формы ордера.

### fr
- Poste de travail de production : les onglets de documents — commandes fournisseur, réceptions, transfert en sous-traitance, réceptions de sous-traitance, expéditions — ont un bouton « Impression ». Placez-vous sur la ligne d'un document et cliquez : tout le document de cette ligne est imprimé, avec toutes ses lignes.
- « Impression » propose les mêmes formulaires que le document lui-même. S'il y en a plusieurs, le bouton ouvre une liste au choix ; les formulaires pour lesquels l'utilisateur n'a pas de droits n'y figurent pas.
- Sur un entrepôt à bons, la ligne de réception ou d'expédition peut être un bon d'entrée ou de sortie : « Impression » propose alors les formulaires du bon.

### en
- Production workplace: the document tabs — supplier orders, receipts, transfer for processing, receipts from processing, shipments — now have a "Print" button. Select a document line and click it: the whole document of that line is printed, with all its lines.
- "Print" offers the same print forms as the document itself. If there are several, the button opens a list to choose from; forms the user has no rights to are not shown.
- On a warehouse with warehouse orders, a receipt or shipment line can be a receiving or issuing order — "Print" then offers the order's forms.

### es
- Puesto de trabajo de producción: las pestañas de documentos — pedidos a proveedor, recepciones, transferencia a procesamiento, recepciones de procesamiento, expediciones — tienen un botón «Impresión». Sitúese en la línea de un documento y púlselo: se imprime todo el documento de esa línea, con todas sus líneas.
- «Impresión» ofrece los mismos formularios que el propio documento. Si hay varios, el botón abre una lista para elegir; los formularios sobre los que el usuario no tiene derechos no aparecen.
- En un almacén con órdenes, la línea de recepción o expedición puede ser una orden de entrada o de salida: «Impresión» ofrece entonces los formularios de la orden.

## 2.0.16.99
### ru
- Рабочее место закупок, закладка «Потребность»: новая кнопка «Создать поступление». Отметьте строки и нажмите кнопку: по каждому заказу на производство проводится поступление от поставщика строки на недостающее количество, без заказа поставщику и без номера накладной (на ордерном складе — приходный ордер). Затем открывается закладка «Поступления».
- «Создать поступление» принимает только недостающее заказам на производство. Пополнение склада до минимального остатка оформляется, как раньше, кнопкой «Заказать» или новым поступлением на закладке «Поступления». Если под заказ уже есть неоформленный черновик поступления, программа предложит сначала провести или удалить его.
- Поступление под заказ на производство без заказа поставщику теперь уменьшает недостачу и тогда, когда по тому же материалу открыт заказ поставщику: материал больше не заказывается и не принимается второй раз.
- Такое поступление распределяется на изделия, которым материала не хватает, с учётом уже взятого со склада и заказанного.
- Возврат поставщику по такому поступлению возвращает недостачу заказу. Стадия заказа на производство учитывает поступления без заказа поставщику.
- При обновлении программа размечает ранее проведённые поступления без заказа поставщику, чтобы недостача по заказам в работе стала верной.

### fr
- Poste de travail des achats, onglet « Besoin » : nouveau bouton « Créer une réception ». Cochez les lignes et cliquez : pour chaque commande de production, une réception du fournisseur de la ligne est validée pour la quantité manquante, sans commande fournisseur ni numéro de facture (bon d'entrée sur un entrepôt à bons). L'onglet « Réceptions » s'ouvre ensuite.
- « Créer une réception » ne réceptionne que le manque des commandes de production. Le réapprovisionnement au stock minimum se fait comme avant avec « Commander » ou par une nouvelle réception dans l'onglet « Réceptions ». S'il existe déjà un brouillon de réception pour la commande, le programme propose de le valider ou de le supprimer d'abord.
- Une réception pour une commande de production sans commande fournisseur réduit désormais le manque même si une commande fournisseur est ouverte pour la même matière : la matière n'est plus commandée ni réceptionnée une seconde fois.
- Cette réception est répartie sur les produits qui manquent de matière, en tenant compte de ce qui a déjà été pris en stock et commandé.
- Un retour fournisseur de cette réception rend le manque à la commande. L'étape de la commande de production tient compte des réceptions sans commande fournisseur.
- Lors de la mise à jour, le programme marque les réceptions sans commande fournisseur déjà validées afin que le manque des commandes en cours soit correct.

### en
- Purchasing workplace, "Need" tab: new "Create receipt" button. Tick the lines and click it: for each production order a receipt from the line's supplier is posted for the missing quantity, without a supplier order and without an invoice number (a receiving order on a warehouse with receiving orders). The "Receipts" tab opens afterwards.
- "Create receipt" only receives what production orders are missing. Replenishment to the minimum stock is done as before with "Order" or with a new receipt on the "Receipts" tab. If there is already a draft receipt for the order, the program asks to post or delete it first.
- A receipt for a production order without a supplier order now reduces the shortage even when a supplier order is open for the same material: the material is no longer ordered or received a second time.
- Such a receipt is allocated to the products that lack the material, taking into account what was already taken from stock and ordered.
- A supplier return of such a receipt gives the shortage back to the order. The production order stage takes receipts without a supplier order into account.
- During the update, the program marks already posted receipts without a supplier order so that the shortage of orders in progress is correct.

### es
- Puesto de trabajo de compras, pestaña «Necesidad»: nuevo botón «Crear recepción». Marque las líneas y púlselo: para cada pedido de producción se contabiliza una recepción del proveedor de la línea por la cantidad que falta, sin pedido a proveedor ni número de factura (una orden de entrada en un almacén con órdenes). Después se abre la pestaña «Recepciones».
- «Crear recepción» solo recibe lo que falta a los pedidos de producción. La reposición al stock mínimo se hace como antes con «Pedir» o con una recepción nueva en la pestaña «Recepciones». Si ya hay un borrador de recepción para el pedido, el programa pide contabilizarlo o eliminarlo primero.
- Una recepción para un pedido de producción sin pedido a proveedor ahora reduce el faltante aunque haya un pedido a proveedor abierto del mismo material: el material ya no se pide ni se recibe por segunda vez.
- Esa recepción se reparte entre los productos a los que les falta el material, teniendo en cuenta lo ya tomado del almacén y lo pedido.
- Una devolución al proveedor de esa recepción devuelve el faltante al pedido. La etapa del pedido de producción tiene en cuenta las recepciones sin pedido a proveedor.
- Durante la actualización, el programa marca las recepciones sin pedido a proveedor ya contabilizadas para que el faltante de los pedidos en curso sea correcto.

## 2.0.16.98
### ru
- Рабочее место закупок: закладка «К поступлению» заменена закладкой «Поступления» — список поступлений товаров и приходных ордеров с отборами панели и постраничным просмотром. Двойной щелчок открывает документ, щелчок по колонке «Заказ поставщику» — заказ.
- На закладке «Поступления» кнопка «Создать» открывает новое поступление — без заказа поставщику и без потребности.
- На закладке «Заказы поставщикам» появились флажки и кнопка «Создать поступление»: отметьте заказы (или выделите строки) и нажмите кнопку. По каждому заказу проводится поступление на всё, что ещё не пришло, а на ордерном складе — приходный ордер. Номер накладной поставщика вводится потом в самом документе. После этого открывается закладка «Поступления».
- Если по заказу уже всё пришло, он не проведён или предварительный, поступление не создаётся, и программа сообщает причину. Повторное нажатие не принимает товар второй раз.

### fr
- Poste de travail des achats : l'onglet « À réceptionner » est remplacé par l'onglet « Réceptions » — la liste des réceptions de marchandises et des bons d'entrée, avec les filtres du panneau et un affichage par pages. Un double-clic ouvre le document, un clic sur la colonne « Commande fournisseur » ouvre la commande.
- Dans l'onglet « Réceptions », le bouton « Créer » ouvre une nouvelle réception, sans commande fournisseur ni besoin.
- L'onglet « Commandes fournisseurs » a des cases à cocher et un bouton « Créer une réception » : cochez les commandes (ou sélectionnez les lignes) et cliquez. Pour chaque commande, une réception est validée pour tout ce qui n'est pas encore arrivé, et un bon d'entrée sur un entrepôt à bons. Le numéro de facture du fournisseur se saisit ensuite dans le document. L'onglet « Réceptions » s'ouvre ensuite.
- Si tout est déjà reçu pour une commande, ou si elle n'est pas validée ou est préliminaire, aucune réception n'est créée et le programme en indique la raison. Un nouveau clic ne réceptionne pas la marchandise une seconde fois.

### en
- Purchasing workplace: the "To receive" tab is replaced by the "Receipts" tab — a list of goods receipts and receiving orders with the panel filters and page-by-page view. Double-click opens the document; a click on the "Supplier order" column opens the order.
- On the "Receipts" tab, the "Create" button opens a new receipt — with no supplier order and no need.
- The "Supplier orders" tab has check boxes and a "Create receipt" button: tick the orders (or select the rows) and click it. For each order a receipt is posted for everything not yet received, or a receiving order on a warehouse with receiving orders. The supplier invoice number is entered later in the document itself. The "Receipts" tab opens afterwards.
- If everything has already been received for an order, or it is not posted or is preliminary, no receipt is created and the program tells why. Clicking again does not receive the goods a second time.

### es
- Puesto de trabajo de compras: la pestaña «Por recibir» se sustituye por la pestaña «Recepciones» — la lista de recepciones de mercancías y órdenes de entrada, con los filtros del panel y vista por páginas. Un doble clic abre el documento; un clic en la columna «Pedido a proveedor» abre el pedido.
- En la pestaña «Recepciones», el botón «Crear» abre una recepción nueva, sin pedido a proveedor ni necesidad.
- La pestaña «Pedidos a proveedores» tiene casillas y un botón «Crear recepción»: marque los pedidos (o seleccione las filas) y púlselo. Para cada pedido se contabiliza una recepción de todo lo que aún no ha llegado, o una orden de entrada en un almacén con órdenes. El número de factura del proveedor se introduce después en el propio documento. Después se abre la pestaña «Recepciones».
- Si ya se recibió todo de un pedido, o no está contabilizado o es preliminar, no se crea la recepción y el programa indica el motivo. Pulsar de nuevo no recibe la mercancía por segunda vez.

## 2.0.16.97
### ru
- Налоговый документ на основании неналоговых (при раздельном учёте): в реализации и поступлении — страница «Основания» и кнопка «Подобрать основания». Отметьте неналоговые документы того же клиента или поставщика — строки товаров заполнятся по ним, цену строки можно поправить. Документ покрывает выбранные документы целиком.
- Такой документ не отгружает и не принимает товар второй раз: фактические остатки, продажи и долги не меняются, а покрытые товары, продажи и долг переходят в налоговый учёт по ценам налогового документа. Оплаты покрытых документов, в том числе введённые позже, переносятся на налоговый документ.
- Покрытый документ нельзя распровести, удалить, пометить и изменить, пока проведён налоговый документ. Возврат покупателя оформляется по налоговой реализации и тоже налоговый; по покрытой реализации возврат не проводится. Возврат поставщику по налоговому поступлению пока недоступен — оформляйте его до налогового документа.

### fr
- Document fiscal établi sur des documents non fiscaux (en comptabilité séparée) : la vente et la réception ont une page « Documents de base » et un bouton « Sélectionner les documents de base ». Cochez les documents non fiscaux du même client ou fournisseur — les lignes d'articles se remplissent, le prix d'une ligne peut être corrigé. Le document couvre entièrement les documents choisis.
- Ce document ne livre ni ne reçoit la marchandise une seconde fois : les stocks, ventes et dettes réels ne changent pas, les articles, ventes et dettes couverts passent en comptabilité fiscale aux prix du document fiscal. Les paiements des documents couverts, y compris ultérieurs, sont reportés sur le document fiscal.
- Un document couvert ne peut pas être dévalidé, supprimé, marqué ni modifié tant que le document fiscal est validé. Le retour client se fait sur la vente fiscale et il est fiscal ; un retour sur la vente couverte n'est pas validé. Le retour fournisseur sur une réception fiscale n'est pas encore disponible : faites-le avant le document fiscal.

### en
- Tax document based on non-tax documents (with separate accounting): sales and receipts have a "Bases" page and a "Select bases" button. Tick non-tax documents of the same customer or supplier — goods lines are filled from them, and a line price can be corrected. The document covers the selected documents in full.
- Such a document does not ship or receive goods a second time: actual stock, sales and debts stay the same, while the covered goods, sales and debt move to tax accounting at the tax document prices. Payments of covered documents, including later ones, are carried to the tax document.
- A covered document cannot be unposted, deleted, marked or changed while the tax document is posted. Customer returns are made on the tax sale and are tax returns; a return on the covered sale is not posted. A return to supplier on a tax receipt is not available yet: make it before the tax document.

### es
- Documento fiscal sobre documentos no fiscales (con contabilidad separada): la venta y la recepción tienen la página «Bases» y el botón «Seleccionar bases». Marque los documentos no fiscales del mismo cliente o proveedor: las líneas de mercancías se rellenan y el precio de una línea se puede corregir. El documento cubre por completo los documentos elegidos.
- Este documento no envía ni recibe la mercancía por segunda vez: las existencias, ventas y deudas reales no cambian, y las mercancías, ventas y deuda cubiertas pasan a la contabilidad fiscal a los precios del documento fiscal. Los pagos de los documentos cubiertos, también los posteriores, se trasladan al documento fiscal.
- Un documento cubierto no se puede anular, eliminar, marcar ni modificar mientras el documento fiscal esté contabilizado. La devolución del cliente se hace sobre la venta fiscal y es fiscal; una devolución sobre la venta cubierta no se contabiliza. La devolución al proveedor sobre una recepción fiscal aún no está disponible: hágala antes del documento fiscal.

## 2.0.16.96
### ru
- Раздельный управленческий и налоговый учёт (Настройки → Бухгалтерия, по умолчанию выключен). Когда он включён, у реализации, поступления, возвратов, приходного и расходного кассового ордера, списания и чека в рабочем месте кассира появляется флажок «Налоговый». Документ без флажка проводится только по управленческому учёту.
- Остатки товаров, долги клиентов и поставщикам, продажи и касса хранят, налоговое движение или нет: полная картина остаётся прежней, а налоговая теперь видна отдельно. Банк всегда налоговый, касса — по документу.
- Новые документы налоговые по умолчанию; это можно изменить настройкой пользователя «Налоговый по умолчанию». В рабочем месте кассира флажок задаётся для каждого чека, оплата чека попадает в кассу с тем же признаком.
- Раздельный учёт нельзя выключить, если в базе уже есть документы только управленческого учёта.

### fr
- Comptabilité de gestion et fiscale séparées (Paramètres → Comptabilité, désactivée par défaut). Une fois activée, la vente, la réception, les retours, les bons d'encaissement et de décaissement, la sortie de stock et le ticket du poste de caisse reçoivent une case « Fiscal ». Un document sans cette case n'est comptabilisé qu'en gestion.
- Les stocks, les dettes clients et fournisseurs, les ventes et la caisse indiquent si le mouvement est fiscal ou non : la vue complète reste la même, la vue fiscale est désormais visible à part. La banque est toujours fiscale, la caisse suit le document.
- Les nouveaux documents sont fiscaux par défaut ; le réglage utilisateur « Documents fiscaux par défaut » permet de le changer. Au poste de caisse, la case se règle pour chaque ticket et le paiement du ticket entre en caisse avec le même indicateur.
- La comptabilité séparée ne peut pas être désactivée si la base contient déjà des documents de gestion uniquement.

### en
- Separate management and tax accounting (Settings → Accounting, off by default). When it is on, sales, receipts, returns, cash receipt and payment orders, write-offs and the cashier workplace ticket get a "Tax" box. A document without it is posted to management accounting only.
- Stock, customer and supplier debts, sales and cash record whether a movement is tax or not: the full picture stays the same, and the tax picture can now be seen separately. Bank is always tax, cash follows the document.
- New documents are tax by default; the "Tax documents by default" user setting changes this. In the cashier workplace the box is set for each ticket, and the ticket payment goes to cash with the same flag.
- Separate accounting cannot be turned off once the database has management-only documents.

### es
- Contabilidad de gestión y fiscal separadas (Configuración → Contabilidad, desactivada por defecto). Al activarla, la venta, la recepción, las devoluciones, las órdenes de cobro y de pago en caja, la baja de existencias y el ticket del puesto de cajero reciben la casilla «Fiscal». Un documento sin ella solo se contabiliza en gestión.
- Las existencias, las deudas de clientes y proveedores, las ventas y la caja registran si el movimiento es fiscal o no: la vista completa no cambia y la vista fiscal se ve ahora por separado. El banco siempre es fiscal; la caja sigue al documento.
- Los documentos nuevos son fiscales por defecto; el ajuste de usuario «Documentos fiscales por defecto» lo cambia. En el puesto de cajero la casilla se fija para cada ticket y el pago del ticket entra en caja con el mismo indicador.
- La contabilidad separada no se puede desactivar si la base ya tiene documentos solo de gestión.

## 2.0.16.95
### ru
- Рабочее место кассы больше не «теряется»: программа узнаёт компьютер и не создаёт новое рабочее место с пустым списком оборудования. Если компьютер незнаком, открывается выбор рабочего места — сначала места с тем же именем компьютера и их оборудование; создать новое можно, только если своего места в списке нет.
- Рабочее место кассира: если компьютер ещё не связан с рабочим местом, выбор открывается сразу, а после выбора сканер подключается без переоткрытия окна. Кнопка «Рабочее место» в нижней панели — сменить рабочее место в любой момент.
- В документах со сканером при неизвестном компьютере — одно напоминание «Оборудование не подключено» со ссылкой на выбор рабочего места; после выбора сканер подключается во всех открытых окнах.
- Карточка рабочего места: список компьютеров этого места, «Перенести на другое рабочее место» и «Перенести оборудование с другого рабочего места» (для администратора).
- Список рабочих мест: «Объединить с...» — дубли, накопленные раньше, объединяются в одно место; совпадающие устройства подсвечены, лишние можно снять.
- При обновлении компьютеры существующих рабочих мест переносятся автоматически; одинаковые рабочие места не сливаются сами — их объединяет администратор.

### fr
- Le poste de travail de la caisse ne « se perd » plus : le programme reconnaît l'ordinateur et ne crée plus de nouveau poste avec une liste de matériel vide. Si l'ordinateur est inconnu, le choix du poste de travail s'ouvre — d'abord les postes portant le même nom d'ordinateur, avec leur matériel ; un nouveau poste ne se crée que si le vôtre n'est pas dans la liste.
- Poste du caissier : si l'ordinateur n'est encore lié à aucun poste, le choix s'ouvre aussitôt, et après le choix le scanner se connecte sans rouvrir la fenêtre. Le bouton « Poste de travail » du panneau inférieur permet de changer de poste à tout moment.
- Dans les documents avec scanner, sur un ordinateur inconnu : un seul rappel « Matériel non connecté » avec un lien vers le choix du poste ; après le choix, le scanner se connecte dans toutes les fenêtres ouvertes.
- Fiche du poste de travail : la liste des ordinateurs de ce poste, « Transférer vers un autre poste » et « Transférer le matériel d'un autre poste » (pour l'administrateur).
- Liste des postes de travail : « Fusionner avec... » — les doublons accumulés auparavant sont réunis en un seul poste ; les appareils identiques sont signalés, ceux en trop peuvent être décochés.
- Lors de la mise à jour, les ordinateurs des postes existants sont repris automatiquement ; les postes identiques ne sont pas fusionnés d'eux-mêmes — l'administrateur les fusionne.

### en
- The till workplace is no longer "lost": the program recognises the computer and no longer creates a new workplace with an empty equipment list. If the computer is unknown, workplace selection opens — workplaces with the same computer name and their equipment come first; a new one can be created only if yours is not in the list.
- Cashier workplace: if the computer is not yet linked to a workplace, the selection opens right away, and after choosing the scanner connects without reopening the window. The "Workplace" button in the bottom panel changes the workplace at any time.
- In documents with a scanner on an unknown computer: a single "Equipment not connected" reminder with a link to workplace selection; after choosing, the scanner connects in all open windows.
- Workplace card: the list of computers of this workplace, "Move to another workplace" and "Move equipment from another workplace" (for the administrator).
- Workplace list: "Merge with..." — duplicates accumulated earlier are merged into one workplace; identical devices are highlighted, extra ones can be cleared.
- On update, the computers of existing workplaces are carried over automatically; identical workplaces are not merged by themselves — the administrator merges them.

### es
- El lugar de trabajo de la caja ya no «se pierde»: el programa reconoce el equipo y ya no crea un nuevo lugar de trabajo con la lista de equipos vacía. Si el equipo es desconocido, se abre la elección del lugar de trabajo: primero los lugares con el mismo nombre de equipo y sus dispositivos; crear uno nuevo solo si el suyo no está en la lista.
- Puesto de cajero: si el equipo aún no está vinculado a un lugar de trabajo, la elección se abre de inmediato y, tras elegir, el escáner se conecta sin volver a abrir la ventana. El botón «Lugar de trabajo» del panel inferior cambia el lugar en cualquier momento.
- En los documentos con escáner en un equipo desconocido: un solo aviso «Equipo no conectado» con un enlace a la elección del lugar de trabajo; tras elegir, el escáner se conecta en todas las ventanas abiertas.
- Ficha del lugar de trabajo: la lista de equipos de este lugar, «Trasladar a otro lugar de trabajo» y «Trasladar equipo de otro lugar de trabajo» (para el administrador).
- Lista de lugares de trabajo: «Fusionar con...» — los duplicados acumulados antes se unen en un solo lugar; los dispositivos idénticos se resaltan y los sobrantes pueden desmarcarse.
- Al actualizar, los equipos de los lugares existentes se trasladan automáticamente; los lugares idénticos no se fusionan solos: los fusiona el administrador.

## 2.0.16.94
### ru
- Рабочее место производства: Tab с последней колонки переводит в первую колонку следующей строки, а не на флажок выделения строки.
- Индикатор выполнения заказа: кружок «частично» больше не мельче остальных — все пять кружков одного размера в рабочих местах производства и закупок, в списке заказов и в заказе.
- Поиск товара при вводе в поле: найденный текст в выпадающем списке выделяется фирменным янтарным цветом вместо зелёного, который сливался с фоном. Товары без остатка показываются приглушённо на всех языках интерфейса, а не только на русском.

### fr
- Poste de production : Tab depuis la dernière colonne mène à la première colonne de la ligne suivante, et non plus à la case de sélection de la ligne.
- Indicateur d'avancement de la commande : le cercle « partiel » n'est plus plus petit que les autres — les cinq cercles ont la même taille dans les postes de production et d'achats, dans la liste des commandes et dans la commande.
- Recherche d'un article à la saisie : le texte trouvé dans la liste déroulante est mis en évidence en ambre, la couleur de la marque, au lieu du vert qui se confondait avec le fond. Les articles hors stock sont affichés atténués dans toutes les langues de l'interface, et plus seulement en russe.

### en
- Production workplace: Tab from the last column moves to the first column of the next line instead of the line selection checkbox.
- Order progress indicator: the «partial» circle is no longer smaller than the others — all five circles have the same size in the production and purchasing workplaces, in the order list and in the order.
- Product search while typing in a field: the found text in the drop-down list is highlighted in the brand amber instead of green, which blended with the background. Out-of-stock products are shown dimmed in every interface language, not only in Russian.

### es
- Puesto de producción: Tab desde la última columna lleva a la primera columna de la línea siguiente y no a la casilla de selección de la línea.
- Indicador de avance del pedido: el círculo «parcial» ya no es más pequeño que los demás — los cinco círculos tienen el mismo tamaño en los puestos de producción y de compras, en la lista de pedidos y en el pedido.
- Búsqueda de un artículo al escribir en un campo: el texto encontrado en la lista desplegable se resalta en ámbar, el color de la marca, en lugar del verde que se confundía con el fondo. Los artículos sin existencias se muestran atenuados en todos los idiomas de la interfaz, no solo en ruso.

## 2.0.16.93
### ru
- Рабочее место производства помещается в окно без общей прокрутки: таблицы заказов, производства и нижних закладок растягиваются по свободной высоте, а не задают её, панель фильтров всегда стоит справа и не уходит под таблицы на узком экране.
- Сообщения рабочего места (ошибки записи и проведения, подсказки) больше не появляются внизу формы и не сдвигают таблицы: они собираются на новой закладке «Сообщения» панели справа, новые — сверху, с временем. В свёрнутой панели значок сообщений показывает число непрочитанных; кнопка «Очистить» очищает список.
- Подписи фильтров в панели — слева от поля.
- Переход между закладками «Заказы» и «Производство» обновляет нижние закладки по текущей строке открытой закладки. Раньше они оставались от строки прежней закладки.

### fr
- Le poste de production tient dans la fenêtre sans défilement général : les tableaux des commandes, de la production et des onglets du bas s'étirent sur la hauteur libre au lieu de l'imposer ; le panneau des filtres reste toujours à droite et ne passe plus sous les tableaux sur un écran étroit.
- Les messages du poste (erreurs d'enregistrement et de validation, indications) n'apparaissent plus en bas du formulaire et ne décalent plus les tableaux : ils sont regroupés dans le nouvel onglet « Messages » du panneau de droite, les plus récents en haut, avec l'heure. Panneau replié, l'icône des messages affiche le nombre de messages non lus ; le bouton « Effacer » vide la liste.
- Les libellés des filtres du panneau sont à gauche du champ.
- Le passage entre les onglets « Commandes » et « Production » met à jour les onglets du bas selon la ligne courante de l'onglet ouvert. Auparavant, ils restaient sur la ligne de l'onglet précédent.

### en
- The production workplace fits the window without a form-wide scroll: the orders, production and bottom-tab tables stretch over the free height instead of setting it; the filter panel always stays on the right and no longer drops under the tables on a narrow screen.
- Workplace messages (saving and posting errors, hints) no longer appear at the bottom of the form or shift the tables: they are collected in the new «Messages» tab of the right panel, newest first, with the time. With the panel collapsed, the messages icon shows the number of unread messages; the «Clear» button empties the list.
- Filter labels in the panel are to the left of the field.
- Switching between the «Orders» and «Production» tabs refreshes the bottom tabs for the current line of the open tab. Previously they kept the line of the previous tab.

### es
- El puesto de producción cabe en la ventana sin desplazamiento general: las tablas de pedidos, de producción y de las pestañas inferiores se estiran por la altura libre en lugar de imponerla; el panel de filtros queda siempre a la derecha y ya no pasa debajo de las tablas en una pantalla estrecha.
- Los mensajes del puesto (errores de guardado y contabilización, avisos) ya no aparecen al pie del formulario ni desplazan las tablas: se reúnen en la nueva pestaña «Mensajes» del panel derecho, los más recientes arriba, con la hora. Con el panel plegado, el icono de mensajes muestra el número de no leídos; el botón «Borrar» vacía la lista.
- Las etiquetas de los filtros del panel están a la izquierda del campo.
- El paso entre las pestañas «Pedidos» y «Producción» actualiza las pestañas inferiores según la línea actual de la pestaña abierta. Antes conservaban la línea de la pestaña anterior.

## 2.0.16.92
### ru
- Рабочее место производства: закладка «Отгрузки» перенесена в конец, перед «Документами» — после переработки.

### fr
- Poste de production : l'onglet « Expéditions » est déplacé à la fin, avant « Documents » — après la sous-traitance.

### en
- Production workplace: the «Shipments» tab is moved to the end, before «Documents» — after subcontracting.

### es
- Puesto de producción: la pestaña «Envíos» se traslada al final, antes de «Documentos» — después de la subcontratación.

## 2.0.16.91
### ru
- Рабочее место производства, закладка «Производство»: склад новой строки выпуска заполняется из настроек пользователя и выбирается вручную, пока строка не записана. Раньше колонка «Склад» не редактировалась, и без склада по умолчанию выпуск не записывался («Списать с» не заполнено).
- Карточка пользователя: новая закладка «Склады» — склад по умолчанию, склад поступлений и склад отгрузок.
- Новые поступления товаров, поступления из переработки, приходные ордера и возвраты от покупателей берут склад поступлений пользователя; реализации, расходные ордера и возвраты поставщикам — склад отгрузок. Если свой склад не задан — склад по умолчанию пользователя, затем основной склад.

### fr
- Poste de production, onglet « Production » : l'entrepôt d'une nouvelle ligne de production est rempli depuis les paramètres de l'utilisateur et se choisit à la main tant que la ligne n'est pas enregistrée. Auparavant, la colonne « Entrepôt » n'était pas modifiable et, sans entrepôt par défaut, la production ne s'enregistrait pas (« Radier de » non rempli).
- Fiche utilisateur : nouvel onglet « Entrepôts » — entrepôt par défaut, entrepôt des réceptions et entrepôt des expéditions.
- Les nouvelles réceptions de marchandises, réceptions de sous-traitance, bons d'entrée et retours clients prennent l'entrepôt des réceptions de l'utilisateur ; les ventes, bons de sortie et retours fournisseurs — l'entrepôt des expéditions. S'il n'est pas défini, l'entrepôt par défaut de l'utilisateur, puis l'entrepôt principal.

### en
- Production workplace, «Production» tab: the warehouse of a new output line is filled from the user settings and can be chosen manually until the line is saved. Previously the «Warehouse» column was not editable and, without a default warehouse, the output could not be saved («Write off from» not filled).
- User card: new «Warehouses» tab — default warehouse, receipts warehouse and shipments warehouse.
- New goods receipts, subcontracting receipts, receipt orders and customer returns take the user's receipts warehouse; sales, issue orders and supplier returns take the shipments warehouse. If it is not set — the user's default warehouse, then the main warehouse.

### es
- Puesto de producción, pestaña «Producción»: el almacén de una nueva línea de producción se rellena desde la configuración del usuario y se elige a mano mientras la línea no esté guardada. Antes la columna «Almacén» no era editable y, sin almacén predeterminado, la producción no se guardaba («Dar de baja de» sin rellenar).
- Ficha de usuario: nueva pestaña «Almacenes» — almacén predeterminado, almacén de recepciones y almacén de expediciones.
- Las nuevas recepciones de mercancías, recepciones de subcontratación, órdenes de entrada y devoluciones de clientes toman el almacén de recepciones del usuario; las ventas, órdenes de salida y devoluciones a proveedores, el almacén de expediciones. Si no está definido, el almacén predeterminado del usuario y luego el almacén principal.

## 2.0.16.90
### ru
- Колонки со своим списком выбора (продукция, материалы, ПФ/ГП, выпуск и отгрузка рабочего места производства, товар поступления в рабочем месте закупок, продукция и материалы заказа на производство) больше не показывают сначала пустой тёмный список с «Показать все»: кнопка выбора в самом поле сразу открывает предзаполненный список.
- Во всех полях выбора справочников и документов включена история выбора: выпадающий список показывает последние выбранные значения, а не пусто.
- Колонка товара в документах при входе показывает последние выбранные товары, а пока их нет — последние созданные с остатком и ценой.

### fr
- Les colonnes qui ont leur propre liste de choix (produit, matières, semi-fini/produit fini, production et expédition du poste de production, article de réception du poste d'achats, produit et matières de la commande de production) n'affichent plus d'abord une liste sombre vide avec « Afficher tout » : le bouton de sélection dans le champ ouvre directement la liste préremplie.
- L'historique de sélection est activé dans tous les champs de choix de référentiels et de documents : la liste déroulante affiche les dernières valeurs choisies au lieu d'être vide.
- La colonne article des documents affiche à l'entrée les derniers articles choisis et, tant qu'il n'y en a pas, les derniers créés avec le stock et le prix.

### en
- Columns with their own choice list (product, materials, semi-finished/finished goods, output and shipment in the production workplace, receipt item in the purchasing workplace, product and materials of a production order) no longer first show an empty dark list with «Show all»: the choice button in the field opens the prefilled list at once.
- Choice history is enabled in all catalog and document choice fields: the drop-down list shows the last selected values instead of being empty.
- The item column in documents shows the last selected items on entry and, until there are any, the most recently created ones with stock and price.

### es
- Las columnas con su propia lista de selección (producto, materiales, semielaborado/producto terminado, producción y expedición del puesto de producción, artículo de recepción del puesto de compras, producto y materiales del pedido de producción) ya no muestran primero una lista oscura vacía con «Mostrar todo»: el botón de selección del campo abre directamente la lista precargada.
- El historial de selección está activado en todos los campos de selección de catálogos y documentos: la lista desplegable muestra los últimos valores elegidos en lugar de quedar vacía.
- La columna de artículo de los documentos muestra al entrar los últimos artículos elegidos y, mientras no los haya, los últimos creados con existencias y precio.

## 2.0.16.89
### ru
- Рабочее место производства, закладка «Продукция»: записанная строка остаётся там, где её ввели, — новая строка после записи остаётся вверху списка, а не уходит к остальным строкам своего заказа.

### fr
- Poste de production, onglet « Produit » : la ligne enregistrée reste là où elle a été saisie — après l'enregistrement, la nouvelle ligne reste en haut de la liste au lieu de rejoindre les autres lignes de sa commande.

### en
- Production workplace, «Product» tab: a saved line stays where it was entered — after saving, a new line stays at the top of the list instead of moving to the other lines of its order.

### es
- Puesto de producción, pestaña «Producto»: la línea guardada se queda donde se introdujo — tras guardarla, la línea nueva permanece arriba de la lista en lugar de irse con las demás líneas de su pedido.

## 2.0.16.88
### ru
- Карточка станка открывается без вертикальной прокрутки: поля — на закладке «Основное» с подписью слева, по строкам одной темы (выработка, время на смену заказа и стоимость часа; склад станка и оператор; признаки). Таблицы «Выработка по номенклатуре» и «Режим работы» — на своих закладках, с числом строк в заголовке.

### fr
- La fiche de la machine s'ouvre sans défilement vertical : les champs sont sur l'onglet « Principal » avec le libellé à gauche, regroupés par ligne de même thème (rendement, temps de changement de commande et coût horaire ; entrepôt de la machine et opérateur ; indicateurs). Les tableaux « Cadence par article » et « Horaires de travail » ont chacun leur onglet, avec le nombre de lignes dans le titre.

### en
- The machine card opens without vertical scrolling: fields are on the «Main» tab with the label on the left, in rows of the same topic (output rate, order changeover time and hourly cost; machine warehouse and operator; flags). The «Output rate by item» and «Working schedule» tables each have their own tab, with the row count in the title.

### es
- La ficha de la máquina se abre sin desplazamiento vertical: los campos están en la pestaña «Principal» con la etiqueta a la izquierda, en filas del mismo tema (rendimiento, tiempo de cambio de pedido y coste por hora; almacén de la máquina y operador; indicadores). Las tablas «Rendimiento por artículo» y «Horario de trabajo» tienen cada una su pestaña, con el número de filas en el título.

## 2.0.16.87
### ru
- Рабочее место «Управление станками» перекомпоновано по высоте: таблица станков и таблицы на закладках внизу больше не растягиваются, всё свободное место окна отдано графику загрузки — строки станков видны без вертикальной прокрутки графика.

### fr
- Le poste « Gestion des machines » est réorganisé en hauteur : le tableau des machines et les tableaux des onglets du bas ne s'étirent plus, toute la place libre de la fenêtre revient au planning de charge — les lignes des machines sont visibles sans défilement vertical du planning.

### en
- The «Machine management» workplace is rearranged vertically: the machine table and the tables on the bottom tabs no longer stretch, all free window space goes to the load chart — machine rows are visible without scrolling the chart vertically.

### es
- El puesto «Gestión de máquinas» se reorganiza en altura: la tabla de máquinas y las tablas de las pestañas inferiores ya no se estiran, todo el espacio libre de la ventana pasa al gráfico de carga: las filas de las máquinas se ven sin desplazamiento vertical del gráfico.

## 2.0.16.86
### ru
- «Заполнить демо-данными» в базе без валюты регламентированного учёта больше не обрывается ошибкой «Не указан курс валюты EUR» на реализациях и оплатах: кнопка сразу просит указать валюту в «Компания и учёт» и записать настройки. Касса и банк демо-набора, заведённые раньше в другой валюте и ещё без документов, при следующем заполнении переводятся в валюту учёта.

### fr
- « Remplir avec des données de démonstration » dans une base sans devise de comptabilité réglementée ne s'interrompt plus sur l'erreur « Le taux de change de EUR n'est pas indiqué » aux ventes et paiements : le bouton demande d'abord d'indiquer la devise dans « Entreprise et comptabilité » et d'enregistrer les paramètres. La caisse et la banque du jeu de démo créées auparavant dans une autre devise et encore sans documents passent dans la devise de comptabilité au remplissage suivant.

### en
- «Fill with demo data» in an infobase without a regulated accounting currency no longer stops with «The EUR exchange rate is not specified» on sales and payments: the button first asks to specify the currency in «Company and accounting» and save the settings. The demo cash desk and bank created earlier in another currency and still without documents switch to the accounting currency on the next fill.

### es
- «Llenar con datos de demostración» en una base sin moneda contable regulada ya no se interrumpe con «No se indica el tipo de cambio de EUR» en ventas y pagos: el botón pide primero indicar la moneda en «Empresa y contabilidad» y guardar los ajustes. La caja y el banco del conjunto demo creados antes en otra moneda y aún sin documentos pasan a la moneda contable en el siguiente llenado.

## 2.0.16.85
### ru
- В мастере первого запуска на шаге выбора возможностей появились флажки, которые раньше были только в «Параметрах»: «Учёт станков» и «Автоматическое создание выпусков при отгрузке» в разделе «Производство», «Выбор партии при продаже» в разделе «Продажи». Без производства учёт станков и автовыпуск не включаются — как и в «Параметрах».

### fr
- À l'étape de choix des fonctionnalités de l'assistant de premier lancement, de nouvelles cases qui n'existaient que dans « Paramètres » : « Gestion des machines » et « Création automatique des fabrications à l'expédition » dans « Production », « Sélection du lot lors de la vente » dans « Ventes ». Sans production, la gestion des machines et la fabrication automatique ne s'activent pas — comme dans « Paramètres ».

### en
- The first-run wizard's feature step now has the checkboxes that were only in «Settings»: «Machine management» and «Automatic creation of production outputs on shipment» under «Production», «Batch selection on sale» under «Sales». Without production, machine management and automatic output are not turned on — as in «Settings».

### es
- En el paso de selección de funciones del asistente de primer inicio aparecen las casillas que antes solo estaban en «Parámetros»: «Gestión de máquinas» y «Creación automática de fabricaciones en el envío» en «Producción», «Selección de lote en la venta» en «Ventas». Sin producción, la gestión de máquinas y la fabricación automática no se activan, como en «Parámetros».

## 2.0.16.84
### ru
- Кнопка «Заполнить демо-данными» («Компания и учёт») работает и в базе с рабочими документами: демо-набор добавляется рядом с ними — свои склады, товары, контрагенты, касса и банк с пометкой «Démo». Документы набора оформляются от организации базы и видны в её отчётах вместе с рабочими — об этом предупреждают вопрос перед заполнением и итог.

### fr
- Le bouton « Remplir avec des données de démonstration » (« Société et comptabilité ») fonctionne aussi dans une base contenant des documents de travail : le jeu de démo s'ajoute à côté — ses propres entrepôts, articles, tiers, caisse et banque marqués « Démo ». Les documents du jeu sont établis au nom de la société de la base et apparaissent dans ses rapports avec les documents de travail — la question avant le remplissage et le résultat le signalent.

### en
- The «Fill with demo data» button («Company and accounting») also works in an infobase with working documents: the demo set is added alongside them — its own warehouses, products, counterparties, cash and bank marked «Démo». Demo documents are issued by the infobase company and appear in its reports together with working documents — the question before filling and the result warn about it.

### es
- El botón «Llenar con datos de demostración» («Empresa y contabilidad») funciona también en una base con documentos de trabajo: el conjunto demo se añade junto a ellos — sus propios almacenes, artículos, contrapartes, caja y banco marcados «Démo». Los documentos del conjunto se emiten a nombre de la empresa de la base y se ven en sus informes junto con los de trabajo — lo advierten la pregunta antes de llenar y el resultado.

## 2.0.16.83
### ru
- Обработка «Формирование заказов поставщику» правильно считает «Заказано»: раньше у заказа, по которому уже были поступления, количество умножалось на их число, и программа предлагала дозаказать меньше нужного.
- Контроль кредита по всем клиентам (регламентная проверка запрета отгрузок) учитывает только долги по реализациям и налоговым накладным. Раньше в долг могли попасть и другие документы расчётов.
- Быстрее работают проведение документов со списанием товара, продаж и заказов поставщику, подбор товара по вводу в строке, сканирование штрихкода в рознице, выбор контрагента и договора в документах и пересчёт розничных цен.

### fr
- Le traitement « Génération des commandes fournisseurs » calcule correctement « Commandé » : auparavant, pour une commande déjà partiellement reçue, la quantité était multipliée par le nombre de réceptions et le programme proposait de commander moins que nécessaire.
- Le contrôle de crédit de tous les clients (vérification planifiée de l'interdiction de livrer) ne prend en compte que les dettes des ventes et des factures fiscales. Auparavant, d'autres documents de règlement pouvaient être comptés.
- Plus rapides : la validation des documents qui sortent du stock, des ventes et des commandes fournisseurs, la sélection d'articles à la saisie, le scan de code-barres en caisse, le choix du tiers et du contrat dans les documents et le recalcul des prix de détail.

### en
- The «Purchase order generation» processor calculates «Ordered» correctly: previously, for an order that already had receipts, the quantity was multiplied by their number and the program suggested ordering less than needed.
- Credit control for all customers (the scheduled shipment ban check) counts only debts from sales and tax invoices. Previously other settlement documents could be counted as debt.
- Faster: posting documents that write off stock, sales and purchase orders, item selection while typing, barcode scanning at the till, choosing the counterparty and contract in documents, and retail price recalculation.

### es
- El procesamiento «Generación de pedidos a proveedor» calcula bien «Pedido»: antes, en un pedido con recepciones, la cantidad se multiplicaba por su número y el programa proponía pedir menos de lo necesario.
- El control de crédito de todos los clientes (comprobación programada de la prohibición de envíos) solo tiene en cuenta las deudas de ventas y facturas fiscales. Antes podían contarse otros documentos de liquidación.
- Más rápido: la contabilización de documentos que dan de baja existencias, de ventas y de pedidos a proveedor, la selección de artículos al escribir, el escaneo de códigos de barras en caja, la elección de contraparte y contrato en los documentos y el recálculo de precios minoristas.

## 2.0.16.82
### ru
- Из формы выбора реализации убраны пустые колонки «Торговая точка», «Статус накладной» и «Вторая ходка», из журнала безналичных платежей — пустая колонка «Тип платёжного документа». Эти поля остались от прежней конфигурации и данных не показывали.
- Расширены автоматические проверки программы: проведение поступления из переработки задним числом, автовыпуск с округлённым до нуля расходом материала, обработчик стадий заказов и права ролей личного кабинета и оператора производства.

### fr
- Les colonnes vides « Point de vente », « Statut du bon » et « Deuxième tournée » sont retirées du formulaire de choix des ventes, et la colonne vide « Type de document de paiement » du journal des paiements par virement. Ces champs venaient de l'ancienne configuration et n'affichaient aucune donnée.
- Les contrôles automatiques du programme sont étendus : validation d'une réception de sous-traitance antidatée, production automatique avec une consommation de matière arrondie à zéro, traitement des étapes des commandes et droits des rôles espace client et opérateur de production.

### en
- The empty «Sales outlet», «Invoice status» and «Second trip» columns are removed from the sale choice form, and the empty «Payment document type» column from the bank payments journal. These fields came from the former configuration and showed no data.
- The program's automatic checks are extended: posting a backdated receipt from processing, automatic production with material consumption rounded to zero, the order stage handler, and the rights of the customer portal and production operator roles.

### es
- Se quitan las columnas vacías «Punto de venta», «Estado del albarán» y «Segundo viaje» del formulario de selección de ventas, y la columna vacía «Tipo de documento de pago» del diario de pagos por transferencia. Estos campos venían de la configuración anterior y no mostraban datos.
- Se amplían las comprobaciones automáticas del programa: contabilización de una recepción de transformación con fecha anterior, producción automática con consumo de material redondeado a cero, el procesamiento de etapas de pedidos y los derechos de los roles de portal de clientes y operador de producción.

## 2.0.16.81
### ru
- Оповещение о минимальном остатке приходит и тогда, когда из проведённого документа удалили строку и провели его снова: остаток товара из удалённой строки проверяется на минимум. Раньше такое перепроведение — например, приходного ордера, реализации или передачи в переработку — оповещения не давало.
- Фирменные печатные формы на выбранном в окне печати языке печатают и тексты бланка, и сумму прописью на этом языке без исключений: язык передаётся бланку напрямую.

### fr
- L'alerte de stock minimum arrive aussi quand une ligne est supprimée d'un document validé puis que le document est revalidé : le stock de l'article de la ligne supprimée est contrôlé par rapport au minimum. Auparavant, une telle revalidation — par exemple d'un bon de réception, d'une vente ou d'un envoi en sous-traitance — ne donnait pas d'alerte.
- Les formulaires à en-tête imprimés dans la langue choisie dans la fenêtre d'impression impriment toujours les textes du modèle et le montant en lettres dans cette langue : la langue est transmise directement au modèle.

### en
- The minimum stock alert now also arrives when a line is deleted from a posted document and the document is posted again: the stock of the item from the deleted line is checked against the minimum. Previously such reposting — for example of a receipt order, a sale or a transfer to processing — gave no alert.
- Branded print forms in the language chosen in the print window always print the template texts and the amount in words in that language: the language is passed to the template directly.

### es
- El aviso de existencias mínimas llega también cuando se elimina una línea de un documento contabilizado y se vuelve a contabilizar: las existencias del artículo de la línea eliminada se comprueban frente al mínimo. Antes, esa recontabilización —por ejemplo de una orden de entrada, una venta o un envío a transformación— no daba aviso.
- Los formularios corporativos impresos en el idioma elegido en la ventana de impresión imprimen siempre los textos de la plantilla y el importe en letras en ese idioma: el idioma se pasa directamente a la plantilla.

## 2.0.16.80
### ru
- Отчёт «Планирование закупок» считает правильно. Раньше проданное количество умножалось на число партий товара на складе, а остаток в итоге по товару показывался по одному складу вместо суммы по всем. Теперь «Продано» — ровно проданное за период, а «Текущий остаток» — сколько товара физически лежит на складе, включая приход по ордерам, ещё не оформленный поступлением. У проданного товара видны и склады, где он лежит без продаж за период. Отбор по месту хранения теперь работает.
- Отчёт «Товары в наличии» (и команда «Товары в наличии» в карточке товара) показывает, сколько товара физически лежит на складе, одной строкой на товар, характеристику и серию, без разбивки по партиям. Если в сохранённой настройке отчёта был отбор или колонка «Партия», этот элемент при открытии пропадёт. Остатки по партиям и стоимости — в «Ведомости по товарам на складах».
- Мобильная форма продажи работает с ордерным складом так же, как основная: в новой продаже ордерный склад не предлагается, а продажа, оформленная по расходным ордерам, показывает колонку «Ордер» и не даёт сменить склад.

### fr
- Le rapport « Planification des achats » calcule correctement. Auparavant, la quantité vendue était multipliée par le nombre de lots de l'article en entrepôt, et le total par article montrait le stock d'un seul entrepôt au lieu de la somme de tous. Désormais « Vendu » est exactement la quantité vendue sur la période, et « Stock actuel » la quantité physiquement en entrepôt, y compris l'entrée par bons pas encore régularisée par une réception. Pour un article vendu, les entrepôts où il est en stock sans vente sur la période apparaissent aussi. Le filtre par entrepôt fonctionne désormais.
- Le rapport « Marchandises en stock » (et la commande « Marchandises en stock » de la fiche article) montre la quantité physiquement en entrepôt, une ligne par article, caractéristique et série, sans détail par lot. Si un paramétrage enregistré du rapport avait un filtre ou une colonne « Lot », cet élément disparaît à l'ouverture. Les stocks par lot et en valeur sont dans le rapport « État des stocks ».
- Le formulaire mobile de vente fonctionne avec l'entrepôt à bons comme le formulaire principal : une nouvelle vente ne propose pas d'entrepôt à bons, et une vente qui régularise des bons de sortie affiche la colonne « Bon » et ne permet pas de changer d'entrepôt.

### en
- The «Purchase planning» report now calculates correctly. Previously the quantity sold was multiplied by the number of batches of the item in the warehouse, and the item total showed the stock of a single warehouse instead of the sum of all. Now «Sold» is exactly the quantity sold in the period, and «Current stock» is the quantity physically in the warehouse, including receipts by orders not yet documented by a purchase receipt. For a sold item, the warehouses holding it without sales in the period are shown too. The filter by warehouse now works.
- The «Goods in stock» report (and the «Goods in stock» command on the product card) shows the quantity physically in the warehouse, one line per product, characteristic and serial, without a breakdown by batch. If a saved report setting had a filter or column «Batch», that element is dropped on opening. Stock by batch and by value is in the «Inventory status» report.
- The mobile sale form works with an order-based warehouse like the main form: a new sale does not offer an order-based warehouse, and a sale that documents issue orders shows the «Order» column and does not allow changing the warehouse.

### es
- El informe «Planificación de compras» calcula correctamente. Antes, la cantidad vendida se multiplicaba por el número de lotes del artículo en el almacén, y el total por artículo mostraba las existencias de un solo almacén en lugar de la suma de todos. Ahora «Vendido» es exactamente lo vendido en el periodo, y «Existencias actuales» la cantidad física en el almacén, incluida la entrada por órdenes aún no formalizada con una recepción. Para un artículo vendido también se ven los almacenes donde está sin ventas en el periodo. El filtro por almacén ya funciona.
- El informe «Productos en stock» (y el comando «Productos en stock» de la ficha del artículo) muestra la cantidad física en el almacén, una línea por artículo, característica y serie, sin desglose por lote. Si una configuración guardada del informe tenía un filtro o una columna «Lote», ese elemento desaparece al abrirla. Las existencias por lote y en valor están en el informe «Estado del inventario».
- El formulario móvil de venta funciona con el almacén por órdenes como el principal: una venta nueva no ofrece un almacén por órdenes, y una venta que formaliza órdenes de salida muestra la columna «Orden» y no permite cambiar el almacén.

## 2.0.16.79
### ru
- Очередь «К оформлению»: в списках приходных и расходных ордеров появилась колонка «К оформлению» — сколько по ордеру ещё не оформлено поступлением или реализацией, и флажок «Только к оформлению» в панели фильтров. Кнопка «Оформить поступлением» / «Оформить реализацией» создаёт один документ по выделенным ордерам; ордера должны быть с одного склада, одной организации, одного контрагента и по одному заказу. После записи документа список обновляется сам.
- Списки ордеров доступны и в разделах продаж (расходные) и закупок (приходные) — менеджерам не нужен раздел «Склад».
- Новый отчёт «Остатки на складах» (разделы «Склад» и «Продажи»): сколько товара физически лежит на складе на выбранную дату, сколько прихода и расхода по ордерам ещё не оформлено и сколько будет по учёту после оформления.

### fr
- File « À régulariser » : les listes des bons de réception et de sortie ont une colonne « À régulariser » — ce qui n'est pas encore régularisé par une réception ou une vente — et une case « À régulariser seulement » dans le panneau des filtres. Le bouton « Régulariser par une réception » / « Régulariser par une vente » crée un document pour les bons sélectionnés ; ils doivent être du même entrepôt, de la même société, du même tiers et de la même commande. Après l'enregistrement du document, la liste se met à jour.
- Les listes des bons sont aussi disponibles dans les sections ventes (bons de sortie) et achats (bons de réception) — les responsables n'ont pas besoin de la section « Entrepôt ».
- Nouveau rapport « Stocks en entrepôt » (sections « Entrepôt » et « Ventes ») : la quantité physiquement en entrepôt à la date choisie, l'entrée et la sortie par bons pas encore régularisées et la quantité selon la comptabilité après régularisation.

### en
- «To document» queue: the receipt and issue order lists have a «To document» column — what has not yet been documented by a purchase receipt or a sale — and a «To document only» flag in the filter panel. The «Document with a receipt» / «Document with a sale» button creates one document for the selected orders; they must be from one warehouse, one company, one counterparty and one order. After the document is saved, the list refreshes itself.
- The order lists are also available in the sales (issue orders) and purchasing (receipt orders) sections — managers do not need the «Warehouse» section.
- New «Warehouse stock» report («Warehouse» and «Sales» sections): the quantity physically in the warehouse on the selected date, the receipts and issues by orders not yet documented, and the quantity per accounting after documenting.

### es
- Cola «Por formalizar»: las listas de órdenes de entrada y salida tienen la columna «Por formalizar» — lo que aún no está formalizado por una recepción o una venta — y la casilla «Solo por formalizar» en el panel de filtros. El botón «Formalizar con una recepción» / «Formalizar con una venta» crea un documento para las órdenes seleccionadas; deben ser del mismo almacén, la misma empresa, el mismo contraparte y el mismo pedido. Tras guardar el documento, la lista se actualiza sola.
- Las listas de órdenes están también en las secciones de ventas (órdenes de salida) y compras (órdenes de entrada): los gestores no necesitan la sección «Almacén».
- Nuevo informe «Existencias en almacenes» (secciones «Almacén» y «Ventas»): la cantidad física en el almacén en la fecha elegida, la entrada y salida por órdenes aún no formalizadas y la cantidad según contabilidad tras formalizar.

## 2.0.16.78
### ru
- Рабочее место производства работает с ордерным складом. Если склад нового документа ордерный, строка закладки «Поступления» создаёт приходный ордер, а строка закладки «Отгрузки» — расходный ордер вместо поступления и реализации. Кнопки «Поступление» и «Отгрузка» на таком складе открывают форму ордера.
- Строки ордеров видны на тех же закладках, без цены и суммы. Ордер, по которому уже оформлены поступление или реализация, в рабочем месте только для просмотра. Строки поступлений и реализаций, оформивших ордера, на закладках не повторяются: приход и отгрузку на складе показывает ордер.
- Приходный ордер, введённый строкой по заказу поставщику, закрывает выбранную строку заказа. В выборе строк заказа поставщику и в остатке к поступлению учитываются и приходные ордера, в том числе непроведённые.
- Закладка «Документы заказа» показывает ордера с движением продукции и материалов, а также автовыпуски по расходным ордерам. Реализация или поступление, оформившие ордер, «отгружено» и «приход» не удваивают.

### fr
- Le poste de travail production fonctionne avec l'entrepôt à bons. Si l'entrepôt du nouveau document fonctionne par bons, une ligne de l'onglet « Réceptions » crée un bon de réception et une ligne de l'onglet « Expéditions » un bon de sortie, à la place de la réception et de la vente. Les boutons « Réception » et « Expédition » ouvrent alors le formulaire du bon.
- Les lignes des bons apparaissent dans les mêmes onglets, sans prix ni montant. Un bon déjà régularisé par une réception ou une vente est en lecture seule dans le poste de travail. Les lignes des réceptions et ventes qui régularisent des bons ne sont pas répétées dans les onglets : l'entrée et la sortie en entrepôt sont montrées par le bon.
- Un bon de réception saisi en ligne sur une commande fournisseur solde la ligne de commande choisie. Le choix des lignes de commande fournisseur et le reste à recevoir tiennent compte des bons de réception, y compris non validés.
- L'onglet « Documents de la commande » affiche les bons avec le mouvement des produits et des matières, ainsi que les fabrications automatiques des bons de sortie. Une vente ou une réception qui régularise un bon ne double pas « expédié » ni « entrée ».

### en
- The production workplace works with order-based warehouses. If the warehouse of the new document is order-based, a line on the «Receipts» tab creates a goods receipt order and a line on the «Shipments» tab a goods issue order instead of a purchase receipt and a sale. The «Receipt» and «Shipment» buttons then open the order form.
- Order lines appear on the same tabs, without price and amount. An order already documented by a receipt or a sale is read-only in the workplace. Lines of receipts and sales that document orders are not repeated on the tabs: the warehouse receipt and shipment are shown by the order.
- A goods receipt order entered as a line for a purchase order closes the selected order line. The choice of purchase order lines and the remainder to receive take receipt orders into account, including unposted ones.
- The «Order documents» tab shows orders with the movement of products and materials, as well as automatic releases of issue orders. A sale or a receipt that documents an order does not double «shipped» or «received».

### es
- El puesto de trabajo de producción trabaja con el almacén por órdenes. Si el almacén del nuevo documento funciona por órdenes, una línea de la pestaña «Recepciones» crea una orden de entrada y una línea de la pestaña «Envíos» una orden de salida, en lugar de la recepción y la venta. Los botones «Recepción» y «Envío» abren entonces el formulario de la orden.
- Las líneas de las órdenes aparecen en las mismas pestañas, sin precio ni importe. Una orden ya formalizada por una recepción o una venta es de solo lectura en el puesto de trabajo. Las líneas de recepciones y ventas que formalizan órdenes no se repiten en las pestañas: la entrada y la salida del almacén las muestra la orden.
- Una orden de entrada introducida como línea de un pedido a proveedor cierra la línea del pedido elegida. La elección de líneas del pedido a proveedor y el resto por recibir tienen en cuenta las órdenes de entrada, incluso no contabilizadas.
- La pestaña «Documentos del pedido» muestra las órdenes con el movimiento de productos y materiales, y las fabricaciones automáticas de las órdenes de salida. Una venta o una recepción que formaliza una orden no duplica «enviado» ni «entrada».

## 2.0.16.77
### ru
- Ордерный склад. В карточке склада появились флажок «Ордерный склад» и дата начала ордерной схемы. На таком складе кладовщик фиксирует фактический приход и отгрузку товара приходными и расходными ордерами (раздел «Склад»), а поступление и реализация оформляют их потом — одним документом или частями, в том числе несколько ордеров одним документом. Документы, датированные раньше даты начала схемы, проводятся как прежде, без ордеров.
- Приходный ордер вводится на основании заказа поставщику, заказа клиента на производство или реализации, расходный — на основании заказа клиента или поступления. Приходный ордер сразу закрывает заказ поставщику и учитывается в потребностях производства; расходный по заказу на производство выпускает продукцию автоматически, как раньше реализация.
- Поступление и реализация на ордерном складе вводятся на основании ордеров: склад берётся из ордера и не меняется, строки — неоформленный остаток ордеров, колонка «Ордер» показывает, какой ордер оформляет строка. Без ордера такой документ не проводится, оформить больше, чем пришло или ушло по ордеру, нельзя. В поступлении и реализации без ордеров выбор склада предлагает только неордерные склады.
- Оформленный ордер защищён: его нельзя удалить, отменить, перенести на другой склад или уменьшить ниже уже оформленного количества.
- Комплект в расходном ордере списывается со склада по составляющим, а реализация по такому ордеру — в тех же количествах.
- Ордеры печатаются фирменной формой «Приходный ордер» / «Расходный ордер» без цен, с подписями сдавшего и принявшего.
- Остатки в рабочем месте закупок, на главной панели и в отчёте «Продажи детально» считаются по фактическому количеству на складе.
- Возврат поставщику по заказу на производство теперь снимает материал с продукции, по которой он ещё числится пришедшим (раньше — в обратном порядке распределения самого поступления). Итог по заказу и материалу тот же.
- Если по заказу уже возвращено поставщику больше, чем останется принятым после отмены или удаления поступления, программа не даст его отменить: сначала отмените возврат.
- Новая заставка при запуске программы — карандашный эскиз склада и растущего графика, в духе типовых решений 1С.

### fr
- Entrepôt à bons. La fiche de l'entrepôt reçoit la case « Entrepôt à bons » et la date de début du schéma par bons. Dans un tel entrepôt, le magasinier enregistre les entrées et sorties réelles de marchandises par des bons de réception et de sortie (section « Entrepôt »), et la réception et la vente les régularisent ensuite — en un document ou par parties, y compris plusieurs bons en un seul document. Les documents datés avant la date de début du schéma sont validés comme avant, sans bons.
- Le bon de réception se crée à partir d'une commande fournisseur, d'une commande client de production ou d'une vente ; le bon de sortie à partir d'une commande client ou d'une réception. Le bon de réception solde immédiatement la commande fournisseur et compte dans les besoins de production ; le bon de sortie d'une commande de production lance la fabrication automatique, comme la vente auparavant.
- La réception et la vente dans un entrepôt à bons se créent à partir des bons : l'entrepôt vient du bon et ne change pas, les lignes reprennent le reste non régularisé des bons, la colonne « Bon » indique quel bon la ligne régularise. Sans bon, un tel document n'est pas validé, et l'on ne peut pas régulariser plus que ce qui est entré ou sorti selon le bon. Dans une réception ou une vente sans bons, le choix de l'entrepôt ne propose que les entrepôts sans bons.
- Un bon régularisé est protégé : on ne peut ni le supprimer, ni l'annuler, ni le changer d'entrepôt, ni le réduire en dessous de la quantité déjà régularisée.
- Un kit dans un bon de sortie sort de l'entrepôt par composants, et la vente selon ce bon dans les mêmes quantités.
- Les bons s'impriment avec le formulaire à en-tête « Bon de réception » / « Bon de sortie », sans prix, avec les signatures de celui qui remet et de celui qui reçoit.
- Les stocks du poste de travail achats, du tableau de bord et du rapport « Ventes en détail » sont calculés sur la quantité réellement en entrepôt.
- Le retour fournisseur d'une commande de production retire désormais la matière de la production pour laquelle elle est encore comptée comme reçue (auparavant — dans l'ordre inverse de la répartition de la réception elle-même). Le total par commande et matière est le même.
- Si l'on a déjà retourné au fournisseur plus que ce qui restera reçu après l'annulation ou la suppression d'une réception de la commande, le programme refuse cette annulation : annulez d'abord le retour.
- Nouvel écran de démarrage du programme — une esquisse au crayon d'un entrepôt et d'un graphique en hausse, dans l'esprit des solutions standard 1C.

### en
- Order-based warehouse. The warehouse card gets an «Order-based warehouse» flag and the start date of the order scheme. In such a warehouse the storekeeper records the actual receipt and shipment of goods with receipt and issue orders («Warehouse» section), and the purchase receipt and the sale document them later — in one document or in parts, including several orders in one document. Documents dated before the scheme start date are posted as before, without orders.
- A receipt order is entered based on a purchase order, a customer production order or a sale; an issue order based on a customer order or a purchase receipt. The receipt order closes the purchase order at once and counts in production needs; the issue order of a production order releases the products automatically, as the sale did before.
- Purchase receipts and sales in an order-based warehouse are entered based on orders: the warehouse comes from the order and does not change, the lines are the undocumented remainder of the orders, the «Order» column shows which order the line documents. Without an order such a document is not posted, and you cannot document more than came in or went out by the order. In receipts and sales without orders, warehouse selection offers only warehouses without orders.
- A documented order is protected: it cannot be deleted, unposted, moved to another warehouse or reduced below the quantity already documented.
- A kit in an issue order leaves the warehouse by components, and the sale by that order in the same quantities.
- Orders print with the branded «Goods receipt note» / «Goods issue note» form without prices, with the signatures of the person handing over and the person receiving.
- Stock in the purchasing workplace, on the dashboard and in the «Sales in detail» report is calculated from the actual quantity in the warehouse.
- A return to the supplier for a production order now removes the material from the product for which it is still counted as received (previously — in the reverse order of the receipt's own distribution). The total per order and material is the same.
- If more has already been returned to the supplier for an order than will remain received after unposting or deleting a receipt, the program does not allow it: unpost the return first.
- New startup splash screen — a pencil sketch of a warehouse and a rising chart, in the style of standard 1C solutions.

### es
- Almacén por órdenes. La ficha del almacén recibe la casilla «Almacén por órdenes» y la fecha de inicio del esquema por órdenes. En un almacén así, el almacenero registra la entrada y salida real de mercancías con órdenes de entrada y de salida (sección «Almacén»), y la recepción y la venta las formalizan después — en un documento o por partes, incluso varias órdenes en un solo documento. Los documentos con fecha anterior al inicio del esquema se contabilizan como antes, sin órdenes.
- La orden de entrada se introduce a partir de un pedido al proveedor, de un pedido de cliente de producción o de una venta; la orden de salida a partir de un pedido de cliente o de una recepción. La orden de entrada cierra de inmediato el pedido al proveedor y cuenta en las necesidades de producción; la orden de salida de un pedido de producción lanza la fabricación automática, como antes la venta.
- La recepción y la venta en un almacén por órdenes se introducen a partir de las órdenes: el almacén viene de la orden y no cambia, las líneas son el resto no formalizado de las órdenes, la columna «Orden» indica qué orden formaliza la línea. Sin orden, un documento así no se contabiliza, y no se puede formalizar más de lo que entró o salió según la orden. En recepciones y ventas sin órdenes, la elección del almacén solo ofrece almacenes sin órdenes.
- Una orden formalizada está protegida: no se puede eliminar, anular, cambiar de almacén ni reducir por debajo de la cantidad ya formalizada.
- Un kit en una orden de salida sale del almacén por componentes, y la venta según esa orden en las mismas cantidades.
- Las órdenes se imprimen con el formulario corporativo «Orden de entrada» / «Orden de salida», sin precios, con las firmas de quien entrega y quien recibe.
- Las existencias del puesto de trabajo de compras, del panel principal y del informe «Ventas en detalle» se calculan por la cantidad real en el almacén.
- La devolución al proveedor de un pedido de producción ahora retira el material de la producción para la que todavía figura como recibido (antes — en el orden inverso del reparto de la propia recepción). El total por pedido y material es el mismo.
- Si ya se ha devuelto al proveedor más de lo que quedará recibido tras anular o eliminar una recepción del pedido, el programa no lo permite: anule primero la devolución.
- Nueva pantalla de inicio del programa — un boceto a lápiz de un almacén y un gráfico ascendente, al estilo de las soluciones estándar de 1C.

## 2.0.16.76
### ru
- Подготовка склада к ордерной схеме (приходные и расходные ордера кладовщика — в следующих сборках). Рядом с учётом партий и стоимости программа теперь ведёт отдельный учёт физического количества товаров на складах. Пока ордеров нет, оба учёта всегда совпадают, и в работе ничего не меняется.
- Остатки в формах документов, в подборе и выборе серий, в списке и карточке товара, в отчётах «Недостаточные запасы», «Налоговые накладные: нехватка товара на складе» и «Товары для заказа», в рабочих местах закупок и производства считаются по физическому количеству — цифры те же, что и раньше.
- Оповещение о минимальном остатке приходит и тогда, когда остаток ушёл ровно в ноль.
- Первое обновление на эту версию займёт дольше обычного: программа один раз переносит историю движений склада в новый учёт и сверяет его с партиями запись за записью. Если сверка найдёт расхождение, обновление остановится с понятным сообщением и база останется на прежней версии — сообщите об этом в поддержку.

### fr
- Préparation de l'entrepôt au schéma par bons (bons de réception et de sortie du magasinier — dans les prochaines versions). À côté de la gestion des lots et des coûts, le programme tient désormais un suivi séparé des quantités physiques en entrepôt. Tant qu'il n'y a pas de bons, les deux suivis coïncident toujours et rien ne change dans votre travail.
- Les stocks affichés dans les formulaires de documents, dans la sélection des articles et des séries, dans la liste et la fiche article, dans les rapports « Stocks insuffisants », « Factures fiscales : stock insuffisant » et « Marchandises à commander », dans les postes de travail achats et production sont calculés sur les quantités physiques — les chiffres sont les mêmes qu'avant.
- L'alerte de stock minimum arrive aussi lorsque le stock tombe exactement à zéro.
- La première mise à jour vers cette version prendra plus de temps que d'habitude : le programme transfère une fois l'historique des mouvements de stock dans le nouveau suivi et le rapproche des lots enregistrement par enregistrement. Si le rapprochement trouve un écart, la mise à jour s'arrête avec un message clair et la base reste sur la version précédente — signalez-le au support.

### en
- Preparing the warehouse for the order-based scheme (storekeeper receipt and issue orders come in the next builds). Next to the batch and cost accounting, the program now keeps a separate record of physical quantities in warehouses. As long as there are no orders, both records always match and nothing changes in your work.
- Stock shown in document forms, in item and series selection, in the item list and card, in the «Insufficient stocks», «Tax invoices: insufficient stock» and «Goods to order» reports, and in the purchasing and production workplaces is calculated from physical quantities — the figures are the same as before.
- The minimum stock alert now also arrives when the stock drops to exactly zero.
- The first update to this version takes longer than usual: the program transfers the history of stock movements into the new record once and reconciles it with the batches record by record. If the reconciliation finds a difference, the update stops with a clear message and the database stays on the previous version — please report it to support.

### es
- Preparación del almacén para el esquema por órdenes (órdenes de entrada y salida del almacenero — en las próximas versiones). Junto a la contabilidad de lotes y costes, el programa lleva ahora un registro aparte de las cantidades físicas en los almacenes. Mientras no haya órdenes, ambos registros coinciden siempre y en su trabajo no cambia nada.
- Las existencias en los formularios de documentos, en la selección de artículos y series, en la lista y la ficha del artículo, en los informes «Existencias insuficientes», «Facturas fiscales: existencias insuficientes» y «Productos a pedido», y en los puestos de trabajo de compras y producción se calculan por cantidades físicas — las cifras son las mismas que antes.
- El aviso de existencias mínimas llega también cuando las existencias bajan exactamente a cero.
- La primera actualización a esta versión tardará más de lo habitual: el programa traslada una vez el historial de movimientos de almacén al nuevo registro y lo concilia con los lotes registro por registro. Si la conciliación encuentra una diferencia, la actualización se detiene con un mensaje claro y la base se queda en la versión anterior — comuníquelo al soporte.

## 2.0.16.75
### ru
- Из программы удалены прежние макеты печатных форм, которые заменены фирменными: Facture, счёт и накладные DevisBL реализации, налоговых накладных и накладной покупки, акт об оказании услуг, акт сверки, заказ поставщику, запрос котировок, письмо о платеже, а также давно не используемые макеты товарной накладной (Торг-12) и чека налоговой накладной. Печать не меняется: все команды печатают фирменные формы, как в прошлой сборке.
- Если вы меняли один из этих макетов, правка не потеряна. Список макетов печатных форм (Настройки программы → Обслуживание → «Пользовательские макеты печати») показывает её строкой с пометкой «удалён из конфигурации» и флажком «Проверить». Откройте её кнопкой «Изменить макет», чтобы скопировать нужное в фирменный макет или сохранить в файл; ненужную правку удалите кнопкой «Удалить изменённый». Так же показываются правки прежних макетов коммерческого предложения.

### fr
- Les anciens modèles d'impression remplacés par les formulaires à en-tête ont été supprimés du programme : facture, facture proforma et bons de livraison DevisBL des ventes, des factures fiscales et des factures d'achat, acte de prestation de services, relevé de compte, commande fournisseur, demande de cotation, lettre de paiement, ainsi que les modèles inutilisés depuis longtemps du bon de livraison (Torg-12) et du ticket de la facture fiscale. L'impression ne change pas : toutes les commandes impriment les formulaires à en-tête, comme dans la version précédente.
- Si vous aviez modifié l'un de ces modèles, la modification n'est pas perdue. La liste des modèles d'impression (Paramètres du programme → Maintenance → « Modèles d'impression personnalisés ») l'affiche sur une ligne marquée « supprimé de la configuration » avec la case « À vérifier ». Ouvrez-la avec « Modifier le modèle » pour copier ce qui vous sert dans le modèle à en-tête ou l'enregistrer dans un fichier ; supprimez une modification inutile avec « Supprimer le modifié ». Les modifications des anciens modèles de devis s'affichent de la même façon.

### en
- The old print templates replaced by the branded forms have been removed from the program: invoice, proforma invoice and DevisBL delivery notes of sales, tax invoices and purchase invoices, the act of services rendered, the reconciliation statement, the purchase order, the request for quotation, the payment letter, as well as the long-unused templates of the goods delivery note (Torg-12) and of the tax invoice receipt. Printing does not change: all commands print the branded forms, as in the previous build.
- If you changed one of these templates, the change is not lost. The print templates list (Program settings → Maintenance → «Custom print templates») shows it in a row marked «removed from the configuration» with the «Check» flag. Open it with «Edit template» to copy what you need into the branded template or save it to a file; delete a change you no longer need with «Delete the changed one». Changes to the old quotation templates are shown the same way.

### es
- Se han eliminado del programa las plantillas de impresión antiguas sustituidas por los formularios corporativos: factura, factura proforma y albaranes DevisBL de ventas, facturas fiscales y facturas de compra, acta de prestación de servicios, acta de conciliación, pedido al proveedor, solicitud de cotización, carta de pago, así como las plantillas sin uso desde hace tiempo del albarán de mercancías (Torg-12) y del ticket de la factura fiscal. La impresión no cambia: todos los comandos imprimen los formularios corporativos, como en la versión anterior.
- Si había modificado alguna de estas plantillas, el cambio no se pierde. La lista de plantillas de impresión (Configuración del programa → Mantenimiento → «Plantillas de impresión personalizadas») lo muestra en una fila marcada «eliminada de la configuración» con la marca «Comprobar». Ábralo con «Editar plantilla» para copiar lo que necesite a la plantilla corporativa o guardarla en un archivo; elimine un cambio innecesario con «Eliminar la modificada». Los cambios de las plantillas antiguas del presupuesto se muestran del mismo modo.

## 2.0.16.74
### ru
- Заказ поставщику, запрос котировок (обычный и с фото), запрос цен по предложению поставщика и письмо о платеже по расходному кассовому ордеру печатаются в фирменном оформлении, как счёт-фактура и накладная: логотип, реквизиты сторон, подвал реквизитов на каждой странице. Команды остались прежними: на месте пункты меню, настройки «сразу на принтер» и выбранный принтер.
- В документах поставщику поставщик стоит слева, ваша организация — справа, как покупатель; печать организации не ставится, как и раньше.
- Заказ поставщику: номер, строки с ценами, итоги без НДС, НДС и с НДС, сумма прописью, комментарий, дата печати и ответственный.
- Запрос котировок: артикул, код поставщика и код производителя товара, единица и количество, без цен. В варианте «с фото» у каждой строки — фото товара: самая новая картинка из карточки товара; у товара без картинки строка печатается без фото. Строка с фото не обрезает длинное наименование и коды.
- Запрос цен: строки с ценами и итогами, как раньше. Подписи «транспорт» и «клиент» с этой формы убраны — у запроса поставщику их нет.
- Письмо о платеже: получатель, сумма крупно и прописью, статья движения денег, способ оплаты, оплачиваемые документы — номер, номер и дата накладной (BL) поставщика, сумма.
- Рассылка заказов поставщикам по e-mail прикладывает фирменный заказ.
- Если вы меняли макеты прежнего заказа поставщику, запроса котировок, письма о платеже или макет DevisBL_A4, правки сохранены в списке макетов печатных форм, но новые формы печатаются общим фирменным макетом. Правка фирменного макета действует на все фирменные формы всех документов.

### fr
- La commande fournisseur, la demande de cotation (normale et avec photos), la demande de prix de l'offre fournisseur et la lettre de paiement du bon de décaissement s'impriment avec la présentation à en-tête, comme la facture et le bon de livraison : logo, coordonnées des parties, pied de page des mentions légales sur chaque page. Les commandes restent les mêmes : les entrées de menu, l'impression directe et l'imprimante choisie sont conservées.
- Dans les documents adressés au fournisseur, le fournisseur figure à gauche et votre société à droite, en tant qu'acheteur ; le cachet de la société n'est pas apposé, comme avant.
- Commande fournisseur : numéro, lignes avec prix, totaux HT, TVA et TTC, montant en toutes lettres, commentaire, date d'impression et responsable.
- Demande de cotation : référence, code fournisseur et code fabricant de l'article, unité et quantité, sans prix. Dans la variante « avec photos », chaque ligne porte la photo de l'article : l'image la plus récente de sa fiche ; un article sans image s'imprime sans photo. La ligne avec photo ne tronque pas une désignation ou des codes longs.
- Demande de prix : lignes avec prix et totaux, comme avant. Les signatures « transport » et « client » sont retirées de ce formulaire : une demande au fournisseur n'en a pas.
- Lettre de paiement : bénéficiaire, montant en grand et en toutes lettres, rubrique de trésorerie, mode de règlement, documents réglés — numéro, numéro et date du BL fournisseur, montant.
- L'envoi des commandes fournisseurs par e-mail joint la commande à en-tête.
- Si vous aviez modifié les modèles de l'ancienne commande fournisseur, de la demande de cotation, de la lettre de paiement ou le modèle DevisBL_A4, vos modifications restent dans la liste des modèles d'impression, mais les nouveaux formulaires utilisent le modèle à en-tête commun. Une modification du modèle à en-tête s'applique à tous les formulaires à en-tête de tous les documents.

### en
- The purchase order, the request for quotation (regular and with photos), the price request of the supplier offer and the payment letter of the cash payment order now print in the branded layout, like the invoice and the delivery note: logo, party details, legal footer on every page. The commands are unchanged: menu items, direct-to-printer settings and the selected printer are kept.
- In documents to the supplier, the supplier is on the left and your company on the right, as the buyer; the company stamp is not placed, as before.
- Purchase order: number, lines with prices, totals excluding VAT, VAT and including VAT, amount in words, comment, print date and person responsible.
- Request for quotation: reference, supplier code and manufacturer code of the item, unit and quantity, no prices. In the «with photos» variant every line shows the item photo: the newest image from the item card; an item without an image prints without a photo. A line with a photo does not cut off a long description or codes.
- Price request: lines with prices and totals, as before. The «carrier» and «customer» signatures are removed from this form: a request to a supplier has none.
- Payment letter: recipient, large amount and amount in words, cash flow item, payment method, documents paid — number, supplier delivery note (BL) number and date, amount.
- Emailing purchase orders to suppliers attaches the branded order.
- If you modified the templates of the former purchase order, request for quotation, payment letter or the DevisBL_A4 template, your changes stay in the print template list, but the new forms use the common branded template. A change to the branded template applies to all branded forms of all documents.

### es
- El pedido al proveedor, la solicitud de cotización (normal y con fotos), la solicitud de precios de la oferta del proveedor y la carta de pago de la orden de pago de caja se imprimen con el diseño corporativo, como la factura y el albarán: logotipo, datos de las partes, pie con los datos legales en cada página. Los comandos no cambian: se conservan las opciones del menú, la impresión directa y la impresora elegida.
- En los documentos al proveedor, el proveedor figura a la izquierda y su empresa a la derecha, como compradora; el sello de la empresa no se estampa, como antes.
- Pedido al proveedor: número, líneas con precios, totales sin IVA, IVA y con IVA, importe en letras, comentario, fecha de impresión y responsable.
- Solicitud de cotización: referencia, código del proveedor y código del fabricante del artículo, unidad y cantidad, sin precios. En la variante «con fotos» cada línea lleva la foto del artículo: la imagen más reciente de su ficha; un artículo sin imagen se imprime sin foto. La línea con foto no recorta una descripción o códigos largos.
- Solicitud de precios: líneas con precios y totales, como antes. Se quitan de este formulario las firmas «transporte» y «cliente»: una solicitud al proveedor no las tiene.
- Carta de pago: beneficiario, importe grande y en letras, partida de tesorería, forma de pago, documentos pagados — número, número y fecha del albarán (BL) del proveedor, importe.
- El envío de pedidos a proveedores por correo adjunta el pedido corporativo.
- Si modificó las plantillas del pedido al proveedor anterior, de la solicitud de cotización, de la carta de pago o la plantilla DevisBL_A4, sus cambios se conservan en la lista de plantillas de impresión, pero los nuevos formularios usan la plantilla corporativa común. Un cambio en la plantilla corporativa se aplica a todos los formularios corporativos de todos los documentos.

## 2.0.16.73
### ru
- «Бланк заказа (A4)» заказа покупателя, акт сверки (обычный, с печатью, без НДС) печатаются в фирменном оформлении, как счёт-фактура и накладная: логотип, реквизиты сторон, подвал реквизитов на каждой странице. Команды остались прежними: на месте пункты меню, настройки «сразу на принтер» и выбранный принтер.
- Бланк заказа: номер, клиент, строки с ценами, итоги без НДС, НДС и с НДС, сумма прописью, дата печати и кто выписал, подписи транспорта и клиента.
- Акт сверки: вступление с руководителями сторон, сальдо на начало и конец периода, документы с дебетом и кредитом, обороты, НДС строк по ставкам (кроме варианта «без НДС»), долг стороны суммой и прописью на языке печати. Суммы — в основной валюте учёта. Руководитель организации — по уставу, как раньше; «с печатью» — печать организации и факсимиле подписи руководителя.
- Акт сверки сравнивает «по нашим данным» и «по данным контрагента» по каждому документу и перечисляет расхождения. Прежняя фраза «по результатам сверки расхождений не выявлено» печаталась всегда; теперь, если расхождений в документе нет, акт пишет, что данные приведены по нашему учёту и подписание акта контрагентом подтверждает отсутствие расхождений.
- Рассылка актов сверки по e-mail прикладывает фирменный акт.
- У приходного и расходного кассового ордера новая печатная форма «Квитанция (Reçu)» на листе A4: сумма крупно и прописью, основание, касса, статья, плательщик или получатель, подписи кассира и плательщика, печать организации. Команда «Чек» для принтера чеков не изменилась.
- Если вы меняли макеты прежнего акта сверки или бланка заказа, правки сохранены в списке макетов печатных форм, но новые формы печатаются общим фирменным макетом. Правка фирменного макета действует на все фирменные формы всех документов.

### fr
- Le « Bon de commande (A4) » de la commande client et l'acte de rapprochement (normal, avec cachet, hors TVA) s'impriment avec la présentation à en-tête, comme la facture et le bon de livraison : logo, coordonnées des parties, pied de page des mentions légales sur chaque page. Les commandes restent les mêmes : les entrées de menu, l'impression directe et l'imprimante choisie sont conservées.
- Bon de commande : numéro, client, lignes avec prix, totaux HT, TVA et TTC, montant en toutes lettres, date d'impression et auteur, signatures transport et client.
- Acte de rapprochement : préambule avec les dirigeants des parties, soldes de début et de fin de période, documents avec débit et crédit, mouvements, TVA des lignes par taux (sauf variante « hors TVA »), dette de la partie en chiffres et en lettres dans la langue d'impression. Les montants sont dans la devise principale. Le dirigeant de la société est celui désigné par les statuts, comme avant ; « avec cachet » ajoute le cachet de la société et le fac-similé de la signature du dirigeant.
- L'acte compare « selon nos données » et « selon les données de la contrepartie » document par document et liste les divergences. L'ancienne phrase « aucune divergence n'a été identifiée » s'imprimait toujours ; désormais, en l'absence de divergence dans le document, l'acte indique que les données proviennent de notre comptabilité et que la signature de la contrepartie confirme l'absence de divergences.
- L'envoi des actes de rapprochement par e-mail joint l'acte à en-tête.
- Le bon d'encaissement et le bon de décaissement ont un nouveau formulaire « Reçu » sur A4 : montant en grand et en toutes lettres, motif, caisse, rubrique, payeur ou bénéficiaire, signatures du caissier et du payeur, cachet de la société. La commande « Ticket » pour l'imprimante de tickets ne change pas.
- Si vous aviez modifié les modèles de l'ancien acte de rapprochement ou du bon de commande, vos modifications restent dans la liste des modèles d'impression, mais les nouveaux formulaires utilisent le modèle à en-tête commun. Une modification du modèle à en-tête s'applique à tous les formulaires à en-tête de tous les documents.

### en
- The customer order «Order form (A4)» and the reconciliation statement (regular, with stamp, without VAT) now print in the branded layout, like the invoice and the delivery note: logo, party details, legal footer on every page. The commands are unchanged: menu items, direct-to-printer settings and the selected printer are kept.
- Order form: number, customer, lines with prices, totals excluding VAT, VAT and including VAT, amount in words, print date and issued by, carrier and customer signatures.
- Reconciliation statement: preamble with the parties' managers, opening and closing balances, documents with debit and credit, turnover, line VAT by rate (except the «without VAT» variant), the party's debt in figures and in words in the print language. Amounts are in the base currency. The company manager is the one appointed by the articles of association, as before; «with stamp» adds the company stamp and the manager's facsimile signature.
- The statement compares «our records» and «counterparty records» document by document and lists the discrepancies. The former sentence «no discrepancies were identified» was always printed; now, when the document shows no discrepancies, the statement says the data come from our records and the counterparty's signature confirms there are no discrepancies.
- Emailing reconciliation statements attaches the branded statement.
- Cash receipt and cash payment orders get a new «Receipt» form on A4: large amount and amount in words, purpose, cash desk, cash flow item, payer or recipient, cashier and payer signatures, company stamp. The «Receipt» command for the receipt printer (Ticket) is unchanged.
- If you modified the templates of the former reconciliation statement or order form, your changes stay in the print template list, but the new forms use the common branded template. A change to the branded template applies to all branded forms of all documents.

### es
- La «Hoja de pedido (A4)» del pedido de cliente y el acta de conciliación (normal, con sello, sin IVA) se imprimen con el diseño corporativo, como la factura y el albarán: logotipo, datos de las partes, pie con los datos legales en cada página. Los comandos no cambian: se conservan las opciones del menú, la impresión directa y la impresora elegida.
- Hoja de pedido: número, cliente, líneas con precios, totales sin IVA, IVA y con IVA, importe en letras, fecha de impresión y emitido por, firmas del transportista y del cliente.
- Acta de conciliación: preámbulo con los directivos de las partes, saldos inicial y final del período, documentos con debe y haber, movimientos, IVA de las líneas por tipo (salvo la variante «sin IVA»), deuda de la parte en cifras y en letras en el idioma de impresión. Los importes están en la moneda principal. El directivo de la empresa es el designado por los estatutos, como antes; «con sello» añade el sello de la empresa y la firma facsímil del directivo.
- El acta compara «según nuestros datos» y «según los datos de la contraparte» documento por documento y enumera las discrepancias. La frase anterior «no se identificaron discrepancias» se imprimía siempre; ahora, si el documento no muestra discrepancias, el acta indica que los datos proceden de nuestra contabilidad y que la firma de la contraparte confirma la ausencia de discrepancias.
- El envío de actas de conciliación por correo adjunta el acta corporativa.
- Las órdenes de ingreso y de pago de caja tienen un nuevo formulario «Recibo» en A4: importe grande y en letras, concepto, caja, partida de tesorería, pagador o beneficiario, firmas del cajero y del pagador, sello de la empresa. El comando «Recibo» para la impresora de tickets no cambia.
- Si modificó las plantillas del acta de conciliación anterior o de la hoja de pedido, sus cambios se conservan en la lista de plantillas de impresión, pero los nuevos formularios usan la plantilla corporativa común. Un cambio en la plantilla corporativa se aplica a todos los formularios corporativos de todos los documentos.

## 2.0.16.72
### ru
- Накладные BL, возврат (Avoir) и акт об оказании услуг печатаются в фирменном оформлении, как коммерческое предложение и счёт-фактура: логотип, реквизиты организации и клиента, итоги без НДС, НДС и с НДС, сумма прописью, подвал реквизитов на каждой странице. Команды остались прежними: на месте пункты меню, настройки «сразу на принтер» и выбранный принтер.
- Накладная BL: оплаты по документу (наличными, чеком, прочие, в кредит) и долг клиента, дата и время печати, кто выписал, подписи транспорта и клиента, номер заказа; адрес доставки клиента, если он отличается от адреса. Варианты «без НДС» и «без цен» — как раньше.
- Команда «Накладная BL» (прежде «Накладная BL (A5)») печатает на листе A4. Рабочее место кассира в режиме PDV по-прежнему печатает накладную без цен — теперь и без итогов и оплат.
- Возврат (Avoir) возврата от покупателя и налогового возврата: основание — накладная или счёт-фактура продажи — и причина возврата; прежде вместо номера заказа печатался номер самого возврата.
- Акт об оказании услуг реализации и поступления печатает только услуги и итоги по ним, сумма прописью — словами; у акта поступления исполнитель — поставщик.
- Убрана команда «Товарная накладная (прежняя форма)». Возврат печатается командой «Возврат товара» (Avoir); ролям, у которых была прежняя команда, добавлены «Возврат товара» и, где у роли есть права на оплаты, «Товарная накладная» (Facture) реализации.
- Роль «Оператор производства» видит документы без цен и сумм — накладная, возврат и акт печатаются ей без цен, счёт-фактура не печатается.
- Если вы меняли макеты прежних накладных BL, акта или «Товарной накладной (прежней формы)», правки сохранены в списке макетов печатных форм, но новые формы печатаются общим фирменным макетом. Правка фирменного макета действует на все фирменные формы всех документов.

### fr
- Les bons de livraison, les avoirs et l'acte de prestation de services s'impriment désormais avec la présentation à en-tête, comme le devis et la facture : logo, coordonnées de la société et du client, totaux HT, TVA et TTC, montant en toutes lettres, pied de page des mentions légales sur chaque page. Les commandes restent les mêmes : les entrées de menu, l'impression directe et l'imprimante choisie sont conservées.
- Bon de livraison : règlements du document (espèces, chèque, autres, crédit) et solde client, date et heure d'impression, auteur, signatures transport et client, numéro de commande ; adresse de livraison du client si elle diffère de son adresse. Les variantes « hors TVA » et « sans prix » restent identiques.
- La commande « Bon de livraison » (auparavant « Bon de livraison (A5) ») imprime sur une feuille A4. Le poste de caisse en mode PDV imprime toujours le bon sans prix — désormais aussi sans totaux ni règlements.
- Avoir du retour client et du retour fiscal : document d'origine — bon de livraison ou facture de vente — et motif du retour ; auparavant, le numéro du retour lui-même s'imprimait à la place du numéro de commande.
- L'acte de prestation de services de la vente et de la réception n'imprime que les services et leurs totaux, montant en toutes lettres ; pour l'acte de réception, le prestataire est le fournisseur.
- La commande « Facture (ancien formulaire) » est supprimée. Le retour s'imprime par la commande « Avoir » ; les rôles qui avaient l'ancienne commande reçoivent « Avoir » et, s'ils ont accès aux règlements, la « Facture » de la vente.
- Le rôle « Opérateur de production » voit les documents sans prix ni montants : le bon, l'avoir et l'acte s'impriment pour lui sans prix, la facture ne s'imprime pas.
- Si vous aviez modifié les modèles des anciens bons de livraison, de l'acte ou de la « Facture (ancien formulaire) », vos modifications restent dans la liste des modèles d'impression, mais les nouveaux formulaires utilisent le modèle à en-tête commun. Une modification du modèle à en-tête s'applique à tous les formulaires à en-tête de tous les documents.

### en
- Delivery notes, credit notes (Avoir) and the act of provision of services now print in the branded layout, like the quotation and the invoice: logo, company and customer details, totals excluding VAT, VAT and including VAT, amount in words, legal footer on every page. The commands are unchanged: menu items, direct-to-printer settings and the selected printer are kept.
- Delivery note: payments on the document (cash, cheque, other, credit) and the customer balance, print date and time, issued by, carrier and customer signatures, order number; the customer delivery address when it differs from the address. The «without VAT» and «without prices» variants work as before.
- The «Delivery note» command (formerly «Delivery note (A5)») prints on A4. The cashier workstation in PDV mode still prints the note without prices — now also without totals and payments.
- Credit note of the customer return and the tax return: the source document — sales delivery note or invoice — and the return reason; previously the return's own number was printed instead of the order number.
- The act of provision of services for sales and receipts prints only the services and their totals, with the amount in words; on the receipt act the contractor is the supplier.
- The «Invoice (former form)» command is removed. Returns print with the «Credit note» command (formerly shown as «Have»); roles that had the former command get «Credit note» and, where the role can read payments, the sales «Invoice».
- The «Production operator» role sees documents without prices and amounts: the delivery note, credit note and act print without prices for it, the invoice is not printed.
- If you modified the templates of the former delivery notes, the act or the «Invoice (former form)», your changes stay in the print template list, but the new forms use the common branded template. A change to the branded template applies to all branded forms of all documents.

### es
- Los albaranes de entrega, las notas de abono (Avoir) y el acta de prestación de servicios se imprimen ahora con el diseño corporativo, como el presupuesto y la factura: logotipo, datos de la empresa y del cliente, totales sin IVA, IVA y con IVA, importe en letras, pie con los datos legales en cada página. Los comandos no cambian: se conservan las opciones del menú, la impresión directa y la impresora elegida.
- Albarán de entrega: pagos del documento (efectivo, cheque, otros, crédito) y saldo del cliente, fecha y hora de impresión, emitido por, firmas del transportista y del cliente, número de pedido; dirección de entrega del cliente si difiere de su dirección. Las variantes «sin IVA» y «sin precios» funcionan como antes.
- El comando «Albarán de entrega» (antes «Albarán de entrega (A5)») imprime en A4. El puesto de caja en modo PDV sigue imprimiendo el albarán sin precios — ahora también sin totales ni pagos.
- Nota de abono de la devolución de cliente y de la devolución fiscal: documento de origen — albarán o factura de venta — y motivo de la devolución; antes se imprimía el número de la propia devolución en lugar del número de pedido.
- El acta de prestación de servicios de la venta y de la recepción imprime solo los servicios y sus totales, con el importe en letras; en el acta de recepción el prestador es el proveedor.
- Se elimina el comando «Factura (formulario anterior)». La devolución se imprime con el comando «Nota de abono» (antes aparecía como «Tener»); los roles que tenían el comando anterior reciben «Nota de abono» y, si pueden leer los pagos, la «Factura» de la venta.
- El rol «Operador de producción» ve los documentos sin precios ni importes: el albarán, la nota de abono y el acta se le imprimen sin precios, la factura no se imprime.
- Si modificó las plantillas de los albaranes anteriores, del acta o de la «Factura (formulario anterior)», sus cambios se conservan en la lista de plantillas de impresión, pero los nuevos formularios usan la plantilla corporativa común. Un cambio en la plantilla corporativa se aplica a todos los formularios corporativos de todos los documentos.

## 2.0.16.71
### ru
- Отчёты оформлены в едином стиле «Античный» вместо «Арктика».
- «Ведомость по продажам» группирует сразу по товару и артикулу, без уровня организации.
- «Ведомость расчётов с покупателями» и «Ведомость расчётов с контрагентами» показывают «Контрагент → объект расчётов» — без уровней организации и договора; «Ведомость расчётов с поставщиками» — без уровней организации и валюты.
- В «Ценах номенклатуры» из настроек убран параметр «Показывать цены закупки».

### fr
- Les rapports utilisent désormais le style de présentation unique « Antique » au lieu d'« Arctique ».
- Le « Relevé des ventes » regroupe directement par article et référence, sans le niveau société.
- Les relevés des comptes clients et des tiers affichent « Tiers → objet de règlement », sans les niveaux société et contrat ; le relevé des comptes fournisseurs — sans les niveaux société et devise.
- Dans « Prix des articles », le paramètre « Afficher les prix d'achat » est retiré des réglages.

### en
- Reports now use the single «Antique» appearance template instead of «Arctic».
- The «Sales statement» groups directly by item and reference, without the company level.
- The customer and counterparty settlement statements show «Counterparty → settlement object», without the company and contract levels; the supplier settlement statement — without the company and currency levels.
- The «Show purchase prices» parameter is removed from the «Item prices» settings.

### es
- Los informes usan ahora la plantilla de presentación única «Antiguo» en lugar de «Ártico».
- La «Relación de ventas» agrupa directamente por artículo y referencia, sin el nivel de empresa.
- Las relaciones de liquidaciones con clientes y con contrapartes muestran «Contraparte → objeto de liquidación», sin los niveles de empresa y contrato; la relación de liquidaciones con proveedores, sin los niveles de empresa y moneda.
- En «Precios de artículos» se ha quitado de la configuración el parámetro «Mostrar precios de compra».

## 2.0.16.70
### ru
- Счёт-фактура (Facture) реализации, налоговой накладной и налоговой накладной покупки, «Товарная накладная на бланке» налоговой накладной, счёт на оплату (Facture proforma) реализации и налоговой накладной и счёт-проформа заказа покупателя печатаются в фирменном оформлении коммерческого предложения. Команды остались прежними: на месте пункты меню, настройки «сразу на принтер» и выбранный принтер.
- На счёте-фактуре — все реквизиты прежней формы и обязательные реквизиты Марокко: продавец и покупатель в двух колонках с адресом, телефонами и кодами IF, PATENTE, RC, CNSS, ICE, код клиента, номера накладных BL по строкам, артикул, количество и единица, цена, ставка и сумма НДС строки, итоги HT, TVA и TTC, сумма прописью, способ оплаты, банковские реквизиты организации, печать и подпись. Счёт-фактура поставщика печатается со сторонами наоборот: продавец — поставщик, покупатель — ваша организация, с номером счёта поставщика.
- Сумма прописью («Arrêtée la présente facture à la somme de…») печатается словами в валюте документа: раньше у валют без заполненных параметров прописи — в том числе у дирхама — она выходила цифрами, а у валютных документов — в дирхамах. Исправление действует во всех печатных формах.
- Крупные итоги фирменных форм (от сотен тысяч до десяти миллионов) печатаются целиком: раньше старшие разряды обрезались.
- Если вы меняли макеты прежних форм Facture или счёта на оплату в списке макетов, правки больше не применяются: формы печатаются фирменным макетом. Прежние правки сохранены, в журнале регистрации при обновлении — предупреждение. Правка макета «Накладная BL (A4)» больше не действует на счёт-проформу заказа, для накладных BL действует по-прежнему. Правка фирменного макета действует сразу на все фирменные формы.

### fr
- La facture du bon de livraison, de la facture fiscale et de la facture fiscale d'achat, la « Facture sur papier à en-tête » de la facture fiscale, la facture proforma du bon de livraison et de la facture fiscale ainsi que la facture proforma de la commande client s'impriment avec la présentation à en-tête du devis. Les commandes ne changent pas : les entrées de menu, le réglage « directement sur l'imprimante » et l'imprimante choisie sont conservés.
- La facture reprend toutes les mentions de l'ancien formulaire et les mentions obligatoires au Maroc : vendeur et client sur deux colonnes avec adresse, téléphones et codes IF, PATENTE, RC, CNSS, ICE, code client, numéros des bons de livraison par ligne, référence, quantité et unité, prix, taux et montant de TVA de la ligne, totaux HT, TVA et TTC, montant en lettres, mode de règlement, coordonnées bancaires de la société, cachet et signature. La facture d'achat s'imprime avec les parties inversées : le vendeur est le fournisseur, le client est votre société, avec le numéro de facture du fournisseur.
- Le montant en lettres (« Arrêtée la présente facture à la somme de… ») s'imprime en toutes lettres dans la devise du document : auparavant, pour les devises sans paramètres d'écriture en lettres — dont le dirham — il sortait en chiffres, et en dirhams pour les documents en devise. La correction s'applique à tous les formulaires imprimables.
- Les gros totaux des formulaires à en-tête (de quelques centaines de milliers à dix millions) s'impriment en entier : auparavant les premiers chiffres étaient coupés.
- Si vous aviez modifié les modèles des anciens formulaires de facture ou de facture proforma dans la liste des modèles, ces modifications ne s'appliquent plus : les formulaires s'impriment avec le modèle à en-tête. Les anciennes modifications sont conservées, un avertissement est écrit dans le journal lors de la mise à jour. La modification du modèle « Bon de livraison (A4) » ne s'applique plus à la facture proforma de la commande, elle reste valable pour les bons de livraison. Une modification du modèle à en-tête s'applique à tous les formulaires à en-tête.

### en
- The invoice (Facture) of the sales document, the tax invoice and the purchase tax invoice, the tax invoice's «Invoice on letterhead», the invoice for payment (Facture proforma) of the sales document and the tax invoice, and the customer order's proforma invoice now print in the branded quotation design. The commands are the same: menu items, the «straight to printer» setting and the chosen printer are kept.
- The invoice carries every detail of the previous form and the details required in Morocco: seller and buyer in two columns with address, phones and IF, PATENTE, RC, CNSS, ICE codes, customer code, delivery note (BL) numbers by line, reference, quantity and unit, price, VAT rate and VAT amount per line, HT, VAT and TTC totals, amount in words, payment method, the company's bank details, stamp and signature. The purchase invoice prints with the parties reversed: the seller is the supplier, the buyer is your company, with the supplier's invoice number.
- The amount in words («Arrêtée la présente facture à la somme de…») is printed in words in the document currency: previously, for currencies without spelling parameters — including the dirham — it came out in figures, and documents in foreign currency showed it in dirhams. The fix applies to all print forms.
- Large totals on branded forms (from hundreds of thousands up to ten million) are printed in full: previously the leading digits were cut off.
- If you had modified the templates of the previous invoice or invoice-for-payment forms in the template list, those changes no longer apply: the forms print with the branded template. The previous changes are kept, and a warning is written to the event log during the update. A change to the «Delivery note (A4)» template no longer affects the customer order's proforma invoice; it still applies to delivery notes. A change to the branded template applies to all branded forms at once.

### es
- La factura del albarán, de la factura fiscal y de la factura fiscal de compra, la «Factura en papel con membrete» de la factura fiscal, la factura para pago (Facture proforma) del albarán y de la factura fiscal y la factura proforma del pedido de cliente se imprimen con el diseño corporativo del presupuesto. Los comandos no cambian: se conservan los elementos del menú, el ajuste «directamente a la impresora» y la impresora elegida.
- La factura incluye todos los datos del formulario anterior y los datos obligatorios en Marruecos: vendedor y cliente en dos columnas con dirección, teléfonos y códigos IF, PATENTE, RC, CNSS, ICE, código de cliente, números de albarán (BL) por línea, referencia, cantidad y unidad, precio, tipo e importe de IVA de la línea, totales HT, IVA y TTC, importe en letras, forma de pago, datos bancarios de la empresa, sello y firma. La factura de compra se imprime con las partes invertidas: el vendedor es el proveedor y el cliente es su empresa, con el número de factura del proveedor.
- El importe en letras («Arrêtée la présente facture à la somme de…») se imprime en letras en la moneda del documento: antes, en las monedas sin parámetros de escritura en letras —entre ellas el dírham— salía en cifras, y en los documentos en divisa salía en dírhams. La corrección se aplica a todos los formularios de impresión.
- Los totales grandes de los formularios corporativos (de cientos de miles a diez millones) se imprimen completos: antes se cortaban las primeras cifras.
- Si había modificado las plantillas de los formularios anteriores de factura o de factura para pago en la lista de plantillas, esos cambios ya no se aplican: los formularios se imprimen con la plantilla corporativa. Los cambios anteriores se conservan y al actualizar se escribe un aviso en el registro. El cambio de la plantilla «Albarán de entrega (A4)» ya no afecta a la factura proforma del pedido; sigue aplicándose a los albaranes. Un cambio de la plantilla corporativa se aplica a la vez a todos los formularios corporativos.

## 2.0.16.69
### ru
- Опция «Коммерческие предложения» (Настройки программы, раздел «Продажи») теперь решает, кто создаёт коммерческие предложения. Опция включена — предложения вводит менеджер, как раньше. Опция выключена — реализация сама создаёт своё коммерческое предложение и обновляет его при каждой записи и печати: номер и дата — как у реализации, товары и услуги, цены и суммы — из реализации. Вручную при выключенной опции предложения не вводятся и в программе не видны.
- При выключенной опции в реализации (в документе и в списке) в меню «Печать» появилась команда «Коммерческое предложение» — она печатает фирменную форму предложения по данным реализации. Из списка можно напечатать сразу несколько реализаций.
- Если опцию включить, предложения, созданные реализациями, становятся обычными документами: в списке предложений колонка «Из реализации» показывает, по какой реализации создано предложение. Первая ручная правка или отправка клиенту отвязывает предложение от реализации; после выключения опции реализация создаст себе новое.
- Из заказа покупателя убраны печатные формы «Коммерческое предложение (A5)», «(A4)», «(A4, без НДС)» и «(A4, без цен)»: коммерческое предложение печатает документ «Коммерческое предложение» (или реализация при выключенной опции).
- Номер ручного коммерческого предложения по-прежнему уникален в пределах года; при совпадении программа сообщает, каким предложением номер уже занят.
- Описание строки коммерческого предложения больше не ограничено 1024 знаками: длинное описание товара или услуги печатается целиком.

### fr
- L'option « Devis » (Paramètres du programme, section « Ventes ») détermine désormais qui crée les devis. Option activée : le commercial saisit les devis comme avant. Option désactivée : le bon de livraison crée lui-même son devis et le met à jour à chaque enregistrement et impression — numéro et date identiques à ceux du bon de livraison, articles et services, prix et montants repris du bon de livraison. Option désactivée, les devis ne se saisissent pas manuellement et n'apparaissent pas dans le programme.
- Option désactivée, le menu « Impression » du bon de livraison (document et liste) propose la commande « Devis » : elle imprime le formulaire à en-tête du devis à partir des données du bon de livraison. Depuis la liste, plusieurs bons de livraison s'impriment d'un coup.
- Si l'option est activée, les devis créés par les bons de livraison deviennent des documents ordinaires : dans la liste des devis, la colonne « Du bon de livraison » indique le bon d'origine. La première modification manuelle ou l'envoi au client détache le devis du bon de livraison ; après désactivation de l'option, le bon de livraison s'en crée un nouveau.
- Les formulaires imprimables « Devis (A5) », « (A4) », « (A4, hors TVA) » et « (A4, sans prix) » sont retirés de la commande client : le devis s'imprime depuis le document « Devis » (ou depuis le bon de livraison si l'option est désactivée).
- Le numéro d'un devis saisi manuellement reste unique dans l'année ; en cas de doublon, le programme indique quel devis utilise déjà ce numéro.
- La description d'une ligne de devis n'est plus limitée à 1024 caractères : une longue description d'article ou de service s'imprime en entier.

### en
- The «Quotations» option (Program settings, Sales section) now decides who creates quotations. Option on — managers enter quotations as before. Option off — each sales document creates its own quotation and updates it on every save and print: same number and date as the sales document, goods and services, prices and amounts taken from it. With the option off, quotations are not entered manually and are not shown in the program.
- With the option off, the «Print» menu of the sales document (form and list) has a «Quotation» command: it prints the branded quotation form from the sales document data. Several sales documents can be printed at once from the list.
- If you turn the option on, quotations created by sales documents become ordinary documents: the «From sales document» column of the quotation list shows where each one came from. The first manual edit or sending to the customer detaches the quotation from the sales document; after the option is turned off again, the sales document creates a new one.
- The customer order no longer has the «Quotation (A5)», «(A4)», «(A4, without VAT)» and «(A4, without prices)» print forms: quotations are printed from the «Quotation» document (or from the sales document when the option is off).
- A manually entered quotation number is still unique within the year; on a clash the program tells you which quotation already uses the number.
- A quotation line description is no longer limited to 1024 characters: a long item or service description prints in full.

### es
- La opción «Presupuestos» (Configuración del programa, sección «Ventas») decide ahora quién crea los presupuestos. Opción activada: el comercial introduce los presupuestos como antes. Opción desactivada: cada albarán crea su propio presupuesto y lo actualiza en cada grabación e impresión, con el mismo número y fecha que el albarán y los artículos, servicios, precios e importes del albarán. Con la opción desactivada, los presupuestos no se introducen a mano ni se muestran en el programa.
- Con la opción desactivada, el menú «Impresión» del albarán (documento y lista) tiene el comando «Presupuesto»: imprime el formulario corporativo del presupuesto con los datos del albarán. Desde la lista se pueden imprimir varios albaranes a la vez.
- Si activa la opción, los presupuestos creados por los albaranes pasan a ser documentos normales: en la lista de presupuestos la columna «Del albarán» muestra su origen. La primera modificación manual o el envío al cliente desvincula el presupuesto del albarán; al volver a desactivar la opción, el albarán crea uno nuevo.
- Del pedido de cliente se han quitado los formularios de impresión «Presupuesto (A5)», «(A4)», «(A4, sin IVA)» y «(A4, sin precios)»: el presupuesto se imprime desde el documento «Presupuesto» (o desde el albarán con la opción desactivada).
- El número de un presupuesto introducido a mano sigue siendo único dentro del año; si coincide, el programa indica qué presupuesto ya lo usa.
- La descripción de una línea del presupuesto ya no está limitada a 1024 caracteres: una descripción larga de artículo o servicio se imprime completa.

## 2.0.16.68
### ru
- Коммерческое предложение печатается общим механизмом фирменных печатных форм — вид формы не изменился. На этот же механизм в следующих сборках переходят счёт-фактура, накладные, возвраты и другие документы для клиентов и поставщиков: все они будут оформлены одинаково.
- Английская печатная форма коммерческого предложения печатает все надписи по-английски (раньше заголовки таблицы, итогов и подписи выходили по-русски).
- Если вы меняли макет печатной формы коммерческого предложения в списке макетов, эта правка больше не применяется: форма печатается фирменным макетом. Прежняя правка сохранена, в журнале регистрации при обновлении — предупреждение. Правка фирменного макета действует сразу на все фирменные формы.

### fr
- Le devis est imprimé par le mécanisme commun des formulaires à en-tête — son aspect n'a pas changé. Dans les prochaines versions, la facture, les bons de livraison, les avoirs et les autres documents destinés aux clients et fournisseurs passeront au même mécanisme : ils auront tous la même présentation.
- Le formulaire imprimable du devis en anglais imprime tous les libellés en anglais (auparavant les en-têtes du tableau, des totaux et de la signature sortaient en russe).
- Si vous aviez modifié le modèle du devis dans la liste des modèles, cette modification ne s'applique plus : le formulaire est imprimé avec le modèle à en-tête. L'ancienne modification est conservée, un avertissement est écrit dans le journal lors de la mise à jour. Une modification du modèle à en-tête s'applique à tous les formulaires à en-tête.

### en
- The quotation is printed by the common branded print form mechanism — the form looks the same. In the next builds the invoice, delivery notes, credit notes and other documents for customers and suppliers move to the same mechanism: they will all share one design.
- The English quotation print form prints all labels in English (previously the table, totals and signature headings came out in Russian).
- If you had modified the quotation print template in the template list, that change no longer applies: the form prints with the branded template. The previous change is kept, and a warning is written to the event log during the update. A change to the branded template applies to all branded forms at once.

### es
- El presupuesto se imprime con el mecanismo común de formularios corporativos: su aspecto no ha cambiado. En las próximas versiones la factura, los albaranes, los abonos y otros documentos para clientes y proveedores pasarán al mismo mecanismo: todos tendrán el mismo diseño.
- El formulario de impresión del presupuesto en inglés imprime todas las etiquetas en inglés (antes los encabezados de la tabla, los totales y la firma salían en ruso).
- Si había modificado la plantilla del presupuesto en la lista de plantillas, esa modificación ya no se aplica: el formulario se imprime con la plantilla corporativa. La modificación anterior se conserva y al actualizar se escribe un aviso en el registro de eventos. Una modificación de la plantilla corporativa se aplica a todos los formularios corporativos.

## 2.0.16.67
### ru
- Печатная форма коммерческого предложения больше не сжимается по высоте: строки шапки, таблицы, итогов и подписи печатаются полной высоты, текст не наезжает друг на друга.
- Заголовок коммерческого предложения печатается на всю ширину листа; плашка редакции перенесена в строку номера и печатается, только когда у предложения есть редакция.
- Длинное наименование товара и единица измерения в строке предложения переносятся на следующую строку, а не обрезаются.

### fr
- Le formulaire imprimable du devis n'est plus écrasé en hauteur : les lignes de l'en-tête, du tableau, des totaux et de la signature s'impriment en pleine hauteur, le texte ne se chevauche plus.
- Le titre du devis s'imprime sur toute la largeur de la page ; le bandeau de révision passe sur la ligne du numéro et n'apparaît que si le devis a une révision.
- Une désignation longue et l'unité de mesure d'une ligne du devis passent à la ligne au lieu d'être coupées.

### en
- The quotation print form is no longer squashed vertically: header, table, totals and signature rows print at full height, text no longer overlaps.
- The quotation title prints across the full page width; the revision badge moves to the number line and appears only when the quotation has a revision.
- A long item name and the unit of measure in a quotation line wrap to the next line instead of being cut off.

### es
- El formulario de impresión del presupuesto ya no se comprime en altura: las filas del encabezado, la tabla, los totales y la firma se imprimen a altura completa, el texto ya no se superpone.
- El título del presupuesto se imprime en todo el ancho de la página; la etiqueta de revisión pasa a la línea del número y solo aparece cuando el presupuesto tiene revisión.
- Un nombre de artículo largo y la unidad de medida de una línea del presupuesto pasan a la línea siguiente en lugar de cortarse.

## 2.0.16.66
### ru
- Старые свойства товаров (закладка «Свойства» из прежней базы — виды и значения свойств) при обновлении переносятся в дополнительные реквизиты: на каждый вид свойства заводится дополнительный реквизит, у товара появляется значение последней строки вида. Уже заданные значения не перезаписываются. Старые данные сохраняются без изменений; итог переноса (сколько перенесено, какие значения пустые) — в журнале регистрации.

### fr
- Les anciennes propriétés des articles (onglet « Propriétés » de l'ancienne base — types et valeurs de propriétés) sont transférées lors de la mise à jour vers les attributs supplémentaires : un attribut supplémentaire est créé pour chaque type de propriété, et l'article reçoit la valeur de la dernière ligne du type. Les valeurs déjà renseignées ne sont pas écrasées. Les anciennes données sont conservées telles quelles ; le bilan du transfert (nombre transféré, valeurs vides) est dans le journal.

### en
- Old item properties (the "Properties" tab from the former database — property types and values) are moved to additional attributes during the update: an additional attribute is created for each property type, and the item gets the value of the type's last line. Values already set are not overwritten. The old data is kept unchanged; the transfer summary (how many moved, which values were empty) is in the event log.

### es
- Las propiedades antiguas de los artículos (pestaña «Propiedades» de la base anterior — tipos y valores de propiedades) se trasladan en la actualización a los atributos adicionales: se crea un atributo adicional por cada tipo de propiedad y el artículo recibe el valor de la última línea del tipo. Los valores ya definidos no se sobrescriben. Los datos antiguos se conservan sin cambios; el resumen del traslado (cuántos se trasladaron, qué valores estaban vacíos) queda en el registro de eventos.

## 2.0.16.65
### ru
- Фильтры панели в 43 списках документов работают через общий механизм отборов: принудительный отбор склада кассира в списке продаж больше не стирается при смене или очистке фильтра панели по тому же полю. Поведение фильтров не изменилось.

### fr
- Les filtres du panneau des 43 listes de documents passent par un mécanisme commun : le filtre d'entrepôt imposé au caissier dans la liste des ventes n'est plus effacé quand on change ou vide le filtre du panneau sur le même champ. Le comportement des filtres ne change pas.

### en
- Panel filters in 43 document lists now use a common filtering mechanism: the cashier's enforced warehouse filter in the sales list is no longer wiped when a panel filter on the same field is changed or cleared. Filter behaviour is otherwise unchanged.

### es
- Los filtros del panel de 43 listas de documentos usan un mecanismo común: el filtro de almacén impuesto al cajero en la lista de ventas ya no se borra al cambiar o vaciar el filtro del panel por el mismo campo. El comportamiento de los filtros no cambia.

## 2.0.16.64
### ru
- Навигатор иерархии (папки, тип, товарная группа, бренд, поставщик, качество, способ пополнения, свойства) появился и в окнах выбора и подбора товара: в документах товар можно искать так же, как в списке. Подбор по назначению (например, продукция в заказе на производство) считает узлы только по своим типам.
- Удалены неиспользуемые формы номенклатуры и мёртвый код; формулы наценки, листания картинок и открытия упаковок в карточке объединены.

### fr
- Le navigateur de hiérarchie (dossiers, type, groupe de marchandises, marque, fournisseur, qualité, mode de réapprovisionnement, propriétés) apparaît aussi dans les fenêtres de choix et de sélection d'articles : dans les documents, on cherche un article comme dans la liste. La sélection par destination (par exemple, les produits dans un ordre de fabrication) compte les nœuds sur ses seuls types.
- Les formulaires d'articles inutilisés et le code mort sont supprimés ; dans la fiche, les calculs de marge, le défilement des images et l'ouverture des conditionnements sont regroupés.

### en
- The hierarchy navigator (folders, type, product group, brand, supplier, quality, replenishment method, properties) now also appears in the item choice and pick windows: in documents an item can be found the same way as in the list. Picking by purpose (for example, products in a production order) counts nodes only for its own types.
- Unused item forms and dead code are removed; in the card, markup calculation, image scrolling and opening packages are merged.

### es
- El navegador de jerarquía (carpetas, tipo, grupo de mercancías, marca, proveedor, calidad, forma de reposición, propiedades) aparece también en las ventanas de selección y de elección de artículos: en los documentos un artículo se busca igual que en la lista. La selección por destino (por ejemplo, productos en un pedido de producción) cuenta los nodos solo por sus propios tipos.
- Se eliminan formularios de artículos sin uso y código muerto; en la ficha se unifican el cálculo del margen, el desplazamiento de imágenes y la apertura de embalajes.

## 2.0.16.63
### ru
- Карточка товара показывает живые данные: на закладке «Склад» — остатки по складам со свободным количеством (без закреплённого за требованиями на станках), «на станках сейчас» по требованиям, заказано поставщикам, потребность производства и продажи за 12 месяцев; на «Производстве» — выработка станков по товару (норма из карточки станка или общая выработка допустимого станка) и для сырья и полуфабрикатов — «где используется»: продукция, в действующие техкарты которой входит товар; на «Служебном» — штрихкоды товара списком.
- Блоки загружаются при первом открытии своей закладки. Блок, читать данные которого роли не разрешено, не показывается — карточка открывается без ошибок под любой ролью.

### fr
- La fiche article affiche des données en direct : l'onglet « Stock » — stocks par entrepôt avec la quantité libre (hors matières affectées aux bons sur les machines), « sur les machines maintenant » par bon, commandé aux fournisseurs, besoin de production et ventes sur 12 mois ; « Production » — cadence des machines pour l'article (norme de la fiche machine ou cadence générale d'une machine autorisée) et, pour les matières premières et semi-finis, « utilisé dans » : les produits dont les gammes en vigueur contiennent l'article ; « Service » — les codes-barres de l'article en liste.
- Les blocs se chargent à la première ouverture de leur onglet. Un bloc dont le rôle n'a pas le droit de lire les données n'est pas affiché : la fiche s'ouvre sans erreur sous tout rôle.

### en
- The item card shows live data: the "Stock" tab — stock by warehouse with the free quantity (excluding materials reserved for requisitions on machines), "on machines now" by requisition, ordered from suppliers, production need and sales over 12 months; "Production" — machine output for the item (the machine card standard or the general output of an allowed machine) and, for raw materials and semi-finished goods, "used in": products whose current routings contain the item; "Service" — the item barcodes as a list.
- Blocks load when their tab is first opened. A block whose data the role may not read is not shown, so the card opens without errors under any role.

### es
- La ficha del artículo muestra datos en vivo: la pestaña «Almacén» — existencias por almacén con la cantidad libre (sin lo reservado para vales en máquinas), «en máquinas ahora» por vale, pedido a proveedores, necesidad de producción y ventas de 12 meses; «Producción» — rendimiento de las máquinas para el artículo (norma de la ficha de la máquina o rendimiento general de una máquina permitida) y, para materias primas y semielaborados, «se usa en»: productos cuyas rutas vigentes contienen el artículo; «Servicio» — los códigos de barras del artículo en lista.
- Los bloques se cargan al abrir su pestaña por primera vez. Un bloque cuyos datos el rol no puede leer no se muestra: la ficha se abre sin errores con cualquier rol.

## 2.0.16.62
### ru
- Карточка товара перегруппирована по важности: в шапке — наименование, артикул, тип, папка и живые показатели (остаток, свободно, розничная и закупочная цена; ниже минимума — красным). Закладки: «Основное», «Цены», «Склад», «Производство», «Комплект», «Свойства», «Описание и печать», «Служебное».
- Скрытые блоки вернулись на свои закладки: товарная группа, производитель и импортёр (при включённом импорте) — «Основное»; упаковки (при включённой опции упаковок) и условия хранения — «Склад»; данные стикера — «Описание и печать»; код, старый код, полное наименование, ответственный, ECommerce и «Отражать в ЛКП» — «Служебное». Техкарта и станки — разделами закладки «Производство».
- Карточка открывается быстрее: цены и технологическая карта загружаются при первом переходе на свою закладку. Видимость закладок по типу настраивается ещё до показа формы — без мигания.

### fr
- La fiche article est réorganisée par importance : l'en-tête montre le nom, la référence, le type, le dossier et des indicateurs en direct (stock, libre, prix de détail et d'achat ; sous le minimum — en rouge). Onglets : « Principal », « Prix », « Stock », « Production », « Kit », « Propriétés », « Description et impression », « Service ».
- Les blocs masqués reviennent sur leurs onglets : groupe de marchandises, fabricant et importateur (avec l'import activé) — « Principal » ; conditionnements (avec l'option activée) et conditions de stockage — « Stock » ; données de l'étiquette — « Description et impression » ; code, ancien code, nom complet, responsable, ECommerce et « Afficher dans l'espace client » — « Service ». Gamme et machines — sections de l'onglet « Production ».
- La fiche s'ouvre plus vite : les prix et la gamme de fabrication se chargent à la première ouverture de leur onglet. La visibilité des onglets selon le type est réglée avant l'affichage du formulaire, sans clignotement.

### en
- The item card is regrouped by importance: the header shows name, article, type, folder and live indicators (stock, free, retail and purchase price; below minimum in red). Tabs: "Main", "Prices", "Stock", "Production", "Kit", "Properties", "Description and printing", "Service".
- Hidden blocks are back on their tabs: product group, manufacturer and importer (with import enabled) on "Main"; packages (with the packages option enabled) and storage conditions on "Stock"; sticker data on "Description and printing"; code, old code, full name, responsible, ECommerce and "Show in customer portal" on "Service". Routing and machines are sections of the "Production" tab.
- The card opens faster: prices and the production routing load when their tab is first opened. Tab visibility by type is set before the form is shown, without flicker.

### es
- La ficha del artículo se reorganiza por importancia: la cabecera muestra nombre, referencia, tipo, carpeta e indicadores en vivo (existencias, libre, precio minorista y de compra; bajo mínimo en rojo). Pestañas: «Principal», «Precios», «Almacén», «Producción», «Kit», «Propiedades», «Descripción e impresión», «Servicio».
- Los bloques ocultos vuelven a sus pestañas: grupo de mercancías, fabricante e importador (con importación activada) en «Principal»; embalajes (con la opción activada) y condiciones de almacenamiento en «Almacén»; datos de la etiqueta en «Descripción e impresión»; código, código antiguo, nombre completo, responsable, ECommerce y «Mostrar en el portal del cliente» en «Servicio». Ruta y máquinas son secciones de la pestaña «Producción».
- La ficha se abre más rápido: los precios y la ruta de fabricación se cargan al abrir su pestaña por primera vez. La visibilidad de las pestañas según el tipo se ajusta antes de mostrar el formulario, sin parpadeo.

## 2.0.16.61
### ru
- В списке товаров слева появился навигатор иерархии: над ним выбирается режим — папки (как раньше), тип, товарная группа, бренд, основной поставщик, качество, способ пополнения или любое дополнительное свойство товара. Узлы показывают число товаров с учётом фильтров панели и раздела, откуда открыт список; «<не задано>» — товары без значения. Выбор узла отбирает список и складывается с фильтрами панели.
- Звёздочка рядом с режимом закрепляет его первым в списке режимов; режим, выбранный узел и избранные режимы запоминаются. Кнопка ↻ пересчитывает узлы.
- На закладке «Фильтры» добавлен отбор «Свойство = значение» по дополнительным реквизитам и сведениям товара — работает в любом режиме навигатора.

### fr
- La liste des articles reçoit à gauche un navigateur de hiérarchie : au-dessus, on choisit le mode — dossiers (comme avant), type, groupe de marchandises, marque, fournisseur principal, qualité, mode de réapprovisionnement ou toute propriété supplémentaire de l'article. Les nœuds affichent le nombre d'articles en tenant compte des filtres du panneau et de la section d'où la liste est ouverte ; « <non renseigné> » regroupe les articles sans valeur. Le choix d'un nœud filtre la liste et se combine avec les filtres du panneau.
- L'étoile à côté du mode l'épingle en tête de la liste des modes ; le mode, le nœud choisi et les modes favoris sont mémorisés. Le bouton ↻ recalcule les nœuds.
- L'onglet « Filtres » reçoit le filtre « Propriété = valeur » sur les attributs et informations supplémentaires de l'article — il fonctionne dans n'importe quel mode du navigateur.

### en
- The item list gets a hierarchy navigator on the left: above it you choose the mode — folders (as before), type, product group, brand, main supplier, quality, replenishment method or any additional item property. Nodes show the number of items taking into account the panel filters and the section the list was opened from; "<not set>" groups items without a value. Choosing a node filters the list and combines with the panel filters.
- The star next to the mode pins it at the top of the mode list; the mode, the selected node and favorite modes are remembered. The ↻ button recounts the nodes.
- The "Filters" tab gets a "Property = value" filter on additional item attributes and information — it works in any navigator mode.

### es
- La lista de artículos recibe a la izquierda un navegador de jerarquía: encima se elige el modo — carpetas (como antes), tipo, grupo de mercancías, marca, proveedor principal, calidad, forma de reposición o cualquier propiedad adicional del artículo. Los nodos muestran el número de artículos teniendo en cuenta los filtros del panel y la sección desde la que se abrió la lista; «<sin definir>» agrupa los artículos sin valor. Elegir un nodo filtra la lista y se combina con los filtros del panel.
- La estrella junto al modo lo fija al principio de la lista de modos; el modo, el nodo elegido y los modos favoritos se recuerdan. El botón ↻ recalcula los nodos.
- La pestaña «Filtros» recibe el filtro «Propiedad = valor» por atributos e información adicionales del artículo; funciona en cualquier modo del navegador.

## 2.0.16.60
### ru
- Список товаров получил панель «Сведения» справа, как у списков документов: закладка «Фильтры» — тип, способ пополнения, наличие (в наличии, нет, ниже минимума), склад остатка (по умолчанию — склад пользователя), товарная группа, бренд, основной поставщик, качество и флажок «Показывать помеченные на удаление»; закладка «Товар» — реквизиты и цены текущего товара; «Движение» — остатки по складам со свободным количеством (без закреплённого на станках), заказано поставщикам, потребность производства и продажи за 12 месяцев. Панель сворачивается в столбик значков, фильтры и состояние запоминаются.
- В таблице списка видны наименование, артикул, единица, остаток и розничная цена — без горизонтальной прокрутки; остальные колонки включаются через «Ещё → Изменить форму». Колонка «Продажи» убрана из списка: продажи — на закладке «Движение».
- Остаток в списке считается по товару целиком: товар с несколькими партиями больше не показывается несколькими строками.

### fr
- La liste des articles reçoit le panneau « Informations » à droite, comme les listes de documents : onglet « Filtres » — type, mode de réapprovisionnement, disponibilité (en stock, en rupture, sous le minimum), entrepôt du stock (par défaut celui de l'utilisateur), groupe de marchandises, marque, fournisseur principal, qualité et la case « Afficher les éléments marqués pour suppression » ; onglet « Article » — attributs et prix de l'article courant ; « Mouvements » — stocks par entrepôt avec la quantité libre (hors matières affectées aux machines), commandé aux fournisseurs, besoin de production et ventes sur 12 mois. Le panneau se replie en colonne d'icônes, les filtres et l'état sont mémorisés.
- Le tableau de la liste montre le nom, la référence, l'unité, le stock et le prix de détail, sans défilement horizontal ; les autres colonnes s'activent par « Plus → Modifier le formulaire ». La colonne « Ventes » est retirée de la liste : les ventes sont dans l'onglet « Mouvements ».
- Le stock de la liste est compté par article : un article en plusieurs lots n'apparaît plus sur plusieurs lignes.

### en
- The item list gets the "Details" panel on the right, like document lists: the "Filters" tab — type, replenishment method, availability (in stock, out of stock, below minimum), stock warehouse (the user's warehouse by default), product group, brand, main supplier, quality and the "Show items marked for deletion" check box; the "Item" tab — attributes and prices of the current item; "Movement" — stock by warehouse with the free quantity (excluding materials reserved on machines), ordered from suppliers, production need and sales over 12 months. The panel collapses into a column of icons; filters and state are remembered.
- The list table shows name, article, unit, stock and retail price without horizontal scrolling; other columns can be enabled via "More → Change form". The "Sales" column is removed from the list: sales are on the "Movement" tab.
- Stock in the list is counted per item: an item with several batches is no longer shown as several rows.

### es
- La lista de artículos recibe el panel «Información» a la derecha, como las listas de documentos: pestaña «Filtros» — tipo, forma de reposición, disponibilidad (en stock, agotado, bajo mínimo), almacén de existencias (por defecto el del usuario), grupo de mercancías, marca, proveedor principal, calidad y la casilla «Mostrar marcados para eliminar»; pestaña «Artículo» — atributos y precios del artículo actual; «Movimientos» — existencias por almacén con la cantidad libre (sin lo reservado en máquinas), pedido a proveedores, necesidad de producción y ventas de 12 meses. El panel se pliega en una columna de iconos; los filtros y el estado se recuerdan.
- La tabla de la lista muestra nombre, referencia, unidad, existencias y precio minorista sin desplazamiento horizontal; las demás columnas se activan con «Más → Cambiar formulario». La columna «Ventas» se quita de la lista: las ventas están en la pestaña «Movimientos».
- Las existencias de la lista se cuentan por artículo: un artículo con varios lotes ya no aparece en varias filas.

## 2.0.16.59
### ru
- Карточка товара больше не перезаписывает чужой штрихкод: если артикул или отсканированный штрихкод уже принадлежит другому товару, штрихкод не записывается, а карточка показывает, чей он. Собственный штрихкод товара с характеристикой, упаковкой или серией при записи карточки больше не теряет их. Так же работают загрузка товаров из Excel (отказы — в сообщениях загрузки) и новая серия: занятый номер EAN-13 генерируется заново.
- Минимальные и максимальные остатки по складам записываются вместе с товаром: у нового товара они больше не могут сохраниться без товара, а запись карточки меняет только склады, где значение изменилось или ещё не записано.
- Цены и технологическая карта из карточки записываются вместе с товаром: если документ цен или карта не записались, товар тоже не сохраняется — раньше он оставался сохранённым без них.
- Проверка «товар с таким артикулом уже существует» срабатывает только у нового товара и при смене артикула: товары с давним дублем артикула снова можно править. Пустое наименование заполняется из полного и наоборот при любой записи товара.
- Дополнительный реквизит хранит одно значение: при записи из карточки, рабочего места производства или группового изменения лишние строки того же реквизита удаляются, а при чтении из старых дублей берётся последнее значение — как показывает карточка.

### fr
- La fiche article n'écrase plus le code-barres d'un autre article : si la référence ou le code-barres scanné appartient déjà à un autre article, le code-barres n'est pas enregistré et la fiche indique à qui il appartient. Le code-barres propre de l'article ne perd plus sa variante, son conditionnement ou son lot à l'enregistrement de la fiche. Il en va de même pour l'import des articles depuis Excel (refus affichés dans les messages de l'import) et pour un nouveau lot : un numéro EAN-13 déjà pris est régénéré.
- Les stocks minimaux et maximaux par entrepôt sont enregistrés avec l'article : pour un nouvel article ils ne peuvent plus être enregistrés sans article, et l'enregistrement de la fiche ne modifie que les entrepôts dont la valeur a changé ou n'existait pas encore.
- Les prix et la gamme de fabrication de la fiche sont enregistrés avec l'article : si le document de prix ou la gamme échoue, l'article n'est pas enregistré non plus — auparavant il restait enregistré sans eux.
- Le contrôle « un article avec cette référence existe déjà » ne s'applique qu'à un nouvel article et au changement de référence : les articles avec un ancien doublon de référence se modifient à nouveau. Le nom vide est rempli à partir du nom complet et inversement à chaque enregistrement.
- Un attribut supplémentaire garde une seule valeur : à l'enregistrement depuis la fiche, le poste de production ou la modification groupée, les lignes en double du même attribut sont supprimées, et la lecture d'anciens doublons prend la dernière valeur, comme la fiche.

### en
- The item card no longer overwrites another item's barcode: if the article number or a scanned barcode already belongs to another item, the barcode is not saved and the card shows who owns it. The item's own barcode no longer loses its characteristic, package or batch when the card is saved. The same applies to importing items from Excel (refusals are shown in the import messages) and to a new batch: an EAN-13 number already taken is generated again.
- Minimum and maximum stock by warehouse are saved together with the item: for a new item they can no longer be saved without the item, and saving the card changes only the warehouses whose value changed or was not saved yet.
- Prices and the production routing from the card are saved together with the item: if the price document or the routing fails, the item is not saved either — previously it stayed saved without them.
- The "a product with such an article already exists" check applies only to a new item and to an article change: items with an old duplicate article can be edited again. An empty name is filled from the full name and vice versa on every save.
- An additional attribute keeps a single value: when saved from the card, the production workplace or bulk editing, duplicate lines of the same attribute are removed, and reading old duplicates takes the last value, as the card shows.

### es
- La ficha del artículo ya no sobrescribe el código de barras de otro artículo: si la referencia o el código escaneado ya pertenece a otro artículo, el código no se guarda y la ficha indica a quién pertenece. El código propio del artículo ya no pierde su característica, embalaje o lote al guardar la ficha. Lo mismo ocurre con la importación de artículos desde Excel (los rechazos aparecen en los mensajes de la importación) y con un lote nuevo: un número EAN-13 ya ocupado se genera de nuevo.
- Las existencias mínimas y máximas por almacén se guardan junto con el artículo: en un artículo nuevo ya no pueden guardarse sin artículo, y al guardar la ficha solo cambian los almacenes cuyo valor cambió o aún no estaba guardado.
- Los precios y la ruta de fabricación de la ficha se guardan junto con el artículo: si el documento de precios o la ruta fallan, el artículo tampoco se guarda; antes quedaba guardado sin ellos.
- La comprobación «ya existe un producto con esta referencia» solo se aplica a un artículo nuevo y al cambiar la referencia: los artículos con un duplicado antiguo de referencia vuelven a poder editarse. El nombre vacío se rellena con el nombre completo y viceversa en cada guardado.
- Un atributo adicional guarda un solo valor: al guardar desde la ficha, el puesto de producción o la modificación en grupo se eliminan las líneas duplicadas del mismo atributo, y al leer duplicados antiguos se toma el último valor, como muestra la ficha.

## 2.0.16.58
### ru
- Материалы, закреплённые за требованиями-накладными на станке, больше не считаются свободными при закупке: в рабочем месте закупок на закладке остатков товара склад станка показывает только свободное количество, отчёт «Товары для заказа» по складу станка и обработка «Формирование заказов поставщикам» вычитают закреплённое.
- Исправлен отчёт «Недостаточные запасы»: минимальный остаток сравнивался не с тем складом, и отчёт пропускал товары ниже минимума. Теперь остаток считается по товару и складу целиком (по всем партиям), а товар с минимумом и нулевым остатком тоже попадает в отчёт.
- Удалена служебная форма «Проба планировщика»: планировщик работает в рабочем месте «Управление станками».
- Роль «Менеджер по закупкам» получила право чтения регистра «Материалы на станках» и справочника станков — без него закупщик не увидел бы свободные остатки складов станков.

### fr
- Les matières affectées aux bons de consommation sur une machine ne sont plus comptées comme libres pour les achats : dans le poste des achats, l'onglet des stocks de l'article montre pour le stock de la machine la seule quantité libre, le rapport « Marchandises à commander » par stock de machine et le traitement « Génération des commandes fournisseurs » déduisent la quantité affectée.
- Correction du rapport « Stocks insuffisants » : le stock minimal était comparé au mauvais entrepôt et le rapport omettait des articles sous le minimum. Le stock est désormais compté par article et entrepôt (tous lots confondus), et un article avec un minimum et un stock nul figure aussi dans le rapport.
- Le formulaire technique « Essai du planificateur » est supprimé : le planificateur fonctionne dans le poste « Gestion des machines ».
- Le rôle « Responsable des achats » obtient la lecture du registre « Matières sur les machines » et du référentiel des machines, sans laquelle l'acheteur ne verrait pas les stocks libres des machines.

### en
- Materials reserved for requisitions on a machine are no longer counted as free for purchasing: in the purchasing workplace the item stock tab shows only the free quantity for the machine stock, and the "Goods to order" report for a machine stock and the "Purchase order generation" processor deduct the reserved quantity.
- Fixed the "Insufficient stocks" report: the minimum stock was compared against the wrong warehouse, so the report missed items below the minimum. Stock is now counted per item and warehouse as a whole (all batches), and an item with a minimum and zero stock is included too.
- The technical "Planner trial" form has been removed: the planner works in the "Machine management" workplace.
- The "Purchasing manager" role can now read the "Materials on machines" register and the machine catalog; without it the buyer would not see the free stock of machine stocks.

### es
- Los materiales reservados para vales de consumo en una máquina ya no se cuentan como libres para compras: en el puesto de compras, la pestaña de existencias del artículo muestra para el almacén de la máquina solo la cantidad libre, y el informe «Productos a pedido» por almacén de máquina y el procesamiento «Generación de pedidos a proveedores» descuentan lo reservado.
- Corregido el informe «Existencias insuficientes»: el stock mínimo se comparaba con un almacén equivocado y el informe omitía artículos por debajo del mínimo. Ahora el stock se cuenta por artículo y almacén en conjunto (todos los lotes), y un artículo con mínimo y stock cero también aparece en el informe.
- Se eliminó el formulario técnico «Prueba del planificador»: el planificador funciona en el puesto «Gestión de máquinas».
- El rol «Gerente de compras» obtiene la lectura del registro «Materiales en máquinas» y del catálogo de máquinas; sin ella el comprador no vería las existencias libres de los almacenes de máquina.

## 2.0.16.57
### ru
- Требование-накладная по строке заказа не проводится, если вместе с другими открытыми требованиями этой строки оно больше количества строки. Раньше такое требование, введённое вручную, проходило, если у той же продукции заказа был остаток на другой строке.
- «Принять автоплан» не размещает строку, если окно на станке изменилось после расчёта черновика (например, сменили выработку станка): строка называется в ошибках, автоплан нужно рассчитать заново. Раньше требование ставилось в другое окно, чем показывал черновик.
- Отчёт «Эффективность станков (OEE)»: требование, у части материалов которого не задан вес, не входит в производительность — раньше норма по остальным материалам её занижала. Такие позиции перечислены в предупреждении отчёта.

### fr
- Un bon de consommation sur une ligne de commande n'est pas validé si, avec les autres bons ouverts de cette ligne, il dépasse la quantité de la ligne. Auparavant, un tel bon saisi à la main passait si le même produit de la commande avait un reste sur une autre ligne.
- « Accepter la planification » ne place pas une ligne si le créneau de la machine a changé depuis le calcul du brouillon (par exemple, cadence de la machine modifiée) : la ligne est citée dans les erreurs, il faut recalculer la planification. Auparavant, le bon était placé dans un autre créneau que celui du brouillon.
- Rapport « Efficacité des machines (TRS) » : un bon dont une partie des matières n'a pas de poids n'entre plus dans la performance ; la norme calculée sur les autres matières la sous-estimait. Ces articles sont listés dans l'avertissement du rapport.

### en
- A requisition for an order line is not posted if, together with the other open requisitions of that line, it exceeds the line quantity. Previously such a manually entered requisition went through if the same product of the order had a remainder on another line.
- "Accept auto-plan" does not place a line if the machine slot changed after the draft was calculated (for example, the machine output rate was changed): the line is listed in the errors and the auto-plan must be recalculated. Previously the requisition was placed in a different slot than the draft showed.
- "Machine efficiency (OEE)" report: a requisition with some materials lacking a weight no longer counts towards performance; the standard calculated from the other materials understated it. Such items are listed in the report warning.

### es
- Un vale de consumo de una línea de pedido no se contabiliza si, junto con los demás vales abiertos de esa línea, supera la cantidad de la línea. Antes, un vale así introducido a mano pasaba si el mismo producto del pedido tenía resto en otra línea.
- «Aceptar planificación» no coloca una línea si el hueco de la máquina cambió después de calcular el borrador (por ejemplo, se cambió el rendimiento de la máquina): la línea aparece en los errores y hay que recalcular la planificación. Antes el vale se colocaba en otro hueco distinto del borrador.
- Informe «Eficiencia de máquinas (OEE)»: un vale con parte de los materiales sin peso ya no entra en el rendimiento; la norma calculada con los demás materiales lo subestimaba. Esas posiciones se indican en el aviso del informe.

## 2.0.16.56
### ru
- В пересчёте, списании и оприходовании «Вид операции» выбирается переключателем «По складу / По станку», а в заголовке документа по станку написано «по станку».
- В списках пересчётов, списаний и оприходований появилась колонка «Станок» (видна при включённом учёте станков); списки по станку открываются быстрее на больших базах.
- Если у документа по станку сменить вид на «По складу», станок и склад станка очищаются — склад выбирается заново, а не остаётся складом станка.
- Если учёт станков выключен, в документе по станку снова виден склад.
- Кнопки «Заполнить» и «Заполнить остатки» пересчёта считают учётные остатки так же, как прежде, но общим механизмом, который проверяют автотесты.

### fr
- Dans l'inventaire, la sortie et l'entrée de stock, le « Type d'opération » se choisit par un commutateur « Par entrepôt / Par machine », et le titre d'un document par machine indique « par machine ».
- Les listes des inventaires, sorties et entrées de stock ont une colonne « Machine » (visible quand la gestion des machines est activée) ; les listes par machine s'ouvrent plus vite sur les grandes bases.
- Si le type d'un document par machine passe à « Par entrepôt », la machine et son stock sont effacés : l'entrepôt est choisi de nouveau au lieu de rester celui de la machine.
- Si la gestion des machines est désactivée, l'entrepôt d'un document par machine est de nouveau visible.
- Les boutons « Remplir » et « Remplir les stocks » de l'inventaire calculent le stock théorique comme avant, mais par un mécanisme commun vérifié par les tests automatiques.

### en
- In stock counts, write-offs and receipts, the "Operation type" is chosen with a "By warehouse / By machine" switch, and the title of a by-machine document says "by machine".
- The lists of stock counts, write-offs and receipts have a "Machine" column (shown when machine accounting is on); by-machine lists open faster on large databases.
- If a by-machine document is switched to "By warehouse", the machine and its stock are cleared: the warehouse is chosen again instead of staying the machine stock.
- If machine accounting is turned off, the warehouse of a by-machine document is visible again.
- The stock count "Fill" and "Fill balances" buttons calculate book stock as before, but through a shared mechanism covered by automated tests.

### es
- En el recuento, la baja y el alta de existencias, el «Tipo de operación» se elige con un conmutador «Por almacén / Por máquina», y el título de un documento por máquina indica «por máquina».
- Las listas de recuentos, bajas y altas tienen una columna «Máquina» (visible con la contabilidad de máquinas activada); las listas por máquina se abren más rápido en bases grandes.
- Si un documento por máquina se cambia a «Por almacén», la máquina y su almacén se borran: el almacén se elige de nuevo en lugar de quedarse el de la máquina.
- Si la contabilidad de máquinas está desactivada, el almacén de un documento por máquina vuelve a verse.
- Los botones «Rellenar» y «Rellenar saldos» del recuento calculan el stock contable como antes, pero con un mecanismo común cubierto por pruebas automáticas.

## 2.0.16.55
### ru
- Отчёт «Простои станков» с флажком «Включать запланированное» больше не считает дважды время, когда у станка одновременно стоят плановое и фактическое обслуживание: плановое учитывается только за пределами фактического, поэтому процент простоя не превышает фонд времени.
- Время ремонта (MTTR) считается по полной длительности ремонта, даже если ремонт переходит через конец периода отчёта. Раньше в MTTR попадала только часть внутри периода.
- Станок, выведенный из работы, попадает в отчёт, если в периоде у него была работа, — его наработка входит в MTBF. Раньше такой станок без обслуживания в отчёт не попадал.
- Отбор отчёта по виду обслуживания, причине, плановости или документу больше не обнуляет процент простоя и MTBF: он отбирает только строки обслуживания, фонд времени и наработка станка остаются. Отбор по часам и показателям не применяется — отчёт сообщает об этом; отбор по станку работает как раньше.
- Обслуживание станка с окончанием не позже начала не проводится и при записи обработками, а не только из формы.

### fr
- Le rapport « Arrêts des machines » avec « Inclure le planifié » ne compte plus deux fois le temps où une machine a à la fois une maintenance planifiée et une maintenance réelle : la planifiée n'est comptée qu'en dehors de la réelle, le pourcentage d'arrêt ne dépasse donc plus la capacité.
- Le temps de réparation (MTTR) est compté sur toute la durée de la réparation, même si elle dépasse la fin de la période du rapport. Auparavant, seule la partie dans la période entrait dans le MTTR.
- Une machine retirée apparaît dans le rapport si elle a travaillé dans la période : ses heures de fonctionnement entrent dans le MTBF. Auparavant, une telle machine sans maintenance n'apparaissait pas.
- Le filtre du rapport par type de maintenance, motif, caractère planifié ou document ne met plus à zéro le pourcentage d'arrêt et le MTBF : il ne sélectionne que les lignes de maintenance, la capacité et les heures de fonctionnement de la machine restent. Le filtre par heures et indicateurs n'est pas appliqué, le rapport le signale ; le filtre par machine fonctionne comme avant.
- Une maintenance de machine dont la fin n'est pas postérieure au début n'est plus validée non plus lorsqu'elle est enregistrée par un traitement, et pas seulement depuis le formulaire.

### en
- The "Machine downtime" report with "Include planned" no longer counts twice the time when a machine has both planned and actual maintenance: planned maintenance is counted only outside the actual one, so the downtime percentage no longer exceeds capacity.
- Repair time (MTTR) is calculated over the full duration of the repair, even if the repair runs past the end of the report period. Previously only the part inside the period went into MTTR.
- A retired machine appears in the report if it worked during the period: its operating hours count towards MTBF. Previously such a machine without maintenance did not appear.
- Filtering the report by maintenance type, reason, planned flag or document no longer zeroes the downtime percentage and MTBF: it selects only maintenance rows, and machine capacity and operating hours remain. Filtering by hours and indicators is not applied, and the report says so; filtering by machine works as before.
- Machine maintenance whose end is not later than its start is no longer posted when saved by a data processor either, not only from the form.

### es
- El informe «Paradas de máquinas» con «Incluir lo planificado» ya no cuenta dos veces el tiempo en que una máquina tiene a la vez mantenimiento planificado y real: el planificado se cuenta solo fuera del real, por lo que el porcentaje de parada ya no supera la capacidad.
- El tiempo de reparación (MTTR) se calcula con la duración completa de la reparación, aunque pase del final del período del informe. Antes solo entraba en el MTTR la parte dentro del período.
- Una máquina fuera de servicio aparece en el informe si trabajó en el período: sus horas de funcionamiento entran en el MTBF. Antes esa máquina sin mantenimiento no aparecía.
- El filtro del informe por tipo de mantenimiento, motivo, carácter planificado o documento ya no pone a cero el porcentaje de parada y el MTBF: solo selecciona las filas de mantenimiento, y la capacidad y las horas de funcionamiento de la máquina se mantienen. El filtro por horas e indicadores no se aplica y el informe lo indica; el filtro por máquina funciona como antes.
- El mantenimiento de una máquina cuyo fin no es posterior al inicio ya no se contabiliza tampoco al guardarlo con un procesamiento, no solo desde el formulario.

## 2.0.16.54
### ru
- Списание и оприходование, введённые на основании пересчёта «По станку», работают со складом этого пересчёта. Раньше, если после пересчёта в карточке станка сменили склад станка, документ при записи подставлял новый склад, и недостача или излишек проводились не на том складе, где их нашли. Сменить у такого документа станок или вид операции нельзя: запись откажет с подсказкой.

### fr
- Les sorties et entrées de stock créées à partir d'un inventaire « Par machine » utilisent le stock de cet inventaire. Auparavant, si le stock de la machine avait été changé dans sa fiche après l'inventaire, le document prenait le nouveau stock à l'enregistrement, et le manquant ou l'excédent était passé sur un autre stock que celui où il avait été constaté. La machine et le type d'opération d'un tel document ne peuvent plus être changés : l'enregistrement est refusé avec une explication.

### en
- Write-offs and receipts created from a "By machine" stock count use the stock of that count. Previously, if the machine stock was changed on the machine card after the count, the document took the new stock when saved, and the shortage or surplus was posted to a different stock from where it was found. The machine and operation type of such a document can no longer be changed: saving is refused with an explanation.

### es
- Las bajas y altas de existencias creadas a partir de un recuento «Por máquina» usan el almacén de ese recuento. Antes, si después del recuento se cambiaba el almacén de la máquina en su ficha, el documento tomaba el almacén nuevo al guardarse, y el faltante o el sobrante se registraba en un almacén distinto de aquel donde se encontró. Ya no se puede cambiar la máquina ni el tipo de operación de ese documento: el guardado se rechaza con una explicación.

## 2.0.16.53
### ru
- Списание безналичных денежных средств, созданное не из формы (обработкой, обменом, на основании в коде), больше не останавливается на проверке «Сумма в валюте регл учета не заполнена»: эту сумму документ сам пересчитывает из суммы и курса при записи, как остальные платёжные документы.

### fr
- Une sortie de fonds bancaire créée hors du formulaire (traitement, échange, saisie par code) ne bloque plus sur le contrôle « Montant en devise comptable non renseigné » : le document recalcule lui-même ce montant à partir du montant et du cours à l'enregistrement, comme les autres documents de paiement.

### en
- A bank payment created outside its form (by a data processor, exchange or code) no longer stops at the "Amount in accounting currency is not filled" check: the document recalculates this amount from the amount and rate when saved, like the other payment documents.

### es
- Un pago bancario creado fuera de su formulario (por un procesamiento, intercambio o código) ya no se detiene en la comprobación «Importe en moneda contable no rellenado»: el documento recalcula este importe a partir del importe y el tipo de cambio al guardarse, como los demás documentos de pago.

## 2.0.16.52
### ru
- В рабочем месте «Управление станками» появилась закладка «Загрузка»: по каждому станку на две недели от выбранной — фонд, занято (работа и обслуживание), свободно, процент занятости и первое свободное окно не короче заданного (поле «Окно не короче, ч» рядом с неделей). Колонки дней раскрашены: зелёный — есть запас, жёлтый — от 85 %, розовый — 100 % и выше, серый — выходной; станок, занятый на 90 % и больше, выделен полужирным. Внизу — свободные часы каждого дня по всем станкам. Щелчок по станку делает его текущим в списке станков.
- Закладка «Под риском»: заказы, которые не успевают к дате отгрузки, — по уже запланированной работе (в том числе затянувшейся), по запланированной, но не запущенной вовремя, и по черновику автоплана; работа на выведенном станке — с подсказкой перепланировать. Черновик автоплана — оценка: другое размещение может успеть. Справа — нужные и свободные часы станков до каждой даты отгрузки и нехватка часов. Закладка считается при открытии и по кнопке «Пересчитать».
- Новый отчёт «План загрузки станков» (Производство → Станки): вариант «По дням» — процент занятости и свободные часы каждого станка по дням периода, вариант «Заказы под риском». Из закладки «Загрузка» подменю «Отчёты» открывает его и отчёты «Загрузка станков», «Простои станков» (с плановым обслуживанием) и «Занятость станков» на период закладки и выбранный станок.

### fr
- Le poste « Gestion des machines » a un nouvel onglet « Charge » : pour chaque machine, sur deux semaines à partir de la semaine choisie — capacité, occupé (travail et maintenance), libre, pourcentage d'occupation et premier créneau libre d'au moins la durée indiquée (champ « Créneau d'au moins, h » à côté de la semaine). Les colonnes des jours sont colorées : vert — marge, jaune — dès 85 %, rose — 100 % et plus, gris — jour de repos ; une machine occupée à 90 % et plus est en gras. En bas — les heures libres de chaque jour pour toutes les machines. Un clic sur une machine la rend courante dans la liste des machines.
- Onglet « À risque » : commandes qui ne tiennent pas la date d'expédition — selon les travaux déjà planifiés (y compris en retard d'exécution), les travaux planifiés mais non lancés à temps et le brouillon de planification automatique ; un travail sur une machine retirée est signalé à replanifier. Le brouillon est une estimation : un autre placement peut tenir le délai. À droite — heures nécessaires et libres des machines jusqu'à chaque date d'expédition et heures manquantes. L'onglet se calcule à l'ouverture et par le bouton « Recalculer ».
- Nouveau rapport « Plan de charge des machines » (Production → Machines) : variante « Par jour » — pourcentage d'occupation et heures libres de chaque machine par jour de la période, variante « Commandes à risque ». Depuis l'onglet « Charge », le sous-menu « Rapports » l'ouvre, ainsi que « Charge des machines », « Arrêts des machines » (avec maintenance prévue) et « Occupation des machines », sur la période de l'onglet et la machine choisie.

### en
- The "Machine management" workplace has a new "Load" tab: for each machine, for two weeks from the selected week — capacity, busy (work and maintenance), free, busy percentage and the first free slot of at least the given length ("Slot of at least, h" field next to the week). Day columns are coloured: green — spare capacity, yellow — from 85 %, pink — 100 % and above, grey — day off; a machine busy 90 % or more is shown in bold. At the bottom — free hours of each day across all machines. Clicking a machine makes it current in the machine list.
- "At risk" tab: orders that will not make their shipment date — by work already scheduled (including work running late), by work scheduled but not started on time and by the auto-plan draft; work on a retired machine is flagged for rescheduling. The draft is an estimate: another placement may be in time. On the right — needed and free machine hours up to each shipment date and the shortfall. The tab is calculated when opened and with the "Recalculate" button.
- New report "Machine load plan" (Production → Machines): "By day" variant — busy percentage and free hours of each machine by day of the period, and the "Orders at risk" variant. From the "Load" tab, the "Reports" submenu opens it as well as "Machine load", "Machine downtime" (with planned maintenance) and "Machine occupancy" for the tab's period and the selected machine.

### es
- El puesto «Gestión de máquinas» tiene una nueva pestaña «Carga»: para cada máquina, en dos semanas desde la semana elegida — capacidad, ocupado (trabajo y mantenimiento), libre, porcentaje de ocupación y primer hueco libre de al menos la duración indicada (campo «Hueco de al menos, h» junto a la semana). Las columnas de los días están coloreadas: verde — hay margen, amarillo — desde 85 %, rosa — 100 % o más, gris — día de descanso; una máquina ocupada al 90 % o más aparece en negrita. Abajo — las horas libres de cada día de todas las máquinas. Un clic en una máquina la hace actual en la lista de máquinas.
- Pestaña «En riesgo»: pedidos que no llegan a la fecha de envío — por el trabajo ya planificado (incluido el que se retrasa), por el trabajo planificado pero no iniciado a tiempo y por el borrador de planificación automática; el trabajo en una máquina fuera de servicio se señala para replanificar. El borrador es una estimación: otra ubicación puede llegar a tiempo. A la derecha — horas necesarias y libres de las máquinas hasta cada fecha de envío y horas que faltan. La pestaña se calcula al abrirla y con el botón «Recalcular».
- Nuevo informe «Plan de carga de máquinas» (Producción → Máquinas): variante «Por días» — porcentaje de ocupación y horas libres de cada máquina por día del período, y variante «Pedidos en riesgo». Desde la pestaña «Carga», el submenú «Informes» lo abre, así como «Carga de máquinas», «Paradas de máquinas» (con mantenimiento previsto) y «Ocupación de máquinas», para el período de la pestaña y la máquina elegida.

## 2.0.16.51
### ru
- Исправлена печать коммерческого предложения: в сборке 2.0.16.50 она останавливалась с ошибкой «Поле объекта не обнаружено (Номер)», а шрифты, выравнивание и ширина колонок формы были сбиты.
- Кнопка печати коммерческого предложения появилась у ролей «Оператор» и «Менеджер по продажам»: в сборке 2.0.16.50 её видели только руководитель и администратор. Цены, суммы и количества на печати оформляются по правилам выбранного языка.
- Коммерческое предложение с отправленными редакциями снова удаляется: в сборке 2.0.16.50 удаление отказывало с сообщением «Редакции коммерческого предложения записывает только сам документ». Редакции удаляются вместе с предложением.
- Печать коммерческого предложения полностью выходит на языке, выбранном в окне печати: сумма прописью, пометка редакции, условия, подпись договора и даты. Раньше у отправленной редакции сумма прописью оставалась на языке, на котором предложение записали. Редакции, записанные до этого обновления, печатают сумму прописью и договор по-прежнему на языке записи. По-испански сумма прописью пока выходит по-французски, как и во всех печатных формах.
- Смена ответственного у отправленного предложения теперь тоже даёт новую редакцию: когда менеджер не указан, на печати стоит ответственный.

### fr
- Correction de l'impression du devis : dans la version 2.0.16.50, elle s'arrêtait sur l'erreur « Champ d'objet introuvable (Номер) », et les polices, l'alignement et la largeur des colonnes étaient décalés.
- Le bouton d'impression du devis est disponible pour les rôles « Opérateur » et « Commercial » : dans la version 2.0.16.50, seuls le directeur et l'administrateur le voyaient. Prix, montants et quantités s'impriment selon les règles de la langue choisie.
- Un devis ayant des révisions envoyées peut de nouveau être supprimé : dans la version 2.0.16.50, la suppression échouait avec le message « Seul le devis lui-même enregistre ses révisions ». Les révisions sont supprimées avec le devis.
- L'impression du devis sort entièrement dans la langue choisie dans la fenêtre d'impression : montant en lettres, mention de révision, conditions, libellé du contrat et dates. Auparavant, pour une révision envoyée, le montant en lettres restait dans la langue d'enregistrement du devis. Les révisions enregistrées avant cette mise à jour gardent le montant en lettres et le contrat dans la langue d'enregistrement. En espagnol, le montant en lettres sort encore en français, comme dans tous les formulaires imprimables.
- Changer le responsable d'un devis envoyé crée désormais aussi une nouvelle révision : quand le contact n'est pas renseigné, c'est le responsable qui figure à l'impression.

### en
- Fixed quotation printing: in build 2.0.16.50 it stopped with the error "Object field not found (Номер)", and the fonts, alignment and column widths of the form were off.
- The quotation print button is now available to the "Operator" and "Sales manager" roles: in build 2.0.16.50 only the director and the administrator saw it. Prices, amounts and quantities are printed according to the chosen language.
- A quotation with sent revisions can be deleted again: in build 2.0.16.50 deletion failed with "Only the quotation itself writes its revisions". The revisions are deleted together with the quotation.
- The quotation now prints entirely in the language chosen in the print window: amount in words, revision label, terms, contract label and dates. Previously a sent revision kept the amount in words in the language the quotation was saved in. Revisions saved before this update still print the amount in words and the contract in the language they were saved in. In Spanish the amount in words is still printed in French, as in all print forms.
- Changing the person responsible for a sent quotation now also creates a new revision: when no manager is set, the responsible person is printed instead.

### es
- Corregida la impresión del presupuesto: en la versión 2.0.16.50 se detenía con el error «Campo del objeto no encontrado (Номер)», y las fuentes, la alineación y el ancho de las columnas estaban desajustados.
- El botón de impresión del presupuesto está disponible para los roles «Operador» y «Gestor de ventas»: en la versión 2.0.16.50 solo lo veían el director y el administrador. Precios, importes y cantidades se imprimen según el idioma elegido.
- Un presupuesto con revisiones enviadas vuelve a poder eliminarse: en la versión 2.0.16.50 la eliminación fallaba con «Solo el propio presupuesto registra sus revisiones». Las revisiones se eliminan junto con el presupuesto.
- El presupuesto se imprime por completo en el idioma elegido en la ventana de impresión: importe en letras, marca de revisión, condiciones, etiqueta del contrato y fechas. Antes, en una revisión enviada el importe en letras quedaba en el idioma en que se guardó el presupuesto. Las revisiones guardadas antes de esta actualización siguen imprimiendo el importe en letras y el contrato en el idioma en que se guardaron. En español, el importe en letras todavía sale en francés, como en todos los formularios de impresión.
- Cambiar el responsable de un presupuesto enviado ahora también crea una nueva revisión: si no se indica el gestor, en la impresión figura el responsable.

## 2.0.16.50
### ru
- Новая печатная форма «Коммерческое предложение» (кнопка «Печать» в документе и в списке): логотип организации из её карточки, реквизиты организации, блоки «Клиент» и «Ваш менеджер», таблица с описанием под каждой строкой, итоги без НДС, НДС и к оплате, сумма прописью, условия, подпись и печать организации, реквизиты в подвале каждой страницы. Форма печатается на русском, французском, английском и испанском.
- У коммерческого предложения появились редакции. Пока предложение в черновике, его можно править сколько угодно. Когда предложение в статусе «Отправлен» (и дальше) записывается с изменениями, номер редакции растёт сам: v1, v2, v3. Смена только статуса новой редакции не создаёт.
- В шапке предложения — ссылка «Редакция v…» с подсказкой, что будет при записи. По щелчку — список отправленных редакций с датой, суммой и автором; выбранная открывается на просмотр ровно в том виде, в каком ушла клиенту (те же наименования, цены и логотип, даже если их потом изменили), её можно перепечатать.
- Кнопка «Вернуть эту редакцию» переносит содержимое старой редакции в текущее предложение; номер документа остаётся прежним, при записи появляется новая редакция. Если какой-то товар из старой редакции уже удалён из базы, строка возвращается без него, а программа называет, чего не нашла.
- На печати отправленное предложение помечено «Редакция v2»; правки после отправки печатаются как «Редакция v3 · черновик». Предложения, отправленные до этого обновления, получают редакцию v1 при первой записи — сохраняется то, что видел клиент.
- Прежняя печать «Коммерческое предложение (A4)» в формате Devis у документа «Коммерческое предложение» убрана: она печатала без учёта редакций. У заказов клиента и реализаций печать Devis осталась.

### fr
- Nouveau formulaire imprimable « Devis » (bouton « Imprimer » dans le document et dans la liste) : logo de l'organisation tiré de sa fiche, coordonnées de l'organisation, blocs « Client » et « Votre contact », tableau avec la description sous chaque ligne, totaux HT, TVA et à payer, montant en lettres, conditions, signature et cachet de l'organisation, coordonnées en pied de chaque page. Le formulaire s'imprime en russe, français, anglais et espagnol.
- Le devis a désormais des révisions. Tant qu'il est en brouillon, on peut le modifier librement. Lorsqu'un devis au statut « Envoyé » (ou suivant) est enregistré avec des modifications, le numéro de révision augmente tout seul : v1, v2, v3. Un simple changement de statut ne crée pas de nouvelle révision.
- Dans l'en-tête du devis, un lien « Révision v… » indique ce qui se passera à l'enregistrement. Un clic ouvre la liste des révisions envoyées avec date, montant et auteur ; celle choisie s'ouvre en lecture telle qu'elle a été envoyée au client (mêmes désignations, prix et logo, même s'ils ont changé depuis) et peut être réimprimée.
- Le bouton « Restaurer cette révision » reprend le contenu de l'ancienne révision dans le devis actuel ; le numéro du document ne change pas, une nouvelle révision apparaît à l'enregistrement. Si un article de l'ancienne révision a été supprimé de la base, la ligne revient sans lui et le programme indique ce qu'il n'a pas trouvé.
- À l'impression, un devis envoyé porte la mention « Révision v2 » ; les modifications après envoi s'impriment comme « Révision v3 · brouillon ». Les devis envoyés avant cette mise à jour reçoivent la révision v1 au premier enregistrement — ce que le client a vu est conservé.
- L'ancienne impression « Devis (A4) » du document « Devis » est retirée : elle imprimait sans tenir compte des révisions. Les commandes client et les ventes gardent l'impression Devis.

### en
- New "Quotation" print form ("Print" button in the document and in the list): the organization logo from its card, organization details, "Customer" and "Your contact" blocks, a table with the description under each line, totals excluding VAT, VAT and amount due, amount in words, terms, signature and organization stamp, details in the footer of every page. The form prints in Russian, French, English and Spanish.
- Quotations now have revisions. While a quotation is a draft, it can be edited freely. When a quotation with the "Sent" status (or later) is written with changes, the revision number goes up by itself: v1, v2, v3. Changing only the status does not create a new revision.
- The quotation header shows a "Revision v…" link that tells what will happen on write. Clicking it lists the sent revisions with date, amount and author; the chosen one opens read-only exactly as it was sent to the customer (same names, prices and logo, even if they changed later) and can be reprinted.
- The "Restore this revision" button brings the content of an old revision into the current quotation; the document number stays the same and a new revision appears on write. If an item from the old revision has since been deleted, the line comes back without it and the program names what it could not find.
- When printed, a sent quotation is marked "Revision v2"; changes after sending print as "Revision v3 · draft". Quotations sent before this update get revision v1 on their first write — what the customer saw is kept.
- The old "Quotation (A4)" Devis-style print of the "Quotation" document is removed: it printed without regard to revisions. Customer orders and sales keep the Devis print.

### es
- Nuevo formulario impreso «Presupuesto» (botón «Imprimir» en el documento y en la lista): logotipo de la organización de su ficha, datos de la organización, bloques «Cliente» y «Su contacto», tabla con la descripción bajo cada línea, totales sin IVA, IVA y a pagar, importe en letras, condiciones, firma y sello de la organización, datos en el pie de cada página. El formulario se imprime en ruso, francés, inglés y español.
- El presupuesto ahora tiene revisiones. Mientras es un borrador, se puede editar libremente. Cuando un presupuesto con estado «Enviado» (o posterior) se graba con cambios, el número de revisión sube solo: v1, v2, v3. Cambiar solo el estado no crea una revisión nueva.
- En la cabecera del presupuesto hay un enlace «Revisión v…» que indica qué pasará al grabar. Al pulsarlo aparece la lista de revisiones enviadas con fecha, importe y autor; la elegida se abre en modo lectura tal como se envió al cliente (mismos nombres, precios y logotipo, aunque hayan cambiado después) y se puede reimprimir.
- El botón «Restaurar esta revisión» trae el contenido de la revisión antigua al presupuesto actual; el número del documento no cambia y al grabar aparece una revisión nueva. Si un artículo de la revisión antigua ya se eliminó de la base, la línea vuelve sin él y el programa indica qué no encontró.
- Al imprimir, un presupuesto enviado lleva la marca «Revisión v2»; los cambios después del envío se imprimen como «Revisión v3 · borrador». Los presupuestos enviados antes de esta actualización reciben la revisión v1 en su primera grabación: se conserva lo que vio el cliente.
- Se retira la impresión anterior «Presupuesto (A4)» de tipo Devis del documento «Presupuesto»: imprimía sin tener en cuenta las revisiones. Los pedidos de cliente y las ventas conservan la impresión Devis.

## 2.0.16.49
### ru
- Станки получили своё рабочее место: «Производство → Управление станками» (в верхней группе раздела и в группе «Станки»). В нём всё, что было на закладке «Станки» рабочего места производства: список станков, планировщик недели, «Готовы к запуску», требования и автоплан. Закладки «Станки» в рабочем месте производства больше нет.
- Кнопки рабочего места станков — неделя, «Разместить», «Запустить», «Завершить», «Отменить», автоплан, обслуживание и «Обновить» — стоят в панели над списком станков и выглядят так же, как «Статус» и «Потребности» над списком продукции: обычного размера, без разъехавшегося шрифта. Форма помещается на экран без вертикальной прокрутки.
- Если учёт станков выключен, пункта «Управление станками» в меню нет; открытое по ссылке рабочее место объясняет, почему оно пустое.

### fr
- Les machines ont leur propre poste : « Production → Gestion des machines » (dans le groupe principal de la section et dans le groupe « Machines »). On y retrouve tout ce qui était dans l'onglet « Machines » du poste de production : liste des machines, planificateur de la semaine, « Prêts à lancer », bons de sortie et planification automatique. L'onglet « Machines » du poste de production n'existe plus.
- Les boutons du poste des machines — semaine, « Planifier », « Lancer », « Terminer », « Annuler », planification automatique, maintenance et « Actualiser » — sont dans la barre au-dessus de la liste des machines et ont le même aspect que « Statut » et « Besoins » au-dessus de la liste des produits : taille normale, police non étirée. Le formulaire tient à l'écran sans défilement vertical.
- Si la gestion des machines est désactivée, l'élément « Gestion des machines » n'apparaît pas dans le menu ; ouvert par un lien, le poste explique pourquoi il est vide.

### en
- Machines now have their own workplace: "Production → Machine management" (in the top group of the section and in the "Machines" group). It holds everything that was on the "Machines" tab of the production workplace: machine list, weekly planner, "Ready to start", requisitions and auto-plan. The production workplace no longer has a "Machines" tab.
- The machine workplace buttons — week, "Place", "Start", "Complete", "Cancel", auto-plan, maintenance and "Refresh" — are in the bar above the machine list and look the same as "Status" and "Requirements" above the product list: normal size, no stretched font. The form fits on the screen without vertical scrolling.
- When machine tracking is off, the "Machine management" menu item is not shown; opened from a link, the workplace explains why it is empty.

### es
- Las máquinas tienen su propio puesto: «Producción → Gestión de máquinas» (en el grupo principal de la sección y en el grupo «Máquinas»). Contiene todo lo que estaba en la pestaña «Máquinas» del puesto de producción: lista de máquinas, planificador de la semana, «Listos para iniciar», vales y plan automático. El puesto de producción ya no tiene la pestaña «Máquinas».
- Los botones del puesto de máquinas — semana, «Planificar», «Iniciar», «Terminar», «Cancelar», plan automático, mantenimiento y «Actualizar» — están en la barra sobre la lista de máquinas y se ven igual que «Estado» y «Necesidades» sobre la lista de productos: tamaño normal, sin la fuente separada. El formulario cabe en la pantalla sin desplazamiento vertical.
- Si el control de máquinas está desactivado, el punto «Gestión de máquinas» no aparece en el menú; abierto por un enlace, el puesto explica por qué está vacío.

## 2.0.16.48
### ru
- «Заполнить демо-данными»: флажков опций больше нет — заполняется то, что включено в функциональных опциях. Блок учёта станков добавляется, если учёт станков включён; сами опции кнопка не включает.
- Кнопки «Заполнить демо-данными» и «Создать свойства номенклатуры» в «Компания и учёт» — обычным шрифтом, надпись больше не разъезжается на macOS.

### fr
- « Remplir avec des données de démonstration » : plus de cases à cocher pour les options — seul ce qui est activé dans les options fonctionnelles est rempli. Le bloc de suivi des machines est ajouté si le suivi des machines est activé ; le bouton n'active pas les options lui-même.
- Les boutons « Remplir avec des données de démonstration » et « Créer les propriétés des articles » de « Entreprise et comptabilité » utilisent la police normale, le libellé ne s'étale plus sur macOS.

### en
- "Fill with demo data": no more option checkboxes — only what is turned on in the functional options is filled. The machine tracking block is added when machine tracking is on; the button does not turn options on by itself.
- The "Fill with demo data" and "Create item properties" buttons in "Company and accounting" use the normal font; the caption no longer spreads out on macOS.

### es
- «Llenar con datos de demostración»: ya no hay casillas de opciones — solo se llena lo activado en las opciones funcionales. El bloque de control de máquinas se añade si el control de máquinas está activado; el botón no activa las opciones por sí mismo.
- Los botones «Llenar con datos de demostración» y «Crear propiedades de artículos» de «Empresa y contabilidad» usan la fuente normal; el texto ya no se separa en macOS.

## 2.0.16.47
### ru
- Настройка → Параметры → Компания и учёт: для администратора — группа «Демо-данные» с кнопкой «Заполнить демо-данными». Она заводит демонстрационный набор (заказы на производство на каждой стадии, коммерческие предложения, продажи, закупки, возвраты, оплаты, договоры, лиды, заявки) в фоне и по окончании показывает, что создано, что уже было, что пропущено и почему. Перед запуском — подтверждение; флажками можно включить нужные опции (производство, автовыпуск при отгрузке, учёт станков).
- Кнопка работает только в демонстрационной или тестовой базе: если в базе есть рабочие документы, заполнение отказывает и называет такой документ (вид, номер, дата) — ничего не записывается.
- Повторное нажатие ничего не дублирует: уже заведённые справочники и документы набора находятся и переиспользуются, недостающие части набора доливаются целиком. Если часть документов какого-то примера удалена вручную, пример помечается «неполным» и не трогается.
- Новый блок «Учёт станков» (флажок «Добавить блок учёта станков»): три станка, требования-накладные во всех состояниях (запланировано, запущено, завершено, отменено), плановое и аварийное обслуживание, инвентаризация и оприходование материалов на станке. После заполнения все отчёты по станкам и закладка «Станки» рабочего места производства показывают данные. Факт кладётся в последние три завершённые смены станка; если часть пришлась на прошлый месяц, в отчётах выберите период шире «Этого месяца».

### fr
- Paramétrage → Paramètres → Entreprise et comptabilité : pour l'administrateur, un groupe « Données de démonstration » avec le bouton « Remplir avec des données de démonstration ». Il crée en arrière-plan un jeu de démonstration (commandes de production à chaque étape, devis, ventes, achats, retours, paiements, contrats, prospects, demandes de recherche) et affiche à la fin ce qui a été créé, ce qui existait déjà, ce qui a été ignoré et pourquoi. Une confirmation précède le lancement ; des cases permettent d'activer les options nécessaires (production, production automatique à l'expédition, suivi des machines).
- Le bouton ne fonctionne que dans une base de démonstration ou de test : si la base contient des documents de travail, le remplissage est refusé et indique un tel document (type, numéro, date) — rien n'est écrit.
- Un nouveau clic ne duplique rien : les référentiels et documents du jeu déjà créés sont retrouvés et réutilisés, les parties manquantes sont ajoutées en entier. Si une partie des documents d'un exemple a été supprimée à la main, l'exemple est marqué « incomplet » et n'est pas modifié.
- Nouveau bloc « Suivi des machines » (case « Ajouter le bloc de suivi des machines ») : trois machines, bons de consommation dans tous les états (planifié, lancé, terminé, annulé), maintenance planifiée et panne, inventaire et entrée de matières sur la machine. Après le remplissage, tous les rapports machines et l'onglet « Machines » du poste de production ont des données. Le réalisé est placé dans les trois dernières équipes terminées ; s'il tombe en partie le mois précédent, choisissez dans les rapports une période plus large que « Ce mois ».

### en
- Settings → Parameters → Company and accounting: for the administrator, a "Demo data" group with the "Fill with demo data" button. It creates a demo set in the background (production orders at every stage, quotations, sales, purchases, returns, payments, contracts, leads, search requests) and at the end shows what was created, what already existed, what was skipped and why. A confirmation comes first; check boxes turn on the options needed (production, automatic output on shipment, machine tracking).
- The button works only in a demo or test infobase: if the infobase has working documents, filling is refused and names such a document (type, number, date) — nothing is written.
- Pressing it again duplicates nothing: catalogs and documents of the set already created are found and reused, missing parts of the set are added as a whole. If some documents of an example were deleted by hand, the example is marked "incomplete" and left untouched.
- New "Machine tracking" block ("Add the machine tracking block" check box): three machines, requisitions in all states (planned, started, completed, cancelled), planned maintenance and a breakdown, stocktaking and materials receipt on a machine. After filling, all machine reports and the "Machines" tab of the production workplace show data. Actuals go into the last three finished shifts of the machine; if part of them falls into the previous month, choose a period wider than "This month" in reports.

### es
- Configuración → Parámetros → Empresa y contabilidad: para el administrador, un grupo «Datos de demostración» con el botón «Llenar con datos de demostración». Crea en segundo plano un conjunto de demostración (pedidos de producción en cada etapa, presupuestos, ventas, compras, devoluciones, pagos, contratos, clientes potenciales, solicitudes de búsqueda) y al terminar muestra qué se creó, qué ya existía, qué se omitió y por qué. Antes se pide confirmación; las casillas activan las opciones necesarias (producción, producción automática al enviar, control de máquinas).
- El botón solo funciona en una base de demostración o de prueba: si la base tiene documentos de trabajo, el llenado se rechaza e indica uno de ellos (tipo, número, fecha) — no se escribe nada.
- Pulsarlo de nuevo no duplica nada: los catálogos y documentos del conjunto ya creados se encuentran y se reutilizan, las partes que faltan se añaden completas. Si parte de los documentos de un ejemplo se eliminó a mano, el ejemplo se marca «incompleto» y no se toca.
- Nuevo bloque «Control de máquinas» (casilla «Añadir el bloque de control de máquinas»): tres máquinas, vales en todos los estados (planificado, iniciado, terminado, cancelado), mantenimiento planificado y avería, inventario y entrada de materiales en la máquina. Tras el llenado, todos los informes de máquinas y la pestaña «Máquinas» del puesto de producción muestran datos. Lo real se coloca en los tres últimos turnos terminados de la máquina; si una parte cae en el mes anterior, elija en los informes un periodo más amplio que «Este mes».

## 2.0.16.46
### ru
- Учёт станков: в карточке станка появилась таблица «Выработка по номенклатуре» — своя выработка, кг/ч, для продукции или материала. Время загрузки на закладке «Станки», «Готовы к запуску», автоплан и норма в отчётах «Выработка станков» и «Эффективность станков» считаются по ней: сначала по норме продукции, иначе по нормам материалов (каждый материал — по своей норме), а где строки нет — по общей выработке станка, как раньше. Уже запланированная загрузка получит новое время, когда её требование будет записано или перенесено, — так же, как при изменении общей выработки.

### fr
- Gestion des machines : la fiche machine comporte un tableau « Cadence par article » — une cadence propre, en kg/h, pour un produit ou une matière. La durée de charge de l'onglet « Machines », « Prêts au lancement », la planification automatique et la norme des rapports « Rendement des machines » et « Efficacité des machines » l'utilisent : d'abord la cadence du produit, sinon celles des matières (chaque matière à sa cadence), et sans ligne — la cadence générale de la machine, comme avant. Une charge déjà planifiée prend la nouvelle durée quand son bon est enregistré ou déplacé — comme lors d'un changement de la cadence générale.

### en
- Machine tracking: the machine card has a new "Output rate by item" table — its own output, kg/h, for a product or a material. The load time on the "Machines" tab, "Ready to start", auto-plan and the standard in the "Machine output" and "Machine efficiency" reports use it: first the product's rate, otherwise the materials' rates (each material at its own rate), and without a line — the machine's general output, as before. A load already planned gets the new time when its requisition is saved or moved — the same as when the general output changes.

### es
- Control de máquinas: la ficha de la máquina tiene la tabla «Rendimiento por artículo» — un rendimiento propio, kg/h, para un producto o un material. El tiempo de carga de la pestaña «Máquinas», «Listos para iniciar», el plan automático y la norma de los informes «Producción de máquinas» y «Eficiencia de máquinas» lo usan: primero el del producto, si no, los de los materiales (cada material a su rendimiento), y sin línea — el rendimiento general de la máquina, como antes. Una carga ya planificada recibe el nuevo tiempo cuando su vale se guarda o se traslada — igual que al cambiar el rendimiento general.

## 2.0.16.45
### ru
- Рабочее место производства, закладка «Станки»: закладка помещается на экран без вертикальной прокрутки и больше не растягивает остальные закладки. Список станков, планировщик и нижние таблицы стали ниже и растягиваются на свободное место. Кнопки собраны в одну панель по группам: неделя, действия с загрузками, автоплан, обслуживание и обновление. Правая панель фильтров заказов на этой закладке скрыта — к станкам она не относится.

### fr
- Poste de production, onglet « Machines » : l'onglet tient à l'écran sans défilement vertical et n'agrandit plus les autres onglets. La liste des machines, le planificateur et les tableaux du bas sont moins hauts et s'étirent sur l'espace libre. Les boutons sont réunis dans une seule barre, par groupes : semaine, actions sur les charges, planification automatique, maintenance et actualisation. Le panneau de droite avec les filtres des commandes est masqué sur cet onglet — il ne concerne pas les machines.

### en
- Production workplace, "Machines" tab: the tab fits on the screen without vertical scrolling and no longer stretches the other tabs. The machine list, the planner and the lower tables are shorter and stretch to fill the free space. The buttons are gathered in one bar by group: week, load actions, auto-plan, maintenance and refresh. The right-hand panel with order filters is hidden on this tab — it does not apply to machines.

### es
- Puesto de producción, pestaña «Máquinas»: la pestaña cabe en la pantalla sin desplazamiento vertical y ya no alarga las demás pestañas. La lista de máquinas, el planificador y las tablas inferiores son más bajos y se estiran al espacio libre. Los botones están reunidos en una sola barra por grupos: semana, acciones con cargas, plan automático, mantenimiento y actualizar. El panel derecho con los filtros de pedidos se oculta en esta pestaña — no se aplica a las máquinas.

## 2.0.16.44
### ru
- Меню «Производство»: всё, что относится к станкам, собрано в группе «Станки» — справочник станков, обслуживание станков, требования-накладные, инвентаризация, оприходование и списание материалов и все отчёты по станкам. Из верхней группы раздела обслуживание станков и требования-накладные убраны.
- Если учёт станков выключен, станков в программе не видно: справочник «Станки» пропал из меню, а поле «Оборудование» — из выпуска продукции. Уже заполненные данные сохраняются и появятся снова при включении учёта.
- Главные документы раздела теперь есть и в своих тематических группах: заказы, продажи и возвраты покупателей — в «Продажи / Опт», доп. расходы на поступление — в «Закупки / Импорт», формирование заказов поставщикам — в «Закупки / Планирование», кассовые документы — в «Казначейство / Касса», безналичные платежи — в «Казначейство / Банк», перемещение товаров — в «Склад / Хранение», печать этикеток — в «Склад / Товары».

### fr
- Menu « Production » : tout ce qui concerne les machines est regroupé dans « Machines » — le référentiel des machines, la maintenance, les bons de sortie, l'inventaire, l'entrée et la sortie de matières et tous les rapports sur les machines. La maintenance et les bons de sortie ne figurent plus dans le groupe principal de la section.
- Si la gestion des machines est désactivée, les machines n'apparaissent plus : le référentiel « Machines » disparaît du menu et le champ « Équipement » de la production. Les données déjà saisies sont conservées et réapparaissent à la réactivation.
- Les documents principaux de chaque section figurent aussi dans leur groupe thématique : commandes, ventes et retours clients dans « Ventes / Gros », frais additionnels de réception dans « Achats / Importation », formation des commandes fournisseurs dans « Achats / Planification », documents de caisse dans « Trésorerie / Caisse », paiements bancaires dans « Trésorerie / Banque », transferts dans « Entrepôt / Stockage », impression d'étiquettes dans « Entrepôt / Articles ».

### en
- "Production" menu: everything about machines is gathered in the "Machines" group — the machine list, maintenance, material requisitions, stocktaking, material receipt and write-off, and all machine reports. Maintenance and material requisitions are no longer in the top group of the section.
- When machine tracking is off, machines are no longer shown: the "Machines" list is gone from the menu and the "Equipment" field from production output. Data already entered is kept and comes back when tracking is turned on again.
- The main documents of each section are now also in their topic groups: customer orders, sales and returns in "Sales / Wholesale", additional receipt costs in "Purchases / Import", supplier order generation in "Purchases / Planning", cash documents in "Treasury / Cash", bank payments in "Treasury / Bank", transfers in "Warehouse / Storage", label printing in "Warehouse / Goods".

### es
- Menú «Producción»: todo lo relativo a las máquinas está reunido en el grupo «Máquinas» — el catálogo de máquinas, el mantenimiento, los vales de salida, el inventario, la entrada y la baja de materiales y todos los informes de máquinas. El mantenimiento y los vales de salida ya no están en el grupo principal de la sección.
- Si el control de máquinas está desactivado, las máquinas no se muestran: el catálogo «Máquinas» desaparece del menú y el campo «Equipo» de la producción. Los datos ya introducidos se conservan y vuelven al activar el control.
- Los documentos principales de cada sección están también en su grupo temático: pedidos, ventas y devoluciones de clientes en «Ventas / Mayorista», gastos adicionales de recepción en «Compras / Importación», formación de pedidos a proveedores en «Compras / Planificación», documentos de caja en «Tesorería / Caja», pagos bancarios en «Tesorería / Banco», traslados en «Almacén / Almacenamiento», impresión de etiquetas en «Almacén / Artículos».

## 2.0.16.43
### ru
- Заголовки колонок в списке реализаций и в таблице товаров передачи в переработку больше не разъезжаются на macOS: «Дата», «Клиент», «Сумма», «Долг» и другие колонки выглядят так же, как в остальных списках. Эти колонки пропустило исправление шрифта шапок в 2.0.16.21.

### fr
- Les en-têtes de colonnes de la liste des ventes et du tableau des articles du transfert en sous-traitance ne s'étalent plus sur macOS : « Date », « Client », « Montant », « Dette » et les autres colonnes s'affichent comme dans les autres listes. Ces colonnes avaient échappé à la correction de la police des en-têtes en 2.0.16.21.

### en
- Column headers in the sales list and in the goods table of the transfer to subcontracting no longer spread out on macOS: "Date", "Customer", "Amount", "Debt" and the other columns now look the same as in other lists. These columns had been missed by the header font fix in 2.0.16.21.

### es
- Los encabezados de columnas de la lista de ventas y de la tabla de artículos de la entrega a subcontratación ya no se separan en macOS: «Fecha», «Cliente», «Importe», «Deuda» y las demás columnas se ven igual que en las otras listas. Estas columnas se habían quedado fuera de la corrección de la fuente de encabezados en 2.0.16.21.

## 2.0.16.42
### ru
- Учёт станков: новый отчёт «Занятость станков» (Производство → Отчёты) — какие станки сейчас загружены, а какие свободны, на любой момент. По каждому станку видно, что на нём идёт (заказ или обслуживание), когда освободится, с какого времени можно поставить новую работу и до какой даты станок загружен по плану, а также сколько часов работы впереди. Отбором можно оставить только загруженные или только свободные станки.
- Те же даты «Освободится», «Свободен с» и «Загружен до» появились в списке станков на закладке «Станки» рабочего места производства. Если работа идёт дольше расчёта, дата освобождения не показывается — она станет известна после «Завершить», а в состоянии станка написано «идёт дольше расчёта».

### fr
- Gestion des machines : nouveau rapport « Occupation des machines » (Production → Rapports) — quelles machines sont occupées et lesquelles sont libres, à n'importe quel moment. Pour chaque machine : ce qui y tourne (commande ou maintenance), quand elle se libère, à partir de quand on peut y placer un nouveau travail, jusqu'à quelle date elle est chargée selon le plan, et combien d'heures de travail restent. Un filtre permet de ne garder que les machines occupées ou libres.
- Les mêmes dates « Libre à », « Créneau libre » et « Chargée jusqu'au » apparaissent dans la liste des machines de l'onglet « Machines » du poste de production. Si un travail dure plus que prévu, l'heure de libération n'est pas affichée — elle sera connue après « Terminer », et l'état de la machine indique « dure plus que prévu ».

### en
- Machine tracking: new report "Machine occupancy" (Production → Reports) — which machines are busy and which are free, at any moment. For each machine it shows what is running (an order or maintenance), when it becomes free, from when new work can be placed on it, until what date it is booked by the plan, and how many hours of work are ahead. A filter keeps only busy or only free machines.
- The same "Free at", "Free slot from" and "Booked until" dates appear in the machine list on the "Machines" tab of the production workplace. If a job runs longer than planned, the free time is not shown — it becomes known after "Finish", and the machine state says "running longer than planned".

### es
- Control de máquinas: nuevo informe «Ocupación de máquinas» (Producción → Informes) — qué máquinas están ocupadas y cuáles libres, en cualquier momento. Para cada máquina se ve qué está en marcha (pedido o mantenimiento), cuándo queda libre, desde cuándo se puede poner un trabajo nuevo, hasta qué fecha está cargada según el plan y cuántas horas de trabajo quedan. Un filtro deja solo las máquinas ocupadas o solo las libres.
- Las mismas fechas «Libre a las», «Hueco libre desde» y «Cargada hasta» aparecen en la lista de máquinas de la pestaña «Máquinas» del puesto de producción. Si un trabajo dura más de lo previsto, la hora de liberación no se muestra — se conocerá tras «Terminar», y el estado de la máquina indica «dura más de lo previsto».

## 2.0.16.41
### ru
- Права личного кабинета партнёра ограничены: он больше не может напрямую изменять взаиморасчёты, продажи, остатки товаров, заказы поставщикам и историю статусов заказов. Статусы заказов записываются программой, поэтому заказ продажи теперь сохраняется и у ролей без прав на историю статусов (касса, интернет-магазин).
- Производство: заказ на производство не проводится, если у материала указана упаковка не 1:1 — иначе количество материала и потребность были бы занижены. Автовыпуск отказывает, если расход материала с нормой округлился до нуля, вместо того чтобы молча его потерять. Поступление из переработки нельзя провести задним числом раньше отгрузки заказа с автовыпуском — продукция была бы выпущена дважды.
- Закупки: закупка не может обеспечивать заказ на производство другой организации. «Заказать у победителя» берёт ставку НДС из предложения поставщика. Заказ поставщику на основании предложения заполняется только оставшимся дефицитом заказа клиента. Заказы на производство, у которых не было рассчитанной стадии, после обновления видны в «Потребности».
- Деньги: долг перевозчику по реализации в валюте ведётся в основной валюте. Налоговая накладная покупки по валютному поступлению получает его валюту и курс, закупочный налоговый регистр — в основной валюте (старые валютные накладные и возвраты перепроведите — их список после обновления в журнале регистрации; в старой накладной без валюты по валютному поступлению укажите валюту и курс и перепроведите её). Бухгалтерская операция пересчитывает валютные суммы проводок по курсам валют.
- Пересчёт товаров: при смене склада или станка в заполненном документе учётные остатки перечитываются, фактическое количество очищается.

### fr
- Droits de l'espace partenaire restreints : il ne peut plus modifier directement les règlements, ventes, stocks, commandes fournisseurs ni l'historique des statuts. Les statuts sont écrits par le programme, la commande client s'enregistre donc aussi pour les rôles sans droits sur l'historique (caisse, boutique en ligne).
- Production : une commande de production n'est pas validée si une matière a un conditionnement autre que 1:1 — sinon sa quantité et le besoin seraient sous-estimés. La production automatique refuse si la consommation d'une matière avec norme est arrondie à zéro, au lieu de la perdre. Une réception de sous-traitance ne peut pas être validée à une date antérieure à l'expédition de la commande avec production automatique — les produits seraient produits deux fois.
- Achats : un achat ne peut pas approvisionner la commande de production d'une autre société. « Commander au gagnant » prend le taux de TVA de l'offre du fournisseur. Une commande fournisseur créée depuis une offre ne reprend que le manque restant de la commande client. Les commandes de production sans étape calculée apparaissent dans « Besoins » après la mise à jour.
- Finances : la dette envers le transporteur d'une vente en devise est tenue en devise principale. La facture fiscale d'achat issue d'une réception en devise reçoit sa devise et son taux, le registre fiscal fournisseurs est en devise principale (revalidez les anciennes factures et retours en devise — leur liste est dans le journal après la mise à jour ; pour une ancienne facture sans devise issue d'une réception en devise, indiquez la devise et le taux puis revalidez-la). L'opération comptable convertit les montants en devise des écritures selon les taux.
- Inventaire : en changeant d'entrepôt ou de machine dans un document rempli, le stock théorique est relu et la quantité réelle effacée.

### en
- Partner account rights restricted: it can no longer change settlements, sales, stock, supplier orders or order status history directly. Order statuses are written by the program, so a sales order now saves for roles without rights on the status history (cash desk, online store) too.
- Production: a production order is not posted if a material has a package other than 1:1 — otherwise the material quantity and requirement would be understated. Automatic output refuses when a normed material consumption rounds to zero instead of silently losing it. A subcontracting receipt cannot be posted back-dated before a shipment of the order with automatic output — the products would be produced twice.
- Purchasing: a purchase cannot supply a production order of another company. "Order from winner" takes the VAT rate from the supplier offer. A supplier order created from an offer is filled only with the remaining shortage of the customer order. Production orders without a calculated stage show in "Requirements" after the update.
- Money: the carrier debt of a foreign-currency sale is kept in the base currency. A purchase tax invoice based on a foreign-currency receipt gets its currency and rate, the supplier tax register is in the base currency (repost old foreign-currency invoices and returns — their list is in the event log after the update; for an old invoice without a currency from a foreign-currency receipt, set the currency and rate and repost it). The accounting operation converts foreign-currency entry amounts by exchange rates.
- Stock count: changing the warehouse or machine in a filled document rereads book stock and clears the actual quantity.

### es
- Derechos del portal del socio restringidos: ya no puede modificar directamente liquidaciones, ventas, existencias, pedidos a proveedores ni el historial de estados. Los estados los escribe el programa, así que el pedido de venta también se guarda en roles sin derechos sobre el historial (caja, tienda en línea).
- Producción: un pedido de producción no se contabiliza si un material tiene un envase distinto de 1:1 — de lo contrario su cantidad y la necesidad quedarían subestimadas. La producción automática se rechaza si el consumo de un material con norma se redondea a cero, en lugar de perderlo. Una recepción de subcontratación no puede contabilizarse con fecha anterior al envío del pedido con producción automática — los productos se producirían dos veces.
- Compras: una compra no puede abastecer el pedido de producción de otra empresa. «Pedir al ganador» toma el tipo de IVA de la oferta del proveedor. Un pedido a proveedor desde una oferta se llena solo con el déficit restante del pedido del cliente. Los pedidos de producción sin etapa calculada aparecen en «Necesidades» tras la actualización.
- Dinero: la deuda con el transportista de una venta en moneda se lleva en la moneda principal. La factura fiscal de compra de una recepción en moneda recibe su moneda y tipo, el registro fiscal de proveedores está en moneda principal (vuelva a contabilizar las facturas y devoluciones antiguas en moneda — su lista está en el registro de eventos tras actualizar; en una factura antigua sin moneda de una recepción en moneda, indique la moneda y el tipo y vuelva a contabilizarla). La operación contable convierte los importes en moneda de los asientos según los tipos.
- Recuento: al cambiar el almacén o la máquina en un documento lleno, se relee el stock contable y se borra la cantidad real.

## 2.0.16.40
### ru
- Инвентаризация станков: в меню «Производство → Станки» — «Инвентаризация станков», «Оприходование материалов» и «Списание материалов». Каждая команда открывает список уже отобранных документов по станкам; новый документ из такого списка сразу создаётся по станку.
- В пересчёте, списании и оприходовании товаров появился вид операции «По станку» (при включённом учёте станков): вместо склада выбирается станок, документ работает со складом станка. Учётное количество пересчёта — всё, что лежит на станке. Списание и оприходование на основании пересчёта получают тот же станок.
- Недостача на станке списывается со свободного остатка станка; материалы, закреплённые за запущенным заказом, списывает его завершение — их списание отклоняется с названием требования. При создании списания и оприходования из пересчёта по станку пустые документы не создаются, а причина отказа проведения показывается.

### fr
- Inventaire des machines : dans le menu « Production → Machines » — « Inventaire des machines », « Entrée de matières » et « Sortie de matières ». Chaque commande ouvre la liste déjà filtrée des documents par machine ; un nouveau document créé depuis cette liste est d'emblée par machine.
- L'inventaire, la sortie et l'entrée de marchandises ont un type d'opération « Par machine » (gestion des machines activée) : on choisit la machine au lieu de l'entrepôt, le document travaille avec le stock de la machine. La quantité théorique de l'inventaire est tout ce qui se trouve sur la machine. La sortie et l'entrée créées depuis l'inventaire reprennent la même machine.
- Un manque sur la machine est sorti du stock libre de la machine ; les matières réservées à une commande lancée sont sorties à sa fin — leur sortie est refusée avec le nom du bon. En créant la sortie et l'entrée depuis un inventaire par machine, aucun document vide n'est créé et le motif d'un refus de validation est affiché.

### en
- Machine stocktaking: the "Production → Machines" menu has "Machine stocktaking", "Materials receipt" and "Materials write-off". Each command opens the list already filtered to machine documents; a new document from that list is created by machine right away.
- Stock count, write-off and receipt of goods have a "By machine" operation type (with machine management on): the machine is chosen instead of the warehouse and the document works with the machine stock. The book quantity of the count is everything on the machine. A write-off and receipt created from the count get the same machine.
- A shortage on the machine is written off from the machine free stock; materials reserved for a started order are written off when it is completed — writing them off is refused, naming the requisition. When a write-off and receipt are created from a machine count, empty documents are not created and the reason for a posting refusal is shown.

### es
- Inventario de máquinas: en el menú «Producción → Máquinas» — «Inventario de máquinas», «Ingreso de materiales» y «Baja de materiales». Cada comando abre la lista ya filtrada de documentos por máquina; un documento nuevo desde esa lista se crea directamente por máquina.
- El recuento, la baja y el ingreso de mercancías tienen el tipo de operación «Por máquina» (con la gestión de máquinas activada): se elige la máquina en lugar del almacén y el documento trabaja con el stock de la máquina. La cantidad contable del recuento es todo lo que hay en la máquina. La baja y el ingreso creados desde el recuento toman la misma máquina.
- Una falta en la máquina se da de baja del stock libre de la máquina; los materiales reservados para un pedido iniciado se dan de baja al terminarlo — su baja se rechaza indicando el vale. Al crear la baja y el ingreso desde un recuento por máquina no se crean documentos vacíos y se muestra el motivo del rechazo de contabilización.

## 2.0.16.39
### ru
- На планировщике закладки «Станки» запланированную загрузку и плановое обслуживание можно растянуть или сжать мышью за край. Меняется только время, количество прежнее: длительность загрузки становится равной рабочим часам станка между новым началом и окончанием (с шагом 15 минут) и сохраняется при переносе.
- В требовании-накладной появилось поле «Длительность вручную, ч»: его заполняет растяжение, его можно поправить руками; очистка поля возвращает расчёт по весу материалов. При переносе загрузки на другой станок ручная длительность сбрасывается — там другая выработка.
- Отчёты учёта станков точнее: «нет заказа» в «Загрузке станков» больше не искажается округлением часов по отдельным документам; «Материалы на станках» показывают отрицательный свободный остаток и там, где на складе станка остатка нет совсем; выведенный станок попадает в отчёты, если у него в периоде есть план или незавершённая загрузка. Вариант отчётов «Основной» назван на языке интерфейса.

### fr
- Dans le planificateur de l'onglet « Machines », une charge planifiée et une maintenance planifiée peuvent être étirées ou réduites à la souris par le bord. Seul l'horaire change, la quantité reste la même : la durée devient les heures de travail de la machine entre le nouveau début et la nouvelle fin (au pas de 15 minutes) et elle est conservée lors d'un déplacement.
- Le bon de consommation a un champ « Durée manuelle, h » : l'étirement le remplit, on peut le corriger à la main ; vider le champ revient au calcul selon le poids des matières. Déplacer la charge sur une autre machine efface la durée manuelle — la cadence y est différente.
- Rapports des machines plus précis : « sans commande » dans « Charge des machines » n’est plus faussé par l’arrondi des heures par document ; « Matières sur les machines » montre aussi un stock libre négatif quand le stock de la machine est vide ; une machine retirée apparaît dans les rapports si elle a un plan ou une charge non terminée sur la période. La variante « Principal » des rapports est dans la langue de l’interface.

### en
- On the "Machines" tab planner, a planned load and planned maintenance can be stretched or shrunk with the mouse by their edge. Only the time changes, the quantity stays the same: the load duration becomes the machine working hours between the new start and end (in 15-minute steps) and is kept when the load is moved.
- The material requisition has a "Manual duration, h" field: stretching fills it, and it can be edited by hand; clearing it brings back the calculation from material weight. Moving the load to another machine clears the manual duration — the output rate there is different.
- Machine reports are more accurate: "no order" in "Machine utilization" is no longer skewed by rounding hours per document; "Materials on machines" also shows negative free stock where the machine stock is empty; a retired machine appears in reports if it has a plan or an unfinished load in the period. The "Main" report variant is named in the interface language.

### es
- En el planificador de la pestaña «Máquinas», una carga planificada y un mantenimiento planificado se pueden estirar o encoger con el ratón por el borde. Solo cambia el horario, la cantidad sigue igual: la duración pasa a ser las horas de trabajo de la máquina entre el nuevo inicio y el nuevo fin (en pasos de 15 minutos) y se mantiene al mover la carga.
- El vale de consumo tiene el campo «Duración manual, h»: lo rellena el estiramiento y se puede corregir a mano; al vaciarlo vuelve el cálculo por el peso de los materiales. Al mover la carga a otra máquina la duración manual se borra — allí el rendimiento es otro.
- Informes de máquinas más precisos: «sin pedido» en «Carga de máquinas» ya no se distorsiona por el redondeo de horas por documento; «Materiales en máquinas» muestra stock libre negativo también donde la máquina no tiene stock; una máquina retirada aparece en los informes si tiene plan o una carga sin terminar en el período. La variante «Principal» de los informes está en el idioma de la interfaz.

## 2.0.16.38
### ru
- Автоплан на закладке «Станки» рабочего места производства: кнопка «Автоплан» раскладывает строки «Готовы к запуску» по станкам в порядке дат отгрузки — каждую строку целиком на станок, который закончит её раньше всех, мимо уже запланированных загрузок и обслуживания. Предложение видно на планировщике светло-зелёным и на закладке «Автоплан»; не успевающие к отгрузке строки — красным, строки, которые поставить нельзя, — с причиной.
- «Принять автоплан» создаёт требования по предложению; уже запланированное не меняется. Если время за это время заняли, строка не размещается и называется в сообщении; устаревшее предложение нужно рассчитать заново.
- В карточке продукции — закладка «Станки»: на каких станках её можно делать. Пустой список — любой станок; автоплан ставит продукцию только на станки из списка.

### fr
- Planification automatique dans l'onglet « Machines » du poste de production : le bouton « Planification auto » répartit les lignes « Prêt à lancer » sur les machines par date d'expédition — chaque ligne entière sur la machine qui la terminera le plus tôt, en évitant les charges et la maintenance déjà planifiées. La proposition apparaît en vert clair dans le planificateur et dans l'onglet « Planification auto » ; les lignes en retard sur l'expédition en rouge, celles qui ne peuvent pas être placées avec leur motif.
- « Valider la planification » crée les bons selon la proposition ; ce qui est déjà planifié ne change pas. Si le créneau a été pris entre-temps, la ligne n'est pas placée et elle est signalée ; une proposition périmée doit être recalculée.
- Dans la fiche produit — onglet « Machines » : sur quelles machines le fabriquer. Liste vide — toute machine ; la planification automatique ne place le produit que sur les machines de la liste.

### en
- Auto-plan on the "Machines" tab of the production workplace: the "Auto-plan" button spreads the "Ready to start" lines over machines in shipment date order — each whole line on the machine that will finish it first, around loads and maintenance already planned. The proposal is shown in light green on the planner and on the "Auto-plan" tab; lines late for shipment are red, lines that cannot be placed show the reason.
- "Accept auto-plan" creates requisitions from the proposal; what is already planned does not change. If a slot was taken meanwhile, that line is not placed and is named in the message; an outdated proposal must be recalculated.
- The product card has a "Machines" tab: which machines can make it. Empty list — any machine; auto-plan puts the product only on the listed machines.

### es
- Planificación automática en la pestaña «Máquinas» del puesto de producción: el botón «Planificación auto» reparte las líneas «Listo para iniciar» entre las máquinas por fecha de envío — cada línea entera en la máquina que la termine antes, sin chocar con cargas y mantenimiento ya planificados. La propuesta se ve en verde claro en el planificador y en la pestaña «Planificación auto»; las líneas que no llegan al envío en rojo, las que no se pueden colocar con su motivo.
- «Aceptar planificación» crea los vales según la propuesta; lo ya planificado no cambia. Si el hueco se ocupó entretanto, la línea no se coloca y se indica en el mensaje; una propuesta desactualizada hay que recalcularla.
- En la ficha del producto — pestaña «Máquinas»: en qué máquinas se puede fabricar. Lista vacía — cualquier máquina; la planificación automática solo lo pone en las máquinas de la lista.

## 2.0.16.37
### ru
- В отчёте «Простои станков» — надёжность станков: число отказов, наработка на отказ (MTBF) — часы работы станка на один отказ, и среднее время ремонта (MTTR). Отказом считается фактический «Ремонт или авария», не запланированный заранее; ТО, переналадка и запланированный ремонт отказами не считаются.

### fr
- Dans le rapport « Arrêts des machines » — fiabilité des machines : nombre de pannes, temps moyen entre pannes (MTBF) — heures de travail de la machine par panne, et temps moyen de réparation (MTTR). Une panne est une « Réparation ou panne » réelle non planifiée à l'avance ; la maintenance, le changement de série et une réparation planifiée ne sont pas des pannes.

### en
- The "Machine downtime" report now shows machine reliability: number of failures, mean time between failures (MTBF) — machine run hours per failure, and mean time to repair (MTTR). A failure is an actual "Repair or breakdown" not planned in advance; maintenance, changeovers and a planned repair are not failures.

### es
- En el informe «Paradas de máquinas» — fiabilidad de las máquinas: número de averías, tiempo medio entre averías (MTBF) — horas de trabajo de la máquina por avería, y tiempo medio de reparación (MTTR). Una avería es una «Reparación o avería» real no planificada de antemano; el mantenimiento, el cambio de serie y una reparación planificada no son averías.

## 2.0.16.36
### ru
- Новый отчёт «Эффективность станков (OEE)» (Производство → Отчёты; при включённом учёте станков): по каждому станку за период — доступность (работа к фонду времени без плановых остановок), производительность (норма выработки к фактическим часам завершённых загрузок), качество (вес выпуска к весу израсходованных материалов) и итоговый OEE.
- Плановыми остановками считается запланированное обслуживание; если по плану было ТО, а станок в это время работал, остановки не было. Качество считается по весу продукции из её карточки: продукция без веса в качество не входит, отчёт называет её в предупреждении.
- В документе «Обслуживание станка» сохраняются плановые даты: после перевода планового ТО в факт видно, когда его планировали.

### fr
- Nouveau rapport « Efficacité des machines (TRS) » (Production → Rapports ; gestion des machines activée) : par machine sur la période — disponibilité (travail sur le temps disponible hors arrêts planifiés), performance (norme de production sur les heures réelles des charges terminées), qualité (poids produit sur poids des matières consommées) et TRS global.
- Les arrêts planifiés sont la maintenance planifiée ; si une maintenance était prévue mais que la machine a tourné pendant ce temps, il n'y a pas eu d'arrêt. La qualité se calcule avec le poids du produit de sa fiche : un produit sans poids n'entre pas dans la qualité, le rapport le signale.
- Le document « Maintenance de machine » conserve les dates prévues : après le passage d'une maintenance planifiée en réel, on voit quand elle était prévue.

### en
- New report "Machine effectiveness (OEE)" (Production → Reports; with machine management on): per machine for the period — availability (run time over available time minus planned stops), performance (standard hours over actual hours of completed loads), quality (output weight over weight of materials used) and overall OEE.
- Planned stops are planned maintenance; if maintenance was planned but the machine ran during that time, there was no stop. Quality uses the product weight from its card: a product without weight is left out of quality and named in the report warning.
- The "Machine maintenance" document keeps the planned dates: after planned maintenance is switched to actual, you can see when it was planned.

### es
- Nuevo informe «Eficiencia de máquinas (OEE)» (Producción → Informes; con la gestión de máquinas activada): por máquina en el período — disponibilidad (trabajo sobre el tiempo disponible sin paradas planificadas), rendimiento (norma sobre las horas reales de las cargas terminadas), calidad (peso producido sobre peso de materiales consumidos) y OEE total.
- Las paradas planificadas son el mantenimiento planificado; si había mantenimiento previsto pero la máquina trabajó en ese tiempo, no hubo parada. La calidad usa el peso del producto de su ficha: un producto sin peso no entra en la calidad y el informe lo indica.
- El documento «Mantenimiento de máquina» guarda las fechas previstas: tras pasar un mantenimiento planificado a real, se ve cuándo estaba previsto.

## 2.0.16.35
### ru
- Отчёты учёта станков (Производство → Отчёты; при включённом учёте станков): «Загрузка станков», «Деньги по станкам», «Выработка станков», «Материалы на станках».
- «Загрузка станков» — по каждому станку за период: фонд времени по режиму работы, работа по плану и по факту, ТО и ремонты, простой без заказа и процент загрузки. Время не задваивается: авария посреди загрузки вычитается из работы и считается ремонтом; что осталось от фонда — «нет заказа». Факт считается до текущего момента: оставшиеся часы недели простоем не считаются.
- «Деньги по станкам» — по завершённым загрузкам: выручка по цене строки заказа без НДС в основной валюте (по курсу заказа), себестоимость материалов выпуска, стоимость часов работы станка (по «Стоимости часа» в карточке станка), затраты на обслуживание; маржа, маржа на час и на кг.
- «Выработка станков» — кг израсходованных материалов, выпущенное количество и часы по станкам, продукции и операторам; норма по выработке станка и время на смену заказа, отклонение от нормы, кг в час, процент выполнения нормы.
- «Материалы на станках» — на выбранную дату: что лежит на каждом станке под заказами и свободным остатком, в штуках, кг и по себестоимости.
- «Вернуть в работу» больше не возвращает загрузку, если после неё на станке уже работала другая — иначе время работы задвоилось бы.

### fr
- Rapports de gestion des machines (Production → Rapports ; gestion des machines activée) : « Charge des machines », « Rentabilité des machines », « Production des machines », « Matières sur les machines ».
- « Charge des machines » — par machine sur la période : temps disponible selon les horaires, travail planifié et réel, maintenance et réparations, inactivité sans commande et taux de charge. Le temps n'est pas compté deux fois : une panne pendant une charge est retirée du travail et comptée en réparation ; le reste du temps disponible est « sans commande ». Le réel est compté jusqu'à maintenant : les heures restantes de la semaine ne sont pas de l'inactivité.
- « Rentabilité des machines » — sur les charges terminées : chiffre d'affaires au prix de la ligne de commande HT en devise principale (au taux de la commande), coût des matières de la production, coût des heures machine (« Coût horaire » de la fiche machine), coûts de maintenance ; marge, marge par heure et par kg.
- « Production des machines » — kg de matières consommées, quantité produite et heures par machine, produit et opérateur ; norme selon le rendement de la machine et le temps de changement, écart à la norme, kg par heure, respect de la norme en %.
- « Matières sur les machines » — à la date choisie : ce qui est sur chaque machine pour les commandes et en stock libre, en quantité, kg et au coût.
- « Remettre en cours » ne relance plus une charge si une autre a déjà tourné sur la machine après elle — sinon le temps de travail serait compté deux fois.

### en
- Machine management reports (Production → Reports; with machine management on): "Machine utilization", "Machine profitability", "Machine output", "Materials on machines".
- "Machine utilization" — per machine for the period: available time from the schedule, planned and actual work, maintenance and repairs, idle time without orders and the utilization percentage. Time is never counted twice: a breakdown during a load is taken out of work and counted as repair; what is left of available time is "no order". Actual time is counted up to now: the remaining hours of the week are not idle time.
- "Machine profitability" — for completed loads: revenue at the order line price excluding VAT in the base currency (at the order rate), material cost of the output, machine hours cost ("Hourly cost" on the machine card), maintenance costs; margin, margin per hour and per kg.
- "Machine output" — kg of materials used, quantity produced and hours by machine, product and operator; standard from the machine output rate and order changeover time, deviation from the standard, kg per hour, standard achievement in %.
- "Materials on machines" — as of the chosen date: what is on each machine for orders and as free stock, in units, kg and at cost.
- "Return to work" no longer reopens a load if another load has already run on the machine after it — otherwise working time would be counted twice.

### es
- Informes de gestión de máquinas (Producción → Informes; con la gestión de máquinas activada): «Carga de máquinas», «Rentabilidad de máquinas», «Producción de máquinas», «Materiales en máquinas».
- «Carga de máquinas» — por máquina en el período: tiempo disponible según el horario, trabajo planificado y real, mantenimiento y reparaciones, inactividad sin pedido y porcentaje de carga. El tiempo no se cuenta dos veces: una avería durante una carga se resta del trabajo y cuenta como reparación; lo que queda del tiempo disponible es «sin pedido». Lo real se cuenta hasta ahora: las horas restantes de la semana no son inactividad.
- «Rentabilidad de máquinas» — de las cargas terminadas: ingresos al precio de la línea del pedido sin IVA en la moneda principal (al tipo del pedido), coste de materiales de la producción, coste de las horas de máquina («Coste por hora» de la ficha), costes de mantenimiento; margen, margen por hora y por kg.
- «Producción de máquinas» — kg de materiales consumidos, cantidad producida y horas por máquina, producto y operador; norma según el rendimiento de la máquina y el tiempo de cambio, desviación de la norma, kg por hora, cumplimiento de la norma en %.
- «Materiales en máquinas» — a la fecha elegida: lo que hay en cada máquina para pedidos y como stock libre, en unidades, kg y a coste.
- «Devolver a producción» ya no reabre una carga si después de ella ya trabajó otra en la máquina — de lo contrario el tiempo de trabajo se contaría dos veces.

## 2.0.16.34
### ru
- Закладка «Станки» в рабочем месте производства (при включённом учёте станков): список станков — что на станке сейчас, загрузка недели в процентах от фонда времени, ближайшее плановое обслуживание; планировщик на неделю — станки строками, загрузки по плану голубые, по факту тёмные, обслуживание серое, нерабочее время по режиму станка — фоном. Неделя листается кнопками ◀ ▶.
- «Готовы к запуску» — строки заказов на производство, которые можно ставить на станок: заказы в производстве и заказы, материалов которых хватает на вашем складе. Видны остаток к размещению, вес материалов в кг и время на выбранном станке; строки идут по дате отгрузки, не успевающие к отгрузке — красным.
- «Разместить» ставит выбранную строку на выбранный станок в ближайшее свободное окно по режиму работы — мимо других загрузок и обслуживания, с шагом 15 минут. Строку можно перетащить на планировщик в нужное время и на нужный станок. Количество можно разбить: часть — на один станок, остаток — на другой.
- Запланированную загрузку можно перетащить на планировщике на другое время или станок; на занятое время (другая загрузка, ремонт) перенос не пройдёт. Запуск, завершение с количеством выпуска и отмена загрузки — кнопками закладки; двойной щелчок открывает документ.
- Загрузка, которая идёт дольше расчёта и не завершена, на планировщике выделена и держит станок занятым, пока её не завершат.

### fr
- Onglet « Machines » dans le poste de travail de production (gestion des machines activée) : liste des machines — ce qui tourne maintenant, charge de la semaine en pourcentage du temps disponible, prochaine maintenance planifiée ; planificateur de la semaine — machines en lignes, charges planifiées en bleu, réelles en foncé, maintenance en gris, heures hors service en fond. Les boutons ◀ ▶ changent de semaine.
- « Prêt à lancer » — lignes de commandes de production à mettre sur machine : commandes en production et commandes dont les matières sont disponibles dans votre entrepôt. Reste à planifier, poids des matières en kg et durée sur la machine choisie ; tri par date d'expédition, en rouge les lignes qui ne tiennent pas le délai.
- « Planifier » place la ligne choisie sur la machine choisie au prochain créneau libre selon ses horaires — en évitant les autres charges et la maintenance, au pas de 15 minutes. La ligne peut aussi être glissée sur le planificateur au moment et sur la machine voulus. La quantité peut être répartie entre plusieurs machines.
- Une charge planifiée se déplace par glisser-déposer vers un autre moment ou une autre machine ; vers un créneau occupé (autre charge, réparation) le déplacement est refusé. Lancer, terminer avec la quantité produite et annuler — par les boutons de l'onglet ; un double-clic ouvre le document.
- Une charge lancée qui dure plus que prévu et n'est pas terminée est mise en évidence et garde la machine occupée jusqu'à « Terminer ».

### en
- "Machines" tab in the production workplace (with machine management on): machine list — what is running now, the week load as a percentage of available time, the next planned maintenance; weekly planner — machines as rows, planned loads in blue, actual in dark, maintenance in grey, off hours from the machine schedule as background. ◀ ▶ buttons switch weeks.
- "Ready to start" — production order lines that can go on a machine: orders in production and orders whose materials are available in your warehouse. Shows the quantity left to place, material weight in kg and time on the selected machine; lines are sorted by shipment date, those that cannot make the shipment are red.
- "Place" puts the selected line on the selected machine in the nearest free slot of its schedule — around other loads and maintenance, in 15-minute steps. A line can also be dragged onto the planner at the wanted time and machine. The quantity can be split: part on one machine, the rest on another.
- A planned load can be dragged on the planner to another time or machine; moving it onto busy time (another load, a repair) is refused. Start, complete with the produced quantity and cancel a load with the tab buttons; a double click opens the document.
- A started load running longer than calculated and not completed is highlighted and keeps the machine busy until "Complete".

### es
- Pestaña «Máquinas» en el puesto de producción (con la gestión de máquinas activada): lista de máquinas — qué está en marcha ahora, carga de la semana en porcentaje del tiempo disponible, próximo mantenimiento planificado; planificador semanal — máquinas en filas, cargas planificadas en azul, reales en oscuro, mantenimiento en gris, horas fuera de horario como fondo. Los botones ◀ ▶ cambian de semana.
- «Listo para iniciar» — líneas de pedidos de producción que se pueden poner en máquina: pedidos en producción y pedidos cuyos materiales hay en su almacén. Muestra lo pendiente de planificar, el peso de los materiales en kg y el tiempo en la máquina elegida; ordenadas por fecha de envío, en rojo las que no llegan a tiempo.
- «Planificar» pone la línea elegida en la máquina elegida en el hueco libre más próximo de su horario — evitando otras cargas y el mantenimiento, en pasos de 15 minutos. La línea también se puede arrastrar al planificador a la hora y máquina deseadas. La cantidad se puede repartir entre varias máquinas.
- Una carga planificada se arrastra en el planificador a otra hora o máquina; sobre un tiempo ocupado (otra carga, una reparación) el traslado se rechaza. Iniciar, terminar con la cantidad producida y cancelar una carga, con los botones de la pestaña; doble clic abre el documento.
- Una carga iniciada que dura más de lo calculado y no se ha terminado se resalta y mantiene la máquina ocupada hasta «Terminar».

## 2.0.16.33
### ru
- Документ «Требование-накладная» (Производство → Требования-накладные; при включённом учёте станков): загрузка станка по строке заказа на производство. Выберите станок, заказ и строку продукции — материалы заполнятся по заказу; количество можно поправить. Статусы: «Запланировано», «Запущено», «Завершено», «Отменено» — команды «Разместить», «Запустить», «Завершить», «Отменить».
- Время загрузки считается само: вес материалов в кг делится на выработку станка и прибавляется время на смену заказа; окончание раскладывается по режиму работы станка. Вес берётся из единицы измерения (кг) или из веса в карточке номенклатуры; если у материала веса нет, требование об этом сообщит.
- Материалы перемещаются на склад станка при «Запустить» (или при «Разместить», если в настройках производства включено «Списывать материалы на станок при размещении») теми же партиями и по той же себестоимости. «Завершить» создаёт выпуск продукции со склада станка на склад требования; что не израсходовано, остаётся на станке и первым идёт в следующую загрузку. Вернуть остаток на склад можно обычным перемещением.
- Материалы, закреплённые за запущенным требованием, нельзя ни продать, ни списать, ни увезти со склада станка. На станке одновременно запущено одно требование. Пока по продукции заказа открыто требование, её не выпускает автовыпуск при отгрузке, ручной выпуск и передача в переработку.
- «Отменить» возвращает материалы на склад, если соседняя загрузка их ещё не израсходовала; иначе они остаются на станке свободным остатком. Ошибочное завершение руководитель или администратор исправляет командой «Вернуть в работу» — пока продукцию выпуска не отгрузили и не списали.
- Учёт станков и производство нельзя выключить, пока есть открытые требования-накладные. У каждого станка свой склад; на складе станка не должно быть оповещения о минимальном остатке.

### fr
- Document « Bon de consommation machine » (Production → Bons de consommation machine ; gestion des machines activée) : chargement d'une machine pour une ligne de commande de production. Choisissez la machine, la commande et la ligne de produit — les matières se remplissent selon la commande ; la quantité peut être corrigée. Statuts : « Planifié », « Lancé », « Terminé », « Annulé » — commandes « Planifier », « Lancer », « Terminer », « Annuler ».
- La durée de charge se calcule seule : le poids des matières en kg est divisé par le rendement de la machine, plus le temps de changement de commande ; la fin est répartie selon les horaires de la machine. Le poids vient de l'unité (kg) ou du poids de la fiche article ; s'il manque, le bon le signale.
- Les matières sont transférées vers l'entrepôt de la machine au « Lancer » (ou au « Planifier » si « Transférer les matières sur la machine à la planification » est coché dans les paramètres de production), avec les mêmes lots et le même coût. « Terminer » crée la production depuis l'entrepôt de la machine vers l'entrepôt du bon ; le non-consommé reste sur la machine et part en premier dans la charge suivante. Un transfert ordinaire le renvoie en stock.
- Les matières réservées par un bon lancé ne peuvent être ni vendues, ni sorties, ni transférées de l'entrepôt de la machine. Un seul bon est lancé à la fois sur une machine. Tant qu'un bon est ouvert pour un produit de la commande, ni la production automatique à l'expédition, ni la production manuelle, ni la sous-traitance ne le produisent.
- « Annuler » renvoie les matières en stock si une autre charge ne les a pas encore consommées ; sinon elles restent sur la machine comme stock libre. Un responsable ou un administrateur corrige une fin erronée avec « Remettre en cours » — tant que les produits n'ont été ni expédiés ni sortis.
- La gestion des machines et la production ne se désactivent pas tant qu'il reste des bons ouverts. Chaque machine a son propre entrepôt ; l'entrepôt d'une machine ne doit pas avoir d'alerte de stock minimum.

### en
- "Machine material requisition" document (Production → Machine material requisitions; with machine management on): loading a machine for a production order line. Choose the machine, the order and the product line — materials are filled from the order; the quantity can be edited. Statuses: "Planned", "Started", "Completed", "Cancelled" — commands "Schedule", "Start", "Complete", "Cancel".
- The load time is calculated automatically: material weight in kg divided by the machine output plus the order changeover time; the end is laid out on the machine working schedule. The weight comes from the unit (kg) or the weight in the item card; if a material has no weight, the requisition says so.
- Materials are moved to the machine warehouse on "Start" (or on "Schedule" when "Move materials to the machine when scheduling" is on in production settings) with the same batches and cost. "Complete" creates a production output from the machine warehouse to the requisition warehouse; what was not consumed stays on the machine and goes first into the next load. A regular transfer brings it back to stock.
- Materials reserved by a started requisition cannot be sold, written off or moved out of the machine warehouse. Only one requisition is started on a machine at a time. While a requisition is open for an order product, neither the automatic output on shipment, nor manual output, nor subcontracting produces it.
- "Cancel" returns the materials to stock if another load has not consumed them yet; otherwise they stay on the machine as free stock. A manager or an administrator fixes a wrong completion with "Return to work" — while the output products are neither shipped nor written off.
- Machine management and production cannot be turned off while open requisitions exist. Each machine has its own warehouse; a machine warehouse must not have a minimum stock notification.

### es
- Documento «Vale de consumo de máquina» (Producción → Vales de consumo de máquina; con la gestión de máquinas activada): carga de una máquina para una línea de pedido de producción. Elija la máquina, el pedido y la línea de producto: los materiales se rellenan según el pedido; la cantidad se puede corregir. Estados: «Planificado», «Iniciado», «Terminado», «Cancelado» — comandos «Planificar», «Iniciar», «Terminar», «Cancelar».
- El tiempo de carga se calcula solo: el peso de los materiales en kg dividido por el rendimiento de la máquina más el tiempo de cambio de pedido; el fin se reparte según el horario de la máquina. El peso sale de la unidad (kg) o del peso de la ficha del artículo; si un material no tiene peso, el vale lo indica.
- Los materiales pasan al almacén de la máquina al «Iniciar» (o al «Planificar» si en los ajustes de producción está activado «Mover los materiales a la máquina al planificar») con los mismos lotes y el mismo coste. «Terminar» crea la producción desde el almacén de la máquina al almacén del vale; lo no consumido queda en la máquina y va primero a la siguiente carga. Un traslado normal lo devuelve al stock.
- Los materiales reservados por un vale iniciado no se pueden vender, dar de baja ni sacar del almacén de la máquina. En una máquina solo hay un vale iniciado a la vez. Mientras un vale esté abierto para un producto del pedido, no lo producen ni la producción automática al enviar, ni la producción manual, ni la subcontratación.
- «Cancelar» devuelve los materiales al stock si otra carga aún no los consumió; si no, quedan en la máquina como stock libre. Un responsable o administrador corrige un fin erróneo con «Devolver a producción», mientras los productos no se hayan enviado ni dado de baja.
- La gestión de máquinas y la producción no se pueden desactivar mientras haya vales abiertos. Cada máquina tiene su propio almacén; el almacén de una máquina no debe tener aviso de stock mínimo.

## 2.0.16.32
### ru
- Учёт станков (Настройки → Производство → «Учёт станков»; доступен при включённом производстве). Справочник «Производственное оборудование» теперь называется «Станки» и стоит в «Производство → Нормативы» рядом с техкартами; там же «Производственный календарь».
- В карточке станка (при включённом учёте станков): вид станка, выработка в кг/ч, время на смену заказа в минутах, склад станка, стоимость часа работы, оператор по умолчанию, флажок «Выведен» и таблица «Режим работы» — смены по дням недели; смена может переходить через полночь, круглосуточная смена отмечается флажком. Дни производственного календаря (выходные и праздники) для станка нерабочие; для непрерывной работы отметьте «Работает без производственного календаря».
- В списке станков колонки «Вид станка», «Выработка, кг/ч», «Выведен»; выведенные станки скрыты, флажок «Показывать выведенные станки» их показывает. Выведенный станок не выбирается в новые документы.
- Документ «Обслуживание станка» (Производство): плановое ТО, ремонт или авария, переналадка; начало и окончание, причина, исполнитель, затраты. Запланированное обслуживание резервирует время станка, после выполнения снимите флажок «Плановое» и укажите фактическое время. Два обслуживания одного станка в одно время не проводятся.
- Отчёт «Простои станков» (Производство → Отчёты): часы простоя и число случаев по станкам, видам и причинам за период, фонд рабочего времени по режиму станка и процент простоя в рабочее время. Если производственный календарь на год не заполнен, отчёт предупреждает об этом.
- В настройках производства — флажок «Списывать материалы на станок при размещении»: пока только запоминается, работать начнёт вместе с требованиями-накладными.

### fr
- Gestion des machines (Paramètres → Production → « Gestion des machines » ; disponible si la production est activée). Le référentiel « Équipement de production » s'appelle désormais « Machines » et se trouve dans « Production → Normes » à côté des gammes ; le « Calendrier » y est aussi.
- Dans la fiche machine (gestion des machines activée) : type de machine, rendement en kg/h, temps de changement de commande en minutes, entrepôt de la machine, coût horaire, opérateur par défaut, case « Retirée » et tableau « Horaires de travail » — postes par jour de la semaine ; un poste peut passer minuit, un poste 24 h/24 se coche. Les jours du calendrier (week-ends et fériés) sont chômés pour la machine ; pour un fonctionnement continu, cochez « Fonctionne sans le calendrier ».
- La liste des machines affiche les colonnes « Type de machine », « Rendement, kg/h », « Retirée » ; les machines retirées sont masquées, la case « Afficher les machines retirées » les montre. Une machine retirée n'est pas proposée dans les nouveaux documents.
- Document « Maintenance de machine » (Production) : maintenance préventive, réparation ou panne, changement de série ; début et fin, motif, intervenant, coûts. La maintenance planifiée réserve le temps de la machine ; une fois faite, décochez « Planifiée » et saisissez les heures réelles. Deux maintenances d'une même machine au même moment ne sont pas validées.
- Rapport « Arrêts des machines » (Production → Rapports) : heures d'arrêt et nombre de cas par machine, type et motif sur la période, temps disponible selon les horaires de la machine et pourcentage d'arrêt pendant les heures de travail. Si le calendrier de l'année n'est pas rempli, le rapport le signale.
- Dans les paramètres de production, la case « Transférer les matières sur la machine à la planification » : pour l'instant elle est seulement enregistrée, elle fonctionnera avec les bons de sortie.

### en
- Machine management (Settings → Production → "Machine management"; available when production is enabled). The "Production equipment" catalog is now called "Machines" and sits in "Production → Standards" next to the routings; the "Calendar" is there too.
- In the machine card (machine management on): machine type, output in kg/h, order changeover time in minutes, machine warehouse, hourly cost, default operator, the "Retired" flag and the "Working schedule" table — shifts by day of week; a shift may run past midnight, a round-the-clock shift is a checkbox. Calendar days (weekends and holidays) are non-working for the machine; for continuous operation select "Works without the working calendar".
- The machine list shows "Machine type", "Output, kg/h" and "Retired" columns; retired machines are hidden, "Show retired machines" shows them. A retired machine is not offered in new documents.
- "Machine maintenance" document (Production): scheduled maintenance, repair or breakdown, changeover; start and end, reason, performed by, costs. Planned maintenance reserves machine time; once done, clear "Planned" and enter the actual time. Two maintenance records of one machine at the same time are not posted.
- "Machine downtime" report (Production → Reports): downtime hours and number of cases by machine, type and reason for the period, available time by the machine schedule and downtime percentage during working time. If the working calendar for the year is empty, the report warns about it.
- In production settings, the "Move materials to the machine when scheduling" flag: for now it is only stored, it will work together with material requisitions.

### es
- Gestión de máquinas (Ajustes → Producción → «Gestión de máquinas»; disponible con la producción activada). El catálogo «Equipo de producción» ahora se llama «Máquinas» y está en «Producción → Normas» junto a las rutas; allí también está el «Calendario».
- En la ficha de la máquina (gestión de máquinas activada): tipo de máquina, rendimiento en kg/h, tiempo de cambio de pedido en minutos, almacén de la máquina, coste por hora, operador por defecto, casilla «Retirada» y tabla «Horario de trabajo» — turnos por día de la semana; un turno puede pasar la medianoche, un turno de 24 horas se marca con una casilla. Los días del calendario (fines de semana y festivos) no son laborables para la máquina; para funcionamiento continuo marque «Funciona sin el calendario laboral».
- La lista de máquinas muestra las columnas «Tipo de máquina», «Rendimiento, kg/h» y «Retirada»; las máquinas retiradas se ocultan, la casilla «Mostrar máquinas retiradas» las muestra. Una máquina retirada no se ofrece en documentos nuevos.
- Documento «Mantenimiento de máquina» (Producción): mantenimiento programado, reparación o avería, cambio de formato; inicio y fin, motivo, ejecutor, costes. El mantenimiento planificado reserva el tiempo de la máquina; una vez hecho, desmarque «Planificado» e indique la hora real. Dos mantenimientos de una misma máquina a la misma hora no se contabilizan.
- Informe «Paradas de máquinas» (Producción → Informes): horas de parada y número de casos por máquina, tipo y motivo en el período, tiempo disponible según el horario de la máquina y porcentaje de parada en horario laboral. Si el calendario laboral del año está vacío, el informe lo avisa.
- En los ajustes de producción, la casilla «Trasladar materiales a la máquina al planificar»: por ahora solo se guarda, funcionará junto con los vales de salida.

## 2.0.16.31
### ru
- Рабочее место закупок, тендеры (при включённых «Тендерах поставщиков»): на закладке «Потребность» в группировке «по заказу клиента» отметьте строки заказа и нажмите «Запросить предложения» — выберите поставщиков, каждому создаётся черновик предложения с материалами, количеством и ценой из его прайса. Повторно тому же поставщику по тем же материалам предложение не создаётся.
- Колонка «Тендер» показывает, сколько предложений запрошено и кто победитель. Внизу закладка «Предложения»: поставщик, цена товара, сумма в основной валюте, срок, сколько материалов дефицита закрывает предложение, победитель. Цены вводятся в самом предложении (двойной щелчок).
- «Победитель» выбирает предложение победителем тендера заказа клиента. «Заказать у победителя» создаёт заказ поставщику под заказ клиента в валюте, по договору и с режимом НДС предложения, по его ценам и на оставшийся дефицит; материалы без дефицита или с черновиком заказа пропускаются с пояснением. Повторно по закрытому дефициту заказ не создаётся.
- Исправлено: при одновременном выборе победителя двумя пользователями победителей могло стать два.

### fr
- Poste des achats, appels d'offres (avec « Appels d'offres fournisseurs » activé) : dans l'onglet « Besoin », regroupement « par commande client », cochez les lignes et cliquez sur « Demander des offres » — choisissez les fournisseurs ; chacun reçoit une offre brouillon avec les matières, la quantité et le prix de son tarif. Aucune nouvelle offre n'est créée pour le même fournisseur et les mêmes matières.
- La colonne « Appel d'offres » indique combien d'offres sont demandées et le gagnant. En bas, l'onglet « Offres » : fournisseur, prix de l'article, montant en devise principale, délai, nombre de matières en manque couvertes, gagnant. Les prix se saisissent dans l'offre (double clic).
- « Gagnant » désigne l'offre gagnante de l'appel d'offres de la commande client. « Commander au gagnant » crée la commande fournisseur pour la commande client dans la devise, selon le contrat et le mode TVA de l'offre, à ses prix et pour le manque restant ; les matières sans manque ou avec une commande brouillon sont ignorées avec une explication. Aucune nouvelle commande n'est créée pour un manque déjà couvert.
- Corrigé : si deux utilisateurs désignaient le gagnant en même temps, il pouvait y avoir deux gagnants.

### en
- Purchasing workstation, tenders (with "Supplier tenders" enabled): on the "Need" tab, grouping "by customer order", check the order lines and click "Request offers" — choose suppliers; each gets a draft offer with the materials, quantity and price from its price list. No new offer is created for the same supplier and materials.
- The "Tender" column shows how many offers were requested and who won. Below, the "Offers" tab: supplier, item price, amount in main currency, lead time, how many shortage materials the offer covers, winner. Prices are entered in the offer itself (double-click).
- "Winner" makes the offer the winner of the customer order tender. "Order from winner" creates the supplier order for the customer order in the offer's currency, contract and VAT mode, at its prices and for the remaining shortage; materials without shortage or with a draft order are skipped with an explanation. No new order is created for a shortage already covered.
- Fixed: when two users chose the winner at the same time, there could be two winners.

### es
- Puesto de compras, licitaciones (con «Licitaciones de proveedores» activado): en la pestaña «Necesidad», agrupación «por pedido del cliente», marque las líneas y pulse «Pedir ofertas» — elija los proveedores; cada uno recibe una oferta borrador con los materiales, la cantidad y el precio de su tarifa. No se crea otra oferta para el mismo proveedor y materiales.
- La columna «Licitación» muestra cuántas ofertas se pidieron y quién ganó. Abajo, la pestaña «Ofertas»: proveedor, precio del artículo, importe en moneda principal, plazo, cuántos materiales con déficit cubre la oferta, ganador. Los precios se introducen en la propia oferta (doble clic).
- «Ganador» hace la oferta ganadora de la licitación del pedido del cliente. «Pedir al ganador» crea el pedido a proveedor para el pedido del cliente en la moneda, contrato y modo de IVA de la oferta, a sus precios y por el déficit restante; los materiales sin déficit o con un borrador de pedido se omiten con una explicación. No se crea otro pedido para un déficit ya cubierto.
- Corregido: si dos usuarios elegían el ganador a la vez, podía haber dos ganadores.

## 2.0.16.30
### ru
- Рабочее место закупок: новая первая закладка «Потребность» — что нужно закупить. Источники: материалы заказов клиентов на производство, которые ещё не выпущены, и пополнение склада до минимального остатка (на складах с оповещением о минимальном остатке).
- По каждой строке видно: сколько нужно, заказано, пришло, взято со склада, есть на складе, дефицит, основной поставщик и последняя цена. Группировка — по товару (по умолчанию), по заказу клиента или по поставщику; флажок «Только с дефицитом». Внизу по выбранному товару — источники, заказы поставщикам и остатки по складам.
- Кнопка «Заказать»: отметьте строки, при необходимости поправьте поставщика и количество «К заказу». На каждый заказ клиента создаётся свой заказ поставщику (он закрывает дефицит этого заказа), на пополнение склада — отдельный заказ. Количество сверх дефицита уходит в заказ на пополнение.
- Повторное нажатие «Заказать» или устаревший экран не создают второй заказ: перед записью дефицит проверяется заново.

### fr
- Poste des achats : nouvel onglet en tête « Besoin » — ce qu'il faut acheter. Sources : matières des commandes clients en production pas encore fabriquées, et réapprovisionnement du stock jusqu'au minimum (entrepôts avec alerte de stock minimum).
- Pour chaque ligne : besoin, commandé, reçu, pris du stock, en stock, manque, fournisseur principal et dernier prix. Regroupement par article (par défaut), par commande client ou par fournisseur ; case « Seulement en manque ». En bas, pour l'article sélectionné : sources, commandes fournisseurs et stocks par entrepôt.
- Bouton « Commander » : cochez les lignes, corrigez au besoin le fournisseur et la quantité « À commander ». Chaque commande client reçoit sa propre commande fournisseur (elle couvre son manque), le réapprovisionnement une commande séparée. La quantité au-delà du manque va dans la commande de réapprovisionnement.
- Un second clic sur « Commander » ou un écran périmé ne crée pas de deuxième commande : le manque est revérifié avant l'enregistrement.

### en
- Purchasing workstation: new first tab "Need" — what has to be purchased. Sources: materials of customer production orders not yet produced, and stock replenishment up to the minimum (warehouses with a minimum stock alert).
- Each line shows: needed, ordered, received, taken from stock, in stock, shortage, main supplier and last price. Grouping by item (default), by customer order or by supplier; "Shortage only" check box. Below, for the selected item: sources, supplier orders and stock by warehouse.
- "Order" button: check the lines, adjust the supplier and the "To order" quantity if needed. Each customer order gets its own supplier order (it covers that order's shortage), replenishment gets a separate order. Quantity above the shortage goes to the replenishment order.
- Clicking "Order" again or a stale screen does not create a second order: the shortage is checked again before saving.

### es
- Puesto de compras: nueva primera pestaña «Necesidad» — lo que hay que comprar. Orígenes: materiales de pedidos de clientes en producción aún no fabricados, y reposición del almacén hasta el mínimo (almacenes con aviso de stock mínimo).
- Cada línea muestra: necesario, pedido, recibido, tomado del almacén, en almacén, déficit, proveedor principal y último precio. Agrupación por artículo (por defecto), por pedido del cliente o por proveedor; casilla «Solo con déficit». Abajo, para el artículo seleccionado: orígenes, pedidos a proveedores y existencias por almacén.
- Botón «Pedir»: marque las líneas, corrija si hace falta el proveedor y la cantidad «A pedir». Cada pedido del cliente recibe su propio pedido a proveedor (cubre su déficit), la reposición un pedido aparte. La cantidad por encima del déficit va al pedido de reposición.
- Pulsar «Pedir» de nuevo o una pantalla desactualizada no crea un segundo pedido: el déficit se vuelve a comprobar antes de guardar.

## 2.0.16.29
### ru
- Рабочее место закупок: строки выбранного заказа поставщику вводятся прямо на закладке «Товары» — товар, количество, упаковка, цена; новая позиция берёт цену из прайса поставщика. Правка проведённого заказа перепроводит его. Строку можно добавить в заказ любой даты, не только сегодняшний.
- Закладка «Поступления»: новая строка — выбор строки заказа с остатком, количество и номер накладной поставщика. Строки с тем же номером накладной попадают в одно поступление.
- Кнопка «Изменить статус» над списком заказов: «В работу» (провести), «В черновик», «Отменить» (пометить на удаление) — для всех выделенных заказов сразу. Заказ с поступлениями в черновик не уходит.
- Новая закладка «К поступлению»: все строки проведённых заказов, по которым ещё ждём товар, — поставщик, заказ, товар, сколько осталось, дата поставки, просрочка. Отметьте строки одного поставщика, укажите номер и дату накладной и нажмите «Оформить поступление»: на каждый заказ создаётся своё поступление с этой накладной. Если хоть одна строка не подходит, поступление по заказу не создаётся совсем.
- Поступление по заказу поставщику в валюте теперь создаётся в валюте заказа по курсу на дату поступления (раньше — в основной валюте). Это исправляет и рабочее место производства. Цена из прайса поставщика пересчитывается в валюту заказа.
- Строки предварительного заказа, которые забрал другой заказ, больше нельзя уменьшить, удалить или снять с проведения: это увело бы остатки в минус. Заказ, забравший чужие строки, в рабочем месте только просматривается — правьте его в форме документа.
- Проведение заказа поставщику, поступления и возврата поставщику блокирует остатки заказа. Если двое одновременно оформляют поступление по одной строке, второе оформление по уже полностью поступившей строке отклоняется, а не принимает товар дважды.

### fr
- Poste des achats : les lignes de la commande fournisseur sélectionnée se saisissent directement dans l'onglet « Articles » — article, quantité, conditionnement, prix ; une nouvelle ligne prend le prix du tarif du fournisseur. Modifier une commande validée la revalide. Une ligne peut s'ajouter à une commande de n'importe quelle date, pas seulement du jour.
- Onglet « Réceptions » : une nouvelle ligne — choix de la ligne de commande avec reste, quantité et numéro de facture du fournisseur. Les lignes avec le même numéro de facture vont dans la même réception.
- Bouton « Changer le statut » au-dessus de la liste des commandes : « En cours » (valider), « En brouillon », « Annuler » (marquer pour suppression) — pour toutes les commandes sélectionnées à la fois. Une commande avec des réceptions ne repasse pas en brouillon.
- Nouvel onglet « À réceptionner » : toutes les lignes des commandes validées encore attendues — fournisseur, commande, article, reste, date de livraison, retard. Cochez les lignes d'un fournisseur, indiquez le numéro et la date de la facture et cliquez sur « Enregistrer la réception » : chaque commande reçoit sa propre réception avec cette facture. Si une seule ligne ne convient pas, aucune réception n'est créée pour la commande.
- La réception d'une commande fournisseur en devise se crée maintenant dans la devise de la commande au taux de la date de réception (auparavant en devise principale). Cela corrige aussi le poste de production. Le prix du tarif fournisseur est converti dans la devise de la commande.
- Les lignes d'une commande préliminaire reprises par une autre commande ne peuvent plus être diminuées, supprimées ou dévalidées : les restes deviendraient négatifs. La commande qui a repris ces lignes est en lecture seule dans le poste — modifiez-la dans le formulaire du document.
- La validation d'une commande fournisseur, d'une réception et d'un retour fournisseur verrouille les restes de la commande. Si deux personnes enregistrent en même temps une réception sur la même ligne, la seconde est refusée lorsque la ligne est déjà entièrement reçue, au lieu de recevoir la marchandise deux fois.

### en
- Purchasing workstation: lines of the selected supplier order are entered right on the "Items" tab — item, quantity, packaging, price; a new line takes the price from the supplier price list. Editing a posted order reposts it. A line can be added to an order of any date, not only today's.
- "Receipts" tab: a new line — choose an order line with a remaining quantity, the quantity and the supplier invoice number. Lines with the same invoice number go into one receipt.
- "Change status" button above the order list: "In progress" (post), "To draft", "Cancel" (mark for deletion) — for all selected orders at once. An order with receipts does not go back to draft.
- New "To receive" tab: all lines of posted orders still awaited — supplier, order, item, remaining, delivery date, overdue. Check the lines of one supplier, enter the invoice number and date and click "Register receipt": each order gets its own receipt with this invoice. If any line does not fit, no receipt is created for that order.
- A receipt for a supplier order in a foreign currency is now created in the order currency at the rate of the receipt date (previously in the main currency). This also fixes the production workstation. The supplier price list price is converted to the order currency.
- Lines of a preliminary order taken by another order can no longer be reduced, deleted or unposted: that would make balances negative. The order that took those lines is read-only in the workstation — edit it in the document form.
- Posting a supplier order, a receipt and a return to supplier locks the order balances. If two people register a receipt for the same line at the same time, the second one is rejected once the line is fully received, instead of receiving the goods twice.

### es
- Puesto de compras: las líneas del pedido a proveedor seleccionado se introducen directamente en la pestaña «Artículos» — artículo, cantidad, embalaje, precio; una línea nueva toma el precio de la tarifa del proveedor. Editar un pedido contabilizado lo vuelve a contabilizar. Se puede añadir una línea a un pedido de cualquier fecha, no solo de hoy.
- Pestaña «Recepciones»: una línea nueva — elección de la línea del pedido con pendiente, cantidad y número de factura del proveedor. Las líneas con el mismo número de factura van a una sola recepción.
- Botón «Cambiar estado» sobre la lista de pedidos: «En curso» (contabilizar), «A borrador», «Cancelar» (marcar para eliminar) — para todos los pedidos seleccionados a la vez. Un pedido con recepciones no vuelve a borrador.
- Nueva pestaña «Por recibir»: todas las líneas de pedidos contabilizados aún pendientes — proveedor, pedido, artículo, pendiente, fecha de entrega, retraso. Marque las líneas de un proveedor, indique el número y la fecha de la factura y pulse «Registrar recepción»: cada pedido recibe su propia recepción con esa factura. Si una sola línea no encaja, no se crea ninguna recepción para ese pedido.
- La recepción de un pedido a proveedor en divisa se crea ahora en la divisa del pedido al tipo de la fecha de recepción (antes, en la moneda principal). Esto corrige también el puesto de producción. El precio de la tarifa del proveedor se convierte a la divisa del pedido.
- Las líneas de un pedido preliminar tomadas por otro pedido ya no se pueden reducir, eliminar ni descontabilizar: los saldos quedarían negativos. El pedido que tomó esas líneas es de solo lectura en el puesto: edítelo en el formulario del documento.
- La contabilización de un pedido a proveedor, una recepción y una devolución al proveedor bloquea los saldos del pedido. Si dos personas registran a la vez una recepción de la misma línea, la segunda se rechaza cuando la línea ya está recibida por completo, en lugar de recibir la mercancía dos veces.

## 2.0.16.28
### ru
- Новое рабочее место закупок (Закупки → Рабочее место закупок): заказы поставщикам одним списком со статусом — черновик, ожидает поставки, просрочен, частично поступил, поступил, перенесён в другой заказ, отменён. Кружки показывают, сколько пришло и сколько оплачено.
- Отборы справа: поставщик, товар, статус, дата поставки, ответственный, вид заказа. Предварительные заказы видны только при отборе по виду заказа. Список листается страницами по 50 заказов.
- По выбранному заказу внизу: товары (заказано, пришло, осталось), поступления с номером накладной поставщика, оплаты и долг или аванс по договору, все документы цепочки. Двойной щелчок открывает документ, после закрытия список обновляется. Кнопка «Создать» открывает новый заказ поставщику.
- Исправлено: форма документа «Прочие расходы» не открывалась после сборки 2.0.16.25 (пересчёт суммы в основной валюте при смене курса).

### fr
- Nouveau poste des achats (Achats → Poste des achats) : les commandes fournisseurs dans une seule liste avec leur statut — brouillon, en attente de livraison, en retard, partiellement reçue, reçue, transférée vers une autre commande, annulée. Les cercles montrent ce qui est reçu et ce qui est payé.
- Filtres à droite : fournisseur, article, statut, date de livraison, responsable, type de commande. Les commandes préliminaires ne s'affichent qu'avec le filtre par type. La liste se parcourt par pages de 50 commandes.
- Pour la commande sélectionnée, en bas : articles (commandé, reçu, reste), réceptions avec le numéro de facture du fournisseur, paiements et dette ou avance au titre du contrat, tous les documents de la chaîne. Un double clic ouvre le document ; à sa fermeture la liste se met à jour. Le bouton « Créer » ouvre une nouvelle commande fournisseur.
- Corrigé : le formulaire du document « Autres dépenses » ne s'ouvrait plus depuis la version 2.0.16.25 (recalcul du montant en devise principale au changement de taux).

### en
- New purchasing workstation (Purchasing → Purchasing workstation): supplier orders in one list with their status — draft, awaiting delivery, overdue, partially received, received, transferred to another order, cancelled. Circles show what has been received and what has been paid.
- Filters on the right: supplier, item, status, delivery date, responsible, order type. Preliminary orders are shown only with the order type filter. The list is paged by 50 orders.
- For the selected order, below: items (ordered, received, remaining), receipts with the supplier invoice number, payments and the debt or advance under the contract, all documents of the chain. Double-click opens a document; the list refreshes when it is closed. The "Create" button opens a new supplier order.
- Fixed: the "Other expenses" document form did not open since build 2.0.16.25 (recalculation of the amount in the main currency when the rate changes).

### es
- Nuevo puesto de compras (Compras → Puesto de compras): los pedidos a proveedores en una sola lista con su estado — borrador, pendiente de entrega, retrasado, recibido parcialmente, recibido, transferido a otro pedido, cancelado. Los círculos muestran lo recibido y lo pagado.
- Filtros a la derecha: proveedor, artículo, estado, fecha de entrega, responsable, tipo de pedido. Los pedidos preliminares solo se ven con el filtro por tipo. La lista se pasa por páginas de 50 pedidos.
- Para el pedido seleccionado, abajo: artículos (pedido, recibido, pendiente), recepciones con el número de factura del proveedor, pagos y la deuda o el anticipo según el contrato, todos los documentos de la cadena. Doble clic abre el documento; al cerrarlo la lista se actualiza. El botón «Crear» abre un nuevo pedido a proveedor.
- Corregido: el formulario del documento «Otros gastos» no se abría desde la versión 2.0.16.25 (recálculo del importe en la moneda principal al cambiar el tipo).

## 2.0.16.27
### ru
- Кнопки перехода по страницам под списками: доступная кнопка выделена цветом, недоступная — блёклая. Сразу видно, куда можно перейти.
- Рабочее место производства: легенда кружков растянута на всю ширину и прижата к правому краю, в одну строку.

### fr
- Boutons de navigation entre les pages sous les listes : un bouton disponible est en couleur, un bouton indisponible est estompé. On voit tout de suite où l'on peut aller.
- Poste de production : la légende des cercles occupe toute la largeur, alignée à droite, sur une seule ligne.

### en
- Page navigation buttons under lists: an available button is colored, an unavailable one is faded. You can see at once where you can go.
- Production workplace: the circle legend spans the full width, right-aligned, on one line.

### es
- Botones de navegación entre páginas bajo las listas: un botón disponible aparece en color, uno no disponible aparece atenuado. Se ve enseguida adónde se puede ir.
- Puesto de producción: la leyenda de los círculos ocupa todo el ancho, alineada a la derecha, en una sola línea.

## 2.0.16.26
### ru
- Закладка окна печати подписана названием печатной формы (например, «Счёт на бланке»), а при нескольких формах — «Печать документов». Раньше заголовок закладки был пустым.

### fr
- L'onglet de la fenêtre d'impression porte le nom du formulaire imprimable (par exemple « Facture sur papier à en-tête »), et avec plusieurs formulaires — « Impression des documents ». Auparavant le titre de l'onglet était vide.

### en
- The print window tab now shows the print form name (for example "Invoice on letterhead"), or "Print documents" when there are several forms. Previously the tab title was empty.

### es
- La pestaña de la ventana de impresión muestra el nombre del formulario de impresión (por ejemplo «Factura en papel con membrete»), y con varios formularios — «Impresión de documentos». Antes el título de la pestaña estaba vacío.

## 2.0.16.25
### ru
- Возврат от покупателя по реализации в валюте теперь проводится: валюта и курс берутся из реализации (флажок, валюта и курс видны, но не правятся), цены и суммы — в валюте, колонка «Сумма (MAD)». Возврат закрывает долг реализации и в валюте, и в основной валюте без курсовой разницы, товар возвращается по себестоимости в основной валюте.
- Налоговая накладная по реализациям в валюте ведётся в их валюте, курс — по отгрузкам. Долг и оплаты переходят с реализаций на накладную в обеих суммах, налоговый учёт — в основной валюте. Отгрузки в разных валютах в одну накладную не входят. Налоговый возврат по накладной в валюте — тоже в её валюте.
- Прочие расходы и их возврат можно оформлять в валюте: флажок «В валюте», валюта и курс. В расходах и в долге они учитываются в основной валюте по курсу. Возврат берёт валюту и курс расходов, РКО и списание на основании — сумму в основной валюте по курсу расходов.
- Услуги переработчика в «Поступлении из переработки» можно указать в валюте. Долг переработчику ведётся в валюте, в себестоимость продукции стоимость услуг попадает в основной валюте по курсу.
- Корректировка долга и сертификат на оплату по документам в валюте подставляют сумму в основной валюте (по курсу документа), колонка подписана основной валютой.
- РКО на основании валютного возврата берёт сумму по курсу на дату платежа. Печать налоговой накладной пишет сумму прописью в валюте документа.

### fr
- Le retour client d'une vente en devise est désormais comptabilisé : la devise et le taux sont repris de la vente (case, devise et taux visibles mais non modifiables), prix et montants en devise, colonne « Montant (MAD) ». Le retour solde la dette de la vente en devise et en devise principale sans écart de change, la marchandise revient au coût en devise principale.
- La facture fiscale des ventes en devise est tenue dans leur devise, au taux des expéditions. La dette et les paiements passent des ventes à la facture dans les deux montants, la comptabilité fiscale reste en devise principale. Des expéditions en devises différentes ne vont pas dans une même facture. Le retour fiscal d'une facture en devise est aussi dans sa devise.
- Les autres dépenses et leur retour peuvent être saisis en devise : case « En devise », devise et taux. Dans les charges et la dette ils sont comptés en devise principale au taux. Le retour reprend la devise et le taux des dépenses ; le décaissement et le virement saisis à partir d'elles prennent le montant en devise principale au taux des dépenses.
- Les services du sous-traitant dans la « Réception de sous-traitance » peuvent être indiqués en devise. La dette envers le sous-traitant est tenue en devise ; le coût des services entre dans le coût des produits en devise principale au taux.
- La régularisation de dette et le certificat de paiement sur des documents en devise proposent le montant en devise principale (au taux du document) ; la colonne indique la devise principale.
- Un décaissement saisi à partir d'un retour en devise prend le montant au taux du jour du paiement. L'impression de la facture fiscale écrit le montant en lettres dans la devise du document.

### en
- A customer return for a foreign-currency sale can now be posted: currency and rate are taken from the sale (checkbox, currency and rate are shown but not editable), prices and amounts in the currency, an "Amount (MAD)" column. The return closes the sale debt both in the currency and in base currency without an exchange difference; goods come back at cost in base currency.
- A tax invoice for foreign-currency sales is kept in their currency at the shipments' rate. Debt and payments move from the sales to the invoice in both amounts; tax accounting stays in base currency. Shipments in different currencies cannot be in one invoice. A tax return on a foreign-currency invoice is in its currency too.
- Other expenses and their return can be entered in a foreign currency: "In currency" checkbox, currency and rate. Expenses and debt record them in base currency at the rate. The return takes the expenses' currency and rate; a cash or bank payment entered from them takes the amount in base currency at the expenses' rate.
- Processor services in "Receipt from processing" can be entered in a foreign currency. The debt to the processor is kept in the currency; the services cost enters the product cost in base currency at the rate.
- Debt adjustment and payment certificate for foreign-currency documents suggest the amount in base currency (at the document rate); the column shows the base currency.
- A cash payment entered from a foreign-currency return takes the amount at the rate on the payment date. The tax invoice print writes the amount in words in the document currency.

### es
- La devolución de cliente de una venta en moneda ahora se contabiliza: la moneda y el tipo se toman de la venta (casilla, moneda y tipo visibles pero no editables), precios e importes en moneda, columna «Importe (MAD)». La devolución cierra la deuda de la venta en moneda y en moneda principal sin diferencia de cambio; la mercancía vuelve al coste en moneda principal.
- La factura fiscal de ventas en moneda se lleva en su moneda, al tipo de los envíos. La deuda y los pagos pasan de las ventas a la factura en ambos importes; la contabilidad fiscal sigue en moneda principal. Envíos en monedas distintas no entran en una misma factura. La devolución fiscal de una factura en moneda también va en su moneda.
- Los otros gastos y su devolución se pueden registrar en moneda: casilla «En moneda», moneda y tipo. En gastos y deuda se cuentan en moneda principal al tipo. La devolución toma la moneda y el tipo de los gastos; el pago en caja o banco introducido a partir de ellos toma el importe en moneda principal al tipo de los gastos.
- Los servicios del transformador en la «Recepción de transformación» se pueden indicar en moneda. La deuda con el transformador se lleva en moneda; el coste de los servicios entra en el coste de los productos en moneda principal al tipo.
- El ajuste de deuda y el certificado de pago sobre documentos en moneda proponen el importe en moneda principal (al tipo del documento); la columna indica la moneda principal.
- Un pago en caja introducido a partir de una devolución en moneda toma el importe al tipo del día del pago. La impresión de la factura fiscal escribe el importe en letras en la moneda del documento.

## 2.0.16.24
### ru
- Заказ клиента, заказ поставщику, коммерческое предложение и предложение поставщика можно оформлять в валюте — так же, как поступление и реализацию: флажок «В валюте», валюта и курс, цены и суммы в валюте документа, колонка «Сумма (MAD)», курс по дате, валюта из договора, вопрос о пересчёте цен при смене валюты.
- При вводе на основании валюта переносится: реализация из заказа клиента, поступление из заказа поставщику, заказ клиента из коммерческого предложения, заказ поставщику из предложения поставщика. Курс берётся на дату нового документа. «Перезаполнить цены по заказу» в реализации пересчитывает цены заказа в валюту реализации.
- Оплата и долг по валютному заказу, стадия заказа и картинка оплаты в списке считаются в основной валюте. Аванс по заказу в валюте ведётся в основной валюте и зачитывается реализацией.
- Тендер сравнивает предложения поставщиков в разных валютах по сумме в основной валюте, а предупреждение «есть предложение дешевле» показывает сумму с валютой.
- Последние цены закупки и продажи и процент наценки в документе в валюте считаются в валюте документа. Раньше наценка в реализации в евро считалась от закупочной цены в дирхамах.
- «Заказы поставщикам» по валютному заказу пишутся в основной валюте. ПКО на основании валютной реализации берёт сумму по курсу на дату оплаты, на основании валютного заказа — по курсу заказа: аванс по заказу ведётся в основной валюте.
- Ввод на основании документа в валюте (в том числе реализации из поступления) теперь берёт курс на дату нового документа, а не курс основания. Копия документа в валюте тоже получает курс на свою дату.
- Форма заказа для интернет-магазина валюты не знает: валютный заказ в ней открывается только для просмотра.

### fr
- La commande client, la commande fournisseur, l'offre commerciale et l'offre fournisseur peuvent être établies en devise, comme la réception et la vente : case « En devise », devise et taux, prix et montants dans la devise du document, colonne « Montant (MAD) », taux à la date, devise du contrat, question de conversion des prix au changement de devise.
- À la saisie à partir d'un document, la devise est reprise : vente depuis la commande client, réception depuis la commande fournisseur, commande client depuis l'offre commerciale, commande fournisseur depuis l'offre fournisseur. Le taux est pris à la date du nouveau document. « Réappliquer les prix de la commande » dans la vente convertit les prix de la commande dans la devise de la vente.
- Le paiement et la dette d'une commande en devise, l'étape de la commande et l'icône de paiement de la liste sont calculés en devise principale. L'acompte sur une commande en devise est tenu en devise principale et imputé par la vente.
- L'appel d'offres compare les offres fournisseurs en différentes devises par le montant en devise principale, et l'avertissement « il y a une offre moins chère » affiche le montant avec la devise.
- Les derniers prix d'achat et de vente et le pourcentage de marge d'un document en devise sont calculés dans la devise du document. Auparavant la marge d'une vente en euros était calculée sur le prix d'achat en dirhams.
- Les « Commandes fournisseurs » d'une commande en devise sont enregistrées en devise principale. Un encaissement saisi à partir d'une vente en devise prend le montant au taux du jour du paiement, à partir d'une commande en devise — au taux de la commande : l'acompte sur commande est tenu en devise principale.
- La saisie à partir d'un document en devise (y compris une vente depuis une réception) prend désormais le taux à la date du nouveau document, et non celui du document de base. La copie d'un document en devise reçoit aussi le taux à sa date.
- Le formulaire de commande de la boutique en ligne ne connaît pas les devises : une commande en devise s'y ouvre en lecture seule.

### en
- Customer orders, supplier orders, commercial offers and supplier offers can be issued in a foreign currency, like receipts and sales: "In currency" checkbox, currency and rate, prices and amounts in the document currency, an "Amount (MAD)" column, rate for the date, contract currency, a question about converting prices when the currency changes.
- When a document is entered from another, the currency is carried over: sale from customer order, receipt from supplier order, customer order from commercial offer, supplier order from supplier offer. The rate is taken for the new document's date. "Refill prices from order" in a sale converts order prices to the sale currency.
- Payment and debt of a foreign-currency order, the order stage and the payment icon in the list are calculated in base currency. An advance on a foreign-currency order is kept in base currency and offset by the sale.
- The tender compares supplier offers in different currencies by the amount in base currency, and the "there is a cheaper offer" warning shows the amount with its currency.
- Last purchase and sale prices and the markup percentage of a foreign-currency document are calculated in the document currency. Previously the markup of a sale in euros was calculated from the purchase price in dirhams.
- "Supplier orders" for a foreign-currency order are recorded in base currency. A cash receipt entered from a foreign-currency sale takes the amount at the rate on the payment date; from a foreign-currency order — at the order rate, since the order advance is kept in base currency.
- Entering a document from a foreign-currency one (including a sale from a receipt) now takes the rate for the new document's date instead of the source rate. A copy of a foreign-currency document also gets the rate for its date.
- The online store order form has no currency: a foreign-currency order opens there read-only.

### es
- El pedido de cliente, el pedido a proveedor, la oferta comercial y la oferta de proveedor se pueden emitir en moneda, como la recepción y la venta: casilla «En moneda», moneda y tipo de cambio, precios e importes en la moneda del documento, columna «Importe (MAD)», tipo a la fecha, moneda del contrato, pregunta de conversión de precios al cambiar la moneda.
- Al introducir un documento a partir de otro, la moneda se traslada: venta desde pedido de cliente, recepción desde pedido a proveedor, pedido de cliente desde oferta comercial, pedido a proveedor desde oferta de proveedor. El tipo se toma a la fecha del nuevo documento. «Volver a rellenar precios del pedido» en la venta convierte los precios del pedido a la moneda de la venta.
- El pago y la deuda de un pedido en moneda, la etapa del pedido y el icono de pago de la lista se calculan en moneda principal. El anticipo de un pedido en moneda se lleva en moneda principal y se compensa con la venta.
- La licitación compara ofertas de proveedores en distintas monedas por el importe en moneda principal, y el aviso «hay una oferta más barata» muestra el importe con la moneda.
- Los últimos precios de compra y venta y el porcentaje de margen de un documento en moneda se calculan en la moneda del documento. Antes el margen de una venta en euros se calculaba sobre el precio de compra en dírhams.
- Los «Pedidos a proveedores» de un pedido en moneda se registran en moneda principal. Un cobro introducido a partir de una venta en moneda toma el importe al tipo del día del pago; a partir de un pedido en moneda — al tipo del pedido, ya que el anticipo del pedido se lleva en moneda principal.
- Al introducir un documento a partir de otro en moneda (también una venta desde una recepción) ahora se toma el tipo a la fecha del nuevo documento y no el del documento base. La copia de un documento en moneda también recibe el tipo a su fecha.
- El formulario de pedido de la tienda online no conoce monedas: un pedido en moneda se abre allí solo para lectura.

## 2.0.16.23
### ru
- ПКО, РКО, поступление и списание безналичных ведутся в валюте кассы или банковского счёта: у евро-счёта платёж в евро. Валюта видна рядом с суммой и задаётся кассой или счётом, курс подставляется на дату платежа и правится вручную. Без курса платёж в валюте не проводится.
- Остаток валютной кассы или счёта учитывается и в основной валюте, и в валюте кассы или счёта.
- Курсовые разницы. Оплата закрывает долг в валюте полностью, а разница между деньгами и долгом в основной валюте записывается по новой статье «Курсовые разницы»: при поступлении денег — доход, при списании — расход. Оплата валютного долга дирхамами закрывает его по курсу на дату оплаты.
- Отчёт «Финансовый результат» и таблица прибылей и убытков показывают курсовые разницы отдельной строкой «2.4. Écarts de change». В чистую прибыль магазина для премий они не входят.
- При вводе оплаты на основании документа и при заполнении по долгам суммы пересчитываются в валюту кассы или счёта.
- Исправлено: списание безналичных при оплате поступления в валюте больше не берёт валюту поступления — валюта всегда та, что у счёта. Печать ПКО, РКО и платёжного поручения показывает валюту документа.
- В валюте проводятся только оплаты клиентов и поставщиков (не чеком) и перемещения денег между кассами и счетами одной валюты. Кассовая смена работает только с кассой в основной валюте. Если в документе выбрать кассу или счёт в другой валюте, сумма и строки оснований пересчитываются в новую валюту. Платежи, оформленные до обновления, остаются в основной валюте.

### fr
- Les encaissements, décaissements, virements reçus et émis sont tenus dans la devise de la caisse ou du compte bancaire : depuis un compte en euros, le paiement est en euros. La devise s'affiche à côté du montant et vient de la caisse ou du compte, le taux est proposé à la date du paiement et peut être modifié. Sans taux, un paiement en devise n'est pas validé.
- Le solde d'une caisse ou d'un compte en devise est suivi à la fois en devise principale et dans la devise de la caisse ou du compte.
- Écarts de change. Le paiement solde entièrement la dette en devise, et l'écart entre l'argent et la dette en devise principale est enregistré sur le nouveau poste « Écarts de change » : gain à l'encaissement, perte au décaissement. Une dette en devise réglée en dirhams est soldée au taux du jour du paiement.
- Le rapport « Résultat financier » et le tableau des profits et pertes montrent les écarts de change sur une ligne séparée « 2.4. Écarts de change ». Ils ne sont pas inclus dans le bénéfice net du magasin pour les primes.
- À la saisie d'un paiement à partir d'un document et au remplissage par les dettes, les montants sont convertis dans la devise de la caisse ou du compte.
- Corrigé : un virement émis pour une réception en devise ne reprend plus la devise de la réception — la devise est toujours celle du compte. L'impression des encaissements, décaissements et ordres de virement indique la devise du document.
- En devise, seuls les paiements clients et fournisseurs (hors chèque) et les transferts de fonds entre caisses et comptes de même devise sont validés. La session de caisse ne fonctionne qu'avec une caisse en devise principale. Si l'on choisit dans le document une caisse ou un compte d'une autre devise, le montant et les lignes sont convertis dans la nouvelle devise. Les paiements saisis avant la mise à jour restent en devise principale.

### en
- Cash receipts, cash payments, bank receipts and bank payments are kept in the currency of the cash desk or bank account: from a euro account the payment is in euros. The currency is shown next to the amount and comes from the cash desk or account; the rate is filled in for the payment date and can be edited. Without a rate a foreign-currency payment is not posted.
- The balance of a foreign-currency cash desk or account is tracked both in base currency and in its own currency.
- Exchange differences. A payment closes the debt in currency completely, and the difference between the money and the debt in base currency is recorded under the new "Exchange differences" item: a gain on receipt, a loss on payment. A currency debt paid in dirhams is closed at the rate on the payment date.
- The "Financial result" report and the profit and loss table show exchange differences on a separate "2.4. Écarts de change" line. They are not included in the store's net profit for bonuses.
- When a payment is entered from a document or filled from debts, amounts are converted to the currency of the cash desk or account.
- Fixed: a bank payment for a foreign-currency receipt no longer takes the receipt's currency — the currency is always the account's. Printed cash receipts, cash payments and payment orders show the document currency.
- In a foreign currency only customer and supplier payments (not by cheque) and transfers between cash desks and accounts of the same currency can be posted. A cash session works only with a cash desk in base currency. Choosing a cash desk or account in another currency converts the amount and lines to the new currency. Payments entered before the update stay in base currency.

### es
- Los cobros y pagos en caja, los ingresos y las transferencias bancarias se llevan en la moneda de la caja o de la cuenta bancaria: desde una cuenta en euros el pago es en euros. La moneda se muestra junto al importe y viene de la caja o la cuenta; el tipo de cambio se rellena a la fecha del pago y se puede corregir. Sin tipo de cambio, un pago en moneda no se contabiliza.
- El saldo de una caja o cuenta en moneda se lleva tanto en moneda principal como en su propia moneda.
- Diferencias de cambio. El pago cierra por completo la deuda en moneda, y la diferencia entre el dinero y la deuda en moneda principal se registra en la nueva partida «Diferencias de cambio»: ganancia al cobrar, pérdida al pagar. Una deuda en moneda pagada en dírhams se cierra al tipo de la fecha del pago.
- El informe «Resultado financiero» y la tabla de pérdidas y ganancias muestran las diferencias de cambio en una línea aparte «2.4. Écarts de change». No se incluyen en el beneficio neto de la tienda para las primas.
- Al introducir un pago a partir de un documento y al rellenarlo por deudas, los importes se convierten a la moneda de la caja o la cuenta.
- Corregido: una transferencia emitida para una recepción en moneda ya no toma la moneda de la recepción — la moneda es siempre la de la cuenta. La impresión de cobros, pagos y órdenes de transferencia indica la moneda del documento.
- En moneda solo se contabilizan pagos de clientes y proveedores (sin cheque) y traspasos entre cajas y cuentas de la misma moneda. El turno de caja solo funciona con una caja en moneda principal. Al elegir en el documento una caja o cuenta de otra moneda, el importe y las líneas se convierten a la nueva moneda. Los pagos introducidos antes de la actualización siguen en moneda principal.

## 2.0.16.22
### ru
- «Поступление товаров» и «Реализация товаров» можно оформлять в валюте. На первой закладке появился флажок «В валюте»: он открывает поля «Валюта» и «Курс». Без флажка документ, как и раньше, ведётся в основной валюте (константа «Валюта регламентированного учёта»).
- Курс подставляется по дате документа из нового справочника курсов «Казначейство — Курсы валют» и правится вручную. Если на дату курса нет, программа об этом скажет. Договор с валютой взаиморасчётов, отличной от основной, сам включает флажок и ставит эту валюту.
- В документе в валюте колонки «Цена» и «Сумма» в товарах и услугах подписаны валютой документа, например «Цена (EUR)», и открывается колонка «Сумма (MAD)» — сумма в основной валюте по курсу. При смене валюты программа предложит пересчитать цены строк в новую валюту.
- У вида цен появился реквизит «Валюта». Цены подбираются с учётом валюты: цена вида цен в евро в документе в дирхамах пересчитывается в дирхамы по курсу на дату, в документе в евро подставляется как есть. Цены поставщиков и фиксированные цены клиентов считаются в основной валюте и тоже пересчитываются в валюту документа.
- При проведении в регистры попадает сумма в основной валюте: себестоимость товаров на складе и дополнительных расходов, выручка и прибыль в продажах, цены поставщиков, заказы поставщикам и взаиморасчёты. Взаиморасчёты дополнительно хранят валюту и сумму в валюте. Оплата в основной валюте закрывает долг по документу в валюте; курсовые разницы пока не считаются.
- Печать реализации подписывает валюту документа, сумма прописью — в валюте документа.
- Возврат от покупателя и налоговая накладная по реализации в валюте пока не поддерживаются: программа не даст их провести.
- При обновлении поступления, уже оформленные в другой валюте, получают флажок «В валюте», их взаиморасчёты и заказы поставщикам пересчитываются в основную валюту.

### fr
- Les « Réceptions de marchandises » et les « Ventes de marchandises » peuvent être établies en devise. Sur le premier onglet, une nouvelle case « En devise » ouvre les champs « Devise » et « Taux ». Sans cette case, le document reste comme avant dans la devise principale (constante « Devise de comptabilité réglementée »).
- Le taux est proposé à la date du document depuis le nouveau registre « Trésorerie — Taux de change » et peut être modifié à la main. S'il n'y a pas de taux à cette date, le programme le signale. Un contrat dont la devise de règlement diffère de la devise principale coche la case et met cette devise.
- Dans un document en devise, les colonnes « Prix » et « Montant » des marchandises et des services portent la devise du document, par exemple « Prix (EUR) », et la colonne « Montant (MAD) » apparaît : le montant en devise principale au taux. Au changement de devise, le programme propose de convertir les prix des lignes.
- Le type de prix reçoit un attribut « Devise ». Les prix sont repris en tenant compte de la devise : un prix en euros dans un document en dirhams est converti en dirhams au taux du jour, dans un document en euros il est repris tel quel. Les prix fournisseurs et les prix fixes des clients sont considérés en devise principale et sont aussi convertis dans la devise du document.
- À la validation, les registres reçoivent le montant en devise principale : coût des marchandises en stock et des frais supplémentaires, chiffre d'affaires et marge des ventes, prix fournisseurs, commandes fournisseurs et règlements. Les règlements conservent en plus la devise et le montant en devise. Un paiement en devise principale solde la dette d'un document en devise ; les écarts de change ne sont pas encore calculés.
- L'impression de la vente indique la devise du document, le montant en lettres est dans la devise du document.
- Le retour client et la facture fiscale sur une vente en devise ne sont pas encore pris en charge : le programme refuse de les valider.
- À la mise à jour, les réceptions déjà établies dans une autre devise reçoivent la case « En devise », leurs règlements et commandes fournisseurs sont convertis en devise principale.

### en
- "Goods receipt" and "Goods sale" documents can now be issued in a foreign currency. A new "In currency" checkbox on the first tab opens the "Currency" and "Rate" fields. Without it, the document stays in the base currency as before (the "Regulated accounting currency" constant).
- The rate is filled in for the document date from the new "Treasury — Exchange rates" register and can be edited by hand. If there is no rate for that date, the program says so. A contract whose settlement currency differs from the base currency checks the box and sets that currency.
- In a foreign-currency document, the "Price" and "Amount" columns of goods and services show the document currency, for example "Price (EUR)", and an "Amount (MAD)" column appears: the amount in base currency at the rate. When the currency changes, the program offers to convert line prices to the new currency.
- Price types get a "Currency" attribute. Prices are filled in with the currency in mind: a price type in euros in a dirham document is converted to dirhams at the rate for the date, in a euro document it is used as is. Supplier prices and fixed customer prices are treated as base currency and are also converted to the document currency.
- On posting, registers receive the amount in base currency: cost of goods in stock and additional expenses, revenue and margin in sales, supplier prices, supplier orders and settlements. Settlements also keep the currency and the amount in currency. A payment in base currency closes the debt of a foreign-currency document; exchange differences are not calculated yet.
- The sale print form shows the document currency, the amount in words is in the document currency.
- Customer returns and tax invoices for a foreign-currency sale are not supported yet: the program refuses to post them.
- On update, receipts already issued in another currency get the "In currency" checkbox, and their settlements and supplier orders are converted to base currency.

### es
- Las «Recepciones de mercancías» y las «Ventas de mercancías» se pueden emitir en moneda extranjera. En la primera pestaña aparece la casilla «En moneda», que abre los campos «Moneda» y «Tipo de cambio». Sin la casilla, el documento sigue como antes en la moneda principal (constante «Moneda contable regulada»).
- El tipo de cambio se rellena a la fecha del documento desde el nuevo registro «Tesorería — Tipos de cambio» y se puede corregir a mano. Si no hay tipo para esa fecha, el programa lo avisa. Un contrato con moneda de liquidación distinta de la principal marca la casilla y pone esa moneda.
- En un documento en moneda, las columnas «Precio» e «Importe» de mercancías y servicios llevan la moneda del documento, por ejemplo «Precio (EUR)», y aparece la columna «Importe (MAD)»: el importe en moneda principal al tipo de cambio. Al cambiar la moneda, el programa propone convertir los precios de las líneas.
- El tipo de precio tiene un nuevo atributo «Moneda». Los precios se rellenan teniendo en cuenta la moneda: un precio en euros en un documento en dírhams se convierte a dírhams al tipo de la fecha, en un documento en euros se usa tal cual. Los precios de proveedores y los precios fijos de clientes se consideran en moneda principal y también se convierten a la moneda del documento.
- Al contabilizar, los registros reciben el importe en moneda principal: coste de las mercancías en almacén y de los gastos adicionales, ingresos y margen de ventas, precios de proveedores, pedidos a proveedores y liquidaciones. Las liquidaciones guardan además la moneda y el importe en moneda. Un pago en moneda principal cierra la deuda de un documento en moneda; las diferencias de cambio aún no se calculan.
- La impresión de la venta indica la moneda del documento, el importe en letras está en la moneda del documento.
- La devolución del cliente y la factura fiscal de una venta en moneda aún no se admiten: el programa no permite contabilizarlas.
- Al actualizar, las recepciones ya emitidas en otra moneda reciben la casilla «En moneda», y sus liquidaciones y pedidos a proveedores se convierten a la moneda principal.

## 2.0.16.21
### ru
- Окно печати: справа вместо таблицы — предпросмотр страниц. Печатная форма показывается разбитой на листы так, как её напечатает принтер: с выбранной бумагой, ориентацией, полями и масштабом. Любое изменение параметров слева сразу перерисовывает страницы.
- В левой панели новые параметры страницы: «Принтер», «Бумага» (с шириной и высотой листа), «Ориентация» (книжная или альбомная), «Поля, мм», «Вписать по ширине» и «Масштаб, %». Для этикеток и нестандартной бумаги — пункт «Свой размер» с шириной и высотой в миллиметрах. «Копий» перенесено вниз, к параметрам принтера.
- В приложении под Windows (не в веб-клиенте) в «Принтере» — принтеры компьютера, сразу выбран принтер по умолчанию, а в «Бумаге» — форматы бумаги выбранного принтера. «Печать» отправляет задание на выбранный принтер без системного диалога; пункт «Выбрать при печати» возвращает диалог. Под macOS, Linux и в веб-клиенте — стандартные форматы бумаги, принтер выбирается в диалоге печати.
- Параметры страницы запоминаются для каждой печатной формы отдельно: этикетка в следующий раз откроется со своим принтером и бумагой, счёт — со своими. Если отмечены печатные формы с разными параметрами, каждая печатается своим заданием.
- Заголовки колонок таблиц на macOS снова читаются: русские буквы в шапках больше не разъезжаются. Шапки всех таблиц и списков выводятся обычным шрифтом интерфейса.

### fr
- Fenêtre d'impression : à droite, un aperçu des pages remplace le tableau. Le formulaire imprimable est découpé en feuilles comme l'imprimante l'imprimera : avec le papier, l'orientation, les marges et l'échelle choisis. Toute modification des paramètres à gauche redessine aussitôt les pages.
- Nouveaux paramètres de page dans le panneau de gauche : « Imprimante », « Papier » (avec la largeur et la hauteur de la feuille), « Orientation » (portrait ou paysage), « Marges, mm », « Ajuster à la largeur » et « Échelle, % ». Pour les étiquettes et le papier non standard, l'option « Format personnalisé » avec largeur et hauteur en millimètres. « Copies » est déplacé plus bas, avec les paramètres de l'imprimante.
- Dans l'application sous Windows (hors client web), « Imprimante » liste les imprimantes de l'ordinateur, l'imprimante par défaut est présélectionnée, et « Papier » propose les formats de l'imprimante choisie. « Imprimer » envoie le travail à l'imprimante choisie sans la boîte de dialogue système ; l'option « Choisir à l'impression » la rétablit. Sous macOS, Linux et dans le client web, formats de papier standard et choix de l'imprimante dans la boîte de dialogue d'impression.
- Les paramètres de page sont mémorisés pour chaque formulaire imprimable : l'étiquette s'ouvrira la prochaine fois avec son imprimante et son papier, la facture avec les siens. Si des formulaires aux paramètres différents sont cochés, chacun est imprimé dans un travail séparé.
- Les en-têtes de colonnes des tableaux sont de nouveau lisibles sur macOS : les lettres cyrilliques ne s'écartent plus. Les en-têtes de tous les tableaux et listes utilisent la police normale de l'interface.

### en
- Print window: a page preview replaces the table on the right. The print form is split into sheets the way the printer will print it: with the chosen paper, orientation, margins and scale. Any change to the settings on the left redraws the pages at once.
- New page settings in the left panel: "Printer", "Paper" (with sheet width and height), "Orientation" (portrait or landscape), "Margins, mm", "Fit to width" and "Scale, %". For labels and non-standard paper, the "Custom size" option with width and height in millimeters. "Copies" has moved down next to the printer settings.
- In the Windows application (not the web client), "Printer" lists the computer's printers with the default printer preselected, and "Paper" offers the formats of the selected printer. "Print" sends the job to the selected printer without the system dialog; the "Choose when printing" option brings the dialog back. On macOS, Linux and in the web client, standard paper formats are offered and the printer is chosen in the print dialog.
- Page settings are remembered for each print form separately: next time the label opens with its own printer and paper, the invoice with its own. If print forms with different settings are selected, each is printed as a separate job.
- Table column headers are readable again on macOS: Cyrillic letters in headers no longer spread apart. Headers of all tables and lists use the regular interface font.

### es
- Ventana de impresión: a la derecha, una vista previa de páginas sustituye a la tabla. El formulario de impresión se divide en hojas tal como lo imprimirá la impresora: con el papel, la orientación, los márgenes y la escala elegidos. Cualquier cambio de los parámetros de la izquierda vuelve a dibujar las páginas al instante.
- Nuevos parámetros de página en el panel izquierdo: «Impresora», «Papel» (con el ancho y el alto de la hoja), «Orientación» (vertical u horizontal), «Márgenes, mm», «Ajustar al ancho» y «Escala, %». Para etiquetas y papel no estándar, la opción «Tamaño personalizado» con ancho y alto en milímetros. «Copias» se ha movido abajo, junto a los parámetros de la impresora.
- En la aplicación para Windows (no en el cliente web), «Impresora» muestra las impresoras del equipo con la predeterminada ya seleccionada, y «Papel» ofrece los formatos de la impresora elegida. «Imprimir» envía el trabajo a la impresora elegida sin el diálogo del sistema; la opción «Elegir al imprimir» lo recupera. En macOS, Linux y en el cliente web se ofrecen formatos de papel estándar y la impresora se elige en el diálogo de impresión.
- Los parámetros de página se recuerdan para cada formulario de impresión por separado: la etiqueta se abrirá la próxima vez con su impresora y su papel, la factura con los suyos. Si se marcan formularios con parámetros distintos, cada uno se imprime en un trabajo aparte.
- Los encabezados de columnas de las tablas vuelven a leerse bien en macOS: las letras cirílicas ya no se separan. Los encabezados de todas las tablas y listas usan la fuente normal de la interfaz.

## 2.0.16.20
### ru
- Окно печати: в 2.0.16.19 левая панель показывала только «Копий» — тумблер языка и список печатных форм не отображались, а «Изменить макет» сообщал, что макета нет. Исправлено: панель показывает все настройки, «Изменить макет» открывает макет показанной печатной формы.
- В тумблере языка вместо названий — короткие коды: RU, FR, EN, ES.
- Карточка номенклатуры: у блока показателей техкарты (плановая себестоимость, доступный выпуск, маржа) исправлена та же настройка раскладки, что скрывала элементы окна печати.

### fr
- Fenêtre d'impression : en 2.0.16.19, le panneau de gauche n'affichait que « Copies » — le sélecteur de langue et la liste des formulaires imprimables manquaient, et « Modifier le modèle » indiquait qu'il n'y avait pas de modèle. Corrigé : le panneau affiche tous les réglages, « Modifier le modèle » ouvre le modèle du formulaire affiché.
- Le sélecteur de langue affiche des codes courts au lieu des noms : RU, FR, EN, ES.
- Fiche article : le bloc des indicateurs de la fiche technique (coût prévisionnel, production disponible, marge) reçoit la même correction de mise en page que la fenêtre d'impression.

### en
- Print window: in 2.0.16.19 the left panel showed only "Copies" — the language switch and the list of print forms were missing, and "Edit template" said there was no template. Fixed: the panel shows all settings, "Edit template" opens the template of the displayed print form.
- The language switch shows short codes instead of names: RU, FR, EN, ES.
- Item card: the bill of materials indicators block (planned cost, available output, margin) gets the same layout fix as the print window.

### es
- Ventana de impresión: en 2.0.16.19 el panel izquierdo mostraba solo «Copias» — faltaban el selector de idioma y la lista de formularios de impresión, y «Editar plantilla» decía que no había plantilla. Corregido: el panel muestra todos los ajustes y «Editar plantilla» abre la plantilla del formulario mostrado.
- El selector de idioma muestra códigos cortos en lugar de nombres: RU, FR, EN, ES.
- Ficha de artículo: el bloque de indicadores de la ficha técnica (coste previsto, producción disponible, margen) recibe la misma corrección de diseño que la ventana de impresión.

## 2.0.16.19
### ru
- Окно печати: тумблер «Язык» перенесён в левую панель — к числу копий и списку печатных форм. Все настройки печати собраны в одной панели слева, печатная форма занимает правую часть окна.

### fr
- Fenêtre d'impression : le sélecteur « Langue » est déplacé dans le panneau de gauche, avec le nombre de copies et la liste des formulaires imprimables. Tous les réglages d'impression sont réunis dans un seul panneau à gauche, le formulaire imprimable occupe la partie droite de la fenêtre.

### en
- Print window: the "Language" switch has moved to the left panel, next to the number of copies and the list of print forms. All print settings are now gathered in one panel on the left, and the print form takes the right part of the window.

### es
- Ventana de impresión: el selector «Idioma» se ha movido al panel izquierdo, junto al número de copias y la lista de formularios de impresión. Todos los ajustes de impresión están reunidos en un panel a la izquierda, y el formulario de impresión ocupa la parte derecha de la ventana.

## 2.0.16.18
### ru
- В окне печати появился тумблер «Язык» со всеми языками программы; по умолчанию выбран язык, на котором вы работаете. При переключении печатная форма формируется заново на выбранном языке — так же она печатается и сохраняется в файл. Отметки «Печатать» сохраняются.
- На выбранном языке выводятся все подписи макета и сумма прописью. Отдельные тексты, которые программа подставляет сама (часть заголовков, значения из списков), пока остаются на языке, на котором вы работаете.
- Если вы меняли макет печатной формы и исправленная надпись не переведена, на другом языке она показывается как есть, а не пропадает.

### fr
- La fenêtre d'impression a un sélecteur « Langue » avec toutes les langues du programme ; par défaut, c'est la langue dans laquelle vous travaillez. Au changement, le formulaire imprimable est régénéré dans la langue choisie — il est imprimé et enregistré dans un fichier de la même façon. Les cases « Imprimer » sont conservées.
- Dans la langue choisie sortent tous les libellés du modèle et le montant en toutes lettres. Certains textes ajoutés par le programme lui-même (une partie des titres, les valeurs des listes) restent pour l'instant dans la langue dans laquelle vous travaillez.
- Si vous avez modifié le modèle d'un formulaire imprimable et que le libellé corrigé n'est pas traduit, il s'affiche tel quel dans une autre langue au lieu de disparaître.

### en
- The print window has a "Language" switch with all program languages; by default it is the language you work in. When switched, the print form is regenerated in the selected language — it is printed and saved to a file the same way. The "Print" checkmarks are kept.
- All template labels and the amount in words come out in the selected language. Some texts the program inserts itself (part of the titles, values from lists) remain in the language you work in for now.
- If you edited a print form template and the corrected label is not translated, it is shown as is in another language instead of disappearing.

### es
- La ventana de impresión tiene un selector «Idioma» con todos los idiomas del programa; por defecto está el idioma en el que trabaja. Al cambiarlo, el formulario de impresión se genera de nuevo en el idioma elegido, y así se imprime y se guarda en un archivo. Las marcas «Imprimir» se conservan.
- En el idioma elegido salen todos los textos de la plantilla y el importe en letras. Algunos textos que el programa añade por sí mismo (parte de los títulos, valores de listas) siguen por ahora en el idioma en el que trabaja.
- Si modificó la plantilla de un formulario de impresión y el texto corregido no está traducido, en otro idioma se muestra tal cual en lugar de desaparecer.

## 2.0.16.17
### ru
- Рабочее место производства: под списком заказов больше нет штатных стрелок прокрутки — листание только нашим пагинатором.
- Легенда индикатора укорочена и помещается в одну строку рядом с пагинатором.
- В колонках «Материал» и «ПФ/ГП» кнопка выбора сразу открывает отобранные значения (материалы заказа, ПФ/ГП заказа) — без промежуточного «Показать все». Набор по строке работает как раньше.
- В передаче в переработку появилась колонка «Кол-во ПФ/ГП» — сколько ПФ/ГП ожидается из материала строки. При выборе ПФ/ГП она заполняется по норме заказа (например, 6 м ткани при норме 2 м на изделие — 3 шт.), значение можно поправить. Поступление из переработки ждёт указанное количество. Если под один ПФ/ГП передано несколько разных материалов, ожидается по самому дефицитному из них. Если количество не указано, всё считается по заказу, как раньше.
- Колонки передачи переставлены: материал, его количество и упаковка, характеристика, ПФ/ГП и его количество. Те же колонки и тот же порядок — в форме документа «Передача в переработку».

### fr
- Poste de production : sous la liste des commandes, les flèches de défilement de la plateforme ont disparu — on ne tourne les pages qu'avec notre pagination.
- La légende de l'indicateur est raccourcie et tient sur une ligne à côté de la pagination.
- Dans les colonnes « Matière » et « SF/PF », le bouton de sélection ouvre directement les valeurs filtrées (matières de la commande, SF/PF de la commande), sans passer par « Tout afficher ». La saisie par texte fonctionne comme avant.
- Le transfert en sous-traitance a une colonne « Qté SF/PF » : combien de SF/PF sont attendus de la matière de la ligne. Au choix du SF/PF, elle est remplie selon la norme de la commande (par exemple 6 m de tissu pour une norme de 2 m par article — 3 pièces) ; la valeur peut être corrigée. La réception de sous-traitance attend la quantité indiquée. Si plusieurs matières différentes sont transférées pour un même SF/PF, l'attendu suit la plus déficitaire. Sans quantité indiquée, tout se calcule selon la commande, comme avant.
- Les colonnes du transfert sont réordonnées : matière, sa quantité et son conditionnement, caractéristique, SF/PF et sa quantité. Mêmes colonnes et même ordre dans le formulaire du document « Transfert en sous-traitance ».

### en
- Production workstation: the platform scroll arrows under the order list are gone — pages are turned only with our paginator.
- The indicator legend is shorter and fits on one line next to the paginator.
- In the "Material" and "SFG/FG" columns the selection button opens the filtered values directly (order materials, order SFG/FG), without the intermediate "Show all". Typing to search works as before.
- The subcontracting transfer has a new "SFG/FG qty" column: how many SFG/FG are expected from the line material. When the SFG/FG is selected it is filled from the order norm (for example, 6 m of fabric at 2 m per item — 3 pcs); the value can be corrected. The subcontracting receipt expects the specified quantity. If several different materials are transferred for one SFG/FG, the expected quantity follows the scarcest one. Without a quantity everything is calculated from the order, as before.
- Transfer columns are reordered: material, its quantity and pack, characteristic, SFG/FG and its quantity. The same columns in the same order are in the "Subcontracting transfer" document form.

### es
- Puesto de producción: bajo la lista de pedidos ya no aparecen las flechas de desplazamiento de la plataforma — las páginas se pasan solo con nuestro paginador.
- La leyenda del indicador es más corta y cabe en una línea junto al paginador.
- En las columnas «Material» y «SE/PT» el botón de selección abre directamente los valores filtrados (materiales del pedido, SE/PT del pedido), sin el paso intermedio «Mostrar todo». La búsqueda por texto funciona como antes.
- El envío a subcontratación tiene una nueva columna «Cant. SE/PT»: cuántos SE/PT se esperan del material de la línea. Al elegir el SE/PT se rellena según la norma del pedido (por ejemplo, 6 m de tela con una norma de 2 m por artículo — 3 uds.); el valor se puede corregir. La recepción de subcontratación espera la cantidad indicada. Si para un mismo SE/PT se envían varios materiales distintos, lo esperado sigue al más deficitario. Sin cantidad indicada, todo se calcula según el pedido, como antes.
- Las columnas del envío se reordenan: material, su cantidad y embalaje, característica, SE/PT y su cantidad. Las mismas columnas en el mismo orden están en el formulario del documento «Envío a subcontratación».

## 2.0.16.16
### ru
- Рабочее место производства: закладка «Переработка» переименована в «Передача в переработку».
- Во всех таблицах документов рабочего места количественные колонки стали уже, а заголовки короче: «Кол-во», «Упак.», «Характ.», «№ накл.» и так далее. Полное название показывается во всплывающей подсказке заголовка.
- В передаче в переработку появилась колонка «ПФ/ГП»: для какого полуфабриката или готового изделия заказа передаётся материал. Колонка необязательная. Выбрать можно только ПФ/ГП из заказа, в состав которого входит материал. Если ПФ/ГП указан, поступление из переработки по этой передаче заполняется именно им, количество — по заказу. Если не указан, состав определяется в поступлении, как раньше. Колонка есть и в рабочем месте, и в форме документа передачи.
- Справа от таблицы передач — таблица свойств ПФ/ГП текущей строки (материал, цвет, ширина и другие дополнительные свойства номенклатуры). Значения можно менять прямо здесь: они записываются в карточку ПФ/ГП и видны везде, где он используется. Оператор производства меняет только эти свойства, остальная карточка номенклатуры ему по-прежнему недоступна. Значения для выбора (список цветов, материалов) пополняет администратор.
- Новая отрасль «Ткани». Если включено производство, она заводит у номенклатуры свойства «Материал», «Цвет», «Ширина» и «Тип обработки». Отрасль выбирается в мастере первого запуска и в «Настройках программы → Компания и учёт». Там же появилась кнопка «Создать свойства номенклатуры»: она заводит недостающие свойства отрасли, уже созданные не дублируются.

### fr
- Poste de production : l'onglet « Sous-traitance » est renommé « Transfert en sous-traitance ».
- Dans toutes les tables de documents du poste, les colonnes de quantité sont plus étroites et les en-têtes plus courts : « Qté », « Cond. », « Caract. », « N° fact. », etc. Le nom complet apparaît dans l'info-bulle de l'en-tête.
- Le transfert en sous-traitance a une nouvelle colonne « SF/PF » : le semi-fini ou le produit fini de la commande pour lequel la matière est transférée. La colonne est facultative. On ne peut choisir qu'un SF/PF de la commande dont la composition contient la matière. Si le SF/PF est indiqué, la réception de sous-traitance sur ce transfert est remplie avec lui, quantité selon la commande ; sinon la composition se définit dans la réception, comme avant. La colonne existe dans le poste et dans le formulaire du transfert.
- À droite de la table des transferts, une table affiche les propriétés du SF/PF de la ligne courante (matière, couleur, largeur et autres propriétés supplémentaires de l'article). Les valeurs se modifient sur place : elles sont enregistrées dans la fiche du SF/PF et visibles partout où il est utilisé. L'opérateur de production ne modifie que ces propriétés, le reste de la fiche article lui reste inaccessible. Les valeurs proposées (couleurs, matières) sont complétées par l'administrateur.
- Nouveau secteur « Textiles ». Si la production est activée, il crée pour les articles les propriétés « Matière », « Couleur », « Largeur » et « Type de traitement ». Le secteur se choisit dans l'assistant de premier lancement et dans « Paramètres du programme → Entreprise et comptabilité », où un bouton « Créer les propriétés des articles » crée les propriétés manquantes du secteur sans dupliquer celles qui existent.

### en
- Production workstation: the "Subcontracting" tab is renamed "Subcontracting transfer".
- In all document tables of the workstation, quantity columns are narrower and headers are shorter: "Qty", "Pack", "Charact.", "Inv. no." and so on. The full name is shown in the header tooltip.
- The subcontracting transfer has a new "SFG/FG" column: the order's semi-finished or finished product the material is transferred for. The column is optional. Only an SFG/FG of the order whose composition includes the material can be selected. If it is set, the subcontracting receipt for this transfer is filled with it, quantity by the order; if not, the composition is defined in the receipt, as before. The column is available both in the workstation and in the transfer document form.
- To the right of the transfer table, a table shows the properties of the current line's SFG/FG (material, color, width and other additional item properties). Values can be changed right there: they are saved in the SFG/FG card and visible wherever it is used. The production operator changes only these properties; the rest of the item card remains unavailable to them. The selectable values (colors, materials) are maintained by the administrator.
- New "Textiles" industry. When production is enabled, it creates the "Material", "Color", "Width" and "Finishing type" item properties. The industry is chosen in the first-start wizard and in "Program settings → Company and accounting", where a "Create item properties" button creates the industry's missing properties without duplicating existing ones.

### es
- Puesto de producción: la pestaña «Subcontratación» pasa a llamarse «Envío a subcontratación».
- En todas las tablas de documentos del puesto, las columnas de cantidad son más estrechas y los encabezados más cortos: «Cant.», «Emb.», «Caract.», «N.º fact.», etc. El nombre completo aparece en la información emergente del encabezado.
- El envío a subcontratación tiene una nueva columna «SE/PT»: el semielaborado o producto terminado del pedido para el que se envía el material. La columna es opcional. Solo se puede elegir un SE/PT del pedido cuya composición incluye el material. Si se indica, la recepción de subcontratación de este envío se rellena con él, con la cantidad según el pedido; si no, la composición se define en la recepción, como antes. La columna está en el puesto y en el formulario del envío.
- A la derecha de la tabla de envíos, una tabla muestra las propiedades del SE/PT de la línea actual (material, color, ancho y otras propiedades adicionales del artículo). Los valores se pueden cambiar ahí mismo: se guardan en la ficha del SE/PT y se ven en todos los sitios donde se usa. El operador de producción solo cambia estas propiedades; el resto de la ficha del artículo le sigue siendo inaccesible. Los valores para elegir (colores, materiales) los mantiene el administrador.
- Nuevo sector «Textiles». Si la producción está activada, crea las propiedades de artículo «Material», «Color», «Ancho» y «Tipo de acabado». El sector se elige en el asistente de primer inicio y en «Configuración del programa → Empresa y contabilidad», donde un botón «Crear propiedades de artículos» crea las propiedades que faltan del sector sin duplicar las existentes.

## 2.0.16.15
### ru
- Права пользователей из группы «Настройки доступа» — «Кассир», «Видеть суммы (производство)», «Редактировать завершённые документы», «Редактировать документы в закрытом периоде», «Не контролировать запрет отгрузок», «Заверение цен» — теперь может выдать или снять только пользователь с ролью «Администратор» или «Руководитель». Остальные пользователи по-прежнему сами меняют свои обычные настройки: принтеры, кассу, склад; при попытке изменить право запись отменяется с сообщением.
- Пользователь кассы (роль PDV) записывает только свои настройки, чужие — нет.
- У служебной роли мобильной доставки снято право внешнего соединения (COM): через него можно было обойти любые ограничения прав. Обмен мобильной доставки этим правом не пользуется.

### fr
- Les droits des utilisateurs du groupe « Paramètres d'accès » — « Caissier », « Voir les montants (production) », « Modifier des documents terminés », « Modifier des documents en période clôturée », « Ne pas contrôler l'interdiction des expéditions », « Validation de prix » — ne peuvent plus être accordés ou retirés que par les utilisateurs ayant le rôle Administrateur ou Dirigeant. Les autres utilisateurs modifient toujours eux-mêmes leurs paramètres courants : imprimantes, caisse, entrepôt ; une tentative de modifier un droit est annulée avec un message.
- L'utilisateur de caisse (rôle PDV) n'enregistre que ses propres paramètres, et non plus ceux des autres.
- Le droit de connexion externe (COM) a été retiré au rôle technique de livraison mobile : il permettait de contourner toutes les restrictions de droits. L'échange de livraison mobile n'utilise pas ce droit.

### en
- User rights from the "Access settings" group — "Cashier", "See amounts (production)", "Edit completed documents", "Edit documents in a closed period", "Do not check the shipment ban", "Price approval" — can now be granted or removed only by users with the Administrator or Leader role. Other users still change their own regular settings themselves: printers, cash desk, warehouse; an attempt to change a right is cancelled with a message.
- The cash desk user (PDV role) saves only their own settings, no longer other users' settings.
- The external connection (COM) right has been removed from the mobile delivery service role: it allowed bypassing any rights restriction. The mobile delivery exchange does not use this right.

### es
- Los derechos de usuario del grupo «Configuración de acceso» — «Cajero», «Ver importes (producción)», «Modificar documentos terminados», «Modificar documentos en período cerrado», «No controlar la prohibición de envíos», «Validación de precios» — ahora solo pueden concederlos o retirarlos los usuarios con el rol Administrador o Líder. Los demás usuarios siguen cambiando ellos mismos sus ajustes habituales: impresoras, caja, almacén; un intento de cambiar un derecho se cancela con un mensaje.
- El usuario de caja (rol PDV) guarda solo sus propios ajustes, ya no los de otros usuarios.
- Se ha retirado el derecho de conexión externa (COM) al rol técnico de entrega móvil: permitía eludir cualquier restricción de derechos. El intercambio de entrega móvil no usa este derecho.

## 2.0.16.14
### ru
- Рабочее место производства: в панели фильтров клиент и продукция теперь выбираются из справочников, а не вводятся частью названия. Переключатель «Производство / Все» убран — рабочее место всегда показывает заказы на производство. Добавлены фильтры по стадии заказа и по периоду даты отгрузки; заказ без даты отгрузки в отбор по периоду не попадает. Фильтры действуют и на закладке «Заказы», и на закладке «Продукция».
- Под списком заказов вместо стрелок платформы — наш пагинатор, как в списках документов: «◀◀ ◀ 1 / 3 ▶ ▶▶» и счётчик «1-50 из 124». В той же строке справа — легенда индикатора: что означает каждый кружок и что значат ○, ◐ и ●.
- Суммы и цены в рабочем месте теперь видны по дополнительному праву пользователя «Видеть суммы (производство)» (Voir les montants (production)). Право задаётся в «Настройка → Пользователи и права → Настройки пользователей»: «Да» — суммы и цены видны и их можно править, «Нет» — скрыты. Пока право пользователю не задано, всё работает как раньше: оператор производства сумм не видит, администратор и остальные видят. Сам список «Настройки пользователей» теперь тоже есть в этом разделе.
- Закладка «Материалы»: колонки стали уже, заголовки короче (полное название — во всплывающей подсказке заголовка), «Способ изготовления» перенесён в конец таблицы. Колонка характеристики показывается, только если в «Настройках программы → Номенклатура» включено использование характеристик.

### fr
- Poste de production : dans le panneau des filtres, le client et le produit se choisissent désormais dans les référentiels au lieu d'être saisis comme une partie du nom. Le sélecteur « Production / Toutes » a été retiré — le poste affiche toujours les commandes de production. Des filtres par étape de la commande et par période de date d'expédition ont été ajoutés ; une commande sans date d'expédition n'entre pas dans le filtre par période. Les filtres s'appliquent aux onglets « Commandes » et « Produits ».
- Sous la liste des commandes, les flèches de la plateforme sont remplacées par notre pagination, comme dans les listes de documents : « ◀◀ ◀ 1 / 3 ▶ ▶▶ » et le compteur « 1-50 sur 124 ». Sur la même ligne, à droite, la légende de l'indicateur : ce que représente chaque cercle et ce que signifient ○, ◐ et ●.
- Les montants et les prix du poste sont désormais visibles selon le droit supplémentaire de l'utilisateur « Voir les montants (production) ». Le droit se règle dans « Paramètres → Utilisateurs et droits → Paramètres utilisateur » : « Oui » — montants et prix visibles et modifiables, « Non » — masqués. Tant que le droit n'est pas défini pour l'utilisateur, rien ne change : l'opérateur de production ne voit pas les montants, l'administrateur et les autres les voient. La liste « Paramètres utilisateur » figure désormais aussi dans cette section.
- Onglet « Matières » : les colonnes sont plus étroites, les en-têtes plus courts (le nom complet apparaît dans l'info-bulle de l'en-tête), « Mode de fabrication » est déplacé en fin de tableau. La colonne caractéristique ne s'affiche que si l'utilisation des caractéristiques est activée dans « Paramètres du programme → Articles ».

### en
- Production workstation: in the filter panel, the customer and the product are now picked from the catalogs instead of being typed as part of the name. The "Production / All" switch has been removed — the workstation always shows production orders. New filters by order stage and by shipment date period have been added; an order without a shipment date does not pass the period filter. The filters apply to both the "Orders" and the "Products" tabs.
- Below the order list, the platform arrows are replaced by our paginator, as in document lists: "◀◀ ◀ 1 / 3 ▶ ▶▶" and the "1-50 of 124" counter. On the same line, on the right, is the indicator legend: what each circle stands for and what ○, ◐ and ● mean.
- Amounts and prices in the workstation are now shown according to the additional user right "See amounts (production)" (Voir les montants (production)). The right is set in "Settings → Users and rights → User settings": "Yes" — amounts and prices are shown and can be edited, "No" — hidden. Until the right is set for a user, nothing changes: the production operator does not see amounts, the administrator and everyone else do. The "User settings" list itself is now available in that section too.
- "Materials" tab: columns are narrower, headers are shorter (the full name is in the header tooltip), "Manufacturing method" has moved to the end of the table. The characteristic column is shown only if characteristics are enabled in "Program settings → Items".

### es
- Puesto de producción: en el panel de filtros, el cliente y el producto se eligen ahora de los catálogos en lugar de escribir parte del nombre. Se ha quitado el selector «Producción / Todos»: el puesto muestra siempre los pedidos de producción. Se han añadido filtros por etapa del pedido y por período de fecha de envío; un pedido sin fecha de envío no entra en el filtro por período. Los filtros se aplican tanto a la pestaña «Pedidos» como a «Productos».
- Debajo de la lista de pedidos, las flechas de la plataforma se sustituyen por nuestro paginador, como en las listas de documentos: «◀◀ ◀ 1 / 3 ▶ ▶▶» y el contador «1-50 de 124». En la misma línea, a la derecha, está la leyenda del indicador: qué representa cada círculo y qué significan ○, ◐ y ●.
- Los importes y precios del puesto se muestran ahora según el derecho adicional del usuario «Ver importes (producción)» (Voir les montants (production)). El derecho se ajusta en «Configuración → Usuarios y derechos → Configuración de usuario»: «Sí» — importes y precios visibles y editables, «No» — ocultos. Mientras el derecho no esté definido para el usuario, nada cambia: el operador de producción no ve los importes, el administrador y los demás sí. La lista «Configuración de usuario» también está ahora en esa sección.
- Pestaña «Materiales»: las columnas son más estrechas, los encabezados más cortos (el nombre completo aparece en la información emergente del encabezado), «Método de fabricación» pasa al final de la tabla. La columna de característica solo se muestra si el uso de características está activado en «Configuración del programa → Artículos».

## 2.0.16.13
### ru
- Французские, английские и испанские названия финансовых справочников и реквизитов приведены к принятым терминам: статья ДДС — «Rubrique de flux de trésorerie» / «Cash flow item», статья затрат и статья расходов — «Nature de charge» / «Expense type», счёт в бухгалтерских отчётах — «Compte comptable» / «General ledger account», отчёт «Движение денежных средств» — «Flux de trésorerie» / «Cash flow», отчёт «Затраты» — «Charges» / «Expenses», типы движения — «Encaissement» и «Décaissement» / «Cash inflow» и «Cash outflow». Русские названия не менялись.

### fr
- Les libellés des catalogues et des attributs financiers suivent désormais la terminologie comptable française : « Rubrique de flux de trésorerie » (au lieu de « Poste de trésorerie »), « Nature de charge » (au lieu de « Article de coût » et « Article de dépense »), « Compte comptable » dans les états comptables, rapport « Flux de trésorerie » (au lieu de « Mouvement de fonds »), rapport « Charges », types de mouvement « Encaissement » et « Décaissement ».

### en
- Financial catalog and field names now use standard accounting terms: "Cash flow item", "Expense type" (instead of "Cost item" and "Item of expenditure"), "General ledger account" in accounting reports, the "Cash flow" report (instead of "Movement of funds"), movement types "Cash inflow" and "Cash outflow".

### es
- Los nombres de los catálogos y campos financieros siguen ahora la terminología contable: «Partida de flujo de efectivo», «Tipo de gasto» (en lugar de «Objeto de los gastos» y «Partida de gastos»), «Cuenta contable» en los informes contables, el informe «Flujo de efectivo» (en lugar de «Movimiento de fondos»), tipos de movimiento «Cobro» y «Pago».

## 2.0.16.12
### ru
- В документах с одной таблицей (кассовые ордера, поступление и списание безналичных, возвраты, перемещение, оприходование, списание, заказ поставщику, кадровые и зарплатные документы и другие) команды «Создать на основании», «Перейти» и «Печать» теперь стоят на командной панели формы вверху, а не в панели таблицы.

### fr
- Dans les documents à un seul tableau (bons d'encaissement et de décaissement, entrées et sorties bancaires, retours, transferts, entrées et sorties de stock, commande fournisseur, documents de personnel et de paie, etc.), les commandes « Générer », « Aller » et « Impression » se trouvent désormais dans la barre de commandes du formulaire, en haut, et non plus dans celle du tableau.

### en
- In documents with a single table (cash receipts and payments, bank receipts and payments, returns, transfers, stock receipts and write-offs, purchase order, HR and payroll documents and others), the "Generate", "Go to" and "Print" commands are now on the form's command bar at the top instead of the table's bar.

### es
- En los documentos con una sola tabla (cobros y pagos de caja, entradas y salidas bancarias, devoluciones, traslados, entradas y bajas de existencias, pedido a proveedor, documentos de personal y nómina, etc.), los comandos «Generar», «Ir a» e «Impresión» están ahora en la barra de comandos del formulario, arriba, y no en la de la tabla.

## 2.0.16.11
### ru
- «Личный кабинет партнера» теперь есть в меню CRM → «Личный кабинет» для администратора: по кнопке «Войти» выбирается покупатель, и кабинет открывается от его имени — с его ценами, корзиной и историей. Кнопка «Выйти» закрывает только кабинет, работа в программе продолжается.
- Окно «Что нового» доступно всем сотрудникам: оно открывается после обновления и из меню «Настройка». Раньше у рабочих ролей оно не открывалось.
- «Отчёт по проводкам» починен и выведен в меню «Бухгалтерии»: в нём снова есть итоги.
- «Виды оплат» переехали из «Продаж» в «Казначейство → Справочники», «Виды заданий» и «Настройки заданий» — в «Настройка → Параметры».
- Отчёт «Налоговые накладные: нехватка товара на складе» переехал из «Продаж» в «Склад».

### fr
- L'« Espace client » du partenaire figure désormais dans le menu CRM → « Espace client » pour l'administrateur : le bouton « Entrer » permet de choisir un client et d'ouvrir l'espace en son nom — avec ses prix, son panier et son historique. Le bouton « Sortir » ferme seulement l'espace, le travail dans le programme continue.
- La fenêtre « Quoi de neuf » est accessible à tous les employés : elle s'ouvre après la mise à jour et depuis le menu « Paramètres ». Auparavant, elle ne s'ouvrait pas pour les rôles de travail.
- Le « Rapport sur les écritures » est réparé et ajouté au menu « Comptabilité » : les totaux s'affichent de nouveau.
- Les « Types de paiement » passent de « Ventes » à « Trésorerie → Catalogues », les « Types de tâches » et « Paramètres des tâches » à « Paramètres → Options ».
- Le rapport « Factures fiscales : stock insuffisant » passe de « Ventes » à « Entrepôt ».

### en
- The "Customer area" of a partner is now in the CRM → "Customer portal" menu for the administrator: the "Enter" button lets you pick a customer and open the portal on their behalf — with their prices, cart and history. The "Exit" button closes only the portal; work in the program continues.
- The "What's new" window is available to all employees: it opens after an update and from the "Settings" menu. Previously it did not open for working roles.
- The "Transaction report" is fixed and added to the "Accounting" menu: totals are shown again.
- "Types of payment" moved from "Sales" to "Treasury → Reference books", "Types of tasks" and "Job settings" to "Settings → Options".
- The "Tax invoices: insufficient stock" report moved from "Sales" to "Warehouse".

### es
- El «Área de clientes» del socio está ahora en el menú CRM → «Portal del cliente» para el administrador: el botón «Entrar» permite elegir un cliente y abrir el portal en su nombre, con sus precios, su carrito y su historial. El botón «Salir» cierra solo el portal; el trabajo en el programa continúa.
- La ventana «Qué hay de nuevo» está disponible para todos los empleados: se abre tras la actualización y desde el menú «Configuración». Antes no se abría para los roles de trabajo.
- El «Informe de transacciones» se ha corregido y se añade al menú «Contabilidad»: vuelve a mostrar los totales.
- Los «Tipos de pago» pasan de «Ventas» a «Tesorería → Catálogos», los «Tipos de tareas» y la «Configuración de tareas» a «Configuración → Parámetros».
- El informe «Facturas fiscales: existencias insuficientes» pasa de «Ventas» a «Almacén».

## 2.0.16.10
### ru
- Меню перестроено во всех оставшихся разделах: «Казначейство», «Бухгалтерия», «Зарплата и кадры», CRM, «Настройка» и «Главное». Теперь в каждом разделе все пункты показываются явно, в одном месте, а кнопка «Создать» предлагает только документы, с которых начинается работа.
- «Казначейство»: наверху — кассовые документы и безналичные платежи. Через «Создать» можно сразу оформить приходный и расходный кассовые ордера, поступление на счёт и списание со счёта. Группы: «Касса», «Банк», «Оплаты клиентов» (сертификаты на оплату и банковские чеки; группа исчезает, если альтернативные оплаты выключены), «Расчёты» (корректировки долга и сверки взаиморасчётов — теперь оба списка в меню), «Справочники». «Кассовая книга» переехала сюда из «Бухгалтерии».
- «Бухгалтерия»: группы «Налоговые документы» (накладные продаж и покупок и возвраты по ним), «Регламентированный учёт» (операции, журнал проводок, план счетов, виды субконто; группа исчезает вместе с регламентированным учётом), «Прочие документы». В меню вышли бухгалтерские отчёты: оборотно-сальдовая ведомость, ведомость по счёту, обороты, анализ и карточка счёта, анализ и карточка субконто.
- Отчёт «Главная книга» удалён: он повторял «Расчеты с покупателями». Его разрез по объектам расчётов теперь — вариант «По объектам расчётов» отчёта «Расчеты с покупателями».
- «Производство / Переработка»: новый пункт «Переработчики» — контрагенты с флажком «Субподрядчик» в карточке. Пункты «Сырьё», «Полуфабрикаты» и «Готовая продукция» теперь действительно показывают только номенклатуру своего типа.
- «Зарплата и кадры»: в меню вышли «Тарифные ставки» и «Отработанное время сотрудников». Вместо общего списка физических лиц — «Сотрудники»: только работающие (принятые и не уволенные). Общий список физических лиц остаётся в «Главном».
- CRM: лиды, каналы и покупатели; новая группа «Личный кабинет» — корзины и история поиска (переехала из «Продаж»). Раздел виден и тогда, когда включён личный кабинет, а лиды — нет.
- «Настройка»: группы «Параметры», «Пользователи и права» (туда перешли пользователи), «Оборудование» (одним пунктом, плюс обновление поставляемых драйверов) и новая «Сервисные операции» — перепроведение документов (из «Казначейства»), корректировка регистров, групповое изменение реквизитов, групповое создание документов, загрузка из Excel, регламентные задания, регистрация изменений для обмена, движения документа.
- «Главное»: добавлен пункт «Право подписи».

### fr
- Le menu est réorganisé dans toutes les sections restantes : « Trésorerie », « Comptabilité », « Paie et personnel », CRM, « Paramètres » et la section principale. Chaque section affiche désormais tous ses éléments explicitement, à un seul endroit, et le bouton « Créer » ne propose que les documents qui ouvrent le travail.
- « Trésorerie » : en haut, les documents de caisse et les paiements bancaires. « Créer » permet d'établir directement les encaissements et décaissements de caisse, les entrées et sorties bancaires. Groupes : « Caisse », « Banque », « Paiements des clients » (bons d'achat et chèques bancaires ; le groupe disparaît si les paiements alternatifs sont désactivés), « Règlements » (ajustements de dette et rapprochements — les deux listes sont maintenant au menu), « Catalogues ». Le « Livre de caisse » passe ici depuis « Comptabilité ».
- « Comptabilité » : groupes « Documents fiscaux » (factures de vente et d'achat et leurs retours), « Comptabilité réglementaire » (opérations, journal des écritures, plan comptable, types de sous-comptes ; le groupe disparaît avec la comptabilité réglementaire), « Autres documents ». Les rapports comptables apparaissent au menu : balance générale, balance par compte, mouvements, analyse et fiche de compte, analyse et fiche de sous-compte.
- Le rapport « Grand livre » est supprimé : il répétait « Situation client ». Sa ventilation par objet de règlement devient la variante « Par objet de règlement » du rapport « Situation client ».
- « Production / Sous-traitance » : nouvel élément « Sous-traitants » — les tiers cochés « Sous-traitant » dans leur fiche. « Matières premières », « Produits semi-finis » et « Produits finis » n'affichent désormais que les articles de leur type.
- « Paie et personnel » : « Tarifs » et « Temps travaillé par les salariés » apparaissent au menu. À la place de la liste générale des personnes : « Employés », uniquement ceux en poste (embauchés et non licenciés). La liste générale des personnes reste dans la section principale.
- CRM : prospects, canaux et clients ; nouveau groupe « Espace client » — paniers et historique de recherche (venu de « Ventes »). La section reste visible quand l'espace client est activé sans les prospects.
- « Paramètres » : groupes « Options », « Utilisateurs et droits » (les utilisateurs y passent), « Matériel » (un seul élément, plus la mise à jour des pilotes fournis) et le nouveau groupe « Opérations de service » — repasser les documents (depuis « Trésorerie »), correction des registres, modification et création de documents en lot, import depuis Excel, tâches planifiées, enregistrement des modifications pour l'échange, mouvements du document.
- Section principale : ajout de l'élément « Droit de signature ».

### en
- The menu is restructured in all remaining sections: "Treasury", "Accounting", "Payroll and staff", CRM, "Settings" and the main section. Every section now shows all its items explicitly, in one place, and the "Create" button offers only the documents that start the work.
- "Treasury": cash documents and bank payments at the top. "Create" now lets you issue cash receipts and payments, bank receipts and bank payments directly. Groups: "Cash", "Bank", "Customer payments" (purchase vouchers and bank cheques; the group disappears when alternative payments are off), "Settlements" (debt adjustments and reconciliations — both lists are now in the menu), "Reference books". The "Cash book" moved here from "Accounting".
- "Accounting": groups "Tax documents" (sales and purchase tax invoices and their returns), "Statutory accounting" (operations, journal of entries, chart of accounts, analytics types; the group disappears together with statutory accounting), "Other documents". Accounting reports are now in the menu: trial balance, account balance, account turnover, account analysis and card, analytics analysis and card.
- The "General ledger" report is removed: it repeated "Settlements with customers". Its breakdown by settlement object is now the "By settlement object" variant of "Settlements with customers".
- "Production / Subcontracting": new "Subcontractors" item — counterparties with the "Subcontractor" checkbox in their card. "Raw materials", "Semi-finished products" and "Finished products" now really show only items of their type.
- "Payroll and staff": "Rates" and "Time worked by employees" are now in the menu. Instead of the general list of individuals — "Employees": only current ones (hired and not dismissed). The general list of individuals stays in the main section.
- CRM: leads, channels and customers; new "Customer portal" group — carts and search history (moved from "Sales"). The section stays visible when the customer portal is on but leads are off.
- "Settings": groups "Options", "Users and rights" (users moved here), "Equipment" (a single item, plus updating supplied drivers) and the new "Service operations" — document reposting (from "Treasury"), register adjustment, bulk attribute change and bulk document creation, import from Excel, scheduled jobs, change registration for exchange, document movements.
- Main section: "Right of signature" item added.

### es
- El menú se reorganiza en todas las secciones restantes: «Tesorería», «Contabilidad», «Nómina y personal», CRM, «Configuración» y la sección principal. Cada sección muestra ahora todos sus elementos de forma explícita, en un solo lugar, y el botón «Crear» ofrece solo los documentos con los que empieza el trabajo.
- «Tesorería»: arriba, los documentos de caja y los pagos bancarios. «Crear» permite emitir directamente cobros y pagos de caja, entradas y salidas bancarias. Grupos: «Caja», «Banco», «Pagos de clientes» (vales de compra y cheques bancarios; el grupo desaparece si los pagos alternativos están desactivados), «Liquidaciones» (ajustes de deuda y conciliaciones — ahora ambas listas están en el menú), «Catálogos». El «Libro de caja» pasa aquí desde «Contabilidad».
- «Contabilidad»: grupos «Documentos fiscales» (facturas de venta y de compra y sus devoluciones), «Contabilidad reglamentaria» (operaciones, diario de asientos, plan de cuentas, tipos de subcuenta; el grupo desaparece junto con la contabilidad reglamentaria), «Otros documentos». Los informes contables aparecen en el menú: balance de sumas y saldos, balance por cuenta, movimientos, análisis y ficha de cuenta, análisis y ficha de subcuenta.
- Se elimina el informe «Libro mayor»: repetía «Liquidaciones con clientes». Su desglose por objeto de liquidación es ahora la variante «Por objeto de liquidación» de «Liquidaciones con clientes».
- «Producción / Subcontratación»: nuevo elemento «Subcontratistas» — contrapartes con la casilla «Subcontratista» en su ficha. «Materias primas», «Productos semielaborados» y «Productos terminados» muestran ahora solo los artículos de su tipo.
- «Nómina y personal»: «Tarifas» y «Tiempo trabajado por empleados» aparecen en el menú. En lugar de la lista general de personas: «Empleados», solo los que están en activo (contratados y no despedidos). La lista general de personas sigue en la sección principal.
- CRM: leads, canales y clientes; nuevo grupo «Portal del cliente» — carritos e historial de búsqueda (trasladado desde «Ventas»). La sección sigue visible cuando el portal del cliente está activado y los leads no.
- «Configuración»: grupos «Parámetros», «Usuarios y derechos» (los usuarios pasan aquí), «Equipo» (un solo elemento, más la actualización de los controladores suministrados) y el nuevo «Operaciones de servicio» — volver a contabilizar documentos (desde «Tesorería»), corrección de registros, cambio y creación de documentos en lote, importación desde Excel, tareas programadas, registro de cambios para el intercambio, movimientos del documento.
- Sección principal: se añade el elemento «Derecho de firma».

## 2.0.16.9
### ru
- Раздел «Склад» перестроен по ходу работы. Наверху — перемещения товаров. Остальное разложено по группам: «Инвентаризация» (пересчёты и задания на пересчёт), «Излишки и списания» (оприходования, списания, уценки), «Комплектация» (акты разбора, пересортица), «Товары» и «Хранение». Все отчёты раздела собраны в одном списке отчётов.
- Группа «Инвентаризация» исчезает из меню целиком, если в «Параметрах» выключены пересчёты, группа «Комплектация» — если выключена комплектация. «Наборы упаковок» уходят из меню вместе с выключенной упаковкой.
- В «Складе» номенклатура открывается пунктом «Товары» — без услуг и комплектов. В группе «Товары» появился общий список штрихкодов: по нему удобно найти товар по коду или проверить дубли. Штрихкоды по-прежнему ведутся и из карточки номенклатуры.
- «Перевозчики» переехали из «Продаж» в «Склад» → «Хранение». Логист теперь видит раздел «Склад»: перевозчиков, места хранения и отчёты по остаткам, на которые у него и раньше были права.
- Отчёт «Движения товара» выведен в меню, его вариант «Отчет по списанию товаров» снова формируется: списания по местам хранения и товарам по дням. Колонка «Оборот (кг)» в обоих вариантах отчёта теперь считает вес всего количества, а не одной единицы товара.
- Список уценок выведен в меню рядом с созданием уценки (раньше создать уценку было можно, а открыть список — нет).
- «Стоимость склада» осталась только в «Складе» (раньше была ещё и в «Бухгалтерии»). «Ведомость по поступлениям» — отчёт о приходе товаров от поставщиков — переехала в «Закупки».
- Кнопка «Создать» в «Складе» предлагает документы, с которых начинается работа: перемещение, оприходование, списание, уценку, пересчёт и задание на пересчёт, акт разбора, пересортицу. Справочники из неё убраны.

### fr
- La section « Entrepôt » suit désormais l'ordre du travail. En haut : les transferts de marchandises. Le reste est réparti en groupes : « Inventaire » (inventaires et tâches d'inventaire), « Excédents et sorties » (entrées, sorties, démarquages), « Assemblage » (actes de désassemblage, reclassements), « Articles » et « Stockage ». Tous les rapports de la section sont réunis dans une seule liste de rapports.
- Le groupe « Inventaire » disparaît entièrement du menu si les inventaires sont désactivés dans les « Options », le groupe « Assemblage » — si l'assemblage est désactivé. Les « Ensembles d'emballages » quittent le menu quand les emballages sont désactivés.
- Dans « Entrepôt », les articles s'ouvrent par « Marchandises » — sans services ni kits. Le groupe « Articles » propose désormais la liste générale des codes-barres : pratique pour retrouver un article par son code ou repérer les doublons. Les codes-barres se saisissent toujours aussi depuis la fiche de l'article.
- Les « Transporteurs » passent de « Ventes » à « Entrepôt » → « Stockage ». Le logisticien voit désormais la section « Entrepôt » : transporteurs, lieux de stockage et rapports de stock auxquels il avait déjà droit.
- Le rapport « Mouvement de marchandises » est ajouté au menu ; sa variante « Rapport de sortie de marchandises » se génère à nouveau : sorties par lieu de stockage et par article, jour par jour. Dans les deux variantes du rapport, la colonne « Mouvement (kg) » calcule désormais le poids de toute la quantité, et non d'une seule unité.
- La liste des démarquages est ajoutée au menu à côté de leur création (auparavant, on pouvait créer un démarquage sans pouvoir ouvrir la liste).
- « Valeur du stock » reste uniquement dans « Entrepôt » (elle figurait aussi dans « Comptabilité »). Le « Relevé des réceptions » — rapport des entrées de marchandises des fournisseurs — passe dans « Achats ».
- Le bouton « Créer » de la section « Entrepôt » propose les documents qui ouvrent le travail : transfert, entrée, sortie, démarquage, inventaire et tâche d'inventaire, acte de désassemblage, reclassement. Les catalogues en sont retirés.

### en
- The "Warehouse" section now follows the course of work. At the top: goods transfers. The rest is grouped into "Stocktaking" (inventories and inventory tasks), "Surpluses and write-offs" (receipts, write-offs, markdowns), "Kitting" (disassembly acts, regrading), "Items" and "Storage". All reports of the section are gathered in one report list.
- The "Stocktaking" group disappears from the menu entirely when inventories are off in "Options", the "Kitting" group — when kitting is off. "Packaging sets" leave the menu when packaging is off.
- In "Warehouse", items open as "Goods" — without services and kits. The "Items" group now has the general list of barcodes: handy for finding an item by its code or spotting duplicates. Barcodes can still be entered from the item card.
- "Carriers" moved from "Sales" to "Warehouse" → "Storage". The logistician now sees the "Warehouse" section: carriers, storage locations and the stock reports they already had rights to.
- The "Movement of goods" report is added to the menu, and its "Goods output report" variant works again: write-offs by storage location and item, day by day. In both report variants the "Movement (kg)" column now shows the weight of the whole quantity, not of a single unit.
- The markdown list is added to the menu next to creating a markdown (previously a markdown could be created, but its list could not be opened).
- "Warehouse value" stays only in "Warehouse" (it was also in "Accounting"). The "Receipt record" — a report on goods received from suppliers — moved to "Purchases".
- The "Create" button in "Warehouse" offers the documents that start the work: transfer, receipt, write-off, markdown, inventory and inventory task, disassembly act, regrading. Reference books are removed from it.

### es
- La sección «Almacén» sigue ahora el orden del trabajo. Arriba: los traslados de mercancías. El resto se agrupa en «Inventario» (inventarios y tareas de inventario), «Excedentes y bajas» (entradas, bajas, rebajas de valor), «Ensamblaje» (actas de desmontaje, reclasificaciones), «Artículos» y «Almacenamiento». Todos los informes de la sección están reunidos en una sola lista de informes.
- El grupo «Inventario» desaparece por completo del menú si los inventarios están desactivados en «Parámetros»; el grupo «Ensamblaje», si el ensamblaje está desactivado. Los «Conjuntos de embalaje» salen del menú cuando el embalaje está desactivado.
- En «Almacén», los artículos se abren como «Mercancías», sin servicios ni kits. El grupo «Artículos» tiene ahora la lista general de códigos de barras: útil para encontrar un artículo por su código o detectar duplicados. Los códigos de barras se siguen registrando también desde la ficha del artículo.
- Los «Transportistas» pasan de «Ventas» a «Almacén» → «Almacenamiento». El logístico ve ahora la sección «Almacén»: transportistas, lugares de almacenamiento e informes de existencias a los que ya tenía derecho.
- El informe «Circulación de mercancías» se añade al menú y su variante «Informe de salida de mercancías» vuelve a generarse: bajas por lugar de almacenamiento y artículo, día a día. En ambas variantes del informe, la columna «Movimiento (kg)» calcula ahora el peso de toda la cantidad, no de una sola unidad.
- La lista de rebajas de valor se añade al menú junto a su creación (antes se podía crear una rebaja, pero no abrir la lista).
- «Valor del almacén» queda solo en «Almacén» (también estaba en «Contabilidad»). El «Registro de recibo», informe de las mercancías recibidas de proveedores, pasa a «Compras».
- El botón «Crear» de la sección «Almacén» ofrece los documentos con los que empieza el trabajo: traslado, entrada, baja, rebaja de valor, inventario y tarea de inventario, acta de desmontaje, reclasificación. Se retiran de él los catálogos.

## 2.0.16.8
### ru
- Пункт «Кураторы договоров» в «Продажах» → «Клиенты» теперь видит и кассир: в нём можно посмотреть и поменять, кто из сотрудников ведёт договор.

### fr
- L'élément « Responsables des contrats » dans « Ventes » → « Clients » est désormais visible aussi pour le caissier : on y voit et modifie quel employé suit chaque contrat.

### en
- The "Contract managers" item in "Sales" → "Customers" is now visible to cashiers as well: it shows, and lets you change, which employee handles each contract.

### es
- El elemento «Responsables de contratos» en «Ventas» → «Clientes» ahora también lo ve el cajero: en él se ve y se cambia qué empleado lleva cada contrato.

## 2.0.16.7
### ru
- Раздел «Продажи» перестроен по ходу работы. Наверху — заказы покупателей, продажи и возвраты от покупателей, рядом — история заказов по статусам. Остальное разложено по группам: «Опт», «Розница», «Цены», «Клиенты», «Справочники». Все отчёты раздела собраны в одном списке отчётов.
- Группа «Опт» (коммерческие предложения, задачи по заказам, заявки на поиск товара) исчезает из меню целиком, если все эти возможности выключены в «Параметрах»; группа «Розница» — если выключены розничные продажи. «Заявка на поиск товара» больше не выводится в меню дважды.
- В «Продажах» номенклатура открывается пунктом «Товары и услуги для продажи» — без сырья и полуфабрикатов, — а договоры пунктом «Договоры с покупателями». Без производства «Товары и услуги для продажи» показывают всю номенклатуру. Поставщики и общие списки контрагентов, номенклатуры и договоров из «Продаж» убраны: они есть в «Закупках», «Складе» и «Казначействе».
- Администратор и руководитель видят в группе «Клиенты» «Кураторы договоров» — кто из сотрудников ведёт договор.
- Отчёт «Просроченные долги покупателей» выведен в меню и исправлен: он показывает только долги с истёкшим сроком оплаты и сколько дней они просрочены (раньше — весь долг сверх кредита). Срок оплаты берётся так же, как при контроле кредита: из договора, а если там не задан — из карточки покупателя; если срок не задан нигде — год. Из обоих отчётов просроченных долгов убран параметр «Вариант задолженности», который ни на что не влиял.
- Отчёты переименованы по тому, что они показывают: «Статистика дневных продаж» — «Продажи по часам», «ABC - анализ продаж» — «ABC-анализ продаж».
- «Реестр реализаций товаров и услуг» переехал из «Казначейства» в «Продажи». Налоговые «Расчеты с покупателями» и «Ведомость по продажам (налоговая)» остались только в «Бухгалтерии», туда же переехал «Проданный товар без накладной».
- Кнопка «Создать» в «Продажах» предлагает только документы, с которых начинается работа: заказ покупателя, продажа, коммерческое предложение, установка цен, правило ценообразования.
- В «Параметрах» → «Продажи» настройки розницы (розничный клиент, договор, печать чека) доступны, только когда розничные продажи включены. Регистр оплат чеками скрывается вместе с альтернативными оплатами.

### fr
- La section « Ventes » suit désormais l'ordre du travail. En haut : commandes clients, ventes et retours clients, à côté l'historique des commandes par statut. Le reste est réparti en groupes : « Vente en gros », « Vente au détail », « Prix », « Clients », « Catalogues ». Tous les rapports de la section sont réunis dans une seule liste de rapports.
- Le groupe « Vente en gros » (offres commerciales, tâches de commandes, demandes de recherche d'articles) disparaît entièrement du menu si toutes ces fonctions sont désactivées dans les « Options » ; le groupe « Vente au détail » — si la vente au détail est désactivée. La « Demande de recherche d'article » n'apparaît plus deux fois dans le menu.
- Dans « Ventes », les articles s'ouvrent par « Articles vendus » — sans matières premières ni produits semi-finis — et les contrats par « Contrats clients ». Sans production, « Articles vendus » affiche tous les articles. Les fournisseurs et les listes générales de tiers, d'articles et de contrats sont retirés de « Ventes » : ils se trouvent dans « Achats », « Entrepôt » et « Trésorerie ».
- L'administrateur et le dirigeant trouvent dans le groupe « Clients » les « Responsables des contrats » : quel employé suit chaque contrat.
- Le rapport « Dettes clients en retard » est ajouté au menu et corrigé : il n'affiche que les dettes dont l'échéance est dépassée et le nombre de jours de retard (auparavant, toute la dette au-delà du crédit). Le délai de paiement est déterminé comme pour le contrôle du crédit : depuis le contrat, sinon depuis la fiche du client ; à défaut, un an. Le paramètre « Variante de dette », sans effet, est retiré des deux rapports de dettes en retard.
- Des rapports sont renommés d'après ce qu'ils affichent : « Statistiques de ventes quotidiennes » devient « Ventes par heure », « ABC - analyse des ventes » devient « Analyse ABC des ventes ».
- Le « Registre de factures de vente » passe de « Trésorerie » à « Ventes ». Les rapports fiscaux des règlements clients et l'état fiscal des ventes restent uniquement dans « Comptabilité », où passe aussi « Stock vendu non facturé ».
- Le bouton « Créer » de la section « Ventes » ne propose que les documents qui ouvrent le travail : commande client, vente, offre commerciale, tarification, règle de tarification.
- Dans « Options » → « Ventes », les réglages de la vente au détail (client de détail, contrat, impression du ticket) ne sont modifiables que si la vente au détail est activée. Le registre des paiements par chèque est masqué avec les paiements alternatifs.

### en
- The "Sales" section now follows the course of work. At the top: customer orders, sales and customer returns, with the order status history next to them. The rest is grouped into "Wholesale", "Retail", "Prices", "Customers", "Reference books". All reports of the section are gathered in one report list.
- The "Wholesale" group (commercial offers, order tasks, item search requests) disappears from the menu entirely when all these features are off in "Options"; the "Retail" group — when retail sales are off. "Item search request" no longer appears in the menu twice.
- In "Sales", items open as "Items for sale" — without raw materials and semi-finished goods — and contracts as "Customer contracts". Without production, "Items for sale" shows all items. Suppliers and the general lists of counterparties, items and contracts are removed from "Sales": they are in "Purchases", "Warehouse" and "Treasury".
- Administrators and managers see "Contract managers" in the "Customers" group: which employee handles each contract.
- The "Overdue customer debts" report is added to the menu and fixed: it shows only debts past their due date and how many days they are overdue (previously, all debt above the credit limit). The payment term is taken as in credit control: from the contract, or from the customer card if the contract has none; if neither has one, a year. The "Debt variant" parameter, which had no effect, is removed from both overdue debt reports.
- Reports are renamed after what they show: "Daily sales statistics" is now "Sales by hour", "ABC - sales analysis" is now "ABC sales analysis".
- The "Sales invoice register" moved from "Treasury" to "Sales". The tax reports on customer settlements and sales stay only in "Accounting", where "Stock sold not invoiced" moved too.
- The "Create" button in "Sales" offers only the documents that start the work: customer order, sale, commercial offer, price setting, pricing rule.
- In "Options" → "Sales", retail settings (retail customer, contract, receipt printing) can be changed only when retail sales are on. The cheque payments register is hidden together with alternative payments.

### es
- La sección «Ventas» sigue ahora el orden del trabajo. Arriba: pedidos de clientes, ventas y devoluciones de clientes, al lado el historial de pedidos por estado. El resto se agrupa en «Venta al por mayor», «Venta minorista», «Precios», «Clientes», «Manuales». Todos los informes de la sección están reunidos en una sola lista de informes.
- El grupo «Venta al por mayor» (ofertas comerciales, tareas de pedidos, solicitudes de búsqueda de artículos) desaparece por completo del menú si todas estas funciones están desactivadas en «Parámetros»; el grupo «Venta minorista», si las ventas minoristas están desactivadas. La «Solicitud de búsqueda de artículo» ya no aparece dos veces en el menú.
- En «Ventas», los artículos se abren con «Artículos para la venta» — sin materias primas ni semielaborados — y los contratos con «Contratos con clientes». Sin producción, «Artículos para la venta» muestra todos los artículos. Los proveedores y las listas generales de contrapartes, artículos y contratos se han quitado de «Ventas»: están en «Compras», «Almacén» y «Tesorería».
- El administrador y el director ven en el grupo «Clientes» los «Responsables de contratos»: qué empleado lleva cada contrato.
- El informe «Deudas vencidas de clientes» se ha añadido al menú y corregido: muestra solo las deudas con el plazo de pago vencido y cuántos días llevan vencidas (antes, toda la deuda por encima del crédito). El plazo de pago se toma como en el control de crédito: del contrato o, si no está indicado, de la ficha del cliente; si no figura en ninguno, un año. El parámetro «Variante de deuda», que no tenía efecto, se ha quitado de los dos informes de deudas vencidas.
- Informes renombrados según lo que muestran: «Estadísticas de ventas diarias» pasa a «Ventas por hora», «ABC-análisis de ventas» pasa a «Análisis ABC de ventas».
- El «Registro de facturas de ventas» pasa de «Tesorería» a «Ventas». Los informes fiscales de liquidaciones con clientes y de ventas quedan solo en «Contabilidad», adonde pasa también «Stock vendido no facturado».
- El botón «Crear» de «Ventas» ofrece solo los documentos con los que empieza el trabajo: pedido de cliente, venta, oferta comercial, fijación de precios, regla de precios.
- En «Parámetros» → «Ventas», los ajustes de venta minorista (cliente minorista, contrato, impresión del ticket) solo se pueden cambiar si las ventas minoristas están activadas. El registro de pagos con cheque se oculta junto con los pagos alternativos.

## 2.0.16.6
### ru
- Раздел «Закупки» перестроен по ходу работы. Наверху — заказы поставщикам, поступления товаров и услуг, возвраты поставщикам и обработка «Формирование заказов поставщикам» (раньше её не было в меню). Рядом — доп. расходы на поступление. Остальное разложено по группам: «Планирование», «Поставщики и цены», «Импорт», «Справочники».
- Группа «Импорт» (коды ТН ВЭД, номера таможенных деклараций) исчезает из меню целиком, если импорт выключен в «Параметрах».
- В «Закупках» номенклатура открывается пунктом «Закупаемые товары» — только то, что пополняется закупкой, — а договоры пунктом «Договоры с поставщиками». Без производства «Закупаемые товары» показывают всю номенклатуру.
- В «Планировании» появились «Минимальные остатки по складам»: их используют отчёты «Товары для заказа» и «Недостаточные запасы», а заполнить их из меню раньше было негде. Отчёт «Потребности производства» скрыт, если производство выключено.
- Отчёт «Просроченные долги поставщиков» исправлен (раньше не формировался) и выведен в меню; он показывает только долги с истёкшим сроком оплаты и сколько дней они просрочены.
- Отчёт «Еженедельное планирование задолженности поставщиков» называется «Долги поставщиков по товарам на складе» — по тому, что он показывает.
- «Реестр поступлений товаров и услуг» переехал из «Казначейства» в «Закупки». Налоговый отчёт «Расчеты с поставщиками» остался только в «Бухгалтерии», «Установка цен номенклатуры» — только в «Продажах».
- Кнопка «Создать» в «Закупках» предлагает только документы, с которых начинается работа: заказ поставщику, поступление, доп. расходы, предложение поставщика.
- Цены закупки теперь видны в меню и у сотрудников склада, логистики и казначейства, предложения поставщиков — и у казначейства: раньше эту группу видел только администратор. Права на данные не менялись.

### fr
- La section « Achats » suit désormais l'ordre du travail. En haut : commandes fournisseurs, réceptions de marchandises et services, retours fournisseurs et le traitement « Génération des commandes fournisseurs » (auparavant absent du menu). À côté : les frais annexes de réception. Le reste est réparti en groupes : « Planification », « Fournisseurs et prix », « Importation », « Référentiels ».
- Le groupe « Importation » (codes SH, numéros de déclaration en douane) disparaît entièrement du menu si l'importation est désactivée dans les « Options ».
- Dans « Achats », les articles s'ouvrent par « Articles achetés » — uniquement ceux réapprovisionnés par achat — et les contrats par « Contrats fournisseurs ». Sans production, « Articles achetés » affiche tous les articles.
- La « Planification » propose les « Stocks minimaux par entrepôt » : les rapports « Marchandises à commander » et « Stocks insuffisants » s'en servent, mais aucun menu ne permettait de les saisir. Le rapport « Besoins de production » est masqué si la production est désactivée.
- Le rapport « Dettes fournisseurs en retard » est corrigé (il ne se générait pas) et ajouté au menu ; il n'affiche que les dettes dont l'échéance est dépassée et le nombre de jours de retard.
- Le rapport « Planning hebdomadaire de debt fournisseurs » s'appelle « Dettes fournisseurs sur stock en magasin », d'après ce qu'il affiche.
- Le « Registre des factures d'achat » passe de « Trésorerie » à « Achats ». Le rapport fiscal des règlements fournisseurs reste uniquement dans « Comptabilité », la « Tarification » uniquement dans « Ventes ».
- Le bouton « Créer » de la section « Achats » ne propose que les documents qui ouvrent le travail : commande fournisseur, réception, frais annexes, offre fournisseur.
- Les prix d'achat sont désormais visibles dans le menu pour le personnel de l'entrepôt, de la logistique et de la trésorerie, et les offres fournisseurs pour la trésorerie : auparavant seul l'administrateur voyait ce groupe. Les droits sur les données n'ont pas changé.

### en
- The "Purchases" section now follows the course of work. At the top: purchase orders, goods and services receipts, returns to suppliers and the "Purchase order generation" tool (previously missing from the menu). Next to them: additional receipt costs. The rest is grouped into "Planning", "Suppliers and prices", "Import", "Reference books".
- The "Import" group (HS codes, customs declaration numbers) disappears from the menu entirely when import is off in "Options".
- In "Purchases", items open as "Purchased items" — only those replenished by purchase — and contracts as "Supplier contracts". Without production, "Purchased items" shows all items.
- "Planning" now has "Minimum stock by warehouse": the "Goods to order" and "Insufficient stocks" reports use it, but there was nowhere in the menu to fill it in. The "Production requirements" report is hidden when production is off.
- The "Overdue supplier debts" report is fixed (it did not generate) and added to the menu; it shows only debts past their due date and how many days they are overdue.
- The "Weekly schedule of debt suppliers" report is now called "Supplier debts on goods in stock", after what it shows.
- The "Purchase invoice register" moved from "Treasury" to "Purchases". The tax report on supplier settlements stays only in "Accounting", "Setting item prices" only in "Sales".
- The "Create" button in "Purchases" offers only the documents that start the work: purchase order, receipt, additional costs, supplier offer.
- Purchase prices are now visible in the menu to warehouse, logistics and treasury staff, and supplier offers to treasury staff: previously only the administrator saw that group. Data access rights have not changed.

### es
- La sección «Compras» sigue ahora el orden del trabajo. Arriba: pedidos a proveedores, recepciones de mercancías y servicios, devoluciones a proveedores y el procesamiento «Generación de pedidos a proveedores» (antes no estaba en el menú). Al lado: los gastos adicionales de recepción. El resto se agrupa en «Planificación», «Proveedores y precios», «Importación», «Catálogos».
- El grupo «Importación» (códigos HS, números de declaración aduanera) desaparece por completo del menú si la importación está desactivada en «Parámetros».
- En «Compras», los artículos se abren con «Artículos comprados» — solo los que se reponen por compra — y los contratos con «Contratos con proveedores». Sin producción, «Artículos comprados» muestra todos los artículos.
- En «Planificación» aparecen las «Existencias mínimas por almacén»: las usan los informes «Productos a pedido» y «Existencias insuficientes», pero no había dónde rellenarlas desde el menú. El informe «Necesidades de producción» se oculta si la producción está desactivada.
- El informe «Deudas vencidas con proveedores» se ha corregido (no se generaba) y se ha añadido al menú; muestra solo las deudas con el plazo de pago vencido y cuántos días llevan vencidas.
- El informe «Calendario semanal de proveedores de deuda» se llama «Deudas con proveedores por mercancía en almacén», según lo que muestra.
- El «Registro de facturas de compra» pasa de «Tesorería» a «Compras». El informe fiscal de liquidaciones con proveedores queda solo en «Contabilidad» y la «Fijación de precios de artículos», solo en «Ventas».
- El botón «Crear» de «Compras» ofrece solo los documentos con los que empieza el trabajo: pedido a proveedor, recepción, gastos adicionales, oferta del proveedor.
- Los precios de compra ahora son visibles en el menú para el personal de almacén, logística y tesorería, y las ofertas de proveedores para tesorería; antes solo el administrador veía ese grupo. Los derechos sobre los datos no han cambiado.

## 2.0.16.5
### ru
- Возможности программы, которыми вы не пользуетесь, можно выключить — тогда они исчезнут из меню. Переключатели собраны в «Настройка» → «Параметры», по форме на раздел: в «Закупках» — импорт (коды ТН ВЭД, таможенные декларации, страна происхождения); в «Продажах» — заказы покупателей, коммерческие предложения, задачи по заказам, заявки на поиск товара, розничные продажи, правила ценообразования; в новой форме «Склад» — ячейки, инвентаризация, комплектация и пересортица; в «Производстве» — переработка; в новых формах «Казначейство» — альтернативные оплаты (сертификаты, банковские чеки), «Бухгалтерия» — раздел и регламентированный учёт (план счетов, проводки, бухгалтерские отчёты), «CRM» — лиды и личный кабинет клиента.
- После обновления всё, что было у вас в меню, остаётся в меню: новые возможности включены. Регламентированный учёт включён, только если был включён раздел «Бухгалтерия».
- Переключатель раздела «Бухгалтерия» переехал из формы «Компания и учёт» в форму «Бухгалтерия».
- В новой базе мастер первого запуска получил шаг «Возможности»: сразу отметьте, чем будете пользоваться, — остальное не попадёт в меню.
- Номер таможенной декларации у серии больше не требует страну происхождения, если импорт выключен.
- Тендеры поставщиков включаются, только если включены заказы покупателей или производство: предложение поставщика вводится по заказу. Мастер первого запуска так же выключает зависимые возможности без основной — регламентированный учёт без бухгалтерии, переработку без производства.

### fr
- Les fonctionnalités que vous n'utilisez pas peuvent être désactivées : elles disparaissent alors du menu. Les interrupteurs se trouvent dans « Paramètres » → « Options », un formulaire par section : dans « Achats » — l'importation (codes SH, déclarations en douane, pays d'origine) ; dans « Ventes » — commandes clients, devis, tâches des commandes, demandes de recherche d'article, vente au détail, règles de tarification ; dans le nouveau formulaire « Entrepôt » — emplacements, inventaire, kits et reclassements ; dans « Production » — la sous-traitance ; dans les nouveaux formulaires « Trésorerie » — moyens de paiement alternatifs (bons, chèques bancaires), « Comptabilité » — la section et la comptabilité réglementée (plan comptable, écritures, états comptables), « CRM » — prospects et espace client.
- Après la mise à jour, tout ce qui était dans votre menu y reste : les nouvelles fonctionnalités sont activées. La comptabilité réglementée n'est activée que si la section « Comptabilité » l'était.
- L'interrupteur de la section « Comptabilité » a quitté le formulaire « Entreprise et comptabilité » pour le formulaire « Comptabilité ».
- Dans une nouvelle base, l'assistant de premier lancement a une étape « Fonctionnalités » : cochez d'emblée ce que vous utiliserez, le reste n'apparaîtra pas dans le menu.
- Le numéro de déclaration en douane d'une série n'exige plus le pays d'origine si l'importation est désactivée.
- Les appels d'offres fournisseurs ne s'activent que si les commandes clients ou la production sont activées : l'offre du fournisseur se saisit sur une commande. L'assistant de premier lancement désactive de même les fonctionnalités dépendantes sans la principale — la comptabilité réglementée sans la comptabilité, la sous-traitance sans la production.

### en
- Features you do not use can now be turned off, and they disappear from the menu. The switches are in "Settings" → "Options", one form per section: in "Purchases" — import (HS codes, customs declarations, country of origin); in "Sales" — customer orders, quotations, order tasks, item search requests, retail sales, pricing rules; in the new "Warehouse" form — storage bins, stock counts, kits and regrading; in "Production" — subcontracting; in the new "Treasury" form — alternative payments (vouchers, bank checks), "Accounting" — the section and statutory accounting (chart of accounts, entries, accounting reports), "CRM" — leads and the customer portal.
- After the update everything that was in your menu stays there: the new features are on. Statutory accounting is on only if the "Accounting" section was on.
- The "Accounting" section switch moved from the "Company and accounting" form to the "Accounting" form.
- In a new infobase the first start wizard has a "Features" step: tick what you will use right away, and the rest stays out of the menu.
- A customs declaration number on a series no longer requires the country of origin when import is off.
- Supplier tenders can be turned on only when customer orders or production are on: a supplier offer is entered from an order. The first start wizard likewise turns off dependent features without their main one — statutory accounting without accounting, subcontracting without production.

### es
- Las funcionalidades que no usa se pueden desactivar y desaparecen del menú. Los interruptores están en «Configuración» → «Parámetros», un formulario por sección: en «Compras» — la importación (códigos HS, declaraciones aduaneras, país de origen); en «Ventas» — pedidos de clientes, presupuestos, tareas de pedidos, solicitudes de búsqueda de artículos, venta minorista, reglas de precios; en el nuevo formulario «Almacén» — ubicaciones, inventario, kits y reclasificaciones; en «Producción» — la subcontratación; en los nuevos formularios «Tesorería» — pagos alternativos (vales, cheques bancarios), «Contabilidad» — la sección y la contabilidad reglamentaria (plan de cuentas, asientos, informes contables), «CRM» — clientes potenciales y portal del cliente.
- Tras la actualización, todo lo que estaba en su menú sigue en él: las nuevas funcionalidades están activadas. La contabilidad reglamentaria solo se activa si la sección «Contabilidad» lo estaba.
- El interruptor de la sección «Contabilidad» pasó del formulario «Empresa y contabilidad» al formulario «Contabilidad».
- En una base nueva, el asistente de primer inicio tiene el paso «Funcionalidades»: marque desde el principio lo que va a usar y el resto no aparecerá en el menú.
- El número de declaración aduanera de una serie ya no exige el país de origen si la importación está desactivada.
- Las licitaciones de proveedores solo se activan si los pedidos de clientes o la producción están activados: la oferta del proveedor se introduce a partir de un pedido. El asistente de primer inicio también desactiva las funcionalidades dependientes sin la principal: la contabilidad reglamentaria sin la contabilidad, la subcontratación sin la producción.

## 2.0.16.4
### ru
- Разделы программы выстроены по ходу работы: Закупки, Продажи, Склад, Производство, Казначейство, Бухгалтерия, Зарплата и кадры, затем CRM и Настройка. Раздел «E-commerce» называется «CRM», как и в других языках интерфейса. Если вы раньше сами переставляли разделы, программа сохранит ваш порядок.
- Группа «Настройки программы» в разделе «Настройка» называется «Параметры».
- Отчёт «Отчет по недостаткам товара» называется «Налоговые накладные: нехватка товара на складе» — по тому, что он показывает.
- Во французском, английском и испанском интерфейсе названия документов и справочников приведены к принятым в этих странах: налоговые накладные — «Facture fiscale», «Tax invoice», «Factura fiscal»; налоговые возвраты — «Avoir», «Credit note», «Factura rectificativa»; номера ГТД — таможенные декларации (DAU, DUM, DUA); кассовая смена — «Session de caisse», «Cash register shift», «Turno de caja». Исправлены дословные переводы: «Акт разбора», «Кадровый приказ», «Кассовая книга», «Возврат поставщику», виды субконто.

### fr
- Les sections du programme suivent l'ordre du travail : Achats, Ventes, Entrepôt, Production, Trésorerie, Comptabilité, Paie et personnel, puis CRM et Paramètres. Si vous aviez réorganisé les sections vous-même, votre ordre est conservé.
- Le groupe « Paramètres du programme » de la section « Paramètres » s'appelle « Options ».
- Le rapport « Stock brouillon » s'appelle « Factures fiscales : stock insuffisant », d'après ce qu'il affiche.
- Les noms des documents et des référentiels suivent les usages : la facture comptable devient « Facture fiscale » (et « Facture fiscale fournisseur » à l'achat), les retours fiscaux deviennent « Avoir client » et « Avoir fournisseur », les numéros de déclaration en douane — « Déclarations en douane (DAU, DUM) », la journée de caisse — « Session de caisse », la feuille de caisse — « Livre de caisse », les types de subconto — « Types d'analytique ».

### en
- The program sections follow the course of work: Purchases, Sales, Warehouse, Production, Treasury, Accounting, Payroll and staff, then CRM and Settings. If you had rearranged the sections yourself, your order is kept.
- The "Program settings" group of the "Settings" section is now called "Options".
- The "Draft stock" report is now called "Tax invoices: insufficient stock", to reflect what it shows.
- Document and catalog names follow common usage: "Accounting invoice" is now "Tax invoice" ("Supplier tax invoice" for purchases); the returns issued with a tax invoice are "Customer credit note" and "Supplier credit note"; customs declaration numbers are "Customs declarations"; "Checkout day" is "Cash register shift"; "Cash sheet" is "Cash book"; "The act of parsing" is "Kit disassembly"; subconto types are "Analytics types"; customer and supplier returns are "Customer return" and "Supplier return".

### es
- Las secciones del programa siguen el orden del trabajo: Compras, Ventas, Almacén, Producción, Tesorería, Contabilidad, Nómina y personal, después CRM y Configuración. Si había reordenado las secciones usted mismo, se conserva su orden.
- El grupo «Configuración del programa» de la sección «Configuración» se llama «Parámetros».
- El informe «Proyecto de stock» se llama «Facturas fiscales: existencias insuficientes», según lo que muestra.
- Los nombres de documentos y catálogos siguen el uso habitual: la factura contable es «Factura fiscal» («Factura fiscal recibida» en compras); las devoluciones con factura fiscal son «Factura rectificativa emitida» y «Factura rectificativa recibida»; los números de declaración de aduanas son «Declaraciones aduaneras (DUA)»; el cambio de caja es «Turno de caja»; la hoja de efectivo es «Libro de caja»; el acto de análisis es «Desmontaje de kit»; los tipos de subconto son «Tipos de analítica»; también se corrigieron la orden de personal, la devolución de cliente y la devolución al proveedor.

## 2.0.16.3
### ru
- Отчёт «Затраты» в разделе «Казначейство» снова формируется. Раньше он останавливался с ошибкой «Поле не найдено "Подразделение"»: группировка была настроена по полю, которого в программе нет. Теперь затраты группируются по организации, месту хранения и статье движения денежных средств.

### fr
- Le rapport « Dépenses » de la section « Trésorerie » se génère de nouveau. Auparavant il s'arrêtait sur l'erreur « Champ introuvable "Подразделение" » : le regroupement portait sur un champ qui n'existe pas dans le programme. Les dépenses sont maintenant regroupées par organisation, entrepôt et poste de flux de trésorerie.

### en
- The "Expenses" report in the "Treasury" section generates again. Previously it stopped with the error "Field not found "Подразделение"": it was grouped by a field that does not exist in the program. Expenses are now grouped by organization, warehouse and cash flow item.

### es
- El informe «Gastos» de la sección «Tesorería» vuelve a generarse. Antes se detenía con el error «Campo no encontrado "Подразделение"»: la agrupación usaba un campo que no existe en el programa. Ahora los gastos se agrupan por organización, almacén y partida de flujo de efectivo.

## 2.0.16.2
### ru
- Цена, которую добавили в карточку товара, теперь подставляется в документ продажи. Если товар выбрали в строке коммерческого предложения, заказа или реализации, когда цены у него ещё не было, строка теряла вид цены и дальше считалась строкой с произвольной ценой: цена, установленная позже, не появлялась даже при повторном выборе того же товара. Теперь вид цены в строке сохраняется, и повторный выбор товара подставляет новую цену. В строках, сохранённых раньше, цену подставит кнопка «Перезаполнить цены» (в реализации — «По прайсу»); она перезаполняет цены всех строк документа, в том числе введённые вручную. Цену товара без прайса по-прежнему можно ввести вручную, в том числе в мобильных формах и в заказе интернет-магазина.

### fr
- Le prix ajouté dans la fiche article est désormais repris dans le document de vente. Si l'article était choisi dans une ligne de devis, de commande ou de vente alors qu'il n'avait pas encore de prix, la ligne perdait son type de prix et était ensuite traitée comme une ligne à prix libre : le prix défini plus tard n'apparaissait pas, même en choisissant de nouveau le même article. Le type de prix de la ligne est maintenant conservé, et choisir de nouveau l'article reprend le nouveau prix. Dans les lignes enregistrées auparavant, le bouton « Actualiser les prix » (dans la vente : « Par liste de prix ») reprend le prix ; il recalcule les prix de toutes les lignes du document, y compris ceux saisis à la main. Le prix d'un article sans tarif peut toujours être saisi à la main, y compris dans les formulaires mobiles et dans la commande de la boutique en ligne.

### en
- A price added on the item card is now picked up by the sales document. If the item was chosen in a line of a quotation, order or sale while it had no price yet, the line lost its price type and was then treated as a free-price line: a price set later did not appear even when the same item was chosen again. The line now keeps its price type, and choosing the item again fills in the new price. In lines saved earlier, the "Update prices" button (in the sale: "By price list") fills in the price; it refills the prices of all lines of the document, including those entered by hand. The price of an item with no price list entry can still be entered by hand, including in the mobile forms and in the online store order.

### es
- El precio añadido en la ficha del artículo ahora se aplica en el documento de venta. Si el artículo se elegía en una línea de presupuesto, pedido o venta cuando aún no tenía precio, la línea perdía su tipo de precio y pasaba a tratarse como línea de precio libre: el precio fijado después no aparecía ni al volver a elegir el mismo artículo. Ahora la línea conserva su tipo de precio, y volver a elegir el artículo aplica el nuevo precio. En las líneas guardadas antes, el botón «Reiniciar precios» (en la venta: «Por Price») aplica el precio; vuelve a rellenar los precios de todas las líneas del documento, incluidos los introducidos a mano. El precio de un artículo sin tarifa se puede seguir introduciendo a mano, también en los formularios móviles y en el pedido de la tienda en línea.

## 2.0.16.1
### ru
- Налоговые документы больше не двигают товар на складе: налоговая накладная, налоговая накладная покупки и налоговые возвраты от покупателя и поставщику меняют только расчёты и деньги. Остатки ведут реализация и поступление. Раньше налоговая накладная списывала уже проданный товар второй раз и отказывала в проведении, если на складе его не осталось, а налоговая накладная покупки оприходовала товар повторно поверх поступления. Склад по-прежнему должен быть помечен как склад налогового учёта.

### fr
- Les documents fiscaux ne font plus bouger les marchandises en stock : la facture fiscale, la facture fiscale d'achat et les retours fiscaux client et fournisseur ne modifient que les règlements et la trésorerie. Les stocks sont tenus par la vente et la réception. Auparavant, la facture fiscale sortait une seconde fois une marchandise déjà vendue et refusait la validation s'il n'en restait plus en stock, et la facture fiscale d'achat entrait la marchandise une seconde fois en plus de la réception. L'entrepôt doit toujours être marqué comme entrepôt de comptabilité fiscale.

### en
- Tax documents no longer move goods in stock: the tax invoice, the purchase tax invoice and the customer and supplier tax returns change only settlements and cash. Stock is kept by the sale and the receipt. Previously the tax invoice wrote off already sold goods a second time and refused to post when none were left in stock, and the purchase tax invoice received the goods a second time on top of the receipt. The warehouse must still be marked as a tax accounting warehouse.

### es
- Los documentos fiscales ya no mueven mercancías en el almacén: la factura fiscal, la factura fiscal de compra y las devoluciones fiscales de cliente y a proveedor solo cambian los cobros y pagos y el dinero. Las existencias las llevan la venta y la recepción. Antes la factura fiscal daba de baja por segunda vez la mercancía ya vendida y se negaba a contabilizarse si no quedaba en el almacén, y la factura fiscal de compra daba entrada a la mercancía por segunda vez además de la recepción. El almacén debe seguir marcado como almacén de contabilidad fiscal.

# Релиз 2.0.15.71 (2026-09-26)

Поставка: `maERP-2.0.15.71.cf`; обновление с опубликованных релизов — `maERP-2.0.15.71.cfu`.
Технологические карты отдельными документами, многоуровневые карты и потери,
полуфабрикаты в переработке, расчёты на налоговой накладной, единые меню печати
и подписи на четырёх языках, избранное в РМК, исправления по итогам регресса.

## 2.0.15.71
### ru
- В рабочем месте кассира заработали плитки избранной номенклатуры. Форма избранного не открывалась совсем: запрос цен и наименований был написан так, что платформа не могла понять, о какой номенклатуре идёт речь, и прерывался с ошибкой при каждом открытии. Плитки не работали с момента появления функции.

### fr
- Dans le poste de caisse, les vignettes des articles favoris fonctionnent désormais. Le formulaire des favoris ne s'ouvrait pas du tout : la requête des prix et des désignations était écrite de telle façon que la plateforme ne pouvait pas déterminer de quel article il s'agissait et s'interrompait par une erreur à chaque ouverture. Les vignettes n'avaient jamais fonctionné depuis l'apparition de la fonction.

### en
- Favourite item tiles now work in the cashier workstation. The favourites form did not open at all: the query for prices and names was written so that the platform could not tell which item was meant, and it failed with an error on every opening. The tiles had never worked since the feature appeared.

### es
- En el puesto de caja ya funcionan los mosaicos de artículos favoritos. El formulario de favoritos no se abría en absoluto: la consulta de precios y denominaciones estaba escrita de modo que la plataforma no podía saber de qué artículo se trataba y se interrumpía con un error en cada apertura. Los mosaicos no habían funcionado nunca desde que apareció la función.

## 2.0.15.70
### ru
- Документ «Пересчёт товаров» и ещё 27 форм документов не открывались бы на тонком клиенте: колонка «Единица» в табличной части товаров обращалась к настройке «Использовать упаковку» способом, который тонкому клиенту недоступен. Ошибка появилась вместе с самой колонкой и найдена проверкой конфигурации до передачи.
- В приходном кассовом ордере меню «Печать» стало одним и в форме документа, и в списке: пункт «Чек» размещался в панели отдельно от остальных, из-за чего кнопок печати было две. Теперь все печатные формы ордера собраны в одно меню.
- В форме подбора двойной щелчок по группе снова открывает её. Список показан иерархически, и войти в папку можно только так; прежде щелчок по группе не делал ничего, и до товаров внутри групп нельзя было добраться иначе как поиском.

### fr
- Le document « Recomptage des marchandises » et 27 autres formulaires de documents n'auraient pas pu s'ouvrir sur le client léger : la colonne « Unité » du tableau des marchandises interrogeait le paramètre « Utiliser le conditionnement » d'une manière indisponible sur le client léger. L'erreur est apparue avec la colonne elle-même et a été détectée par la vérification de la configuration avant la livraison.
- Dans l'entrée de caisse, le menu « Impression » est désormais unique dans le formulaire du document comme dans la liste : l'élément « Ticket » était placé séparément des autres, ce qui donnait deux boutons d'impression. Toutes les impressions de l'entrée de caisse sont maintenant réunies dans un seul menu.
- Dans le formulaire de sélection, un double-clic sur un groupe l'ouvre de nouveau. La liste est hiérarchique et c'est le seul moyen d'entrer dans un dossier ; auparavant le clic sur un groupe ne faisait rien et les articles à l'intérieur des groupes n'étaient accessibles que par la recherche.

### en
- The Goods recount document and 27 other document forms would have failed to open on the thin client: the Unit column of the goods table queried the "Use packaging" setting in a way unavailable on the thin client. The defect arrived together with the column itself and was caught by the configuration check before handover.
- In the cash receipt order the Print menu is now a single one both in the document form and in the list: the Receipt entry was placed separately from the rest, which produced two print buttons. All print forms of the order are now gathered in one menu.
- In the picking form a double click on a folder opens it again. The list is hierarchical and that is the only way into a folder; previously clicking a folder did nothing, and items inside folders could be reached only by search.

### es
- El documento «Recuento de mercancías» y otros 27 formularios de documentos no se habrían abierto en el cliente ligero: la columna «Unidad» de la tabla de mercancías consultaba el ajuste «Usar embalaje» de una forma no disponible en el cliente ligero. El error apareció junto con la propia columna y se detectó con la comprobación de la configuración antes de la entrega.
- En la orden de caja de entrada el menú «Impresión» ahora es único tanto en el formulario del documento como en la lista: el elemento «Ticket» estaba colocado aparte de los demás, lo que producía dos botones de impresión. Todas las impresiones de la orden están ahora reunidas en un solo menú.
- En el formulario de selección, el doble clic en un grupo vuelve a abrirlo. La lista es jerárquica y es la única forma de entrar en una carpeta; antes el clic en un grupo no hacía nada y los artículos dentro de los grupos solo se alcanzaban con la búsqueda.

## 2.0.15.69
### ru
- Подбор товара в документах больше не падает с ошибкой «Поле объекта не обнаружено (ЭтоГруппа)». Двойной щелчок по строке в форме подбора снова добавляет товар в документ, щелчок по группе, как и раньше, товар не добавляет.

### fr
- La sélection d'articles dans les documents ne s'interrompt plus avec l'erreur « Champ d'objet non trouvé (EstUnGroupe) ». Un double-clic sur une ligne du formulaire de sélection ajoute de nouveau l'article au document ; un clic sur un groupe n'ajoute toujours rien.

### en
- Item picking in documents no longer fails with the error "Object field not found (ЭтоГруппа)". Double-clicking a row in the picking form adds the item to the document again; clicking a folder still adds nothing.

### es
- La selección de artículos en los documentos ya no falla con el error «Campo del objeto no encontrado (ЭтоГруппа)». El doble clic en una fila del formulario de selección vuelve a añadir el artículo al documento; al hacer clic en un grupo sigue sin añadirse nada.

## 2.0.15.68
### ru
- Меню «Печать» стало одним во всех документах, где показывалось два: возвраты от покупателя, заказ покупателя, налоговая накладная, поступление товаров, приходный и расходный кассовые ордера, а также форма выбора реализации.
- Из меню реализации убран повтор «Счёт на оплату». Второй пункт приходил от налоговой накладной и печатал ровно тот же счёт — теперь он остался только в самой налоговой накладной.
- Разведены одинаковые названия печатных форм: прежняя накладная называется «Товарная накладная (прежняя)», печать чека без окна просмотра — «Чек на принтер».
- В испанском интерфейсе чек назывался Cheque, то есть банковский чек. Исправлено на Ticket de caja.

### fr
- Le menu « Impression » est désormais unique dans tous les documents où il apparaissait en double : retours client, commande client, facture fiscale, réception de marchandises, entrées et sorties de caisse, ainsi que le formulaire de sélection des ventes.
- Le doublon « Facture proforma » a été retiré du menu des ventes. Le second élément venait de la facture fiscale et imprimait exactement la même proforma : il ne subsiste que dans la facture fiscale elle-même.
- Les libellés identiques ont été différenciés : l'ancienne facture s'appelle « Facture (ancienne) » et l'impression directe du ticket « Ticket (impression directe) ».
- Dans l'interface espagnole, le ticket s'appelait Cheque, c'est-à-dire un chèque bancaire. Corrigé en Ticket de caja.

### en
- The Print menu is now a single one in every document where two were shown: customer returns, customer order, tax invoice, goods receipt, cash receipt and cash payment orders, and the sales selection form.
- The duplicate Proforma invoice entry was removed from the sales menu. The second entry came from the tax invoice and printed exactly the same form; it now remains only in the tax invoice itself.
- Identical print form names were disambiguated: the previous invoice is now Invoice (previous), and direct receipt printing is Receipt (direct print).
- In the Spanish interface the receipt was called Cheque, i.e. a bank cheque. Corrected to Ticket de caja.

### es
- El menú «Impresión» ahora es único en todos los documentos donde aparecía dos veces: devoluciones de cliente, pedido de cliente, factura fiscal, recepción de mercancías, órdenes de caja de entrada y salida, y el formulario de selección de ventas.
- Se eliminó el duplicado «Factura proforma» del menú de ventas. El segundo elemento provenía de la factura fiscal e imprimía exactamente lo mismo; ahora permanece solo en la propia factura fiscal.
- Se diferenciaron los nombres iguales: la factura anterior se llama «Factura (anterior)» y la impresión directa del ticket, «Ticket (impresión directa)».
- En la interfaz española el ticket se llamaba Cheque, es decir, un cheque bancario. Corregido a Ticket de caja.

## 2.0.15.67
### ru
- В списке продаж меню «Печать» стало одним. Раньше в панели было две кнопки «Печать» с разными наборами печатных форм: часть форм была разложена по меню вручную, остальные платформа добавляла сама и показывала отдельной кнопкой. Теперь все печатные формы реализации собраны в одно меню.

### fr
- Dans la liste des ventes, le menu « Impression » est désormais unique. Auparavant, la barre affichait deux boutons « Impression » avec des jeux de formulaires différents : une partie des formulaires était placée manuellement, les autres étaient ajoutés par la plateforme dans un bouton séparé. Tous les formulaires d'impression de la vente sont maintenant réunis dans un seul menu.

### en
- The Print menu in the sales list is now a single one. Previously the bar showed two Print buttons with different sets of print forms: some forms were placed manually, the rest were added by the platform as a separate button. All print forms of the sales document are now gathered in one menu.

### es
- En la lista de ventas el menú «Impresión» ahora es único. Antes la barra mostraba dos botones «Impresión» con conjuntos distintos de formularios: una parte estaba colocada manualmente y el resto lo añadía la plataforma en un botón aparte. Ahora todos los formularios de impresión de la venta están reunidos en un solo menú.

## 2.0.15.66
### ru
- В печати Devis / BL на A4 без НДС выправлен блок итогов. Подпись и сумма строк TOTAL HT, TOTAL TVA и TOTAL TTC стояли в одиночных ячейках: рамка блока обрывалась раньше, чем у блока TOTAL над ним, суммы прижимались влево и длинное число могло не поместиться. Теперь ячейки объединены так же, как в обычном блоке TOTAL, и оба блока совпадают по ширине.

### fr
- Dans l'impression Devis / BL au format A4 hors taxes, le bloc des totaux a été corrigé. Le libellé et le montant des lignes TOTAL HT, TOTAL TVA et TOTAL TTC occupaient des cellules simples : le cadre du bloc s'arrêtait avant celui du bloc TOTAL situé au-dessus, les montants étaient collés à gauche et un nombre long pouvait ne pas tenir. Les cellules sont désormais fusionnées comme dans le bloc TOTAL habituel, et les deux blocs ont la même largeur.

### en
- The totals block of the Devis / BL A4 printout without VAT has been fixed. The label and the amount of the TOTAL HT, TOTAL TVA and TOTAL TTC lines sat in single cells: the block frame ended earlier than the frame of the TOTAL block above it, the amounts were pushed to the left and a long number could fail to fit. The cells are now merged the same way as in the regular TOTAL block, and both blocks are of equal width.

### es
- En la impresión Devis / BL en A4 sin IVA se corrigió el bloque de totales. La etiqueta y el importe de las líneas TOTAL HT, TOTAL TVA y TOTAL TTC estaban en celdas sueltas: el marco del bloque terminaba antes que el del bloque TOTAL situado encima, los importes quedaban pegados a la izquierda y un número largo podía no caber. Ahora las celdas están combinadas igual que en el bloque TOTAL habitual y ambos bloques coinciden en anchura.

## 2.0.15.65
### ru
- Реквизиты документов теперь называются одинаково во всех документах и на всех четырёх языках. Раньше одно и то же поле в разных документах подписывалось по-разному, особенно в переводах: «Основание» по-английски в восемнадцати документах называлось Footing (не то слово), «Цена включает НДС» по-французски писалась то TVA incluse, то TVA inclus, «Организация» переводилась тремя разными словами. Всего выправлено 62 подписи в 29 документах.
- Контрагент подписан по смыслу документа: в продаже, заказе клиента, коммерческом предложении, возврате от покупателя и налоговой накладной — «Клиент»; в поступлении, заказе поставщику, возврате поставщику и накладной на закупку — «Поставщик»; в передаче в переработку и поступлении из переработки — «Переработчик»; в кассовых, банковских и прочих денежных документах, где контрагент бывает и тем и другим, — «Контрагент». Так же теперь подписаны и поля отбора в списках этих документов: раньше в приходном и расходном кассовом ордере фильтр назывался «Клиент», хотя ордер бывает и по поставщику.
- В отчётах колонка «Контрагент» больше не зависит от того, из какого документа пришла строка. В «Истории товара», где в одну таблицу собираются одиннадцать видов документов, и в ведомости расчётов с контрагентами заголовок колонки задан явно на четырёх языках и остаётся «Контрагент» — до этого он мог показать «Клиент» над строками по поставщику.
- В перемещении товаров, акте разбора и выпуске продукции поля складов подписаны «Списать с» и «Оприходовать на» на всех языках — раньше эти подписи были только в русском интерфейсе, а в остальных оба поля назывались «Место хранения».

### fr
- Les attributs des documents portent désormais le même nom dans tous les documents et dans les quatre langues. Auparavant, un même champ était libellé différemment selon le document, surtout dans les traductions : « Base » était rendu en anglais par Footing (mot erroné) dans dix-huit documents, « TVA incluse » s'écrivait tantôt TVA incluse, tantôt TVA inclus, et « Organisation » était traduit par trois mots différents. Au total, 62 libellés ont été corrigés dans 29 documents.
- Le tiers est libellé selon le sens du document : « Client » dans la vente, la commande client, la proposition commerciale, le retour client et la facture fiscale ; « Fournisseur » dans la réception, la commande fournisseur, le retour fournisseur et la facture fiscale d'achat ; « Sous-traitant » dans le transfert en sous-traitance et la réception de sous-traitance ; « Contrepartie » dans les documents de caisse et de banque, où le tiers peut être l'un ou l'autre. Les champs de filtre des listes de ces documents suivent la même règle : le filtre des ordres de caisse s'appelait « Client », alors qu'un ordre peut concerner un fournisseur.
- Dans les états, la colonne « Contrepartie » ne dépend plus du document d'origine de la ligne. Dans « Historique de l'article », qui réunit onze types de documents dans un même tableau, et dans l'état des règlements avec les tiers, l'en-tête est défini explicitement dans les quatre langues et reste « Contrepartie » — auparavant il pouvait afficher « Client » au-dessus de lignes fournisseur.
- Dans le transfert de marchandises, l'acte de démontage et la production, les champs d'entrepôt sont libellés « Radier de » et « Réceptionner à » dans toutes les langues — ces libellés n'existaient jusqu'ici qu'en russe, ailleurs les deux champs s'appelaient « Entrepôt ».

### en
- Document attributes now carry the same name in every document and in all four languages. Previously the same field was labelled differently from document to document, especially in translations: "Basis" was rendered as Footing (the wrong word) in eighteen documents, "VAT included" was written both as TVA incluse and TVA inclus in French, and "Organization" was translated with three different words. In total, 62 labels were corrected across 29 documents.
- The counterparty is labelled by the meaning of the document: "Customer" in the sale, customer order, commercial proposal, customer return and tax invoice; "Supplier" in the receipt, purchase order, supplier return and purchase tax invoice; "Processor" in transfer to subcontracting and receipt from subcontracting; "Counterparty" in cash and bank documents, where the party can be either. The list filter fields of those documents now follow the same rule: in cash orders the filter used to read "Customer", although an order can be for a supplier.
- In reports, the "Counterparty" column no longer depends on which document the row came from. In "Product history", which gathers eleven document types into one table, and in the counterparty settlements report, the column header is set explicitly in all four languages and stays "Counterparty" — before that it could show "Customer" above supplier rows.
- In goods transfer, disassembly act and production, the warehouse fields are labelled "Write off from" and "Receive to" in every language — until now those labels existed only in the Russian interface, elsewhere both fields read "Warehouse".

### es
- Los atributos de los documentos se llaman ahora igual en todos los documentos y en los cuatro idiomas. Antes, un mismo campo se etiquetaba de forma distinta según el documento, sobre todo en las traducciones: «Base» se traducía al inglés como Footing (palabra equivocada) en dieciocho documentos, «IVA incluido» se escribía en francés unas veces TVA incluse y otras TVA inclus, y «Organización» se traducía con tres palabras distintas. En total se corrigieron 62 etiquetas en 29 documentos.
- La contraparte se etiqueta según el sentido del documento: «Cliente» en la venta, el pedido de cliente, la propuesta comercial, la devolución de cliente y la factura fiscal; «Proveedor» en la recepción, el pedido a proveedor, la devolución a proveedor y la factura fiscal de compra; «Procesador» en la entrega a maquila y la recepción de maquila; «Contraparte» en los documentos de caja y banco, donde puede ser lo uno o lo otro. Los campos de filtro de las listas de esos documentos siguen la misma regla: en las órdenes de caja el filtro decía «Cliente», aunque una orden puede ser de un proveedor.
- En los informes, la columna «Contraparte» ya no depende del documento del que proviene la línea. En «Historial del artículo», que reúne once tipos de documentos en una sola tabla, y en el estado de liquidaciones con contrapartes, el encabezado se define explícitamente en los cuatro idiomas y sigue siendo «Contraparte»; antes podía mostrar «Cliente» sobre líneas de proveedor.
- En el traslado de mercancías, el acta de desmontaje y la producción, los campos de almacén se etiquetan «Dar de baja de» y «Recibir en» en todos los idiomas: hasta ahora esas etiquetas solo existían en la interfaz rusa, en las demás ambos campos decían «Almacén».

## 2.0.15.64
### ru
- Отчёт «История товара» снова показывает строки. В прошлой сборке отбор по датам в схеме отчёта был, а поля периода на форму не выводились: период всегда оставался пустым и отчёт получался пустым. Теперь на форме отчёта есть поле «Период» с обычным выбором периода, а вызов из документа («Товар» → «История товара» на строке табличной части) по-прежнему открывает отчёт сразу за последние 12 месяцев. Если период не заполнен, показывается вся история товара. Отбор по товару на форме по умолчанию снят: из меню отчётов отчёт открывается по всем товарам, а команда из документа ставит отбор по товару и контрагенту сама.

### fr
- L'état « Historique de l'article » affiche de nouveau des lignes. Dans la version précédente, la sélection par dates existait dans le schéma de l'état, mais les champs de période n'étaient pas affichés sur le formulaire : la période restait toujours vide et l'état sortait vide. Le formulaire de l'état comporte maintenant un champ « Période » avec le choix de période habituel, et l'appel depuis un document (« Article » → « Historique article » sur une ligne de la partie tabulaire) ouvre toujours l'état sur les 12 derniers mois. Si la période n'est pas renseignée, tout l'historique de l'article s'affiche. La sélection par article est décochée par défaut : depuis le menu des états, l'état s'ouvre sur tous les articles, tandis que l'appel depuis un document pose lui-même la sélection par article et par tiers.

### en
- The "Product history" report shows rows again. In the previous build the date filter existed in the report schema, but the period fields were not placed on the form: the period always stayed empty and the report came out empty. The report form now has a "Period" field with the usual period picker, and opening the report from a document ("Product" → "Product history" on a table row) still shows the last 12 months right away. With the period left empty, the whole history of the product is shown. The product filter is cleared by default: from the reports menu the report opens for all products, while the call from a document sets the product and counterparty filters itself.

### es
- El informe «Historial del artículo» vuelve a mostrar líneas. En la compilación anterior la selección por fechas estaba en el esquema del informe, pero los campos del período no se mostraban en el formulario: el período quedaba siempre vacío y el informe salía vacío. Ahora el formulario del informe tiene el campo «Período» con el selector de período habitual, y la llamada desde un documento («Artículo» → «Historial del artículo» en una línea de la parte tabular) sigue abriendo el informe por los últimos 12 meses. Si el período se deja vacío, se muestra todo el historial del artículo. La selección por artículo está desmarcada por defecto: desde el menú de informes el informe se abre para todos los artículos, mientras que la llamada desde un documento establece por sí misma la selección por artículo y por contraparte.

## 2.0.15.63
### ru
- В пагинаторе списков документов появились кнопки перехода в начало и в конец: «◀◀» листает на первую страницу, «▶▶» — на последнюю. Прежние стрелки на страницу назад и вперёд остались на своих местах.
- Рядом со страницами показывается счётчик записей — «1-50 из 124»: сколько строк попало на текущую страницу и сколько их всего с учётом фильтров правой панели (строка поиска на счётчик не влияет). Пустой список подписан «Нет записей». Счётчик заменяет тот, что пропал вместе с типовым листанием в прошлой сборке.
### fr
- La pagination des listes de documents a reçu des boutons de saut : « ◀◀ » va à la première page, « ▶▶ » à la dernière. Les flèches page précédente et page suivante restent à leur place.
- À côté des pages s'affiche un compteur d'enregistrements — « 1-50 sur 124 » : combien de lignes figurent sur la page courante et combien il y en a au total avec les filtres du panneau de droite (la recherche rapide n'agit pas sur le compteur). Une liste vide porte la mention « Aucun enregistrement ». Ce compteur remplace celui qui avait disparu avec la pagination de la plateforme dans la version précédente.
### en
- The document list paginator now has jump buttons: "◀◀" goes to the first page, "▶▶" to the last one. The previous and next page arrows stay where they were.
- A record counter is shown next to the pages — "1-50 of 124": how many rows are on the current page and how many there are in total with the right-hand panel filters applied (the search box does not affect the counter). An empty list reads "No records". This counter replaces the one that disappeared together with the platform pagination in the previous build.
### es
- El paginador de las listas de documentos tiene ahora botones de salto: «◀◀» va a la primera página y «▶▶» a la última. Las flechas de página anterior y siguiente siguen en su sitio.
- Junto a las páginas se muestra un contador de registros: «1-50 de 124», es decir, cuántas filas hay en la página actual y cuántas en total con los filtros del panel derecho aplicados (el cuadro de búsqueda no afecta al contador). Una lista vacía aparece como «Sin registros». Este contador sustituye al que desapareció junto con la paginación de la plataforma en la compilación anterior.

## 2.0.15.62
### ru
- Из печати налоговой накладной убран лишний вариант — в меню он назывался «Товарная накладная (новая форма)», на кнопке формы «Товарная накладная (Socassif)»: это был экземпляр накладной одного клиента, а не отдельная форма. Печать накладных ведётся общими формами — «Товарная накладная» и «Товарная накладная на бланке»; сама структура накладной сохранена, лишним был только дубль в меню. Макет и код печати Socassif удалены из конфигурации.
- В списках документов убран второй, типовой набор стрелок перехода по страницам — он стоял в правом нижнем углу таблицы и дублировал наш пагинатор «‹ 1/1 ›» внизу слева. Листание страниц осталось одно, наше. Приведены к одному виду все списки документов с постраничным просмотром.
### fr
- Une variante d'impression superflue a été retirée de la facture comptable — « Facture (nouveau formulaire) » dans le menu, « Facture Socassif » sur le bouton du formulaire : il s'agissait de l'exemplaire d'un seul client, et non d'un formulaire distinct. Les factures s'impriment avec les formes communes — « Facture » et « Facture (papier à en-tête) » ; la structure de la facture est conservée, seul le doublon du menu était de trop. Le modèle et le code d'impression Socassif ont été supprimés de la configuration.
- Dans les listes de documents, le second jeu de flèches de pagination, celui de la plateforme, a été retiré : il occupait le coin inférieur droit du tableau et faisait double emploi avec notre pagination « ‹ 1/1 › » en bas à gauche. Il ne reste qu'une seule pagination, la nôtre. Toutes les listes de documents avec consultation par pages sont désormais uniformes.
### en
- A redundant print variant has been removed from the tax invoice — "Invoice (new form)" in the menu, "Socassif Invoice" on the form button: it was one customer's own copy, not a separate form. Invoices are printed with the common forms — "Invoice" and "Invoice on letterhead"; the invoice structure itself is kept, only the duplicate menu entry was redundant. The Socassif template and printing code have been removed from the configuration.
- In document lists the second, platform set of page arrows has been removed: it sat in the bottom right corner of the table and duplicated our "‹ 1/1 ›" paginator at the bottom left. Only one pagination remains, ours. All document lists with page-by-page viewing are now consistent.
### es
- Se ha quitado una variante de impresión sobrante de la factura fiscal: «Factura (formulario nuevo)» en el menú y «Factura Socassif» en el botón del formulario. Era el ejemplar de un solo cliente, no un formulario aparte. Las facturas se imprimen con las formas comunes — «Factura» y «Factura en papel con membrete»; la estructura de la factura se mantiene, solo sobraba el duplicado en el menú. La plantilla y el código de impresión Socassif se han eliminado de la configuración.
- En las listas de documentos se ha quitado el segundo juego de flechas de páginas, el de la plataforma: estaba en la esquina inferior derecha de la tabla y duplicaba nuestro paginador «‹ 1/1 ›» de abajo a la izquierda. Queda una sola paginación, la nuestra. Todas las listas de documentos con vista por páginas quedan uniformes.

## 2.0.15.61
### ru
- Фильтр «Оплата» в списке заказов клиентов больше не показывает пустой список. Позиции «Не оплачен», «Частично» и «Оплачен» не находили ни одного заказа: пока по заказу нет проведённой реализации, состояние оплаты не определялось вовсе — и значок в колонке оплаты не показывался, и фильтру было нечего искать. Теперь состояние есть у каждого заказа: оно считается по расчётам с клиентом, привязанным к этому заказу, — приходным кассовым ордерам, введённым на основании заказа, и реализациям по нему. Аванс наличными, полученный по заказу, виден как «частично» или «оплачен» ещё до отгрузки.
- Предупреждение: аванс, полученный на расчётный счёт, в это состояние пока не попадает — поступление безналичных денежных средств к заказу клиента не привязывается. Такой заказ до отгрузки показывается как неоплаченный.
- Признак просрочки в колонке оплаты больше не показывается. Раньше заказ с истёкшим сроком оплаты всегда помечался как неоплаченный, даже если клиент внёс часть суммы; теперь он показывается по факту оплаты — «частично». Отдельного значка для просрочки пока нет.
- Заказ, отгруженный и оплаченный не полностью, теперь показывается как «частично», а не как «оплачен». Раньше значок «оплачен» появлялся, как только не оставалось долга по отгруженной части, хотя остальное ещё не отгружено и не оплачено.
### fr
- Le filtre « Paiement » dans la liste des commandes clients n'affiche plus une liste vide. Les positions « Impayé », « Partiel » et « Payé » ne trouvaient aucune commande : tant qu'une commande n'a pas de vente validée, son état de paiement n'était pas déterminé du tout — l'icône de la colonne de paiement restait vide et le filtre n'avait rien à chercher. Désormais chaque commande a un état : il est calculé d'après les règlements du client rattachés à cette commande — les entrées de caisse créées sur la base de la commande et les ventes qui en découlent. Un acompte reçu en espèces sur la commande apparaît comme « partiel » ou « payé » avant même l'expédition.
- Avertissement : un acompte reçu sur le compte bancaire n'entre pas encore dans cet état — l'entrée de fonds non espèces ne se rattache pas à une commande client. Une telle commande reste affichée comme impayée jusqu'à l'expédition.
- L'indication de retard de paiement n'apparaît plus dans la colonne de paiement. Auparavant, une commande dont l'échéance était dépassée était toujours marquée comme impayée, même si le client avait versé une partie du montant ; elle est désormais affichée selon le paiement réel — « partiel ». Il n'existe pas encore d'icône distincte pour le retard.
- Une commande expédiée et payée partiellement s'affiche désormais comme « partiel » et non comme « payé ». Auparavant l'icône « payé » apparaissait dès qu'il ne restait plus de dette sur la partie expédiée, alors que le reste n'était ni expédié ni payé.
### en
- The "Payment" filter in the customer order list no longer shows an empty list. The "Unpaid", "Partial" and "Paid" positions found no orders at all: until an order has a posted sale, its payment state was not determined at all — the payment column icon stayed empty and the filter had nothing to match. Every order now has a state: it is calculated from the customer settlements linked to that order — cash receipts entered on the basis of the order and the sales made from it. A cash advance received against the order shows as "partial" or "paid" even before shipment.
- Warning: an advance received to the bank account does not yet count towards this state — a non-cash funds receipt cannot be linked to a customer order. Such an order is shown as unpaid until shipment.
- The overdue indication is no longer shown in the payment column. Previously an order past its due date was always marked unpaid, even when the customer had paid part of the amount; it now reflects the actual payment — "partial". There is no separate icon for overdue yet.
- An order that is shipped and paid only in part is now shown as "partial" rather than "paid". Previously the "paid" icon appeared as soon as no debt remained on the shipped part, while the rest was neither shipped nor paid.
### es
- El filtro «Pago» en la lista de pedidos de clientes ya no muestra una lista vacía. Las posiciones «No pagado», «Parcial» y «Pagado» no encontraban ningún pedido: mientras un pedido no tiene una venta contabilizada, su estado de pago no se determinaba en absoluto: el icono de la columna de pago quedaba vacío y el filtro no tenía nada que buscar. Ahora cada pedido tiene estado: se calcula por las liquidaciones con el cliente vinculadas a ese pedido, es decir, los recibos de caja creados sobre la base del pedido y las ventas derivadas de él. Un anticipo recibido en efectivo por el pedido se ve como «parcial» o «pagado» incluso antes de la expedición.
- Advertencia: un anticipo recibido en la cuenta bancaria todavía no entra en este estado, porque la entrada de fondos no en efectivo no se vincula a un pedido de cliente. Ese pedido se muestra como no pagado hasta la expedición.
- La indicación de vencimiento ya no se muestra en la columna de pago. Antes, un pedido con el plazo vencido se marcaba siempre como no pagado, aunque el cliente hubiera abonado una parte del importe; ahora se muestra según el pago real: «parcial». Todavía no hay un icono propio para el vencimiento.
- Un pedido expedido y pagado solo en parte se muestra ahora como «parcial» y no como «pagado». Antes el icono «pagado» aparecía en cuanto no quedaba deuda por la parte expedida, aunque el resto no estuviera ni expedido ni pagado.

## 2.0.15.60
### ru
- Французские сообщения программы снова видны. Тексты, где в кавычках стоял апостроф — а во французском он почти в каждой фразе, — были записаны так, что платформа французский вариант не распознавала и показывала русский или английский. Исправлено 374 таких текста: сообщения об оборудовании и кассах, длительные операции, групповое изменение реквизитов, регистрация изменений для обмена.
- Подписи, заведённые не на всех языках, доведены до четырёх: 670 заголовков, синонимов, подсказок и списков выбора в формах, метаданных и печатных формах. Раньше на французском, английском или испанском на их месте показывался русский текст или служебное имя реквизита.
- Испанское «от» в дате документа означало «до»: в 55 местах — формы документов, договоров и регистров — стоял предлог «a» вместо «de».
- В корректировке долга, в описании обработки регистрации изменений и в счётчике зарегистрированных объектов сообщения были только на русском — переведены.
- Подпись «Наценка, %» в заказе покупателя и реализации была записана так, что платформа читала только русский вариант — теперь работают все четыре языка.
### fr
- Les messages français du programme sont de nouveau visibles. Les textes contenant une apostrophe entre guillemets — et le français en contient presque partout — étaient écrits de telle sorte que la plateforme ne reconnaissait pas la version française et affichait le russe ou l'anglais. 374 textes corrigés : messages liés aux équipements et aux caisses, opérations longues, modification groupée des attributs, enregistrement des modifications pour l'échange.
- Les libellés qui n'existaient pas dans toutes les langues sont complétés dans les quatre : 670 titres, synonymes, info-bulles et listes de choix dans les formulaires, les métadonnées et les états imprimés. Auparavant, en français, en anglais ou en espagnol, le texte russe ou le nom technique de l'attribut s'affichait à leur place.
- L'espagnol « от » dans la date du document signifiait « jusqu'à » : à 55 endroits — formulaires de documents, de contrats et de registres — la préposition « a » figurait au lieu de « de ».
- Dans la correction de dette, dans la description du traitement d'enregistrement des modifications et dans le compteur d'objets enregistrés, les messages n'existaient qu'en russe : ils sont traduits.
- Le libellé « Majoration, % » dans la commande client et la vente était écrit de telle sorte que la plateforme ne lisait que la version russe : les quatre langues fonctionnent désormais.
### en
- French program messages are visible again. Texts with an apostrophe inside quotes — and French has one in almost every phrase — were written so that the platform did not recognize the French variant and showed Russian or English instead. 374 such texts fixed: equipment and POS messages, long operations, bulk attribute change, change registration for data exchange.
- Captions that existed in only some languages are now complete in all four: 670 titles, synonyms, tooltips and choice lists across forms, metadata and printed forms. Previously the French, English or Spanish interface showed Russian text or the technical attribute name in their place.
- The Spanish word for "dated" in a document date meant "until": in 55 places — document, contract and register forms — the preposition "a" was used instead of "de".
- In debt adjustment, in the change registration data processor description and in the registered objects counter, messages existed in Russian only and are now translated.
- The "Markup, %" caption in the customer order and the sale was written so that the platform read only the Russian variant; all four languages now work.
### es
- Los mensajes en francés del programa vuelven a verse. Los textos con un apóstrofo entre comillas — y el francés lo lleva en casi cada frase — estaban escritos de modo que la plataforma no reconocía la versión francesa y mostraba el ruso o el inglés. Se han corregido 374 textos: mensajes de equipos y cajas, operaciones largas, modificación grupal de atributos, registro de cambios para el intercambio.
- Los rótulos que no existían en todos los idiomas se han completado en los cuatro: 670 títulos, sinónimos, ayudas emergentes y listas de elección en formularios, metadatos y formularios impresos. Antes, en francés, inglés o español aparecía en su lugar el texto ruso o el nombre técnico del atributo.
- La preposición española en la fecha del documento significaba «hasta»: en 55 lugares — formularios de documentos, contratos y registros — figuraba «a» en vez de «de».
- En la corrección de deuda, en la descripción del procesamiento de registro de cambios y en el contador de objetos registrados los mensajes solo existían en ruso; ya están traducidos.
- El rótulo «Margen, %» en el pedido de cliente y en la venta estaba escrito de modo que la plataforma solo leía la versión rusa; ahora funcionan los cuatro idiomas.

## 2.0.15.59
### ru
- Подписи на нерусских языках: в испанском интерфейсе колонка и поле «Номер» подписывались словом «Habitación» — по-испански это «комната». Исправлено на «Número» в справочниках договоров, серий номенклатуры и документов физлиц, в списках реализаций и налоговых накладных мобильного клиента, в личном кабинете партнёра, в обработке «Клиент-банк», в печатной форме платёжной ведомости на аванс, в счёте SOCASSIF и в кассовой книге.
- Заголовки, которые были заведены только по-русски и потому в остальных интерфейсах показывались по-русски или именем реквизита, переведены на все четыре языка: «Путь базы» в шаблоне конфигурации, «от» и «Период» в установке плановых показателей, флажок ограничений миграции данных в настройках регистрации изменений, колонка загрузки в загрузке банков, номер заказа в личном кабинете партнёра.
### fr
- Libellés dans les langues autres que le russe : dans l'interface espagnole, la colonne et le champ « Numéro » portaient le mot « Habitación », qui signifie « chambre » en espagnol. Corrigé en « Número » dans les contrats, les séries d'articles et les pièces d'identité, dans les listes des ventes et des factures fiscales du client mobile, dans l'espace partenaire, dans le traitement « Client-banque », dans l'état imprimé du bordereau de paie sur acompte, dans la facture SOCASSIF et dans le livre de caisse.
- Les libellés saisis uniquement en russe, qui s'affichaient donc en russe ou sous le nom de l'attribut dans les autres interfaces, sont traduits dans les quatre langues : « Chemin de la base » dans le modèle de configuration, « de » et « Période » dans la saisie des objectifs, la case des restrictions de migration des données dans les réglages d'enregistrement des modifications, la colonne de chargement dans l'import des banques, le numéro de commande dans l'espace partenaire.
### en
- Captions in languages other than Russian: in the Spanish interface the "Number" column and field were captioned "Habitación", which is Spanish for "room". Corrected to "Número" in counterparty contracts, item series and personal documents, in the sales and tax invoice lists of the mobile client, in the partner portal, in the "Client-bank" data processor, in the printed advance payroll sheet, in the SOCASSIF invoice and in the cash book.
- Captions entered in Russian only, and therefore shown in Russian or as an attribute name in the other interfaces, are now translated into all four languages: "Database path" in the configuration template, "from" and "Period" in planned target entry, the data migration restrictions checkbox in change registration settings, the load column in bank import, the order number in the partner portal.
### es
- Rótulos en idiomas distintos del ruso: en la interfaz española la columna y el campo «Número» aparecían con la palabra «Habitación». Corregido a «Número» en los contratos con contrapartes, las series de artículos y los documentos de personas físicas, en las listas de ventas y facturas fiscales del cliente móvil, en el portal del socio, en el procesamiento «Cliente-banco», en la nómina impresa de anticipo, en la factura SOCASSIF y en el libro de caja.
- Los rótulos escritos solo en ruso, que por ello se mostraban en ruso o con el nombre del atributo en las demás interfaces, están traducidos a los cuatro idiomas: «Ruta de la base» en la plantilla de configuración, «a» y «Período» en el registro de objetivos, la casilla de restricciones de migración de datos en los ajustes de registro de cambios, la columna de carga en la importación de bancos, el número de pedido en el portal del socio.

## 2.0.15.58
### ru
- Расчёты с контрагентом переезжают на налоговую накладную. Раньше долг по отгрузке оставался висеть в обычных взаиморасчётах, а налоговая накладная заводила тот же долг во втором, налоговом контуре — одни и те же деньги считались дважды, и отчёты по двум контурам не сходились. Теперь при проведении налоговой накладной долг отгрузки и её оплаты сторнируются, а накладная принимает их на себя: сальдо контрагента не меняется, а расшифровка долга идёт по накладной. То же самое сделано по закупке — для налоговой накладной покупки и поступлений. Контроль кредита, запрет отгрузок, дашборд и отчёты по долгам продолжают видеть долг, ставший долгом по накладной.
- Вторую налоговую накладную по уже покрытой отгрузке провести нельзя: программа сообщит, какой накладной отгрузка уже закрыта. Запрет распространяется и на копию накладной. Без него повторная накладная сторнировала бы оплаты второй раз и раздваивала долг.
- Сертификат на оплату и возврат от покупателя, введённые после налоговой накладной, теперь попадают на саму накладную, а не на закрытую отгрузку — долг контрагента считается верно.
### fr
- Les règlements avec le tiers sont transférés sur la facture fiscale. Auparavant, la dette du bon de livraison restait dans les règlements ordinaires tandis que la facture fiscale créait la même dette dans le circuit fiscal : le même argent était compté deux fois et les deux circuits ne concordaient pas. Désormais, à la validation de la facture fiscale, la dette du bon de livraison et ses règlements sont extournés et la facture les reprend à son compte : le solde du tiers ne change pas et le détail de la dette suit la facture. Il en va de même à l'achat, pour la facture fiscale d'achat et les réceptions. Le contrôle du crédit, le blocage des expéditions, le tableau de bord et les états de dettes voient toujours cette dette, devenue dette de la facture.
- Une seconde facture fiscale sur un bon de livraison déjà couvert ne peut plus être validée : le programme indique par quelle facture il est déjà couvert. L'interdiction s'applique aussi à la copie d'une facture. Sans elle, la seconde facture extournerait les règlements une deuxième fois et dédoublerait la dette.
- Le certificat de paiement et le retour client saisis après la facture fiscale s'imputent désormais sur la facture elle-même et non sur le bon de livraison soldé : la dette du tiers est correcte.
### en
- Settlements with the counterparty move onto the tax invoice. Previously the delivery note's debt stayed in ordinary settlements while the tax invoice created the same debt in the tax circuit — the same money was counted twice and the two circuits did not agree. Now, when a tax invoice is posted, the delivery note's debt and its payments are reversed and the invoice takes them over: the counterparty balance is unchanged and the debt breakdown follows the invoice. The same has been done on the purchase side, for the purchase tax invoice and receipts. Credit control, the shipment ban, the dashboard and the debt reports still see that debt, now held by the invoice.
- A second tax invoice for a delivery note that is already covered can no longer be posted: the program reports which invoice already covers it. The ban also applies to a copy of an invoice. Without it, the second invoice would reverse the payments a second time and double the debt.
- A payment certificate and a customer return entered after the tax invoice now land on the invoice itself rather than on the settled delivery note, so the counterparty debt is correct.
### es
- Las liquidaciones con la contraparte se trasladan a la factura fiscal. Antes la deuda del albarán seguía en las liquidaciones ordinarias mientras la factura fiscal creaba la misma deuda en el circuito fiscal: el mismo dinero se contaba dos veces y los dos circuitos no cuadraban. Ahora, al contabilizar la factura fiscal, la deuda del albarán y sus pagos se extornan y la factura los asume: el saldo de la contraparte no cambia y el desglose de la deuda sigue a la factura. Lo mismo se ha hecho en la compra, para la factura fiscal de compra y las recepciones. El control de crédito, el bloqueo de envíos, el panel y los informes de deuda siguen viendo esa deuda, ahora de la factura.
- Ya no se puede contabilizar una segunda factura fiscal sobre un albarán ya cubierto: el programa indica qué factura lo cubre. La prohibición también alcanza a la copia de una factura. Sin ella, la segunda factura extornaría los pagos por segunda vez y duplicaría la deuda.
- El certificado de pago y la devolución del cliente registrados después de la factura fiscal se imputan ahora a la propia factura y no al albarán saldado, de modo que la deuda de la contraparte es correcta.

## 2.0.15.57
### ru
- В рабочем месте кассира появилось избранное. Кнопка «Избранное» рядом с «Добавить» открывает окно с плитками избранных товаров: на плитке название и цена, клик добавляет товар в чек, повторный клик увеличивает количество. Товар кладётся в избранное и убирается из него правой кнопкой мыши — по строке чека или по самой плитке, отдельных кнопок на экране это не занимает. Избранное своё у каждого кассира. Строка заголовка внутри формы кассира убрана — место отдано рабочей области, название рабочего места видно в закладке.
### fr
- Les favoris arrivent dans le poste de caisse. Le bouton « Favoris », à côté de « Ajouter », ouvre une fenêtre de tuiles : chaque tuile porte le nom et le prix, un clic ajoute l’article au ticket, un second clic augmente la quantité. On ajoute et on retire un article des favoris par un clic droit — sur la ligne du ticket ou sur la tuile — sans occuper l’écran avec des boutons supplémentaires. Chaque caissier a ses propres favoris. La ligne de titre à l’intérieur du formulaire de caisse a été supprimée : la place revient à la zone de travail, le nom du poste reste visible dans l’onglet.
### en
- Favourites have arrived in the cashier workplace. The "Favourites" button next to "Add" opens a window of tiles: each tile shows the name and the price, a click adds the product to the receipt, a second click increases the quantity. A product is added to and removed from favourites with a right click — on the receipt line or on the tile itself — without taking up screen space with extra buttons. Each cashier has their own favourites. The title line inside the cashier form has been removed: the space goes to the working area, and the workplace name stays visible in the tab.
### es
- Los favoritos llegan al puesto de caja. El botón «Favoritos», junto a «Agregar», abre una ventana de mosaicos: cada mosaico muestra el nombre y el precio, un clic agrega el artículo al ticket y un segundo clic aumenta la cantidad. El artículo se agrega y se quita de favoritos con el botón derecho del ratón — en la línea del ticket o en el propio mosaico — sin ocupar la pantalla con botones adicionales. Cada cajero tiene sus propios favoritos. Se ha quitado la línea de título dentro del formulario de caja: el espacio pasa al área de trabajo y el nombre del puesto sigue visible en la pestaña.

## 2.0.15.56
### ru
- В табличных частях документов «Поступление товаров и услуг», «Реализация товаров и услуг», «Налоговая накладная» и «Налоговая накладная (покупка)» и в обработке «Продажи в розницу» колонка «Всего» во французском интерфейсе называется «Montant TTC» — сумма с НДС. Раньше она была подписана «Seulement» («только»), что к сумме отношения не имеет. В испанском интерфейсе та же колонка называется «Total» вместо дословного «Por todo».
### fr
- Dans les parties tabulaires des documents « Réception de biens et services », « Vente de biens et services », « Facture fiscale » et « Facture fiscale (achat) » ainsi que dans le traitement « Ventes en détail », la colonne « Всего » s'intitule désormais « Montant TTC » en français. Elle portait le libellé « Seulement », qui n'a aucun rapport avec un montant. En espagnol, la même colonne s'appelle « Total » au lieu du littéral « Por todo ».
### en
- In the tabular sections of the "Goods and services receipt", "Goods and services sale", "Tax invoice" and "Tax invoice (purchase)" documents and in the "Retail sales" data processor, the "Total" column is now labelled "Montant TTC" in the French interface. It used to read "Seulement" ("only"), which has nothing to do with an amount. In Spanish the same column is now "Total" instead of the literal "Por todo".
### es
- En las partes tabulares de los documentos «Recepción de bienes y servicios», «Venta de bienes y servicios», «Factura fiscal» y «Factura fiscal (compra)» y en el procesamiento «Ventas al por menor», la columna «Total» se llama ahora «Montant TTC» en la interfaz francesa. Antes ponía «Seulement» («solamente»), que nada tiene que ver con un importe. En español esa misma columna se llama «Total» en lugar del literal «Por todo».

## 2.0.15.55
### ru
- Из отчёта «Ведомость по продажам» убран логотип чужой компании: в шапке отчёта печаталась картинка, оставшаяся от базы, из которой переносился отчёт. Теперь отчёт начинается сразу с заголовка и таблицы.
### fr
- Le logo d'une autre société a été retiré de l'état « État des ventes » : l'en-tête affichait une image héritée de la base dont l'état avait été repris. L'état commence désormais directement par son titre et son tableau.
### en
- The foreign company logo has been removed from the "Sales status" report: its header printed an image inherited from the database the report was taken from. The report now starts straight with its title and table.
### es
- Se ha quitado el logotipo de otra empresa del informe «Estado de ventas»: en el encabezado se imprimía una imagen heredada de la base de la que se trasladó el informe. El informe empieza ahora directamente por su título y su tabla.

## 2.0.15.54
### ru
- Реквизит «Артикул» во французском интерфейсе называется «Référence» — у номенклатуры, у номенклатуры контрагентов и в заявке на поиск товара. Раньше он был подписан «Article» — тем же словом, что и сама номенклатура в табличных частях и регистрах, и колонки путались. Русское, английское и испанское названия не изменились.
- На форме номенклатуры поле артикула больше не подписано «ID»: оно берёт название реквизита и называется так же, как в списках и подборах.
### fr
- L'attribut « Article » (référence) s'appelle désormais « Référence » dans l'interface française — pour les articles, les articles des partenaires et la demande de recherche de produit. Il portait le même nom que l'article lui-même dans les parties tabulaires et les registres, ce qui prêtait à confusion. Les libellés russe, anglais et espagnol sont inchangés.
- Sur la fiche article, le champ de la référence n'est plus intitulé « ID » : il reprend le libellé de l'attribut et porte le même nom que dans les listes et les sélections.
### en
- The "Article" (item reference) attribute is now labelled "Référence" in the French interface — for items, partner items and the product search request. It used to read "Article", the same word as the item itself in document tables and registers, which made the columns confusing. The Russian, English and Spanish labels are unchanged.
- On the item form the reference field is no longer labelled "ID": it takes the attribute's own name and matches the lists and pick forms.
### es
- El atributo «Articulo» (referencia) ahora se llama «Référence» en la interfaz francesa — en artículos, artículos de los socios y la solicitud de búsqueda de producto. Antes se mostraba como «Article», la misma palabra que el propio artículo en las partes tabulares y los registros, lo que confundía las columnas. Las etiquetas en ruso, inglés y español no cambian.
- En el formulario del artículo el campo de la referencia ya no se titula «ID»: toma el nombre del atributo y coincide con las listas y las selecciones.

## 2.0.15.53
### ru
- Пробная смена шрифта интерфейса на Arial. На macOS русские заголовки колонок выводились с разъехавшимися буквами, тогда как латиница и цифры печатались нормально. Если заголовки стали ровными — шрифт остаётся; если что-то поехало в размерах, правка откатывается.
### fr
- Changement d'essai de la police de l'interface pour Arial. Sur macOS, les en-têtes de colonnes en cyrillique s'affichaient avec des lettres espacées, alors que les caractères latins et les chiffres étaient normaux. Si les en-têtes sont redevenus réguliers, la police reste ; si les tailles ont bougé, la modification sera annulée.
### en
- Trial switch of the interface font to Arial. On macOS, Cyrillic column headers were drawn with letters spaced apart, while Latin text and digits looked normal. If the headers are even now, the font stays; if sizes shifted, the change will be rolled back.
### es
- Cambio de prueba de la fuente de la interfaz a Arial. En macOS, los encabezados de columna en cirílico se mostraban con las letras separadas, mientras que el texto latino y los números salían normales. Si los encabezados se ven parejos, la fuente se queda; si los tamaños se desplazaron, el cambio se revertirá.

## 2.0.15.52
### ru
- В табличных частях документов снова видна единица измерения. Колонка «Единица» была пустой во всех документах — поступлениях, реализациях, заказах, перемещениях, — хотя значение в строке стояло: его стирало оформление колонки. Теперь единица показывается; если упаковки не используются, в колонке стоит базовая единица номенклатуры.
- В выпуске продукции надпись «Создан автоматически при проведении документа» переехала из шапки формы вниз закладки «Основное» и больше не висит над всеми закладками.
### fr
- L'unité de mesure est de nouveau visible dans les parties tabulaires des documents. La colonne « Unité » restait vide dans tous les documents — achats, ventes, commandes, transferts — alors que la valeur était bien saisie : elle était effacée par la mise en forme de la colonne. L'unité s'affiche désormais ; si les emballages ne sont pas utilisés, la colonne montre l'unité de base de l'article.
- Dans la production, la mention « Créée automatiquement lors de la validation du document » passe de l'en-tête du formulaire au bas de l'onglet « Principal » et ne surplombe plus tous les onglets.
### en
- The unit of measure is visible again in document tables. The "Unit" column was empty in every document — purchases, sales, orders, transfers — although the value was there: the column's conditional appearance erased it. The unit is now shown; when packaging is not used, the column shows the item's base unit.
- In production output, the "Created automatically when document was posted" notice moved from the form header to the bottom of the "Main" tab and no longer hangs above every tab.
### es
- La unidad de medida vuelve a verse en las partes tabulares de los documentos. La columna «Unidad» quedaba vacía en todos los documentos —compras, ventas, pedidos, traslados— aunque el valor estaba en la línea: lo borraba el formato condicional de la columna. Ahora la unidad se muestra; si no se usan embalajes, la columna muestra la unidad base del artículo.
- En la producción, el aviso «Creada automáticamente al contabilizar el documento» pasa del encabezado del formulario al final de la pestaña «Principal» y ya no queda por encima de todas las pestañas.

## 2.0.15.51
### ru
- Круговые диаграммы дашбордов снова показывают доли. «Остатки по товарным группам», «Выручка по сотрудникам» и «Активные заказы по статусам» закрашивались одним цветом на весь круг, и все три дашборда выглядели одинаково.
- Значки на дашбордах заменены текстом и цветом: раньше вместо них на части систем выводились пустые квадратики. Просроченные отгрузки теперь выделяются красным, а шкала процента рисуется теми же кружками, что индикатор выполнения заказа.
- Шрифт интерфейса больше не требует Calibri. На компьютерах без него — а это все macOS и Linux — платформа подставляла замену, и буквы получались разреженными. Теперь берётся стандартный шрифт системы; размер текста не изменился.
### fr
- Les diagrammes circulaires des tableaux de bord affichent de nouveau les parts. « Stock par groupe d'articles », « CA par employé » et « Commandes actives par statut » étaient remplis d'une seule couleur sur tout le cercle, et les trois tableaux de bord se ressemblaient.
- Les pictogrammes des tableaux de bord sont remplacés par du texte et de la couleur : sur certains systèmes, ils s'affichaient en carrés vides. Les expéditions en retard sont désormais en rouge et la barre de pourcentage utilise les mêmes cercles que l'indicateur d'avancement de la commande.
- La police de l'interface n'exige plus Calibri. Sur les postes qui ne l'ont pas — tous les macOS et Linux — la plateforme lui substituait une autre police, aux lettres espacées. La police standard du système est désormais utilisée ; la taille du texte est inchangée.
### en
- Dashboard pie charts show shares again. "Stock by item group", "Revenue by employee" and "Active orders by status" were filled with a single color over the whole circle, and all three dashboards looked alike.
- Dashboard pictograms are replaced by text and color: on some systems they were drawn as empty boxes. Overdue shipments are now shown in red, and the percentage bar uses the same circles as the order progress indicator.
- The interface font no longer requires Calibri. On machines without it — every macOS and Linux — the platform substituted another font and letters came out spaced apart. The system's standard font is used now; the text size is unchanged.
### es
- Los gráficos circulares de los paneles vuelven a mostrar las proporciones. «Existencias por grupo de artículos», «Ingresos por empleado» y «Pedidos activos por estado» se rellenaban de un solo color en todo el círculo, y los tres paneles se veían iguales.
- Los pictogramas de los paneles se sustituyen por texto y color: en algunos sistemas se dibujaban como cuadros vacíos. Los envíos atrasados se muestran ahora en rojo y la barra de porcentaje usa los mismos círculos que el indicador de avance del pedido.
- La fuente de la interfaz ya no exige Calibri. En equipos que no la tienen —todos los macOS y Linux— la plataforma la sustituía por otra y las letras salían espaciadas. Ahora se usa la fuente estándar del sistema; el tamaño del texto no cambia.

## 2.0.15.50
### ru
- Кнопка «Подбор товара» в заказе на производство теперь предлагает только готовую продукцию и полуфабрикаты, списком без групп — как и выбор в колонке «Номенклатура». В заказе на продажу подбор остался прежним, по всей номенклатуре.
- Акт приёмки из переработки печатает строку «В том числе услуги переработчика» с суммой и НДС: услуги входят в себестоимость принятой продукции, поэтому они показаны как часть итога, а не добавляются к нему.
- Мелкие правки: в печати запроса котировок номер документа не ищется — его там и не должно быть (запрос адресован поставщику); в подборе номенклатуры разрядность поля количества читается один раз, а не при каждом вводе; в операции валютные суммы проводки приводятся по типу регистра, а не по более широкому литералу.
- Обновление добавит индекс по дате создания номенклатуры: на большой базе первый запуск после обновления займёт на несколько минут дольше.
### fr
- Le bouton « Sélection des articles » de la commande de production ne propose désormais que les produits finis et les produits semi-finis, en liste sans groupes — comme le choix dans la colonne « Nomenclature ». Dans une commande de vente, la sélection reste inchangée, sur toute la nomenclature.
- Le bon de réception de sous-traitance imprime la ligne « Dont services du sous-traitant » avec le montant et la TVA : ces services entrent dans le coût des produits reçus, ils sont donc montrés comme une part du total et non ajoutés à celui-ci.
- Petites corrections : l'impression de la demande de prix ne cherche plus le numéro du document — il n'y a pas lieu d'y figurer (la demande s'adresse au fournisseur) ; dans la sélection des articles, la précision du champ de quantité est lue une seule fois et non à chaque saisie ; dans l'opération, les montants en devise des écritures sont ramenés au type du registre et non à un littéral plus large.
- La mise à jour ajoutera un index sur la date de création de la nomenclature : sur une grande base, le premier lancement après la mise à jour prendra quelques minutes de plus.
### en
- The "Product picking" button in a production order now offers only finished and semi-finished products, as a flat list without groups — like the choice in the "Item" column. In a sales order, picking stays as before, over all items.
- The subcontracting acceptance act prints the line "Including processor services" with the amount and VAT: these services are part of the cost of the received products, so they are shown as a share of the total rather than added to it.
- Small fixes: the quotation request printout no longer looks for the document number — it does not belong there (the request is addressed to the supplier); in item picking the quantity field precision is read once instead of on every entry; in the operation document the currency amounts of the entries are coerced to the register type rather than to a wider literal.
- The update will add an index on the item creation date: on a large database the first start after the update takes a few minutes longer.
### es
- El botón «Selección de artículos» en el pedido para producción ahora ofrece solo productos terminados y semielaborados, como lista sin grupos, igual que la selección en la columna «Nomenclatura». En el pedido de venta la selección sigue igual, sobre toda la nomenclatura.
- El acta de recepción de subcontratación imprime la línea «Incluidos los servicios del procesador» con el importe y el IVA: esos servicios entran en el coste de los productos recibidos, por eso se muestran como parte del total y no se suman a él.
- Correcciones menores: la impresión de la solicitud de cotización ya no busca el número del documento — no corresponde que esté (la solicitud se dirige al proveedor); en la selección de artículos la precisión del campo de cantidad se lee una sola vez y no en cada entrada; en la operación los importes en divisa de los asientos se ajustan al tipo del registro y no a un literal más amplio.
- La actualización añadirá un índice por la fecha de creación de la nomenclatura: en una base grande el primer arranque tras la actualización tardará unos minutos más.

## 2.0.15.49
### ru
- Подбор номенклатуры в рабочем месте производства и в заказе на производство теперь предлагает только подходящие позиции. В колонке «Продукция» рабочего места и в товарах заказа на производство — готовая продукция и полуфабрикаты. В колонке «Материал» закупок и переработки рабочего места и в материалах заказа — сырьё, полуфабрикаты и товары. Услуги и комплекты в эти колонки не предлагаются.
- Кнопка выбора в колонке продукции открывает короткий список: 10 последних созданных позиций готовой продукции и полуфабрикатов с датой создания, а под ними — «Выбрать из справочника…». Справочник открывается списком без групп и только с продукцией и полуфабрикатами; ввод наименования текстом тоже находит только их.
- Кнопка выбора в колонке материала на закладках «Заказы поставщику», «Поступления» и «Переработка» начинается с материалов текущего заказа: рядом с каждым видно, сколько его не хватает, сколько осталось принять или сколько нужно передать переработчику. Выбор подставляет материал вместе с характеристикой, а количество, поставщика и строку заказа поставщику — как при вводе руками. Материал вне заказа выбирают пунктом «Выбрать из справочника…» (сырьё, полуфабрикаты, товары) или «Выбрать из всей номенклатуры…». Ввод материала текстом не ограничен.
- Если нужной продукции нет в списке, проверьте тип номенклатуры в её карточке: продукция должна иметь тип «Продукция» или «Полуфабрикат». Позицию другого типа в колонку продукции выбрать нельзя. Уже введённые строки заказов не меняются.
- У заказа с видом операции «Продажа» выбор товаров остался прежним, без отбора по типу.
- Форма выбора номенклатуры с отбором по типу теперь открывается списком без групп: все подходящие позиции видны сразу. Это касается и документов, где отбор по типу был и раньше, — выпуска продукции, поступлений, реализаций, перемещений и других. Без отбора по типу справочник открывается по группам, как прежде.
### fr
- La sélection des articles dans le poste de production et dans la commande de production ne propose désormais que les articles adaptés. Dans la colonne « Produit » du poste et dans les articles de la commande de production : produits finis et produits semi-finis. Dans la colonne « Matière » des achats et de la sous-traitance du poste et dans les matières de la commande : matières premières, produits semi-finis et marchandises. Les services et les kits ne sont proposés dans aucune de ces colonnes.
- Le bouton de choix de la colonne produit ouvre une courte liste : les 10 derniers produits finis et semi-finis créés, avec leur date de création, puis « Choisir dans le référentiel… ». Le référentiel s'ouvre en liste sans groupes, avec seulement les produits finis et semi-finis ; la saisie du nom au clavier ne trouve qu'eux aussi.
- Le bouton de choix de la colonne matière des onglets « Commandes fournisseur », « Réceptions » et « Sous-traitance » commence par les matières de la commande en cours : à côté de chacune on voit ce qui manque, ce qui reste à recevoir ou ce qu'il faut transférer au sous-traitant. Le choix reprend la matière avec sa caractéristique, puis la quantité, le fournisseur et la ligne de commande fournisseur comme en saisie manuelle. Une matière hors commande se choisit par « Choisir dans le référentiel… » (matières premières, semi-finis, marchandises) ou « Choisir dans toute la nomenclature… ». La saisie de la matière au clavier n'est pas limitée.
- Si le produit voulu n'est pas dans la liste, vérifiez le type de nomenclature dans sa fiche : un produit doit avoir le type « Produit fini » ou « Produit semi-fini ». Un article d'un autre type ne peut pas être choisi dans la colonne produit. Les lignes de commandes déjà saisies ne changent pas.
- Pour une commande de type « Vente », le choix des articles reste le même, sans filtre par type.
- Le formulaire de choix des articles avec un filtre par type s'ouvre désormais en liste sans groupes : tous les articles adaptés sont visibles d'emblée. Cela vaut aussi pour les documents qui avaient déjà un filtre par type : production, réceptions, ventes, transferts et autres. Sans filtre par type, le référentiel s'ouvre par groupes, comme avant.
### en
- Item selection in the production workplace and in the production order now offers only suitable items. In the workplace "Product" column and in the production order goods: finished products and semi-finished products. In the workplace "Material" column of purchasing and subcontracting and in the order materials: raw materials, semi-finished products and goods. Services and kits are not offered in these columns.
- The choice button of the product column opens a short list: the 10 most recently created finished and semi-finished products with their creation date, followed by "Choose from the catalog…". The catalog opens as a flat list without groups, showing only finished and semi-finished products; typing a name also finds only them.
- The choice button of the material column on the "Purchase orders", "Receipts" and "Subcontracting" tabs starts with the materials of the current order: next to each one you see the shortage, what is left to receive or what must be sent to the subcontractor. The choice fills in the material with its characteristic, then the quantity, supplier and purchase order line as with manual entry. A material outside the order is chosen with "Choose from the catalog…" (raw materials, semi-finished products, goods) or "Choose from all items…". Typing a material is not restricted.
- If the product you need is not in the list, check the item type in its card: a product must have the type "Finished product" or "Semi-finished product". An item of another type cannot be chosen in the product column. Order lines already entered do not change.
- For an order with the "Sale" operation type, choosing goods stays as before, without a type filter.
- The item choice form with a type filter now opens as a list without groups: all suitable items are visible at once. This also applies to documents that already had a type filter: production output, receipts, sales, transfers and others. Without a type filter, the catalog opens by groups as before.
### es
- La selección de artículos en el puesto de producción y en el pedido de producción ahora ofrece solo los artículos adecuados. En la columna «Producto» del puesto y en los artículos del pedido de producción: productos terminados y semielaborados. En la columna «Material» de compras y subcontratación del puesto y en los materiales del pedido: materias primas, semielaborados y mercancías. Los servicios y los kits no se ofrecen en ninguna de estas columnas.
- El botón de selección de la columna de producto abre una lista corta: los 10 últimos productos terminados y semielaborados creados, con su fecha de creación, y debajo «Elegir del catálogo…». El catálogo se abre como lista sin grupos y solo con productos terminados y semielaborados; al escribir el nombre también se encuentran solo ellos.
- El botón de selección de la columna de material en las pestañas «Pedidos a proveedor», «Recepciones» y «Subcontratación» empieza por los materiales del pedido actual: junto a cada uno se ve cuánto falta, cuánto queda por recibir o cuánto hay que enviar al subcontratista. La selección rellena el material con su característica y después la cantidad, el proveedor y la línea del pedido a proveedor como en la entrada manual. Un material fuera del pedido se elige con «Elegir del catálogo…» (materias primas, semielaborados, mercancías) o «Elegir de toda la nomenclatura…». La entrada del material por teclado no está limitada.
- Si el producto que necesita no está en la lista, revise el tipo de nomenclatura en su ficha: un producto debe tener el tipo «Producto terminado» o «Producto semiterminado». Un artículo de otro tipo no se puede elegir en la columna de producto. Las líneas de pedidos ya introducidas no cambian.
- En un pedido con el tipo de operación «Venta», la selección de artículos sigue igual, sin filtro por tipo.
- El formulario de selección de artículos con filtro por tipo ahora se abre como lista sin grupos: todos los artículos adecuados se ven de inmediato. Esto también vale para los documentos que ya tenían filtro por tipo: producción, recepciones, ventas, traslados y otros. Sin filtro por tipo, el catálogo se abre por grupos como antes.

## 2.0.15.48
### ru
- В рабочем месте производства новая нижняя закладка «Поступления из переработки»: продукцию от переработчика теперь вводят строкой, не открывая документ. Строка сразу создаёт и проводит поступление или добавляется в сегодняшнее поступление той же передачи. Прежняя кнопка «Поступление из переработки» на закладке «Переработка» осталась и открывает документ; рядом появилась кнопка «Поступление строкой» — она переводит на новую закладку с новой строкой по отмеченной передаче.
- В строке указывают передачу в переработку, продукцию, количество и при необходимости процент потерь. Переработчик и склад берутся из передачи. Сырьё не вводится: программа сама считает его по технологической карте с процентом потерь и пересчитывает при каждой правке строки.
- Поступление вводится только по проведённой передаче своего заказа и не больше ожидаемой продукции: сколько осталось принять, видно в списке выбора продукции. Строку раннего поступления нельзя править, если после него по передачам заказа уже принималась продукция: правьте последнее поступление или откройте документ.
- Стоимость услуг переработчика теперь хранится по строкам продукции, в шапке документа — их сумма. Если изменить сумму в шапке, она распределяется по строкам по весу технологической карты (количество, нормы карты и процент потерь). Каждая строка получает в себестоимость свои услуги. В рабочем месте услуги видны колонкой «Услуги», если вам показываются суммы. Кнопка «+ услуга переработки» задаёт сумму услуг на весь документ выделенной строки и распределяет её так же, как правка шапки. Если удалить строку, её услуги переходят на оставшиеся строки: сумма счёта переработчика не уменьшается.
- Если сырьё поступления правили вручную в форме документа, документ это теперь помнит (флажок «Сырьё изменено вручную» в шапке). Строки такого документа в рабочем месте только для просмотра — правьте их в документе. Команда «Рассчитать сырьё» в документе снимает флажок.
- Старые поступления из переработки при обновлении получили услуги по строкам, а флажок ручного сырья — те, у которых сырьё не совпадает с расчётом по технологической карте. Документы не перепроводились, их движения и суммы в шапке не менялись. Если перепровести старое поступление вручную, себестоимость строк может сдвинуться на копейки округления.
### fr
- Le poste de production a un nouvel onglet en bas, « Réceptions de sous-traitance » : les produits du sous-traitant se saisissent désormais en ligne, sans ouvrir le document. La ligne crée et valide aussitôt la réception, ou s'ajoute à la réception du jour du même transfert. L'ancien bouton « Réception de sous-traitance » de l'onglet « Sous-traitance » reste et ouvre le document ; à côté, le bouton « Réception en ligne » ouvre le nouvel onglet avec une nouvelle ligne sur le transfert coché.
- Dans la ligne on indique le transfert de sous-traitance, le produit, la quantité et, si besoin, le pourcentage de pertes. Le sous-traitant et l'entrepôt sont repris du transfert. Les matières ne se saisissent pas : le programme les calcule selon la gamme avec le pourcentage de pertes et les recalcule à chaque modification de la ligne.
- La réception ne se saisit que sur un transfert validé de sa commande et pas au-delà des produits attendus : ce qu'il reste à recevoir est visible dans la liste de choix des produits. La ligne d'une réception antérieure ne peut pas être modifiée si des produits ont déjà été reçus après elle sur les transferts de la commande : modifiez la dernière réception ou ouvrez le document.
- Le coût des services du sous-traitant est désormais conservé par ligne de produit, l'en-tête du document en est la somme. Si l'on modifie la somme dans l'en-tête, elle est répartie sur les lignes selon le poids de la gamme (quantité, normes et pourcentage de pertes). Chaque ligne reçoit ses propres services dans son coût de revient. Dans le poste de production, les services apparaissent dans la colonne « Services » si les montants vous sont affichés. Le bouton « + service de sous-traitance » fixe le montant des services pour tout le document de la ligne sélectionnée et le répartit comme la modification de l'en-tête. Si l'on supprime une ligne, ses services passent sur les lignes restantes : le montant de la facture du sous-traitant ne diminue pas.
- Si les matières d'une réception ont été modifiées à la main dans le document, le document s'en souvient désormais (case « Matières modifiées manuellement » dans l'en-tête). Les lignes d'un tel document sont en lecture seule dans le poste de production : modifiez-les dans le document. La commande « Calculer les matières » du document décoche la case.
- Lors de la mise à jour, les anciennes réceptions de sous-traitance ont reçu leurs services par ligne, et la case des matières manuelles a été cochée pour celles dont les matières ne correspondent pas au calcul selon la gamme. Les documents n'ont pas été revalidés, leurs mouvements et les montants de l'en-tête n'ont pas changé. Si vous revalidez à la main une ancienne réception, le coût des lignes peut varier de quelques centimes d'arrondi.
### en
- The production workstation has a new bottom tab, "Subcontracting receipts": products from the processor are now entered as a line, without opening the document. The line immediately creates and posts the receipt, or is added to today's receipt of the same transfer. The old "Subcontracting receipt" button on the "Subcontracting" tab stays and opens the document; next to it, the new "Receipt as a line" button switches to the new tab with a new line for the ticked transfer.
- In the line you specify the subcontracting transfer, the product, the quantity and, if needed, the loss percentage. The processor and warehouse come from the transfer. Materials are not entered: the program calculates them from the bill of materials with the loss percentage and recalculates them on every change of the line.
- A receipt is entered only against a posted transfer of its order and not beyond the expected products: what is left to receive is shown in the product choice list. The line of an earlier receipt cannot be edited if products have already been received after it against the order transfers: edit the latest receipt or open the document.
- The processor services cost is now stored per product line; the document header holds their sum. If you change the sum in the header, it is spread over the lines by the bill of materials weight (quantity, norms and loss percentage). Each line gets its own services in its cost. In the workstation the services are shown in the "Services" column if amounts are shown to you. The "+ processing service" button sets the services amount for the whole document of the selected line and spreads it the same way as editing the header. If you delete a line, its services move to the remaining lines: the processor invoice amount does not decrease.
- If the materials of a receipt were edited by hand in the document form, the document now remembers it (the "Materials edited manually" check box in the header). The lines of such a document are read-only in the workstation: edit them in the document. The "Calculate materials" command in the document clears the check box.
- On update, old subcontracting receipts got their services per line, and the manual materials check box was set for those whose materials do not match the calculation from the bill of materials. The documents were not reposted; their movements and header amounts did not change. If you repost an old receipt by hand, the line costs may shift by a few cents of rounding.
### es
- El puesto de producción tiene una nueva pestaña inferior, «Recepciones de subcontratación»: los productos del procesador ahora se introducen como línea, sin abrir el documento. La línea crea y contabiliza la recepción al momento, o se añade a la recepción de hoy del mismo envío. El botón anterior «Recepción de subcontratación» de la pestaña «Subcontratación» se mantiene y abre el documento; a su lado, el botón «Recepción en línea» pasa a la nueva pestaña con una línea nueva para el envío marcado.
- En la línea se indica el envío a subcontratista, el producto, la cantidad y, si hace falta, el porcentaje de pérdidas. El procesador y el almacén se toman del envío. Las materias no se introducen: el programa las calcula según el escandallo con el porcentaje de pérdidas y las recalcula en cada cambio de la línea.
- La recepción solo se introduce sobre un envío contabilizado de su pedido y no por encima de los productos esperados: lo que queda por recibir se ve en la lista de elección de productos. La línea de una recepción anterior no se puede editar si después de ella ya se recibieron productos por los envíos del pedido: edite la última recepción o abra el documento.
- El coste de los servicios del procesador ahora se guarda por línea de producto; la cabecera del documento es su suma. Si se cambia la suma en la cabecera, se reparte entre las líneas según el peso del escandallo (cantidad, normas y porcentaje de pérdidas). Cada línea recibe sus propios servicios en su coste. En el puesto de producción los servicios se ven en la columna «Servicios» si se le muestran los importes. El botón «+ servicio de procesamiento» fija el importe de servicios para todo el documento de la línea seleccionada y lo reparte igual que el cambio de la cabecera. Si se elimina una línea, sus servicios pasan a las líneas restantes: el importe de la factura del procesador no disminuye.
- Si las materias de una recepción se modificaron a mano en el documento, el documento ahora lo recuerda (casilla «Materias modificadas manualmente» en la cabecera). Las líneas de ese documento son de solo lectura en el puesto de producción: edítelas en el documento. El comando «Calcular materias» del documento desmarca la casilla.
- Al actualizar, las recepciones de subcontratación antiguas recibieron sus servicios por línea, y la casilla de materias manuales se marcó en las que no coinciden con el cálculo según el escandallo. Los documentos no se volvieron a contabilizar; sus movimientos y los importes de la cabecera no cambiaron. Si vuelve a contabilizar a mano una recepción antigua, el coste de las líneas puede variar unos céntimos por redondeo.

## 2.0.15.47
### ru
- Переключатель «Автоматический выпуск при продаже» теперь называется «Автоматическое создание выпусков при отгрузке». Он находится там же: Настройки программы → Производство. Это та самая настройка, переименование которой было обещано в версии 2.0.15.43.
- Под отгрузкой понимаются и продажа (расходная накладная), и передача в переработку по заказу на производство: включённый переключатель создаёт выпуск в обоих случаях, выключенный — ни в одном. Подсказка к переключателю переписана под то, как он работает сейчас, в том числе про то, что сначала берётся свободный остаток склада.
- Значение настройки при обновлении сохраняется: если переключатель был включён, он остаётся включённым.
### fr
- Le commutateur « Fabrication automatique à la vente » s'appelle désormais « Création automatique des fabrications à l'expédition ». Il se trouve au même endroit : Paramètres du programme → Production. C'est le réglage dont le changement de nom avait été annoncé dans la version 2.0.15.43.
- Par expédition on entend à la fois la vente (bon de livraison) et le transfert en sous-traitance sur une commande en production : le commutateur activé crée la fabrication dans les deux cas, désactivé — dans aucun. L'infobulle du commutateur a été réécrite selon son fonctionnement actuel, y compris le fait que le stock libre est pris en premier.
- La valeur du réglage est conservée lors de la mise à jour : si le commutateur était activé, il le reste.
### en
- The "Automatic production output on sale" switch is now called "Automatic creation of production outputs on shipment". It is in the same place: Program settings → Production. This is the setting whose renaming was announced in version 2.0.15.43.
- A shipment means both a sale (delivery note) and a transfer to subcontracting for a production order: with the switch on, the output is created in both cases; with it off, in neither. The switch tooltip has been rewritten to match how it works now, including that the free stock is taken first.
- The setting's value is kept on update: if the switch was on, it stays on.
### es
- El interruptor «Fabricación automática al vender» ahora se llama «Creación automática de fabricaciones en el envío». Está en el mismo lugar: Configuración del programa → Producción. Es el ajuste cuyo cambio de nombre se anunció en la versión 2.0.15.43.
- Por envío se entiende tanto la venta (albarán) como la transferencia a subcontratación de un pedido de producción: con el interruptor activado la fabricación se crea en ambos casos; desactivado, en ninguno. La ayuda del interruptor se ha reescrito según su funcionamiento actual, incluido que primero se toma el stock libre.
- El valor del ajuste se conserva al actualizar: si el interruptor estaba activado, sigue activado.

## 2.0.15.46
### ru
- Готовая продукция и полуфабрикаты, которые уже лежат на складе, больше не выпускаются заново. При автоматическом выпуске сначала берётся свободный остаток склада, производится только недостающее. Правило одно и для отгрузки, и для передачи в переработку. Раньше при отгрузке программа выпускала продукцию заново, даже если такая же лежала на складе не под этот заказ.
- Остаток берётся любой, в том числе приготовленный под другой заказ. Отгрузка одного заказа может забрать продукцию, которую готовили для другого. Автоматический выпуск другой заказ сам не доделает, если по нему уже выпущено всё заказанное: его отгрузка откажет по нехватке, и недостающее нужно выпустить вручную.
- Свободным считается только то, что не нужно более поздним документам. Отгрузка или передача, проведённая задним числом, не забирает продукцию, которую позже уже отгрузили или передали, — иначе склад у более позднего документа ушёл бы в минус. Такой документ выпустит недостающее сам.
- Сырьё под взятое со склада не списывается, и на складе не остаётся лишней партии продукции по себестоимости сырья. Себестоимость самой отгрузки от этого не меняется, но меняется себестоимость следующих продаж этой позиции.
- Потребность заказа в материалах, когда продукция взята со склада, не уменьшается: дефицит заказа остаётся прежним.
- Важно: не перепроводите вручную старые отгрузки и передачи — ни по одной, ни групповым проведением, ни групповым изменением реквизитов (оно тоже перепроводит документы). Их автоматический выпуск будет пересчитан по новому правилу и может уменьшиться, исчезнуть или вырасти (тогда возможен отказ по нехватке сырья). Если выпущенное тогда уже продано более поздним документом, стоимость остатка на складе разойдётся с количеством; дефицит заказа в материалах снова вырастет, а стадия заказа может откатиться. Фоновое перепроведение автоматические выпуски не трогает.
### fr
- Les produits finis et semi-finis déjà en stock ne sont plus refabriqués. La fabrication automatique prend d'abord le stock libre et ne produit que ce qui manque. La règle est la même pour l'expédition et pour le transfert en sous-traitance. Auparavant, à l'expédition, le programme refabriquait le produit même s'il y en avait en stock hors de cette commande.
- Tout stock est pris, y compris celui préparé pour une autre commande. L'expédition d'une commande peut prendre des produits préparés pour une autre. La fabrication automatique ne complétera pas cette autre commande si tout ce qui était commandé y a déjà été fabriqué : son expédition sera refusée faute de stock, et le manquant doit être fabriqué à la main.
- N'est libre que ce dont les documents ultérieurs n'ont pas besoin. Une expédition ou un transfert validé à une date antérieure ne prend pas les produits déjà expédiés ou transférés plus tard — sinon le stock du document ultérieur deviendrait négatif. Un tel document fabrique lui-même ce qui manque.
- Les matières correspondant à ce qui est pris en stock ne sont pas sorties, et il ne reste pas en stock de lot superflu au coût des matières. Le coût de revient de l'expédition elle-même ne change pas, mais celui des ventes suivantes de cet article change.
- Le besoin en matières de la commande n'est pas diminué quand le produit est pris en stock : le déficit de la commande reste le même.
- Important : ne revalidez pas à la main les anciennes expéditions et les anciens transferts — ni un par un, ni par validation groupée, ni par modification groupée des attributs (elle revalide aussi les documents). Leur fabrication automatique sera recalculée selon la nouvelle règle et peut diminuer, disparaître ou augmenter (un refus faute de matières est alors possible). Si ce qui a été fabriqué a déjà été vendu par un document ultérieur, la valeur du stock ne correspondra plus à la quantité ; le déficit de matières de la commande augmentera de nouveau et l'étape de la commande peut reculer. La revalidation en arrière-plan ne touche pas aux fabrications automatiques.
### en
- Finished products and semi-finished goods that are already in stock are no longer produced again. Automatic production output takes the free stock first and produces only what is missing. The rule is the same for shipments and for transfers to subcontracting. Previously, on shipment, the program produced the item again even when the same item was in stock outside this order.
- Any stock is taken, including stock prepared for another order. Shipping one order may take products prepared for another. Automatic production output will not complete that other order if everything ordered has already been produced for it: its shipment will be refused for lack of stock, and the missing quantity must be produced by hand.
- Only what later documents do not need counts as free. A shipment or transfer posted with an earlier date does not take products already shipped or transferred later — otherwise the later document's stock would go negative. Such a document produces what is missing itself.
- Materials for what is taken from stock are not written off, and no surplus product batch at material cost is left in stock. The cost of the shipment itself does not change, but the cost of later sales of this item does.
- The order's material requirement is not reduced when the product is taken from stock: the order deficit stays the same.
- Important: do not repost old shipments and transfers by hand — neither one by one, nor by group posting, nor by group attribute editing (it reposts documents too). Their automatic production output will be recalculated under the new rule and may shrink, disappear or grow (a refusal for lack of materials is then possible). If what was produced then has already been sold by a later document, the stock value will no longer match the quantity; the order's material deficit will grow again and the order stage may roll back. Background reposting does not touch automatic production outputs.
### es
- Los productos terminados y semielaborados que ya están en almacén ya no se fabrican de nuevo. La fabricación automática toma primero el stock libre y solo produce lo que falta. La regla es la misma para el envío y para la transferencia a subcontratación. Antes, al enviar, el programa volvía a fabricar el producto aunque hubiera en almacén fuera de este pedido.
- Se toma cualquier stock, incluido el preparado para otro pedido. El envío de un pedido puede llevarse productos preparados para otro. La fabricación automática no completará ese otro pedido si ya se fabricó todo lo pedido para él: su envío se rechazará por falta de stock, y lo que falta debe fabricarse a mano.
- Solo es libre lo que los documentos posteriores no necesitan. Un envío o una transferencia contabilizados con fecha anterior no se llevan los productos ya enviados o transferidos después; de lo contrario, el stock del documento posterior quedaría en negativo. Ese documento fabrica por sí mismo lo que falta.
- Las materias de lo que se toma del almacén no se dan de baja, y no queda en almacén un lote sobrante de producto al coste de las materias. El coste del propio envío no cambia, pero sí el de las ventas siguientes de este artículo.
- La necesidad de materiales del pedido no se reduce cuando el producto se toma del almacén: el déficit del pedido sigue igual.
- Importante: no vuelva a contabilizar a mano envíos y transferencias antiguos, ni uno a uno, ni con la contabilización en grupo, ni con la modificación en grupo de atributos (también vuelve a contabilizar los documentos). Su fabricación automática se recalculará según la nueva regla y puede reducirse, desaparecer o aumentar (entonces es posible un rechazo por falta de materias). Si lo fabricado ya se vendió en un documento posterior, el valor del stock no coincidirá con la cantidad; el déficit de materiales del pedido volverá a crecer y la etapa del pedido puede retroceder. La recontabilización en segundo plano no toca las fabricaciones automáticas.

## 2.0.15.45
### ru
- В таблице продукции поступления из переработки появилась колонка «Процент потерь». Она заполняется из технологической карты принимаемой продукции на дату документа: программа берёт проценты строк карты и усредняет их по нормам расхода. Один процент на всю строку продукции — если в карте у материалов разные проценты, в документ попадает их среднее.
- Сырьё, которое списывается у переработчика, теперь считается по технологической карте пропорционально ПРИНЯТОМУ количеству, а не берётся целиком. Раньше частичная приёмка списывала всё переданное сырьё под неполный выпуск. Из этого следует главное: себестоимость продукции из переработки считается иначе, чем раньше.
- Если остатка сырья у переработчика осталось не больше, чем расчётные потери, он уходит в списание этого же поступления: крошка не висит за переработчиком, её стоимость входит в себестоимость принятого. Отдельный документ списания при этом не создаётся. Без заполненного процента потерь в карте порог равен нулю, и дочистки нет — остаток висит, как раньше.
- Дочистка касается только партий той передачи, по которой введено поступление. Сырьё, лежащее у переработчика по другой, ещё не вернувшейся передаче, она не трогает.
- Сырьё пересчитывается, пока вы правите продукцию: меняете количество, упаковку, номенклатуру или процент потерь — строки сырья пересобираются. Как только вы сами взялись за таблицу сырья — поправили количество, серию, добавили строку, — пересчёт прекращается и строки остаются вашими. Вернуть расчёт можно кнопкой «Рассчитать сырьё» над таблицей. У записанного документа пересчёт не включается сам никогда.
- Документ больше не проводится, если заполнена только одна сторона: сырьё без продукции списало бы стоимость в никуда, а продукция без сырья и без стоимости услуг пришла бы на склад с нулевой себестоимостью. В обоих случаях программа скажет, чего не хватает.
- Позиция, которую передали переработчику и приняли обратно той же номенклатурой (перешив, покраска), расходуется по принятому количеству: технологическая карта к ней не применяется.
- Если технологической карты нет ни у одной принимаемой позиции, в сырьё по-прежнему попадает весь остаток передачи. Если карта есть хотя бы у одной, позиция остатка, которой нет в карте, в строки не попадает — добавьте её руками.
### fr
- Le tableau des produits de la réception de sous-traitance a une nouvelle colonne « Pourcentage de pertes ». Elle est remplie d'après la gamme du produit reçu à la date du document : le programme prend les pourcentages des lignes de la gamme et en fait une moyenne pondérée par les normes. Un seul pourcentage pour toute la ligne de produit — si les matières de la gamme ont des pourcentages différents, c'est leur moyenne qui entre dans le document.
- Les matières sorties chez le sous-traitant sont désormais calculées d'après la gamme, proportionnellement à la quantité REÇUE, et non prises en totalité. Auparavant une réception partielle sortait toutes les matières transférées pour une production incomplète. Conséquence principale : le coût de revient des produits de sous-traitance se calcule autrement qu'avant.
- S'il ne reste chez le sous-traitant pas plus que les pertes calculées, le reliquat part en sortie sur cette même réception : les miettes ne restent pas chez le sous-traitant et leur valeur entre dans le coût de revient du reçu. Aucun document de sortie distinct n'est créé. Sans pourcentage de pertes renseigné dans la gamme, le seuil est nul et il n'y a pas de nettoyage — le reliquat reste, comme avant.
- Le nettoyage ne concerne que les lots du transfert sur lequel la réception est saisie. Les matières présentes chez le sous-traitant au titre d'un autre transfert non encore revenu ne sont pas touchées.
- Les matières sont recalculées pendant que vous modifiez les produits : quantité, emballage, article ou pourcentage de pertes — les lignes de matières sont reconstruites. Dès que vous touchez vous-même au tableau des matières — quantité, lot, ligne ajoutée —, le recalcul s'arrête et les lignes restent les vôtres. Le bouton « Calculer les matières » au-dessus du tableau rend le calcul. Sur un document enregistré, le recalcul ne se déclenche jamais tout seul.
- Le document ne se valide plus si un seul côté est rempli : des matières sans produits feraient disparaître leur valeur, et des produits sans matières ni coût de prestation entreraient en stock à coût nul. Dans les deux cas le programme indique ce qui manque.
- Un article transféré au sous-traitant et repris sous le même article (retouche, teinture) est consommé à hauteur de la quantité reçue : la gamme ne lui est pas appliquée.
- Si aucun des produits reçus n'a de gamme en vigueur, la totalité du reliquat du transfert entre dans les matières, comme avant. Si au moins un en a une, un article du reliquat absent de la gamme n'entre pas dans les lignes — ajoutez-le à la main.
### en
- The products table of a subcontracting receipt has a new "Loss percentage" column. It is filled from the bill of materials of the accepted product as of the document date: the program takes the percentages of the bill's lines and averages them by consumption norms. One percentage for the whole product line — if the bill's materials carry different percentages, their average goes into the document.
- The materials written off at the subcontractor are now calculated from the bill of materials in proportion to the ACCEPTED quantity instead of being taken in full. Previously a partial acceptance wrote off all transferred materials against an incomplete output. The main consequence: the cost of subcontracted products is calculated differently than before.
- If no more than the calculated losses remain at the subcontractor, the remainder goes into the write-off of this same receipt: crumbs do not stay with the subcontractor and their value enters the cost of what was accepted. No separate write-off document is created. Without a loss percentage in the bill the threshold is zero and there is no clean-up — the remainder stays, as before.
- The clean-up touches only the batches of the transfer the receipt is entered against. Materials held at the subcontractor under another transfer that has not yet come back are left alone.
- Materials are recalculated while you edit the products: change the quantity, the package, the item or the loss percentage and the material lines are rebuilt. As soon as you touch the materials table yourself — a quantity, a batch, an added line — the recalculation stops and the lines stay yours. The "Calculate materials" button above the table brings the calculation back. On a saved document the recalculation never starts by itself.
- The document no longer posts if only one side is filled in: materials without products would write their value off into nowhere, and products without materials and without a service cost would arrive in stock at zero cost. In both cases the program says what is missing.
- An item transferred to the subcontractor and accepted back as the same item (re-sewing, dyeing) is consumed at the accepted quantity: the bill of materials is not applied to it.
- If none of the accepted items has a bill of materials, the whole transfer remainder still goes into the materials. If at least one has, an item of the remainder that is absent from the bill does not enter the lines — add it by hand.
### es
- La tabla de productos de la recepción de procesamiento tiene una nueva columna «Porcentaje de pérdidas». Se rellena desde el escandallo del producto recibido en la fecha del documento: el programa toma los porcentajes de las líneas del escandallo y los promedia según las normas de consumo. Un solo porcentaje para toda la línea de producto: si los materiales del escandallo tienen porcentajes distintos, al documento entra su media.
- Las materias primas que se dan de baja en el procesador se calculan ahora según el escandallo, en proporción a la cantidad RECIBIDA, y no se toman por completo. Antes una recepción parcial daba de baja todas las materias transferidas para una producción incompleta. La consecuencia principal: el coste de los productos de procesamiento se calcula de otra manera que antes.
- Si en el procesador no queda más que las pérdidas calculadas, el resto se da de baja en esta misma recepción: las migajas no se quedan con el procesador y su valor entra en el coste de lo recibido. No se crea ningún documento de baja aparte. Sin porcentaje de pérdidas en el escandallo el umbral es cero y no hay limpieza: el resto se queda, como antes.
- La limpieza afecta solo a los lotes de la transferencia por la que se introduce la recepción. Las materias que están en el procesador por otra transferencia aún no devuelta no se tocan.
- Las materias se recalculan mientras usted corrige los productos: cambia la cantidad, el paquete, el artículo o el porcentaje de pérdidas y las líneas de materias se reconstruyen. En cuanto usted mismo toca la tabla de materias —una cantidad, un lote, una línea añadida—, el recálculo se detiene y las líneas quedan suyas. El botón «Calcular materias primas» sobre la tabla devuelve el cálculo. En un documento guardado el recálculo nunca se activa solo.
- El documento ya no se contabiliza si solo se ha rellenado un lado: materias sin productos harían desaparecer su valor, y productos sin materias y sin coste de servicios entrarían en almacén con coste cero. En ambos casos el programa indica qué falta.
- Un artículo transferido al procesador y recibido de vuelta como el mismo artículo (rehacer, teñir) se consume por la cantidad recibida: el escandallo no se le aplica.
- Si ninguno de los productos recibidos tiene escandallo, en las materias entra todo el resto de la transferencia, como antes. Si al menos uno lo tiene, un artículo del resto que no figure en el escandallo no entra en las líneas: añádalo a mano.

## 2.0.15.44
### ru
- Ожидаемая продукция передачи в переработку теперь считается по дереву материалов заказа, а не по его строкам товаров. Передаёте переработчику сырьё — программа подставляет полуфабрикат, из которого это сырьё делают; передаёте полуфабрикат — подставляет то, что из него собирают. Раньше подставлялась готовая продукция заказа, и по заказу с деревом материалов поступление заполнялось не тем.
- Ожидаемое количество ограничено переданным: передали половину сырья — программа ждёт половину продукции, а не весь заказ. Потолок прежний — сколько заказано.
- Ожидаемая продукция пересчитывается, пока вы набираете строки передачи. Как только вы поправили её руками, пересчёт прекращается и строки остаются вашими; вернуть расчёт можно кнопкой «Заполнить по заказу» над таблицей продукции. У записанного документа пересчёт не включается сам никогда.
- Поступление из переработки списывает у переработчика партии СВОЕГО заказа и партии, переданные без заказа. Партии других заказов того же переработчика ему больше не доступны: раньше поступление по одному заказу могло съесть сырьё другого, а при частичной приёмке второе поступление списывало то же самое ещё раз.
- Следствие, о котором важно знать: поступление, которому не хватает сырья своего заказа, теперь не проводится, даже если у переработчика лежит сырьё по другому заказу. В сообщении о нехватке сказано, какие партии считаются. Часть старых поступлений по этой причине может потребовать указания своей передачи-основания, чтобы перепровестись.
- Поступление из переработки, перепроведённое с изменённой датой, больше не вычитает собственные прежние движения второй раз: раньше документ, у которого дату сдвинули вперёд, мог отказаться проводиться с сообщением о нехватке сырья, которое у переработчика есть.
### fr
- La production attendue d'un transfert en sous-traitance est désormais calculée d'après l'arbre des matières de la commande et non d'après ses lignes d'articles. Vous transférez des matières — le programme propose le semi-fini qu'on en fait ; vous transférez un semi-fini — il propose ce qu'on assemble à partir de lui. Auparavant c'était le produit fini de la commande, et pour une commande avec arbre des matières la réception se remplissait mal.
- La quantité attendue est limitée par ce qui est transféré : la moitié des matières transférée — la moitié de la production attendue, pas la commande entière. Le plafond reste la quantité commandée.
- La production attendue est recalculée pendant que vous saisissez les lignes du transfert. Dès que vous la corrigez à la main, le recalcul s'arrête et les lignes restent les vôtres ; le bouton « Remplir selon la commande » au-dessus du tableau rend le calcul. Sur un document enregistré, le recalcul ne se déclenche jamais tout seul.
- La réception de sous-traitance sort chez le sous-traitant les lots de SA commande et les lots transférés sans commande. Les lots des autres commandes du même sous-traitant ne lui sont plus accessibles : auparavant une réception d'une commande pouvait consommer les matières d'une autre, et en réception partielle la seconde réception sortait deux fois la même chose.
- Conséquence à connaître : une réception à qui il manque les matières de sa commande ne se valide plus, même s'il reste chez le sous-traitant des matières d'une autre commande. Le message de manque précise quels lots sont pris en compte. Certaines anciennes réceptions peuvent de ce fait exiger l'indication de leur transfert d'origine pour être revalidées.
- Une réception de sous-traitance revalidée avec une date modifiée ne retranche plus une seconde fois ses propres mouvements précédents : auparavant un document dont la date était avancée pouvait refuser de se valider en signalant un manque de matières pourtant présentes.
### en
- The expected output of a subcontracting transfer is now calculated from the order's material tree rather than from its item lines. You transfer materials — the program suggests the semi-finished product made from them; you transfer a semi-finished product — it suggests what is assembled from it. Previously it suggested the order's finished product, and for an order with a material tree the receipt was filled with the wrong item.
- The expected quantity is limited by what is transferred: transfer half the materials and the program expects half the output, not the whole order. The ceiling is still the ordered quantity.
- The expected output is recalculated while you enter the transfer lines. As soon as you correct it by hand the recalculation stops and the lines stay yours; the "Fill from order" button above the output table brings the calculation back. On a saved document the recalculation never starts by itself.
- A subcontracting receipt writes off the subcontractor's batches of ITS OWN order and batches transferred without an order. Batches of the same subcontractor's other orders are no longer available to it: previously a receipt for one order could eat another order's materials, and on partial acceptance the second receipt wrote off the same thing again.
- A consequence worth knowing: a receipt short of its own order's materials no longer posts, even if the subcontractor holds materials of another order. The shortage message says which batches are counted. Some older receipts may therefore need their basis transfer specified in order to repost.
- A subcontracting receipt reposted with a changed date no longer subtracts its own previous movements a second time: previously a document whose date was moved forward could refuse to post, reporting a shortage of materials the subcontractor did have.
### es
- La producción esperada de una transferencia a subcontratación se calcula ahora por el árbol de materiales del pedido y no por sus líneas de artículos. Si transfiere materiales, el programa propone el semielaborado que se hace con ellos; si transfiere un semielaborado, propone lo que se monta a partir de él. Antes proponía el producto terminado del pedido, y en un pedido con árbol de materiales la recepción se rellenaba con lo que no era.
- La cantidad esperada está limitada por lo transferido: si transfiere la mitad de los materiales, el programa espera la mitad de la producción, no todo el pedido. El tope sigue siendo lo pedido.
- La producción esperada se recalcula mientras usted introduce las líneas de la transferencia. En cuanto la corrige a mano, el recálculo se detiene y las líneas quedan suyas; el botón «Rellenar según el pedido» sobre la tabla devuelve el cálculo. En un documento guardado el recálculo nunca se activa solo.
- La recepción de subcontratación da de baja en el subcontratista los lotes de SU pedido y los lotes transferidos sin pedido. Los lotes de otros pedidos del mismo subcontratista ya no están a su alcance: antes una recepción de un pedido podía comerse los materiales de otro, y en recepción parcial la segunda recepción daba de baja lo mismo otra vez.
- Consecuencia que conviene conocer: una recepción a la que le faltan los materiales de su pedido ya no se contabiliza, aunque el subcontratista tenga materiales de otro pedido. El mensaje de falta indica qué lotes se cuentan. Por eso algunas recepciones antiguas pueden necesitar que se indique su transferencia de origen para volver a contabilizarse.
- Una recepción de subcontratación recontabilizada con la fecha cambiada ya no resta por segunda vez sus propios movimientos anteriores: antes un documento cuya fecha se adelantaba podía negarse a contabilizarse informando de una falta de materiales que sí estaban.

## 2.0.15.43
### ru
- Полуфабрикат, который вы передаёте переработчику, теперь выпускается сам. При проведении передачи в переработку программа создаёт выпуск продукции на секунду раньше передачи, берёт состав из технологической карты полуфабриката до самого нижнего уровня и списывает это сырьё со склада. Раньше полуфабрикат приходилось выпускать вручную до каждой передачи, иначе передача не проводилась — передавать было нечего.
- Если полуфабрикат уже лежит на складе, выпускается только недостающая часть: передаёте пять, на складе два — выпустится три. Лежащее на складе повторно не выпускается никогда.
- Выпускается не больше, чем нужно заказу: потолок — потребность заказа в этом полуфабрикате за вычетом уже выпущенного. Если потребность исчерпана, а на складе пусто, передача не проводится и говорит о нехватке: это защита от расхода сырья на двойную норму против заказа.
- Отмена проведения передачи распроводит её выпуск, пометка удаления переходит на него, а удаление передачи помечает выпуск на удаление. Правится такой выпуск только перепроведением своей передачи — как и выпуск при отгрузке.
- Переключатель «использовать выпуск продукции при продаже» теперь управляет и автоматическим выпуском при передаче в переработку. Имя настройки осталось прежним, переименование придёт отдельной сборкой; пока выключенный флажок гасит автоматический выпуск в обоих местах.
- Сырьё и покупные позиции передаются переработчику как раньше: автоматический выпуск их не касается. Если у передаваемого полуфабриката нет действующей технологической карты или заказ в нём не нуждается, программа скажет об этом, а передача пройдёт без выпуска.
- Порядок блокировок при поступлении из переработки выровнен с остальными документами производственного контура: реже встречаются взаимные блокировки, когда кладовщик проводит следующую передачу, пока проводится поступление по предыдущей.
- Заодно точнее стал автоматический выпуск ПРИ ОТГРУЗКЕ. Он больше не засчитывает себе то, что уже ушло переработчику: выпущенное вручную и переданное в переработку при отгрузке выпускается заново, а не списывается со склада, на котором его нет. И потолок «сколько всего можно выпустить по заказу» теперь считается и по строкам товаров заказа, и по его материалам — для позиции, которая в заказе одновременно и товар, и материал другой строки, он вырос.
### fr
- Le semi-fini que vous transférez au sous-traitant est désormais fabriqué automatiquement. À la validation du transfert en sous-traitance, le programme crée une production une seconde avant le transfert, prend la composition dans la gamme du semi-fini jusqu'au niveau le plus bas et sort ces matières du stock. Auparavant il fallait produire le semi-fini à la main avant chaque transfert, sinon le transfert ne se validait pas : il n'y avait rien à transférer.
- Si le semi-fini est déjà en stock, seule la part manquante est produite : vous transférez cinq, il y en a deux en stock — trois seront produits. Ce qui est en stock n'est jamais produit deux fois.
- On ne produit pas plus que la commande n'en a besoin : le plafond est le besoin de la commande en ce semi-fini moins ce qui a déjà été produit. Si le besoin est épuisé et le stock vide, le transfert n'est pas validé et signale le manque : c'est une protection contre la consommation de matières au double de la norme de la commande.
- L'annulation de la validation du transfert dévalide sa production, le marquage à supprimer se reporte sur elle, et la suppression du transfert marque la production à supprimer. Une telle production ne se modifie que par la revalidation de son transfert — comme la production à l'expédition.
- L'option « utiliser la production à la vente » pilote maintenant aussi la production automatique au transfert en sous-traitance. Le nom du paramètre reste inchangé, son renommage viendra dans une autre version ; pour l'instant, décocher la case coupe la production automatique aux deux endroits.
- Les matières et les articles achetés sont transférés au sous-traitant comme avant : la production automatique ne les concerne pas. Si le semi-fini transféré n'a pas de gamme en vigueur, ou si la commande n'en a pas besoin, le programme le signale et le transfert passe sans production.
- L'ordre des blocages à la réception de sous-traitance est aligné sur les autres documents de production : les blocages mutuels sont plus rares lorsque le magasinier valide le transfert suivant pendant la validation de la réception précédente.
- La fabrication automatique À L'EXPÉDITION est devenue plus juste au passage. Elle ne s'attribue plus ce qui est déjà parti chez le sous-traitant : ce qui a été fabriqué à la main puis transféré est refabriqué à l'expédition au lieu d'être sorti d'un stock où il n'est pas. Et le plafond « combien peut-on fabriquer en tout pour la commande » se calcule désormais sur les lignes d'articles ET sur les matières de la commande — pour un article qui y est à la fois article et matière d'une autre ligne, il a augmenté.
### en
- A semi-finished product you transfer to a subcontractor is now produced automatically. When the subcontracting transfer is posted, the program creates a production output one second before the transfer, takes the composition from the routing of the semi-finished product down to the lowest level, and writes those materials off the warehouse. Previously the semi-finished product had to be produced by hand before every transfer, otherwise the transfer would not post: there was nothing to transfer.
- If the semi-finished product is already in the warehouse, only the missing part is produced: you transfer five, two are in stock — three will be produced. What is in stock is never produced twice.
- No more is produced than the order needs: the ceiling is the order's need for that semi-finished product minus what has already been produced. If the need is exhausted and the warehouse is empty, the transfer does not post and reports the shortage: this protects against consuming materials at twice the order's norm.
- Unposting the transfer unposts its output, the deletion mark carries over to it, and deleting the transfer marks the output for deletion. Such an output changes only by reposting its transfer — just like the output on shipment.
- The "use production output on sale" switch now also governs the automatic output on transfer to subcontracting. The setting keeps its old name, renaming will come in a separate build; for now, clearing the checkbox turns the automatic output off in both places.
- Materials and purchased items are transferred to the subcontractor as before: the automatic output does not touch them. If the transferred semi-finished product has no routing in force, or the order does not need it, the program says so and the transfer goes through without an output.
- The lock order on a subcontracting receipt is aligned with the other production documents: mutual locks are rarer when a storekeeper posts the next transfer while the receipt for the previous one is being posted.
- The automatic output ON SHIPMENT became more accurate along the way. It no longer credits itself with what has already gone to the subcontractor: what was produced by hand and then transferred is produced again on shipment instead of being written off a warehouse where it is not. And the ceiling "how much may be produced in total for the order" is now counted over the order's item lines AND its materials — for an item that is both a line and a material of another line, it has grown.
### es
- El semielaborado que transfiere al subcontratista ahora se fabrica solo. Al contabilizar la transferencia a subcontratación, el programa crea una producción un segundo antes de la transferencia, toma la composición de la ficha técnica del semielaborado hasta el nivel más bajo y da de baja esos materiales del almacén. Antes había que producir el semielaborado a mano antes de cada transferencia, o la transferencia no se contabilizaba: no había nada que transferir.
- Si el semielaborado ya está en el almacén, solo se produce la parte que falta: transfiere cinco, hay dos en stock — se producirán tres. Lo que está en el almacén nunca se produce dos veces.
- No se produce más de lo que el pedido necesita: el tope es la necesidad del pedido de ese semielaborado menos lo ya producido. Si la necesidad está agotada y el almacén vacío, la transferencia no se contabiliza e informa de la falta: es una protección contra gastar materiales al doble de la norma del pedido.
- Descontabilizar la transferencia descontabiliza su producción, la marca de borrado pasa a ella, y borrar la transferencia marca la producción para borrar. Esa producción solo cambia al volver a contabilizar su transferencia — igual que la producción en el envío.
- El interruptor «usar producción al vender» ahora gobierna también la producción automática al transferir a subcontratación. El ajuste conserva su nombre, el cambio de nombre llegará en otra versión; por ahora, desmarcar la casilla apaga la producción automática en ambos sitios.
- Los materiales y los artículos comprados se transfieren al subcontratista como antes: la producción automática no los toca. Si el semielaborado transferido no tiene ficha técnica vigente, o el pedido no lo necesita, el programa lo indica y la transferencia pasa sin producción.
- El orden de bloqueos en la recepción de subcontratación se ha alineado con los demás documentos de producción: los bloqueos mutuos son más raros cuando el almacenero contabiliza la siguiente transferencia mientras se contabiliza la recepción de la anterior.
- De paso, la producción automática AL ENVIAR se ha vuelto más exacta. Ya no se apunta lo que ya se fue al subcontratista: lo fabricado a mano y luego transferido se vuelve a fabricar al enviar, en vez de darse de baja de un almacén donde no está. Y el tope «cuánto se puede fabricar en total para el pedido» se calcula ahora por las líneas de artículos Y por los materiales del pedido — para un artículo que es a la vez línea y material de otra línea, ha crecido.
## 2.0.15.42
### ru
- У выпуска продукции появился признак «Создан автоматически». Раньше выпуск, сделанный программой при отгрузке, отличался от вашего собственного только тем, что в основании у него стояла расходная накладная. Теперь это отдельный признак документа: при обновлении он проставляется всем выпускам, созданным программой до этой сборки.
- Поведение выпусков не изменилось: автоматический по-прежнему правится только перепроведением своей накладной, а ваш собственный остаётся полностью в вашем распоряжении. Изменился только способ, которым программа их различает — и теперь он не сломается, когда выпуск начнёт создаваться не только при отгрузке.
- Это подготовка к автоматическому выпуску полуфабриката при передаче в переработку: он придёт следующей сборкой.
### fr
- La production porte désormais un indicateur « Créé automatiquement ». Auparavant, une production faite par le programme lors de l'expédition ne se distinguait de la vôtre que par le document de base, un bon de livraison. C'est maintenant un attribut à part : lors de la mise à jour, il est apposé à toutes les productions créées par le programme avant cette version.
- Le comportement ne change pas : la production automatique ne se modifie toujours que par la revalidation de son bon de livraison, et la vôtre reste entièrement à votre main. Seule change la façon dont le programme les distingue — et elle ne cassera plus quand la production sera créée ailleurs qu'à l'expédition.
- C'est la préparation de la production automatique du semi-fini lors du transfert en sous-traitance, qui arrivera à la version suivante.
### en
- A production output now carries a "Created automatically" flag. Previously an output made by the program on shipment differed from your own only by having a delivery note as its basis. It is now a separate attribute: on update it is set on every output the program created before this build.
- Behaviour is unchanged: an automatic output is still modified only by reposting its delivery note, and your own output remains entirely yours. Only the way the program tells them apart has changed — and it will no longer break once outputs start being created somewhere other than shipment.
- This prepares the automatic output of a semi-finished product when it is transferred to a subcontractor, which arrives in the next build.
### es
- La producción tiene ahora un indicador «Creado automáticamente». Antes, una producción hecha por el programa al enviar solo se distinguía de la suya por tener un albarán como base. Ahora es un atributo aparte: al actualizar se marca en todas las producciones que el programa creó antes de esta versión.
- El comportamiento no cambia: la producción automática sigue modificándose solo al volver a contabilizar su albarán, y la suya sigue siendo enteramente suya. Solo cambia la forma en que el programa las distingue — y ya no se romperá cuando la producción empiece a crearse fuera del envío.
- Es la preparación de la producción automática del semielaborado al transferirlo a subcontratación, que llegará en la siguiente versión.

## 2.0.15.41
### ru
- Нормы расхода в технологических картах теперь хранятся с десятью знаками после запятой, а количества — с шестью вместо трёх. Раньше цепочка из трёх уровней с нормами по 0,05 давала 0,000125, число не помещалось в три знака и записывалось нулём: материал молча исчезал и из потребности, и из списания.
- Количество материала считается из точной нормы одним действием. Раньше оно сначала округлялось в упаковках и только потом пересчитывалось по коэффициенту упаковки, из-за чего мелкая норма обнулялась ещё до пересчёта.
- Если материал всё же теряется — его количество на заданный объём продукции меньше точности количества, — заказ больше не заполняется молча. Материалы такой строки не заполняются, документ не проводится, а сообщение называет материал и предлагает увеличить количество продукции или укрупнить норму в карте. Прежняя версия обещала предупреждение, но оно не срабатывало никогда.
- В торговых документах количество на форме показывается тремя знаками, как и раньше: выросшая точность нужна производству и в накладных только мешала бы. В заказе и выпуске норма расхода показывается шестью знаками, а хранится с десятью.
- Размер присоединённого файла перестал считаться количеством: он всегда им не был, а теперь не зависит от точности количеств.
### fr
- Les normes de consommation des gammes de fabrication sont désormais stockées avec dix décimales, et les quantités avec six au lieu de trois. Auparavant une chaîne de trois niveaux avec des normes de 0,05 donnait 0,000125, valeur qui n'entrait pas dans trois décimales et s'enregistrait à zéro : la matière disparaissait silencieusement du besoin et de la sortie.
- La quantité de matière est calculée à partir de la norme exacte en une seule opération. Auparavant elle était d'abord arrondie en conditionnements puis recalculée selon le coefficient, ce qui annulait une norme fine avant même le recalcul.
- Si la matière est malgré tout perdue — sa quantité pour le volume de production indiqué est inférieure à la précision des quantités —, la commande n'est plus remplie en silence. Les matières de cette ligne ne sont pas remplies, le document n'est pas validé, et le message nomme la matière et propose d'augmenter la quantité de production ou d'arrondir la norme. La version précédente promettait un avertissement qui ne se déclenchait jamais.
- Dans les documents commerciaux la quantité s'affiche avec trois décimales comme auparavant : la précision accrue sert à la production et ne ferait qu'encombrer les factures. Dans la commande et la production, la norme s'affiche avec six décimales et se stocke avec dix.
- La taille d'un fichier joint n'est plus traitée comme une quantité : elle ne l'a jamais été, et ne dépend plus de la précision des quantités.
### en
- Consumption norms in production routings are now stored with ten decimal places, and quantities with six instead of three. Previously a three-level chain with norms of 0.05 produced 0.000125, which did not fit into three decimals and was stored as zero: the material silently vanished from both the requirement and the write-off.
- Material quantity is computed from the exact norm in a single step. It used to be rounded in packages first and only then recalculated by the package coefficient, so a fine norm was zeroed before the recalculation.
- If a material is lost anyway — its quantity for the given production volume is below the quantity precision — the order is no longer filled silently. The materials of such a line are not filled, the document is not posted, and the message names the material and suggests increasing the production quantity or coarsening the norm. The previous version promised a warning that never fired.
- In trade documents the quantity is shown with three decimals as before: the increased precision serves production and would only clutter invoices. In the order and the production release the norm is shown with six decimals and stored with ten.
- The size of an attached file is no longer treated as a quantity: it never was one, and no longer depends on quantity precision.
### es
- Las normas de consumo de las rutas de fabricación se almacenan ahora con diez decimales, y las cantidades con seis en lugar de tres. Antes, una cadena de tres niveles con normas de 0,05 daba 0,000125, valor que no cabía en tres decimales y se guardaba como cero: el material desaparecía en silencio de la necesidad y de la baja.
- La cantidad de material se calcula a partir de la norma exacta en un solo paso. Antes se redondeaba primero en envases y solo después se recalculaba por el coeficiente, de modo que una norma fina se anulaba antes del recálculo.
- Si aun así el material se pierde — su cantidad para el volumen de producción indicado es inferior a la precisión de cantidades —, el pedido ya no se rellena en silencio. Los materiales de esa línea no se rellenan, el documento no se registra y el mensaje nombra el material y propone aumentar la cantidad de producción o redondear la norma. La versión anterior prometía un aviso que nunca se activaba.
- En los documentos comerciales la cantidad se muestra con tres decimales como antes: la mayor precisión sirve a producción y en las facturas solo estorbaría. En el pedido y en la producción la norma se muestra con seis decimales y se almacena con diez.
- El tamaño de un archivo adjunto ha dejado de tratarse como cantidad: nunca lo fue y ya no depende de la precisión de las cantidades.

## 2.0.15.40
### ru
- На закладке «Материалы» рабочего места производства состав заказа теперь показывается деревом: под изделием стоят его полуфабрикаты, а под каждым полуфабрикатом — материалы, из которых его делают. Раньше это был плоский список, и по нему нельзя было понять, к чему относится материал. Узлы раскрываются и сворачиваются, а в заголовке закладки считаются все строки дерева, а не только верхний уровень.
- Первой колонкой стал «Материал», а «Продукция» встала за ним: отступы дерева рисуются в первой колонке, и стоять они должны у материала, который и образует иерархию.
- Заполнение материалов по технологической карте в заказе клиента на производство теперь разворачивает карту в глубину. Если материал изделия — полуфабрикат с собственной картой, в заказ попадает и он сам, и материалы, из которых он делается, с количеством, пересчитанным по всей цепочке.
- Разворачивание останавливается там, где дальше идти незачем: на позиции, которая закупается, на полуфабрикате, который в карте помечен способом изготовления «Переработчик», и на позиции без действующей карты или с отменённой картой. Способ «Оба» разворачиванию не мешает — такой полуфабрикат мы делаем и сами.
- Глубже четырёх уровней карта не разворачивается: заполнение сообщает об этом и называет всю цепочку, а материалы такого изделия не заполняет. Так же обрабатывается кольцо в картах, когда изделие через полуфабрикаты ссылается само на себя: сообщение прямо показывает цепочку вида «A → B → A». Заказ с таким изделием не проводится.
- В материалах заказа появилось скрытое поле «Код родительской строки» — им и хранится дерево. У всех заказов, заведённых раньше, оно пустое, и такие заказы остаются плоскими, как были.
- Потребность в материалах по заказу считается по листьям дерева: полуфабрикат, который мы разворачиваем, в потребность не попадает — вместо него туда идут материалы, из которых он делается. Иначе система просила бы закупить и полуфабрикат, и его сырьё. Полуфабрикат, который закупается или делается переработчиком, потребностью остаётся.
- По тому же правилу работает автоматический выпуск при отгрузке: он списывает материалы-листья, а не полуфабрикат, которого на складе нет.
- Копирование строки изделия в заказе и в рабочем месте переносит всё поддерево материалов целиком и правильно перевязывает его на новую строку.
### fr
- Dans l'onglet « Matières » du poste de production, la composition de la commande s'affiche désormais en arbre : sous le produit figurent ses produits semi-finis, et sous chaque semi-fini les matières dont il est fait. C'était auparavant une liste plate où l'on ne voyait pas à quoi se rapportait une matière. Les nœuds se déplient et se replient, et le titre de l'onglet compte toutes les lignes de l'arbre, pas seulement le niveau supérieur.
- La colonne « Matière » passe en premier et « Produit » derrière : les retraits de l'arbre se dessinent dans la première colonne, et ils doivent accompagner la matière, qui porte la hiérarchie.
- Le remplissage des matières selon la gamme de fabrication dans la commande client en production développe maintenant la gamme en profondeur. Si une matière du produit est un semi-fini ayant sa propre gamme, la commande reçoit et ce semi-fini et les matières dont il est fait, avec la quantité recalculée sur toute la chaîne.
- Le développement s'arrête là où il n'a plus de sens : sur une position achetée, sur un semi-fini dont la gamme indique le mode de fabrication « Sous-traitant », et sur une position sans gamme en vigueur ou dont la gamme est annulée. Le mode « Les deux » n'arrête pas le développement : ce semi-fini, nous le fabriquons aussi.
- Au-delà de quatre niveaux la gamme n'est plus développée : le remplissage le signale en nommant toute la chaîne et ne remplit pas les matières d'un tel produit. Une boucle dans les gammes, lorsqu'un produit se référence lui-même à travers ses semi-finis, est traitée de même : le message montre la chaîne sous la forme « A → B → A ». Une commande contenant un tel produit n'est pas validée.
- Les matières de la commande comportent un nouveau champ masqué « Code de la ligne parente » : c'est lui qui porte l'arbre. Pour toutes les commandes créées auparavant il est vide, et ces commandes restent plates comme avant.
- Le besoin en matières de la commande se calcule sur les feuilles de l'arbre : le semi-fini que nous développons n'y figure pas, ce sont les matières dont il est fait qui y vont. Sinon le système demanderait d'acheter à la fois le semi-fini et sa matière première. Un semi-fini acheté ou réalisé par un sous-traitant reste un besoin.
- La production automatique à l'expédition suit la même règle : elle sort les matières-feuilles, et non le semi-fini qui n'est pas en stock.
- La copie d'une ligne de produit, dans la commande comme dans le poste de production, reprend tout le sous-arbre des matières et le rattache correctement à la nouvelle ligne.
### en
- On the "Materials" tab of the production workstation the order composition is now shown as a tree: under the product are its semi-finished products, and under each semi-finished product the materials it is made from. It used to be a flat list in which you could not tell what a material belonged to. Nodes expand and collapse, and the tab title counts every row of the tree, not only the top level.
- "Material" is now the first column and "Product" follows it: the tree indents are drawn in the first column, and they belong next to the material, which is what forms the hierarchy.
- Filling materials from the production routing in a customer production order now expands the routing in depth. If a material of the product is a semi-finished product with a routing of its own, the order receives both it and the materials it is made from, with the quantity recalculated along the whole chain.
- Expansion stops where going deeper makes no sense: on an item that is purchased, on a semi-finished product marked in the routing with the "Subcontractor" manufacturing method, and on an item with no current routing or with a cancelled one. The "Both" method does not stop expansion — we make such a semi-finished product ourselves as well.
- Deeper than four levels the routing is not expanded: filling reports this and names the whole chain, and leaves the materials of such a product empty. A loop in the routings, where a product references itself through its semi-finished products, is handled the same way: the message shows the chain as "A → B → A". An order with such a product is not posted.
- The order materials have a new hidden field, "Parent line code" — this is what holds the tree. For every order created earlier it is empty, and such orders stay flat as they were.
- The material requirement of the order is calculated from the leaves of the tree: the semi-finished product we expand does not go into the requirement — the materials it is made from go instead. Otherwise the system would ask to purchase both the semi-finished product and its raw material. A semi-finished product that is purchased or made by a subcontractor stays a requirement.
- Automatic production on shipment follows the same rule: it writes off the leaf materials, not the semi-finished product that is not in stock.
- Copying a product line, both in the order and in the workstation, carries the whole material subtree along and re-links it to the new line correctly.
### es
- En la pestaña «Materiales» del puesto de producción la composición del pedido se muestra ahora como un árbol: bajo el producto están sus productos semiacabados, y bajo cada semiacabado los materiales con los que se hace. Antes era una lista plana en la que no se veía a qué correspondía cada material. Los nodos se despliegan y se pliegan, y el título de la pestaña cuenta todas las filas del árbol, no solo el nivel superior.
- La columna «Material» pasa a ser la primera y «Producto» va detrás: las sangrías del árbol se dibujan en la primera columna, y deben acompañar al material, que es el que forma la jerarquía.
- El relleno de materiales según la ruta de fabricación en el pedido de cliente para producción desarrolla ahora la ruta en profundidad. Si un material del producto es un semiacabado con su propia ruta, al pedido entran tanto ese semiacabado como los materiales con los que se hace, con la cantidad recalculada a lo largo de toda la cadena.
- El desarrollo se detiene donde ya no tiene sentido seguir: en una posición que se compra, en un semiacabado marcado en la ruta con el método de fabricación «Subcontratista» y en una posición sin ruta vigente o con la ruta anulada. El método «Ambos» no detiene el desarrollo: ese semiacabado también lo hacemos nosotros.
- Más allá de cuatro niveles la ruta no se desarrolla: el relleno lo indica nombrando toda la cadena y deja sin rellenar los materiales de ese producto. Un bucle en las rutas, cuando un producto se referencia a sí mismo a través de sus semiacabados, se trata igual: el mensaje muestra la cadena como «A → B → A». Un pedido con ese producto no se contabiliza.
- En los materiales del pedido aparece un campo oculto nuevo, «Código de la línea padre»: es el que guarda el árbol. En todos los pedidos creados anteriormente está vacío, y esos pedidos siguen siendo planos como antes.
- La necesidad de materiales del pedido se calcula por las hojas del árbol: el semiacabado que desarrollamos no entra en la necesidad; en su lugar entran los materiales con los que se hace. De lo contrario el sistema pediría comprar tanto el semiacabado como su materia prima. Un semiacabado que se compra o que hace el subcontratista sigue siendo una necesidad.
- La producción automática en la expedición sigue la misma regla: da de baja los materiales hoja, y no el semiacabado que no está en el almacén.
- La copia de una línea de producto, tanto en el pedido como en el puesto de producción, arrastra todo el subárbol de materiales y lo vuelve a enlazar correctamente con la nueva línea.

## 2.0.15.39
### ru
- В технологической карте у каждой строки материалов появились два новых поля: «Способ изготовления» и «% потерь». Способ изготовления отвечает на вопрос, кто делает этот материал или полуфабрикат: «Наше производство», «Переработчик» или «Оба». Пока это признак для справки — на расчёты он начнёт влиять в следующих сборках, когда появится передача полуфабрикатов переработчику.
- «% потерь» — это ожидаемая доля сырья, которая теряется при изготовлении. В карте он задаётся как значение по умолчанию; фактический процент будет указываться в поступлении из переработки и правиться там же. Сейчас карта его только хранит и показывает.
- Оба поля правятся в двух местах: в самом документе технологической карты и на закладке «Техкарта» в карточке номенклатуры. В списке регистра «Состав техкарты» они только показываются — этот список ведётся документами и вручную не правится. На закладке «Материалы» рабочего места производства способ изготовления показывается для справки — там он берётся из той версии карты, по которой заполнен заказ.
- Если один и тот же материал указан в карте дважды с разными способом изготовления или процентом потерь, карта теперь не записывается и прямо об этом сообщает: при записи такие строки объединяются в одну, и без предупреждения второе значение потерялось бы молча.
- У всех технологических карт, заведённых раньше, при обновлении проставляется способ «Наше производство» и нулевой процент потерь — и в документах, и в истории карт.
- Проведение заказа на производство, которое переписывает технологическую карту изменившимся составом, больше не сбрасывает способ изготовления и процент потерь: у материалов, оставшихся в составе, они сохраняются.
### fr
- Dans la gamme de fabrication, chaque ligne de matières comporte deux nouveaux champs : « Mode de fabrication » et « % de pertes ». Le mode de fabrication indique qui réalise cette matière ou ce produit semi-fini : « Notre production », « Sous-traitant » ou « Les deux ». Pour l'instant c'est une information de référence — elle influencera les calculs dans les prochaines versions, avec l'envoi de produits semi-finis au sous-traitant.
- Le « % de pertes » est la part de matière perdue attendue lors de la fabrication. Dans la gamme il sert de valeur par défaut ; le pourcentage réel sera indiqué et modifié dans la réception de sous-traitance. Pour l'instant la gamme se contente de le conserver et de l'afficher.
- Les deux champs se modifient à deux endroits : dans le document de la gamme et sous l'onglet « Gamme » de la fiche article. Dans la liste du registre « Composition de la gamme » ils sont seulement affichés — cette liste est alimentée par les documents et ne se modifie pas à la main. Sous l'onglet « Matières » du poste de production, le mode de fabrication est affiché pour information — il provient de la version de la gamme qui a servi à remplir la commande.
- Si une même matière figure deux fois dans la gamme avec un mode de fabrication ou un pourcentage de pertes différents, la gamme n'est plus enregistrée et le signale : à l'enregistrement ces lignes sont fusionnées, et sans avertissement la seconde valeur disparaîtrait en silence.
- Pour toutes les gammes créées auparavant, la mise à jour renseigne le mode « Notre production » et un pourcentage de pertes nul — dans les documents comme dans l'historique des gammes.
- La validation d'une commande de production qui réécrit la gamme avec une composition modifiée ne remet plus à zéro le mode de fabrication ni le pourcentage de pertes : pour les matières restées dans la composition, ils sont conservés.
### en
- In the production routing every material line now has two new fields: "Manufacturing method" and "Loss %". The manufacturing method answers who makes this material or semi-finished product: "In-house production", "Subcontractor" or "Both". For now it is reference information — it will affect calculations in later builds, once transfers of semi-finished products to the subcontractor appear.
- "Loss %" is the expected share of material lost during manufacturing. In the routing it is a default value; the actual percentage will be entered and corrected in the receipt from subcontracting. For now the routing only stores and shows it.
- Both fields are edited in two places: in the routing document itself and on the "Routing" tab of the item card. In the list of the "Routing composition" register they are shown only — that list is written by documents and cannot be edited by hand. On the "Materials" tab of the production workstation the manufacturing method is shown for reference — taken from the routing version the order was filled from.
- If the same material appears twice in a routing with a different manufacturing method or loss percentage, the routing is no longer saved and says so: on saving such lines are merged into one, and without a warning the second value would be lost silently.
- For every routing created earlier, the update fills in the "In-house production" method and a zero loss percentage — both in the documents and in the routing history.
- Posting a production order that rewrites the routing with a changed composition no longer resets the manufacturing method and the loss percentage: for materials that stayed in the composition they are preserved.
### es
- En la ruta de fabricación cada línea de materiales tiene dos campos nuevos: «Método de fabricación» y «% de pérdidas». El método de fabricación responde a quién hace ese material o producto semiacabado: «Producción propia», «Subcontratista» o «Ambos». Por ahora es información de referencia: influirá en los cálculos en las próximas versiones, cuando aparezca el envío de productos semiacabados al subcontratista.
- El «% de pérdidas» es la parte de material que se espera perder durante la fabricación. En la ruta es un valor por defecto; el porcentaje real se indicará y se corregirá en la recepción de subcontratación. Por ahora la ruta solo lo guarda y lo muestra.
- Ambos campos se editan en dos sitios: en el propio documento de la ruta y en la pestaña «Ruta» de la ficha del artículo. En la lista del registro «Composición de la ruta» solo se muestran: esa lista la escriben los documentos y no se edita a mano. En la pestaña «Materiales» del puesto de producción el método de fabricación se muestra a título informativo: se toma de la versión de la ruta con la que se rellenó el pedido.
- Si el mismo material aparece dos veces en la ruta con distinto método de fabricación o porcentaje de pérdidas, la ruta ya no se guarda y lo indica: al guardar esas líneas se fusionan en una, y sin aviso el segundo valor se perdería en silencio.
- En todas las rutas creadas anteriormente, la actualización rellena el método «Producción propia» y un porcentaje de pérdidas cero, tanto en los documentos como en el historial de rutas.
- La contabilización de un pedido de producción que reescribe la ruta con una composición modificada ya no borra el método de fabricación ni el porcentaje de pérdidas: en los materiales que siguen en la composición se conservan.

## 2.0.15.38
### ru
- Рабочее место производства: замечание «строка не записана» больше не повторяется на каждое нажатие Enter во время ввода. Пока вы в строке, рабочее место молчит и только помечает её как незаписанную; сказать о незаполненном оно может один раз — когда вы действительно уйдёте со строки. Так теперь во всех нижних закладках: «Заказы поставщику», «Поступления», «Выпуск», «Отгрузки», «Переработка».
- При выводе сообщения прежние сообщения очищаются: в окне остаётся то, что относится к текущему действию, а не список замечаний за всю работу.
- На закладке «Переработка» колонка «Склад» стала редактируемой, пока строка не записана: склад уходит в шапку новой передачи в переработку. Раньше поле показывалось только для чтения, а без склада передачу записать нельзя — если ни склад пользователя, ни основное место хранения в настройках не заданы, ввод упирался в тупик. У записанной строки склад по-прежнему меняется только в самом документе: смена склада переписала бы списанные партии.
### fr
- Poste de production : la remarque « ligne non enregistrée » ne se répète plus à chaque appui sur Entrée pendant la saisie. Tant que vous êtes dans la ligne, le poste se tait et se contente de la marquer comme non enregistrée ; il ne signale les champs manquants qu'une fois, quand vous quittez réellement la ligne. Il en va de même dans tous les onglets du bas : « Commandes fournisseur », « Réceptions », « Production », « Expéditions », « Sous-traitance ».
- À l'affichage d'un message, les messages précédents sont effacés : la fenêtre ne garde que ce qui concerne l'action en cours, et non la liste des remarques de toute la séance.
- Dans l'onglet « Sous-traitance », la colonne « Entrepôt » devient modifiable tant que la ligne n'est pas enregistrée : l'entrepôt passe dans l'en-tête du nouvel envoi en sous-traitance. Auparavant le champ était en lecture seule, et sans entrepôt l'envoi ne peut pas être enregistré — si ni l'entrepôt de l'utilisateur ni le lieu de stockage principal ne sont renseignés, la saisie était bloquée. Pour une ligne enregistrée, l'entrepôt se change toujours dans le document lui-même : le changer réécrirait les lots sortis.
### en
- Production workstation: the "line not saved" notice no longer repeats on every Enter while you type. As long as you stay in the line the workstation keeps quiet and only marks it as unsaved; it reports the missing fields once, when you actually leave the line. This now holds in every bottom tab: "Supplier orders", "Receipts", "Output", "Shipments", "Subcontracting".
- Showing a message clears the previous ones: the window keeps what belongs to the current action instead of a list of notices from the whole session.
- On the "Subcontracting" tab the "Warehouse" column is editable while the line is unsaved: the warehouse goes into the header of the new transfer to the subcontractor. The field used to be read-only, and without a warehouse the transfer cannot be saved — if neither the user's warehouse nor the main storage location is set, entry hit a dead end. For a saved line the warehouse still changes only in the document itself: changing it would rewrite the batches written off.
### es
- Puesto de producción: el aviso «línea no guardada» ya no se repite con cada pulsación de Intro durante la entrada. Mientras esté en la línea, el puesto calla y solo la marca como no guardada; informa de los campos vacíos una vez, cuando abandona realmente la línea. Así ocurre ahora en todas las pestañas inferiores: «Pedidos a proveedor», «Recepciones», «Fabricación», «Expediciones», «Subcontratación».
- Al mostrar un mensaje se borran los anteriores: la ventana conserva lo que corresponde a la acción actual y no la lista de avisos de toda la sesión.
- En la pestaña «Subcontratación» la columna «Almacén» se puede editar mientras la línea no esté guardada: el almacén pasa a la cabecera del nuevo envío a subcontratación. Antes el campo era de solo lectura y sin almacén el envío no se puede guardar; si no están indicados ni el almacén del usuario ni el lugar de almacenamiento principal, la entrada quedaba bloqueada. En una línea guardada el almacén se cambia solo en el propio documento: cambiarlo reescribiría los lotes dados de baja.

## 2.0.15.37
### ru
- Из меню убраны пункты, которые показывались дважды. «Рабочее место производства» в разделе «Производство», «Настройки программы» в разделе «Настройка» и «Ventes en détail» в розничных продажах открывались двумя разными пунктами с одним названием — остался один, рабочий.
- Отборы номенклатуры «Готовая продукция», «Полуфабрикаты» и «Сырьё» больше не показываются в разделах «Продажи», «Закупки» и «Склад»: там открывается полный список номенклатуры, а отборы остались в разделе «Производство», для которого и делались.
### fr
- Les entrées de menu qui apparaissaient en double ont été retirées. « Poste de production » dans la section « Production », « Paramètres du programme » dans « Configuration » et « Ventes en détail » dans la vente au détail s'ouvraient par deux entrées portant le même nom — il n'en reste qu'une, la bonne.
- Les sélections de nomenclature « Produits finis », « Produits semi-finis » et « Matières premières » ne s'affichent plus dans les sections « Ventes », « Achats » et « Stock » : la liste complète y est ouverte, et les sélections restent dans « Production », pour laquelle elles ont été faites.
### en
- Menu entries that appeared twice were removed. "Production workstation" in the Production section, "Application settings" in Settings and "Ventes en détail" in retail sales each opened through two entries with the same name — one, the working one, remains.
- The item filters "Finished products", "Semi-finished products" and "Raw materials" no longer appear in the Sales, Purchases and Warehouse sections: those open the full item list, and the filters stay in Production, which they were made for.
### es
- Se han retirado las entradas de menú que aparecían dos veces. «Puesto de producción» en la sección «Producción», «Configuración del programa» en «Configuración» y «Ventes en détail» en ventas al por menor se abrían con dos entradas del mismo nombre; queda una, la que funciona.
- Los filtros de nomenclatura «Productos terminados», «Productos semielaborados» y «Materias primas» ya no se muestran en las secciones «Ventas», «Compras» y «Almacén»: allí se abre la lista completa, y los filtros permanecen en «Producción», para la que se hicieron.

## 2.0.15.36
### ru
- Раздел «Производство» перестроен. В первом списке теперь «Рабочее место производства», «Заказы клиентов на производство» и «Выпуск продукции» — выпуск больше не спрятан уровнем ниже.
- Давальческая схема выделена в группу «Переработка»: «Передача в переработку» и «Поступление из переработки». Прежняя группа «Производственные операции» и служебный пункт «Товары в переработке» (регистр) из меню убраны — одноимённый отчёт остался в панели отчётов.
- Группа «Справочники» стала «Нормативами»: «Технологические карты» вынесены наверх группы, номенклатура открывается тремя отборами — «Готовая продукция», «Полуфабрикаты», «Сырьё»; «Производственное оборудование» ушло в «См. также».
- Из панели «Создать» убрано создание выпуска продукции, передачи и поступления из переработки, номенклатуры и оборудования: выпуск создаётся автовыпуском при отгрузке или из рабочего места, поступление — на основании передачи. Создание технологической карты осталось.
- Новый отчёт «Себестоимость продукции» в разделе «Производство»: за выбранный период по каждой продукции количество, себестоимость без НДС, НДС в её составе и себестоимость единицы, с расшифровкой по характеристикам и документам выпуска. Данные берутся из учёта — из прихода товаров, а не считаются заново. Продукция переработчика входит в отчёт наравне с собственным выпуском.
### fr
- La section « Production » est réorganisée. La première liste contient désormais « Poste de production », « Commandes clients en production » et « Fabrication » — la fabrication n'est plus cachée au niveau inférieur.
- La sous-traitance est isolée dans le groupe « Sous-traitance » : « Envoi en sous-traitance » et « Réception de sous-traitance ». L'ancien groupe « Opérations de production » et l'entrée technique « Marchandises en sous-traitance » (registre) sont retirés du menu — le rapport du même nom reste dans le panneau des rapports.
- Le groupe « Catalogues » devient « Normes » : les « Fiches technologiques » passent en tête du groupe, la nomenclature s'ouvre par trois sélections — « Produits finis », « Produits semi-finis », « Matières premières » ; l'« Équipement de production » passe dans « Voir aussi ».
- Le panneau « Créer » ne propose plus de créer une fabrication, un envoi ou une réception de sous-traitance, une nomenclature ou un équipement : la fabrication naît de l'expédition ou du poste de production, la réception se saisit sur la base de l'envoi. La création d'une fiche technologique reste.
- Nouveau rapport « Coût de revient des produits » dans la section « Production » : pour la période choisie, par produit — quantité, coût hors TVA, TVA incluse dans ce coût et coût unitaire, avec le détail par caractéristique et par document de fabrication. Les données viennent de la comptabilité — de l'entrée en stock — et ne sont pas recalculées. Les produits du sous-traitant y figurent au même titre que la fabrication propre.
### en
- The "Production" section is rebuilt. The first list now holds "Production workstation", "Customer production orders" and "Production output" — output is no longer hidden one level down.
- Subcontracting is separated into the "Subcontracting" group: "Send to subcontractor" and "Receipt from subcontractor". The former "Production operations" group and the technical "Goods at subcontractor" entry (a register) are removed from the menu — the report of the same name stays in the reports panel.
- The "Reference books" group becomes "Standards": "Bills of materials" move to the top of the group, the item list opens through three filters — "Finished products", "Semi-finished products", "Raw materials"; "Production equipment" moves to "See also".
- The "Create" panel no longer offers creating a production output, a send or receipt of subcontracting, an item or equipment: output is created by auto-output on shipment or from the workstation, and a receipt is entered based on the send. Creating a bill of materials stays.
- A new "Product cost" report in the "Production" section: for the chosen period, per product — quantity, cost excluding VAT, the VAT inside that cost and the unit cost, broken down by characteristic and output document. The figures come from the accounting data — from the goods receipt — and are not recalculated. Subcontractor products are included alongside own output.
### es
- La sección «Producción» se ha reorganizado. La primera lista contiene ahora «Puesto de producción», «Pedidos de clientes para producción» y «Fabricación»: la fabricación ya no queda escondida un nivel más abajo.
- La subcontratación se separa en el grupo «Subcontratación»: «Envío a subcontratación» y «Recepción de subcontratación». El antiguo grupo «Operaciones de producción» y la entrada técnica «Mercancías en subcontratación» (registro) se retiran del menú; el informe del mismo nombre permanece en el panel de informes.
- El grupo «Manuales» pasa a ser «Normas»: las «Fichas tecnológicas» encabezan el grupo, la nomenclatura se abre con tres filtros — «Productos terminados», «Productos semielaborados», «Materias primas»; el «Equipo de producción» pasa a «Véase también».
- El panel «Crear» ya no permite crear una fabricación, un envío o una recepción de subcontratación, una nomenclatura o un equipo: la fabricación nace del envío o del puesto de producción y la recepción se registra sobre la base del envío. Se mantiene la creación de la ficha tecnológica.
- Nuevo informe «Coste de los productos» en la sección «Producción»: para el período elegido, por cada producto — cantidad, coste sin IVA, el IVA incluido en ese coste y el coste unitario, con desglose por característica y documento de fabricación. Los datos proceden de la contabilidad — de la entrada de mercancías — y no se recalculan. Los productos del subcontratista figuran junto con la fabricación propia.

## 2.0.15.35
### ru
- Рабочее место производства: в заголовке каждой нижней закладки показывается число строк — «Поступления (3)», «Переработка (0)».
- Кнопки ввода на основании переехали в командную панель своей закладки: «Заказ поставщику» — над «Заказами поставщику», «Поступление» — над «Поступлениями», «Выпуск по заказу» — над «Выпуском», «Отгрузка» — над «Отгрузками», «Передача в переработку» — над «Переработкой». Кнопка появляется, когда выбран ровно один заказ на производство, по которому разрешён ввод на основании. Над верхними таблицами остались «Статус» и «Потребности».
- Колонки строк документов получили постоянную ширину: «Поступления» помещаются в ширину экрана, колонка «Статус» больше не занимает половину таблицы.
- На закладке «Документы» две новые колонки — «Продукция» и «Материалы». В них движение документа со знаком: приход зелёным, расход красным; в подвале таблицы итог «поступило − списано = остаток». Движение показывают только проведённые непомеченные документы, количество берётся по документу целиком, поэтому документ со строками других заказов попадает в итог полностью.
- В подсказке индикатора к процентам добавились количества: по заказу — сколько материалов пришло и сколько ожидается; по документам заказа целиком — сколько материалов списано, сколько продукции пришло и отгружено. Легенда кружков и цифры открываются значком подсказки у заголовка колонки «Индикатор».
### fr
- Poste de production : l'en-tête de chaque onglet du bas affiche le nombre de lignes — « Réceptions (3) », « Sous-traitance (0) ».
- Les boutons de saisie sur la base ont rejoint la barre de commandes de leur onglet : « Commande fournisseur » au-dessus des « Commandes fournisseur », « Réception » au-dessus des « Réceptions », « Production par commande » au-dessus de « Production », « Expédition » au-dessus des « Expéditions », « Envoi en sous-traitance » au-dessus de « Sous-traitance ». Le bouton apparaît quand une seule commande en production autorisant la saisie sur la base est choisie. Au-dessus des tableaux du haut restent « Statut » et « Besoins ».
- Les colonnes des lignes de documents ont une largeur fixe : les « Réceptions » tiennent dans la largeur de l'écran et la colonne « Statut » ne prend plus la moitié du tableau.
- L'onglet « Documents » reçoit deux colonnes — « Produits » et « Matières ». Elles portent le mouvement du document avec son signe : entrée en vert, sortie en rouge ; le pied du tableau donne le total « entré − sorti = reste ». Seuls les documents validés et non marqués comptent, et la quantité est celle du document entier : un document contenant des lignes d'autres commandes y entre en totalité.
- L'infobulle de l'indicateur ajoute les quantités aux pourcentages : pour la commande — matières reçues et attendues ; pour les documents de la commande en entier — matières sorties, produits entrés et expédiés. La légende des pastilles et les chiffres s'ouvrent par l'icône d'infobulle près de l'en-tête de la colonne « Indicateur ».
### en
- Production workstation: the header of every bottom tab shows the number of rows — "Receipts (3)", "Subcontracting (0)".
- The based-on buttons moved to the command bar of their own tab: "Supplier order" above "Supplier orders", "Receipt" above "Receipts", "Output by order" above "Output", "Shipment" above "Shipments", "Send to subcontractor" above "Subcontracting". A button appears when exactly one production order that allows based-on entry is chosen. "Status" and "Requirements" stay above the upper tables.
- Document line columns got a fixed width: "Receipts" now fit the screen width and the "Status" column no longer takes half the table.
- The "Documents" tab gets two new columns — "Products" and "Materials". They show the document's movement with its sign: receipts in green, write-offs in red; the table footer gives the total "received − written off = balance". Only posted and unmarked documents count, and the quantity is that of the whole document, so a document with lines of other orders enters the total in full.
- The indicator tooltip now adds quantities to the percentages: for the order — materials received and expected; for the whole documents of the order — materials written off, products received and shipped. The circle legend and the figures open from the tooltip icon next to the "Indicator" column header.
### es
- Puesto de producción: el título de cada pestaña inferior muestra el número de líneas — «Recepciones (3)», «Subcontratación (0)».
- Los botones de entrada sobre la base se han trasladado a la barra de comandos de su pestaña: «Pedido a proveedor» sobre «Pedidos a proveedor», «Recepción» sobre «Recepciones», «Producción por pedido» sobre «Producción», «Envío» sobre «Envíos», «Envío a subcontratista» sobre «Subcontratación». El botón aparece cuando hay elegido exactamente un pedido para producción que admite la entrada sobre la base. Sobre las tablas superiores quedan «Estado» y «Necesidades».
- Las columnas de las líneas de documentos tienen ancho fijo: las «Recepciones» caben en el ancho de la pantalla y la columna «Estado» ya no ocupa media tabla.
- La pestaña «Documentos» recibe dos columnas nuevas: «Productos» y «Materiales». Muestran el movimiento del documento con su signo: la entrada en verde, la salida en rojo; el pie de la tabla da el total «entrado − dado de baja = resto». Solo cuentan los documentos contabilizados y no marcados, y la cantidad es la del documento completo, así que un documento con líneas de otros pedidos entra entero en el total.
- La ayuda del indicador añade cantidades a los porcentajes: del pedido — materiales recibidos y esperados; de los documentos del pedido completos — materiales dados de baja, productos entrados y enviados. La leyenda de los círculos y las cifras se abren con el icono de ayuda junto al título de la columna «Indicador».

## 2.0.15.34
### ru
- Рабочее место производства: новая нижняя закладка «Переработка» — строки сырья передач в переработку выбранного заказа на производство. Введённая строка создаёт или меняет передачу и проводит новую и проведённую; новая передача сразу получает ожидаемую продукцию заказа. Переработчиком выбирается только контрагент с признаком «Субподрядчик», количество по умолчанию — потребность материала.
- Кнопка «Поступление из переработки» над таблицей (при отметке строк одной проведённой передачи) открывает поступление на основании передачи. Продукция в нём заполняется остатком: ожидаемая минус уже поступившая по этой передаче, но не больше, чем заказу осталось выпустить.
- Если по партиям передачи уже поступала продукция, передача в рабочем месте не меняется: строки не добавляются, не правятся и не удаляются, «В черновик» и «Отменить» отклоняются — недостающее сырьё оформляется новой передачей. У передачи с поступлениями в форме документа нельзя сменить заказ и переработчика.
- Продукция, поступившая из переработки по заказу, теперь считается выпущенной: она входит в долю выпуска и стадию заказа, в количества «Выпуск по заказу» и в расчёт выпуска при отгрузке — отгрузка в пределах поступившего не выпускает продукцию второй раз. Стадия уже существующих заказов с такими поступлениями пересчитается при следующей записи любого документа заказа; если перепровести их старую отгрузку, её выпуск при отгрузке уменьшится на поступившее от переработчика.
- Оператору производства на начальной странице открывается рабочее место производства вместо панели показателей.
- Стоимость услуг переработчика в поступлении вносит пользователь с правом видеть суммы.
### fr
- Poste de production : nouvel onglet du bas « Sous-traitance » — les lignes de matières des transferts en sous-traitance de la commande en production sélectionnée. Une ligne saisie crée ou modifie le transfert et valide un transfert nouveau ou déjà validé ; un nouveau transfert reçoit aussitôt les produits attendus de la commande. Seul un partenaire marqué « Sous-traitant » peut être choisi, la quantité par défaut est le besoin en matière.
- Le bouton « Réception de sous-traitance » au-dessus du tableau (lignes cochées d'un seul transfert validé) ouvre la réception à partir du transfert. Les produits y sont remplis par le reste : attendus moins déjà reçus pour ce transfert, sans dépasser ce qui reste à produire pour la commande.
- Si des produits ont déjà été reçus sur les lots du transfert, celui-ci ne change plus dans le poste : les lignes ne s'ajoutent, ne changent ni ne se suppriment, « En brouillon » et « Annuler » sont refusés — la matière manquante passe par un nouveau transfert. Dans le document, la commande et le sous-traitant d'un transfert ayant des réceptions ne peuvent plus changer.
- Les produits reçus de sous-traitance pour une commande comptent désormais comme produits : ils entrent dans la part de production et l'étape de la commande, dans les quantités de « Production par commande » et dans le calcul de production à l'expédition — une expédition dans la limite du reçu ne produit pas une seconde fois. L'étape des commandes existantes ayant de telles réceptions sera recalculée au prochain enregistrement d'un document de la commande ; si leur ancienne expédition est revalidée, sa production automatique diminuera du reçu du sous-traitant.
- L'opérateur de production voit le poste de production sur la page d'accueil à la place du tableau de bord.
- Le coût des services du sous-traitant dans la réception est saisi par un utilisateur autorisé à voir les montants.
### en
- Production workstation: new bottom tab "Subcontracting" — raw material lines of the subcontracting transfers of the selected production order. An entered line creates or changes the transfer and posts a new or already posted one; a new transfer immediately gets the order's expected products. Only a counterparty flagged "Subcontractor" can be selected as processor; the default quantity is the material requirement.
- The "Subcontracting receipt" button above the table (lines of one posted transfer ticked) opens a receipt based on the transfer. Its products are filled with the remainder: expected minus already received for this transfer, but no more than the order still has to produce.
- If products have already been received against the transfer batches, the transfer no longer changes in the workstation: lines cannot be added, changed or deleted, and "To draft" and "Cancel" are refused — missing material goes in a new transfer. In the document form, the order and processor of a transfer with receipts cannot change.
- Products received from subcontracting for an order now count as produced: they are included in the order's output share and stage, in "Output by order" quantities and in output-on-shipment — shipping within the received quantity does not produce a second time. The stage of existing orders with such receipts is recalculated on the next save of any document of the order; if their old shipment is reposted, its automatic output decreases by what the processor delivered.
- The production operator's home page shows the production workstation instead of the dashboard.
- The processor's service cost in the receipt is entered by a user allowed to see amounts.
### es
- Puesto de producción: nueva pestaña inferior «Subcontratación» — las líneas de materias primas de los envíos a subcontratista del pedido para producción seleccionado. Una línea introducida crea o modifica el envío y contabiliza uno nuevo o ya contabilizado; un envío nuevo recibe al momento los productos esperados del pedido. Solo se puede elegir como procesador una contraparte marcada «Subcontratista»; la cantidad por defecto es la necesidad del material.
- El botón «Recepción de subcontratación» sobre la tabla (líneas marcadas de un solo envío contabilizado) abre la recepción a partir del envío. Sus productos se rellenan con el resto: esperados menos ya recibidos por ese envío, sin superar lo que falta por producir del pedido.
- Si ya se recibieron productos contra los lotes del envío, este ya no cambia en el puesto: las líneas no se añaden, ni cambian, ni se eliminan, y «A borrador» y «Cancelar» se rechazan — el material que falta va en un envío nuevo. En el documento, el pedido y el procesador de un envío con recepciones ya no pueden cambiar.
- Los productos recibidos de subcontratación para un pedido cuentan ahora como producidos: entran en la parte de producción y la etapa del pedido, en las cantidades de «Producción por pedido» y en el cálculo de producción al enviar — un envío dentro de lo recibido no produce por segunda vez. La etapa de los pedidos existentes con esas recepciones se recalculará al guardar de nuevo cualquier documento del pedido; si se vuelve a contabilizar su envío antiguo, su producción automática disminuirá en lo recibido del subcontratista.
- El operador de producción ve en la página inicial el puesto de producción en lugar del panel de indicadores.
- El coste de servicios del subcontratista en la recepción lo introduce un usuario autorizado a ver importes.

## 2.0.15.33
### ru
- Рабочее место производства: новая нижняя закладка «Выпуск» — строки ручных выпусков выбранного заказа на производство и автовыпусков его отгрузок. Введённая строка создаёт или меняет выпуск; новый и проведённый выпуск сразу проводится, черновик остаётся черновиком; материалы заполняются по технологической карте на дату выпуска, шапка документа повторяет первую строку. Кнопка выбора в колонке «Продукция» предлагает продукцию заказа с количеством, которое осталось выпустить.
- Новая нижняя закладка «Отгрузки» — строки реализаций заказа. Новая реализация берёт клиента, договор и режим НДС из заказа, строка — цену, ставку НДС и скидку из строки заказа с той же продукцией; пользователь с правом видеть суммы может изменить цену. При проведении реализация сама выпускает недостающую продукцию (колонка «Автовыпуск»); если провести не удалось, например не хватает материалов, новая реализация сохраняется черновиком с причиной.
- «Статус» и удаление строк работают как на закладках закупок. Автовыпуски только для просмотра: они меняются вместе со своей реализацией. Если после реализации проведён ручной выпуск по заказу, новую строку отгрузки введите в новую реализацию, а эту правьте в форме документа; выпуск, после которого уже проведена отгрузка, так же правится в форме, а продукция добавляется новым выпуском.
- В форме документа правятся: выпуски с сериями, партиями или услугами в материалах, с материалами, изменёнными вручную, и продукция без технологической карты; реализации с услугами, доп. расходами, зачётом авансов, кассовой сменой или налоговой накладной; строки с сериями. Если выпущено больше заказанного, строка записывается с предупреждением.
- Кнопка «Выпуск по заказу» в панели над таблицами «Заказы» и «Продукция» (при отметке строки) и ввод на основании заказа на производство: новый выпуск сразу заполнен продукцией, которую осталось выпустить, и материалами по картам.
- Прайс поставщиков: поступление без цены больше не записывает нулевую цену — раньше она перекрывала цены того же товара у других поставщиков.
### fr
- Poste de production : nouvel onglet du bas « Production » — les lignes des productions manuelles de la commande en production sélectionnée et des productions automatiques de ses expéditions. Une ligne saisie crée ou modifie la production ; une production nouvelle ou validée est validée aussitôt, un brouillon reste brouillon ; les matières sont remplies selon la fiche technique à la date de production, l'en-tête reprend la première ligne. Le bouton de choix de la colonne « Produit » propose les produits de la commande avec la quantité restant à produire.
- Nouvel onglet du bas « Expéditions » — les lignes des ventes de la commande. Une nouvelle vente reprend le client, le contrat et le mode TVA de la commande, et la ligne le prix, le taux de TVA et la remise de la ligne de commande du même produit ; un utilisateur autorisé à voir les montants peut modifier le prix. À la validation, la vente produit elle-même les produits manquants (colonne « Production automatique ») ; si la validation échoue, par exemple faute de matières, la nouvelle vente est enregistrée en brouillon avec la raison.
- « Statut » et la suppression de lignes fonctionnent comme sur les onglets d'achats. Les productions automatiques sont en lecture seule : elles changent avec leur vente. Si une production manuelle de la commande a été validée après une vente, saisissez la nouvelle ligne d'expédition dans une nouvelle vente et modifiez celle-ci dans le document ; de même, une production suivie d'une expédition validée se modifie dans le document et les produits s'ajoutent par une nouvelle production.
- Se modifient dans le document : les productions avec séries, lots ou services dans les matières, avec matières modifiées à la main, et les produits sans fiche technique ; les ventes avec services, frais annexes, imputation d'avances, journée de caisse ou facture fiscale ; les lignes avec séries. Si la production dépasse la quantité commandée, la ligne est enregistrée avec un avertissement.
- Bouton « Production par commande » dans la barre au-dessus des tableaux « Commandes » et « Produit » (ligne cochée) et saisie à partir de la commande en production : la nouvelle production est déjà remplie des produits restant à produire et des matières selon les fiches.
- Tarifs fournisseurs : une réception sans prix n'enregistre plus de prix nul — il masquait auparavant les prix du même article chez les autres fournisseurs.
### en
- Production workstation: new bottom tab "Output" — lines of the manual outputs of the selected production order and of the automatic outputs of its shipments. An entered line creates or changes the output; a new or posted output is posted immediately, a draft stays a draft; materials are filled from the routing card on the output date, and the document header repeats the first line. The choice button in the "Product" column offers the order products with the quantity still to be produced.
- New bottom tab "Shipments" — lines of the order's sales. A new sale takes the customer, contract and VAT mode from the order, and the line takes the price, VAT rate and discount from the order line with the same product; a user allowed to see amounts can change the price. On posting, the sale produces the missing products itself ("Automatic output" column); if posting fails, for example for lack of materials, the new sale is saved as a draft with the reason.
- "Status" and line deletion work as on the purchase tabs. Automatic outputs are read-only: they change together with their sale. If a manual output of the order was posted after a sale, enter the new shipment line in a new sale and edit that one in its document form; likewise, an output followed by a posted shipment is edited in its form and products are added with a new output.
- Edited in the document form: outputs with series, batches or services in materials, with manually changed materials, and products without a routing card; sales with services, additional costs, advance offsets, a checkout day or a tax invoice; lines with series. If more is produced than ordered, the line is saved with a warning.
- "Output by order" button in the bar above the "Orders" and "Production" tables (with a row ticked) and entry based on a production order: the new output is already filled with the products still to be produced and materials from the routing cards.
- Supplier prices: a receipt without a price no longer records a zero price — it used to override prices of the same item from other suppliers.
### es
- Puesto de producción: nueva pestaña inferior «Producción» — las líneas de las producciones manuales del pedido para producción seleccionado y de las producciones automáticas de sus envíos. Una línea introducida crea o modifica la producción; una producción nueva o contabilizada se contabiliza al momento y un borrador sigue siendo borrador; los materiales se rellenan según la ficha técnica en la fecha de producción y la cabecera repite la primera línea. El botón de selección de la columna «Producto» ofrece los productos del pedido con la cantidad que falta por producir.
- Nueva pestaña inferior «Envíos» — las líneas de las ventas del pedido. Una venta nueva toma el cliente, el contrato y el modo de IVA del pedido, y la línea el precio, el tipo de IVA y el descuento de la línea del pedido con el mismo producto; un usuario autorizado a ver importes puede cambiar el precio. Al contabilizarse, la venta produce ella misma los productos que faltan (columna «Producción automática»); si no se puede contabilizar, por ejemplo por falta de materiales, la venta nueva se guarda como borrador con el motivo.
- «Estado» y la eliminación de líneas funcionan como en las pestañas de compras. Las producciones automáticas son de solo lectura: cambian con su venta. Si una producción manual del pedido se contabilizó después de una venta, introduzca la nueva línea de envío en una venta nueva y edite esa en el documento; del mismo modo, una producción seguida de un envío contabilizado se edita en el documento y los productos se añaden con una producción nueva.
- Se editan en el documento: producciones con series, lotes o servicios en los materiales, con materiales cambiados a mano, y productos sin ficha técnica; ventas con servicios, gastos adicionales, compensación de anticipos, cambio de caja o factura fiscal; líneas con series. Si se produce más de lo pedido, la línea se guarda con un aviso.
- Botón «Producción por pedido» en la barra sobre las tablas «Pedidos» y «Producto» (con una línea marcada) e introducción a partir del pedido para producción: la producción nueva ya viene rellenada con los productos que faltan por producir y los materiales según las fichas.
- Precios de proveedores: una recepción sin precio ya no registra un precio cero — antes ocultaba los precios del mismo artículo de otros proveedores.

## 2.0.15.32
### ru
- Рабочее место производства: новые нижние закладки «Заказы поставщику» и «Поступления» — строки документов выбранного заказа на производство вводятся прямо в таблице. После ввода строки документ создаётся или меняется и сразу проводится. Если новый документ провести не удалось, он сохраняется черновиком, а причина выводится сообщением и в статусе строки.
- Новая строка попадает в документ ближайшей строки того же поставщика; колонка «Документ» предлагает документы этого заказа за сегодня или «Новый документ» — в документ прошлых дней новая строка не добавляется. В поступлении колонка «Заказ поставщику» выбирает строку заказа поставщику с остатком к поступлению: материал и количество подставляются, а приход засчитывается нужному изделию; если у поставщика есть незакрытая строка заказа по материалу, её нужно выбрать. Номер и дата накладной поставщика вводятся в строке.
- Удаление строк убирает их из документа; документ без строк помечается на удаление. Кнопка «Статус» над таблицами (при отметке строк) проводит документы, возвращает их в черновик или помечает на удаление. Правка строки черновика его не проводит.
- Строки с сериями, а также поступления с услугами, доп. расходами, зачётом авансов или завершённые правятся в форме документа — она открывается двойным щелчком по статусу строки. Строку заказа поставщику, по которой уже есть поступления, нельзя удалить, сменить в ней материал или уменьшить количество ниже поступившего, а сам заказ — вернуть в черновик или отменить.
- Оператор производства вводит поступления; заказы поставщику у него только для просмотра — права ролей не менялись.
### fr
- Poste de production : nouveaux onglets du bas « Commandes fournisseur » et « Réceptions » — les lignes des documents de la commande en production sélectionnée se saisissent directement dans le tableau. Après la saisie d'une ligne, le document est créé ou modifié et validé aussitôt. Si un nouveau document ne peut pas être validé, il est enregistré en brouillon et la raison s'affiche dans un message et dans le statut de la ligne.
- Une nouvelle ligne rejoint le document de la ligne la plus proche du même fournisseur ; la colonne « Document » propose les documents de cette commande du jour ou « Nouveau document » — une nouvelle ligne ne s'ajoute pas à un document d'un jour précédent. Dans une réception, la colonne « Commande fournisseur » choisit une ligne de commande fournisseur restant à recevoir : la matière et la quantité sont reprises et l'entrée est imputée au bon produit ; si le fournisseur a une ligne de commande ouverte pour la matière, il faut la choisir. Le numéro et la date du bon du fournisseur se saisissent dans la ligne.
- La suppression de lignes les retire du document ; un document sans lignes est marqué pour suppression. Le bouton « Statut » au-dessus des tableaux (lignes cochées) valide les documents, les remet en brouillon ou les marque pour suppression. Modifier une ligne d'un brouillon ne le valide pas.
- Les lignes avec séries et les réceptions avec services, frais annexes, imputation d'avances ou terminées se modifient dans le document, ouvert par un double clic sur le statut de la ligne. Une ligne de commande fournisseur ayant des réceptions ne peut pas être supprimée, changer de matière ni descendre sous la quantité reçue, et la commande ne peut pas être remise en brouillon ni annulée.
- L'opérateur de production saisit les réceptions ; les commandes fournisseur restent en lecture seule pour lui — les droits des rôles n'ont pas changé.
### en
- Production workstation: new bottom tabs "Supplier orders" and "Receipts" — lines of the documents of the selected production order are entered directly in the table. After a line is entered, the document is created or changed and posted immediately. If a new document cannot be posted, it is saved as a draft and the reason is shown in a message and in the line status.
- A new line goes to the document of the nearest line of the same supplier; the "Document" column offers today's documents of this order or "New document" — a new line is not added to a document from an earlier day. In a receipt, the "Supplier order" column selects a supplier order line still to be received: the material and quantity are filled in and the receipt is counted for the right product; if the supplier has an open order line for the material, it must be selected. The supplier invoice number and date are entered in the line.
- Deleting lines removes them from the document; a document without lines is marked for deletion. The "Status" button above the tables (with lines ticked) posts documents, returns them to draft or marks them for deletion. Editing a draft line does not post the draft.
- Lines with series and receipts with services, additional costs, advance offsets or completed are edited in the document form, opened by double-clicking the line status. A supplier order line with receipts cannot be deleted, change its material or go below the received quantity, and the order cannot be returned to draft or cancelled.
- The production operator enters receipts; supplier orders stay read-only for them — role rights did not change.
### es
- Puesto de producción: nuevas pestañas inferiores «Pedidos a proveedor» y «Recepciones»: las líneas de los documentos del pedido para producción seleccionado se introducen directamente en la tabla. Tras introducir una línea, el documento se crea o modifica y se contabiliza al momento. Si un documento nuevo no puede contabilizarse, se guarda como borrador y el motivo se muestra en un mensaje y en el estado de la línea.
- Una línea nueva va al documento de la línea más cercana del mismo proveedor; la columna «Documento» ofrece los documentos de este pedido de hoy o «Documento nuevo»: una línea nueva no se añade a un documento de días anteriores. En una recepción, la columna «Pedido a proveedor» elige una línea de pedido a proveedor pendiente de recibir: el material y la cantidad se rellenan y la entrada se asigna al producto correcto; si el proveedor tiene una línea de pedido abierta para el material, hay que elegirla. El número y la fecha del albarán del proveedor se introducen en la línea.
- Eliminar líneas las quita del documento; un documento sin líneas se marca para eliminar. El botón «Estado» sobre las tablas (con líneas marcadas) contabiliza documentos, los devuelve a borrador o los marca para eliminar. Editar una línea de un borrador no lo contabiliza.
- Las líneas con series y las recepciones con servicios, gastos adicionales, compensación de anticipos o terminadas se editan en el documento, que se abre con doble clic en el estado de la línea. Una línea de pedido a proveedor con recepciones no se puede eliminar, cambiar de material ni bajar de la cantidad recibida, y el pedido no se puede devolver a borrador ni cancelar.
- El operador de producción introduce recepciones; los pedidos a proveedor quedan en solo lectura para él: los derechos de los roles no han cambiado.

## 2.0.15.31
### ru
- Рабочее место производства: колонки процентов обеспечения, поступления, выпуска, отгрузки и оплаты убраны — индикатор показывает то же самое. Проценты текущего заказа и расшифровка кружков — во всплывающей подсказке колонки «Индикатор».
- Нижние закладки «Материалы» и «Документы» можно свернуть кнопкой на разделителе под таблицей заказов, тогда заказы занимают всё окно. Перетаскивать разделитель мышью платформа в таких формах не позволяет.
- Кнопки «Статус», «Заказ поставщику», «Поступление», «Передача в переработку», «Отгрузка» и «Потребности» появляются в панели над таблицей, когда строки отмечены флажком, — на закладках «Заказы» и «Продукция». Документ вводится на основании отмеченного заказа.
- На закладке «Продукция» статус, стадия и индикатор стоят первыми колонками, «Заказ на производство» — последней; новая строка добавляется в начало списка.
- В фильтрах «Клиент» и «Продукция» вводится текст: ищется часть наименования без учёта регистра.
- Мастер первого запуска: исправлена ошибка «Object field is not writable (Параметры)» при заполнении новой базы.
### fr
- Poste de production : les colonnes de pourcentage d'approvisionnement, de réception, de production, d'expédition et de paiement sont retirées — l'indicateur montre la même chose. Les pourcentages de la commande courante et la légende des cercles apparaissent dans l'info-bulle de la colonne « Indicateur ».
- Les onglets du bas « Matières » et « Documents » se réduisent avec le bouton du séparateur sous le tableau des commandes ; les commandes occupent alors toute la fenêtre. La plateforme ne permet pas de déplacer ce séparateur à la souris dans ce type de formulaire.
- Les boutons « Statut », « Commande fournisseur », « Réception », « Envoi en sous-traitance », « Expédition » et « Besoins » apparaissent dans la barre au-dessus du tableau lorsque des lignes sont cochées, sur les onglets « Commandes » et « Produit ». Le document est saisi à partir de la commande cochée.
- Sur l'onglet « Produit », le statut, l'étape et l'indicateur sont les premières colonnes et « Commande en production » la dernière ; une nouvelle ligne s'ajoute en haut de la liste.
- Les filtres « Client » et « Produit » acceptent du texte : la recherche porte sur une partie du nom, sans tenir compte de la casse.
- Assistant de premier démarrage : correction de l'erreur « Object field is not writable (Параметры) » lors du remplissage d'une nouvelle base.
### en
- Production workstation: the percentage columns for materials ordered, received, output, shipment and payment are removed — the indicator shows the same thing. The current order's percentages and the circle legend are in the tooltip of the "Indicator" column.
- The bottom "Materials" and "Documents" tabs can be collapsed with the button on the separator under the order table, so orders take the whole window. The platform does not allow dragging this separator with the mouse in such forms.
- The "Status", "Supplier order", "Receipt", "Send to subcontractor", "Shipment" and "Requirements" buttons appear in the bar above the table when rows are ticked, on the "Orders" and "Production" tabs. The document is created from the ticked order.
- On the "Production" tab, status, stage and indicator are the first columns and "Production order" is the last; a new line is added at the top of the list.
- The "Customer" and "Product" filters accept text: they search for part of the name, case-insensitive.
- First launch wizard: fixed the "Object field is not writable (Параметры)" error when filling a new database.
### es
- Puesto de producción: se quitan las columnas de porcentaje de abastecimiento, recepción, producción, envío y pago — el indicador muestra lo mismo. Los porcentajes del pedido actual y la leyenda de los círculos están en la información emergente de la columna «Indicador».
- Las pestañas inferiores «Materiales» y «Documentos» se contraen con el botón del separador bajo la tabla de pedidos; entonces los pedidos ocupan toda la ventana. La plataforma no permite arrastrar este separador con el ratón en este tipo de formularios.
- Los botones «Estado», «Pedido a proveedor», «Recepción», «Envío a subcontratista», «Envío» y «Necesidades» aparecen en la barra sobre la tabla al marcar filas, en las pestañas «Pedidos» y «Producción». El documento se crea a partir del pedido marcado.
- En la pestaña «Producción», estado, etapa e indicador son las primeras columnas y «Pedido para producción» la última; una línea nueva se añade al principio de la lista.
- Los filtros «Cliente» y «Producto» admiten texto: buscan una parte del nombre sin distinguir mayúsculas.
- Asistente de primer inicio: corregido el error «Object field is not writable (Параметры)» al rellenar una base nueva.

## 2.0.15.30
### ru
- Рабочее место производства: в списке заказов строки снова одинарной высоты — многострочный комментарий заказа раздувал все строки, колонка комментария убрана (комментарий виден в форме заказа).
- Заказы и нижние закладки «Материалы» и «Документы» помещаются на одном экране.
- Фильтры перенесены в панель справа, как в списках документов: переключатель «Производство / Все», клиент и продукция. Панель по умолчанию свёрнута, одни и те же фильтры действуют на закладки «Заказы» и «Продукция»; фильтр по продукции на «Заказах» отбирает заказы с этой продукцией в составе, на «Продукции» — её строки.
- На закладке «Продукция» видны те же сведения, что в списке заказов: стадия, индикатор, проценты обеспечения, поступления, выпуска, отгрузки и оплаты, дата отгрузки и менеджер.
- Кнопки «Заказ поставщику», «Поступление», «Передача в переработку», «Отгрузка» и «Потребности» перенесены с общей панели формы на панель над таблицей и появляются, когда выделен заказ на производство в работе.
### fr
- Poste de production : dans la liste des commandes, les lignes retrouvent une hauteur simple — un commentaire sur plusieurs lignes agrandissait toutes les lignes ; la colonne du commentaire est retirée (le commentaire reste visible dans la commande).
- Les commandes et les onglets du bas « Matières » et « Documents » tiennent sur un seul écran.
- Les filtres passent dans le panneau de droite, comme dans les listes de documents : sélecteur « Production / Toutes », client et produit. Le panneau est réduit par défaut et les mêmes filtres s'appliquent aux onglets « Commandes » et « Produit » ; le filtre produit retient sur « Commandes » les commandes contenant ce produit et sur « Produit » ses lignes.
- L'onglet « Produit » affiche les mêmes informations que la liste des commandes : étape, indicateur, pourcentages d'approvisionnement, de réception, de production, d'expédition et de paiement, date d'expédition et manager.
- Les boutons « Commande fournisseur », « Réception », « Envoi en sous-traitance », « Expédition » et « Besoins » quittent la barre générale du formulaire pour une barre au-dessus du tableau ; ils apparaissent lorsqu'une commande en production lancée est sélectionnée.
### en
- Production workstation: rows in the order list are single-height again — a multi-line order comment stretched every row; the comment column is removed (the comment is still visible in the order form).
- Orders and the bottom "Materials" and "Documents" tabs fit on one screen.
- Filters moved to the right panel, as in document lists: the "Production / All" switch, customer and product. The panel is collapsed by default, and the same filters apply to the "Orders" and "Production" tabs; the product filter keeps orders containing that product on "Orders" and its lines on "Production".
- The "Production" tab shows the same information as the order list: stage, indicator, percentages of materials ordered, received, output, shipment and payment, shipping date and manager.
- The "Supplier order", "Receipt", "Send to subcontractor", "Shipment" and "Requirements" buttons moved from the general form bar to a bar above the table and appear when a production order in progress is selected.
### es
- Puesto de producción: en la lista de pedidos las filas vuelven a tener altura simple — un comentario de varias líneas agrandaba todas las filas; se quita la columna del comentario (sigue visible en el pedido).
- Los pedidos y las pestañas inferiores «Materiales» y «Documentos» caben en una sola pantalla.
- Los filtros pasan al panel derecho, como en las listas de documentos: selector «Producción / Todos», cliente y producto. El panel está contraído por defecto y los mismos filtros actúan en las pestañas «Pedidos» y «Producción»; el filtro de producto deja en «Pedidos» los pedidos que contienen ese producto y en «Producción» sus líneas.
- La pestaña «Producción» muestra la misma información que la lista de pedidos: etapa, indicador, porcentajes de abastecimiento, recepción, producción, envío y pago, fecha de envío y gerente.
- Los botones «Pedido a proveedor», «Recepción», «Envío a subcontratista», «Envío» y «Necesidades» pasan de la barra general del formulario a una barra sobre la tabla y aparecen al seleccionar un pedido para producción en marcha.

## 2.0.15.29
### ru
- Рабочее место производства переделано: вверху две закладки — «Заказы» и «Продукция». На закладке «Заказы» по умолчанию видны заказы клиентов на производство, переключатель «Все заказы» показывает и продажи; выбор запоминается. У заказа видны стадия, индикатор и проценты обеспечения, поступления, выпуска, отгрузки и оплаты.
- На закладке «Продукция» заказ на производство вводится прямо в таблице, без открытия формы: укажите клиента, продукцию и количество — после окончания редактирования строки программа сама создаст заказ-черновик и заполнит материалы по технологической карте. Следующие строки того же клиента попадают в тот же черновик; в колонке «Заказ на производство» можно выбрать другой черновик клиента или «Новый заказ». Черновики в списке выбора подписаны номером, датой, клиентом и суммой (без права на суммы — количеством).
- Строки черновика правятся и удаляются прямо в таблице; черновик, у которого удалены все строки, помечается на удаление. Строки заказа в работе доступны только для просмотра. Если заказ тем временем изменил другой пользователь, таблица перечитывается и правку нужно повторить.
- Кнопка «Статус» действует на выделенные заказы: «В работу» проводит заказ, «В черновик» отменяет проведение, «Отменить» помечает на удаление. Стадия заказа по-прежнему считается автоматически по документам.
- Внизу рабочего места по текущему заказу видны закладки «Материалы» (состав, потребность, заказано, пришло, из остатка, дефицит и к поступлению) и «Документы» — вся цепочка заказа, включая поступления по заказам поставщику, возвраты из переработки и автоматические выпуски при отгрузке.
- Кнопки «Заказ поставщику», «Поступление», «Передача в переработку», «Отгрузка» создают документ на основании заказа в работе, кнопка «Потребности» открывает отчёт по этому заказу. Кнопки видны по правам пользователя.
### fr
- Le poste de production est refait : en haut, deux onglets « Commandes » et « Production ». L'onglet « Commandes » affiche par défaut les commandes clients en production ; le sélecteur « Toutes les commandes » affiche aussi les ventes, et le choix est mémorisé. Pour chaque commande sont visibles l'étape, l'indicateur et les pourcentages d'approvisionnement, de réception, de production, d'expédition et de paiement.
- Dans l'onglet « Production », la commande en production se saisit directement dans le tableau, sans ouvrir le formulaire : indiquez le client, le produit et la quantité — à la fin de la saisie de la ligne, le programme crée lui-même une commande brouillon et remplit les matières selon la gamme. Les lignes suivantes du même client vont dans le même brouillon ; la colonne « Commande en production » permet de choisir un autre brouillon du client ou « Nouvelle commande ». Les brouillons de la liste de choix sont libellés par numéro, date, client et montant (sans droit sur les montants — par quantité).
- Les lignes d'un brouillon se modifient et se suppriment directement dans le tableau ; un brouillon dont toutes les lignes sont supprimées est marqué pour suppression. Les lignes d'une commande lancée sont en lecture seule. Si un autre utilisateur a modifié la commande entre-temps, le tableau est relu et la modification doit être refaite.
- Le bouton « Statut » agit sur les commandes sélectionnées : « Lancer » valide la commande, « En brouillon » annule la validation, « Annuler » la marque pour suppression. L'étape de la commande reste calculée automatiquement d'après les documents.
- En bas du poste, pour la commande courante, les onglets « Matières » (composition, besoin, commandé, reçu, du stock, déficit et à recevoir) et « Documents » montrent toute la chaîne de la commande, y compris les réceptions sur commandes fournisseur, les retours de sous-traitance et les productions automatiques à l'expédition.
- Les boutons « Commande fournisseur », « Réception », « Envoi en sous-traitance » et « Expédition » créent le document à partir de la commande lancée ; le bouton « Besoins » ouvre le rapport de cette commande. Les boutons s'affichent selon les droits de l'utilisateur.
### en
- The production workstation is redesigned: at the top there are two tabs, "Orders" and "Production". The "Orders" tab shows customer production orders by default; the "All orders" switch also shows sales, and the choice is remembered. Each order shows its stage, indicator and the percentages of materials ordered, received, output, shipment and payment.
- On the "Production" tab a production order is entered right in the table, without opening the form: specify the customer, product and quantity — when you finish editing the line, the application creates a draft order and fills in materials from the production routing. Further lines of the same customer go to the same draft; in the "Production order" column you can pick another draft of the customer or "New order". Drafts in the choice list are labelled with number, date, customer and amount (quantity for users without access to amounts).
- Draft lines are edited and deleted right in the table; a draft with all lines deleted is marked for deletion. Lines of an order in progress are read-only. If another user changed the order in the meantime, the table is reloaded and the change has to be repeated.
- The "Status" button acts on the selected orders: "Start" posts the order, "To draft" undoes posting, "Cancel" marks it for deletion. The order stage is still calculated automatically from documents.
- At the bottom, for the current order, the "Materials" tab (composition, requirement, ordered, received, from stock, shortage and to receive) and the "Documents" tab show the whole order chain, including receipts on supplier orders, returns from subcontractors and automatic output on shipment.
- The "Supplier order", "Receipt", "Send to subcontractor" and "Shipment" buttons create a document based on the order in progress; the "Requirements" button opens the report for that order. Buttons are shown according to user rights.
### es
- El puesto de producción se ha rehecho: arriba hay dos pestañas, «Pedidos» y «Producción». La pestaña «Pedidos» muestra por defecto los pedidos de clientes para producción; el selector «Todos los pedidos» muestra también las ventas, y la elección se recuerda. Cada pedido muestra su etapa, el indicador y los porcentajes de abastecimiento, recepción, producción, envío y pago.
- En la pestaña «Producción» el pedido para producción se introduce directamente en la tabla, sin abrir el formulario: indique el cliente, el producto y la cantidad; al terminar de editar la línea, el programa crea un pedido borrador y rellena los materiales según la ruta de fabricación. Las siguientes líneas del mismo cliente van al mismo borrador; en la columna «Pedido para producción» se puede elegir otro borrador del cliente o «Pedido nuevo». Los borradores de la lista de selección se identifican por número, fecha, cliente e importe (sin derecho a importes, por cantidad).
- Las líneas de un borrador se editan y eliminan directamente en la tabla; un borrador sin líneas se marca para eliminar. Las líneas de un pedido en marcha son de solo lectura. Si otro usuario modificó el pedido entretanto, la tabla se relee y hay que repetir el cambio.
- El botón «Estado» actúa sobre los pedidos seleccionados: «Poner en marcha» contabiliza el pedido, «A borrador» anula la contabilización, «Cancelar» lo marca para eliminar. La etapa del pedido se sigue calculando automáticamente según los documentos.
- Abajo, para el pedido actual, las pestañas «Materiales» (composición, necesidad, pedido, recibido, del stock, déficit y por recibir) y «Documentos» muestran toda la cadena del pedido, incluidas las recepciones por pedidos a proveedor, las devoluciones de subcontratistas y la producción automática al enviar.
- Los botones «Pedido a proveedor», «Recepción», «Envío a subcontratista» y «Envío» crean el documento a partir del pedido en marcha; el botón «Necesidades» abre el informe de ese pedido. Los botones se muestran según los derechos del usuario.

## 2.0.15.28
### ru
- Реквизит «Автор» больше не используется: в документах и справочниках остаётся один реквизит «Ответственный». Поле «Автор» убрано с форм заказа клиента, коммерческого предложения и заявки на поиск товара и из списка заказов клиентов.
- При обновлении программа переносит заполненного автора в пустого ответственного у документов и справочников с реквизитом «Ответственный». Где ответственный уже указан, он не меняется. Записи, у которых автор не перенесён, перечислены в журнале регистрации (событие обновления программы).
- У проектов и шаблонов конфигураций появился реквизит «Ответственный» вместо «Автора»: при создании в него подставляется текущий пользователь.
- Запись документов оплаты при обновлении программы и при групповом изменении реквизитов больше не перепроводит связанные налоговые накладные.
### fr
- L'attribut « Auteur » n'est plus utilisé : les documents et les référentiels n'ont plus qu'un attribut « Responsable ». Le champ « Auteur » est retiré des formulaires de commande client, de devis et de demande de recherche d'article, ainsi que de la liste des commandes clients.
- Lors de la mise à jour, le programme reporte l'auteur renseigné dans le responsable vide des documents et référentiels qui ont un attribut « Responsable ». Un responsable déjà indiqué n'est pas modifié. Les enregistrements dont l'auteur n'est pas reporté sont listés dans le journal d'enregistrement (événement de mise à jour du programme).
- Les projets et modèles de configuration ont un attribut « Responsable » au lieu de l'« Auteur » : à la création, l'utilisateur courant y est renseigné.
- L'enregistrement des documents de paiement lors de la mise à jour du programme et de la modification groupée des attributs ne reporte plus les factures fiscales liées.
### en
- The "Author" attribute is no longer used: documents and catalogs keep a single "Person responsible" attribute. The "Author" field is removed from the customer order, commercial offer and item search request forms and from the customer order list.
- During the update, the application moves a filled author into an empty person responsible for documents and catalogs that have the "Person responsible" attribute. A person responsible that is already set is not changed. Records whose author was not moved are listed in the event log (application update event).
- Configuration projects and templates now have a "Person responsible" attribute instead of "Author": the current user is filled in on creation.
- Writing payment documents during the application update and during group attribute changes no longer reposts related tax invoices.
### es
- El atributo «Autor» ya no se usa: los documentos y catálogos conservan un único atributo «Responsable». El campo «Autor» se quita de los formularios de pedido de cliente, oferta comercial y solicitud de búsqueda de artículo, y de la lista de pedidos de clientes.
- Durante la actualización, el programa traslada el autor rellenado al responsable vacío de los documentos y catálogos que tienen el atributo «Responsable». Un responsable ya indicado no se cambia. Los registros cuyo autor no se trasladó se enumeran en el registro de eventos (evento de actualización del programa).
- Los proyectos y plantillas de configuración tienen un atributo «Responsable» en lugar de «Autor»: al crearlos se rellena con el usuario actual.
- La grabación de documentos de pago durante la actualización del programa y el cambio masivo de atributos ya no vuelve a contabilizar las facturas fiscales relacionadas.

## 2.0.15.27
### ru
- Исправлена ошибка «Метод объекта не обнаружен (Найти)» при открытии списка коммерческих предложений: список открывается, фильтры на правой панели работают.
- В выпуске продукции поле даты документа больше не растягивается на всю строку.
### fr
- Correction de l'erreur « Méthode de l'objet introuvable (Найти) » à l'ouverture de la liste des devis : la liste s'ouvre et les filtres du panneau droit fonctionnent.
- Dans la fabrication, le champ de date du document ne s'étire plus sur toute la ligne.
### en
- Fixed the "Object method not found (Найти)" error when opening the commercial offer list: the list opens and the right panel filters work.
- In production output, the document date field no longer stretches across the whole row.
### es
- Corregido el error «Método del objeto no encontrado (Найти)» al abrir la lista de ofertas comerciales: la lista se abre y los filtros del panel derecho funcionan.
- En la fabricación, el campo de fecha del documento ya no se estira a toda la fila.

## 2.0.15.26
### ru
- В поступлении товаров и услуг комментарий больше не обязателен для заполнения. В других документах обязательного комментария нет.
- В коммерческом предложении появилось меню «Создать на основании» с двумя пунктами: «Заказ клиента» создаёт заказ на продажу, «Заказ клиента на производство» — заказ с видом операции «Производство» и материалами по техкартам. Остальное в заказах одинаково. Те же две кнопки есть в списке коммерческих предложений. Вид заказа теперь выбирается командой, а не определяется по номенклатуре предложения.
- Описание в коммерческом предложении ведётся у каждой строки: выделите строку и допишите описание справа от таблицы. Описание строки не переносится в карточку номенклатуры, у двух строк одной номенклатуры могут быть разные описания. Новая строка получает описание из карточки, если в карточке включён вывод описания на печать. Печатная форма предложения выводит описание строки.
- Поля шапки: дата отгрузки в заказе клиента и коммерческом предложении, дата поставки в заказе поставщику, единица в выпуске продукции и валюта в поступлении больше не обрезаются; поле даты документа не растягивается на всю строку; комментарий технологической карты занимает три строки, а не всю высоту формы.
### fr
- Dans la réception de marchandises et services, le commentaire n'est plus obligatoire. Aucun autre document n'exige de commentaire.
- Le devis dispose d'un menu « Créer sur la base de » à deux entrées : « Commande client » crée une commande de vente, « Commande client en production » une commande de type « Production » avec les matières selon les gammes. Le reste des commandes est identique. Les deux mêmes boutons figurent dans la liste des devis. Le type de commande est désormais choisi par la commande et non déduit des articles du devis.
- La description dans le devis se saisit par ligne : sélectionnez la ligne et complétez la description à droite du tableau. La description de la ligne n'est plus reportée dans la fiche article, et deux lignes du même article peuvent avoir des descriptions différentes. Une nouvelle ligne reprend la description de la fiche si l'impression de la description y est activée. L'impression du devis affiche la description de la ligne.
- Champs d'en-tête : la date de livraison de la commande client et du devis, la date de réception de la commande fournisseur, l'unité de la fabrication et la devise de la réception ne sont plus tronquées ; le champ de date du document ne s'étire plus sur toute la ligne ; le commentaire de la gamme occupe trois lignes et non toute la hauteur du formulaire.
### en
- In the goods and services receipt, the comment is no longer required. No other document requires a comment.
- The commercial offer has a "Create based on" menu with two items: "Customer order" creates a sales order, "Customer production order" creates an order with the "Production" operation type and materials by routing. Otherwise the orders are the same. The same two buttons are in the commercial offer list. The order type is now chosen by the command rather than derived from the offer items.
- The description in a commercial offer is kept per row: select a row and write the description to the right of the table. The row description is no longer copied to the item card, and two rows of the same item may have different descriptions. A new row takes the description from the card if printing the description is enabled there. The offer print form shows the row description.
- Header fields: the shipping date in the customer order and commercial offer, the delivery date in the supplier order, the unit in production output and the currency in the goods receipt are no longer cut off; the document date field no longer stretches across the whole row; the production routing comment takes three lines instead of the full form height.
### es
- En la recepción de mercancías y servicios, el comentario ya no es obligatorio. Ningún otro documento exige comentario.
- La oferta comercial tiene un menú «Crear en base a» con dos opciones: «Pedido de cliente» crea un pedido de venta, «Pedido de cliente para producción», un pedido con el tipo de operación «Producción» y los materiales por ruta. El resto de los pedidos es igual. Los mismos dos botones están en la lista de ofertas comerciales. El tipo de pedido ahora se elige con el comando y no se deduce de los artículos de la oferta.
- La descripción en la oferta comercial se lleva por fila: seleccione la fila y escriba la descripción a la derecha de la tabla. La descripción de la fila ya no se copia a la ficha del artículo, y dos filas del mismo artículo pueden tener descripciones distintas. Una fila nueva toma la descripción de la ficha si allí está activada la impresión de la descripción. La impresión de la oferta muestra la descripción de la fila.
- Campos de la cabecera: la fecha de envío del pedido de cliente y de la oferta comercial, la fecha de entrega del pedido a proveedor, la unidad de la fabricación y la moneda de la recepción ya no se cortan; el campo de fecha del documento ya no se estira a toda la fila; el comentario de la ruta de fabricación ocupa tres líneas y no toda la altura del formulario.

## 2.0.15.25
### ru
- Формы заказа клиента, коммерческого предложения, заказа поставщику, поступления товаров, выпуска продукции и технологической карты разложены по закладкам: на первой закладке «Основное» — все реквизиты шапки, комментарий и ответственный, на следующих — табличные части с числом строк в заголовке. Материалы заказа на производство остаются на закладке товаров, рядом с продукцией.
- В шапке этих форм заголовок поля стоит слева от поля, а не над ним — форма стала компактнее.
- Исправлена ошибка «Поле не найдено» при выборе строки в списках выпусков продукции и актов разбора: панель «Детали» справа снова показывает сведения о документе. В той же панели у уценки товаров показывается новая цена, у поступления дополнительных расходов — сумма товара.
- Фильтры на правой панели списков: у двадцати видов документов без суммы (выпуск продукции, акт разбора, перемещение, списание, пересчёт товаров, установка цен и других) убран фильтр «Сумма», который приводил к ошибке и не давал отбирать список.
- Заказ, созданный на закладке «Коммерческие предложения» списка «Заказы клиентов на производство», сразу получает вид операции «Производство» и материалы по техкартам — даже если в предложении только закупаемые позиции.
- «Связанные документы» открываются и из выпуска продукции, а в дереве связей видны документы, введённые на основании выпуска и возврата поставщику.
- Форма выпуска продукции переведена на французский, английский и испанский: подписи полей, колонок и кнопка заполнения по техкарте. Заголовок формы документа («№ … от …: Проведён») показывается на языке пользователя.
### fr
- Les formulaires de commande client, de devis, de commande fournisseur, de réception, de fabrication et de gamme sont organisés en onglets : le premier onglet « Principal » regroupe tous les champs d'en-tête, le commentaire et le responsable, les suivants les tableaux avec le nombre de lignes dans le titre. Les matières d'une commande en production restent dans l'onglet des articles, à côté des produits.
- Dans l'en-tête de ces formulaires, le libellé du champ est à gauche du champ et non au-dessus — le formulaire est plus compact.
- Correction de l'erreur « Champ introuvable » à la sélection d'une ligne dans les listes de fabrications et d'actes de démontage : le panneau « Détails » affiche de nouveau les informations du document. Dans ce panneau, la dépréciation affiche le nouveau prix et la réception de frais supplémentaires le montant de l'article.
- Filtres du panneau droit des listes : pour vingt types de documents sans montant (fabrication, acte de démontage, transfert, sortie, inventaire, fixation des prix et autres), le filtre « Montant », qui provoquait une erreur et empêchait de filtrer la liste, est retiré.
- Une commande créée depuis l'onglet « Devis » de la liste « Commandes clients en production » reçoit directement le type d'opération « Production » et les matières selon les gammes — même si le devis ne contient que des articles achetés.
- « Documents liés » s'ouvre aussi depuis une fabrication, et l'arbre des liens montre les documents saisis sur la base d'une fabrication et d'un retour fournisseur.
- Le formulaire de fabrication est traduit en français, anglais et espagnol : libellés des champs, des colonnes et bouton de remplissage selon la gamme. Le titre du formulaire de document (« n° … du … : Reporté ») s'affiche dans la langue de l'utilisateur.
### en
- Customer order, commercial offer, supplier order, goods receipt, production output and production routing forms are arranged on tabs: the first "Main" tab holds all header fields, the comment and the person responsible; the following tabs hold the tables with the row count in the title. Production order materials stay on the goods tab next to the products.
- In the header of these forms, field titles are to the left of the field instead of above it — the form is more compact.
- Fixed the "Field not found" error when selecting a row in the production output and disassembly lists: the "Details" panel shows the document information again. In the same panel, a markdown shows the new price and an additional costs receipt shows the item amount.
- Filters on the right panel of lists: for twenty document types without an amount (production output, disassembly, transfer, write-off, stocktaking, price setting and others) the "Amount" filter, which caused an error and blocked filtering, is removed.
- An order created on the "Commercial offers" tab of the "Customer production orders" list gets the "Production" operation type and materials by routing right away — even if the offer holds only purchased items.
- "Related documents" also opens from a production output, and the link tree shows documents entered based on a production output and a supplier return.
- The production output form is translated into French, English and Spanish: field and column titles and the fill-by-routing button. The document form title ("No. … of …: Posted") is shown in the user's language.
### es
- Los formularios de pedido de cliente, oferta comercial, pedido a proveedor, recepción de mercancías, fabricación y ruta de fabricación se organizan en pestañas: la primera pestaña «Principal» reúne todos los campos de la cabecera, el comentario y el responsable; las siguientes, las tablas con el número de filas en el título. Los materiales de un pedido de producción siguen en la pestaña de artículos, junto a los productos.
- En la cabecera de estos formularios, el título del campo está a la izquierda del campo y no encima — el formulario es más compacto.
- Corregido el error «Campo no encontrado» al seleccionar una fila en las listas de fabricaciones y actas de desmontaje: el panel «Detalles» vuelve a mostrar la información del documento. En ese panel, la depreciación muestra el precio nuevo y la recepción de gastos adicionales, el importe del artículo.
- Filtros del panel derecho de las listas: en veinte tipos de documentos sin importe (fabricación, acta de desmontaje, traslado, baja, recuento, fijación de precios y otros) se quita el filtro «Importe», que provocaba un error e impedía filtrar la lista.
- Un pedido creado en la pestaña «Ofertas comerciales» de la lista «Pedidos de clientes para producción» recibe enseguida el tipo de operación «Producción» y los materiales por ruta, aunque la oferta solo tenga artículos comprados.
- «Documentos relacionados» también se abre desde una fabricación, y el árbol de vínculos muestra los documentos introducidos a partir de una fabricación y de una devolución a proveedor.
- El formulario de fabricación está traducido al francés, inglés y español: títulos de campos, columnas y el botón de relleno por ruta. El título del formulario del documento («n.º … del …: Contabilizado») se muestra en el idioma del usuario.

## 2.0.15.24
### ru
- Демо-данные для тестовой базы: команда `scripts/fixtures.sh --demo` заводит заказы клиента на производство по всем схемам — под заказ без своего остатка, из своего остатка материалов, ручной выпуск по заказу, изделие с составом в заказе, закупка пришла частично, материалы ещё не заказаны, черновик, частичная отгрузка, производство на склад и новая версия технологической карты — так, что в списке заказов видна каждая стадия от «Черновика» до «Выполнен».
- В тот же набор входят коммерческие предложения, заказы-продажи, договоры, лиды и заявки на поиск товара во всех статусах, закупки, реализации, возвраты и оплаты. Набор заводится одной транзакцией в текущем дне и повторно не дублируется. Только для тестовых баз.
- Встроенные автотесты: новый сценарий проверяет демо-набор — стадии и индикаторы заказов на производство, статусы продаж, предложений и договоров, автоматические выпуски.
### fr
- Données de démonstration pour la base de test : la commande `scripts/fixtures.sh --demo` crée des commandes client en production selon tous les schémas — sur commande sans stock propre, à partir du stock de matières, fabrication manuelle sur commande, article avec composition dans la commande, achat reçu en partie, matières pas encore commandées, brouillon, expédition partielle, production pour le stock et nouvelle version de gamme — de sorte que chaque étape, du « Brouillon » à « Terminée », apparaisse dans la liste des commandes.
- Le même jeu comprend des devis, des commandes de vente, des contrats, des leads et des demandes de recherche d'article dans tous les statuts, ainsi que des achats, des ventes, des retours et des paiements. Il est créé en une seule transaction sur la journée en cours et n'est pas dupliqué à la relance. Réservé aux bases de test.
- Tests automatiques intégrés : un nouveau scénario vérifie le jeu de démonstration — étapes et indicateurs des commandes en production, statuts des ventes, des devis et des contrats, fabrications automatiques.
### en
- Demo data for the test infobase: the `scripts/fixtures.sh --demo` command creates customer production orders for every scheme — made to order without own stock, from own material stock, manual output for an order, an item with its composition in the order, a partially received purchase, materials not yet ordered, a draft, a partial shipment, production to stock and a new routing version — so that every stage from "Draft" to "Completed" shows in the order list.
- The same set includes commercial offers, sales orders, contracts, leads and item search requests in every status, plus purchases, sales, returns and payments. It is created in one transaction within the current day and is not duplicated on a rerun. Test infobases only.
- Built-in automated tests: a new scenario checks the demo set — production order stages and indicators, sales, offer and contract statuses, automatic outputs.
### es
- Datos de demostración para la base de pruebas: el comando `scripts/fixtures.sh --demo` crea pedidos de cliente de producción según todos los esquemas — bajo pedido sin stock propio, desde el stock propio de materiales, fabricación manual por pedido, artículo con composición en el pedido, compra recibida en parte, materiales aún no pedidos, borrador, envío parcial, producción para stock y nueva versión de la ruta — de modo que cada etapa, del «Borrador» a «Completado», aparezca en la lista de pedidos.
- El mismo conjunto incluye ofertas comerciales, pedidos de venta, contratos, leads y solicitudes de búsqueda de artículos en todos los estados, además de compras, ventas, devoluciones y pagos. Se crea en una sola transacción dentro del día actual y no se duplica al volver a ejecutarlo. Solo para bases de prueba.
- Pruebas automáticas integradas: un nuevo escenario comprueba el conjunto de demostración — etapas e indicadores de los pedidos de producción, estados de ventas, ofertas y contratos, fabricaciones automáticas.

## 2.0.15.23
### ru
- Выпуск продукции: заполнение материалов по технологической карте — кнопкой «Заполнить техкарту» и при выборе продукции — выполняется одним обращением к серверу; раньше форма обращалась к серверу ещё и на каждую строку материалов. Из формы убран неработающий код прежней конфигурации (проверка веса, доли стоимости, подстановка цены закупки), остальное поведение формы не меняется.
- Выпуск продукции: над колонкой «Стоимость» в таблице материалов больше нет заголовка «Доля стоимости» — сама доля никогда не рассчитывалась. Колонки «Цена» и «Стоимость» остались на своих местах.
- Удалена константа «Упрощённый выпуск ГП»: она ни на что не влияла и в настройках не показывалась. После обновления база перестраивается.
- Предупреждение о необходимости перезаполнить выпуски при смене технологической карты — в карточке номенклатуры и при проведении заказа на производство — больше не учитывает выпуски, созданные автоматически при отгрузке: их перезаполняет перепроведение реализации.
- Встроенные автотесты: новый сценарий ручного выпуска — материалы по технологической карте на дату документа, одна и несколько позиций продукции, продукция без карты, предупреждение о выпусках без учёта автоматических.
### fr
- Fabrication : le remplissage des matières selon la gamme de fabrication — par le bouton du tableau des matières et au choix du produit — se fait en un seul appel au serveur ; auparavant, le formulaire appelait aussi le serveur pour chaque ligne de matières. Le code inopérant hérité de la configuration d'origine (contrôle du poids, parts de coût, prix d'achat proposé) est retiré, le reste du comportement du formulaire ne change pas.
- Fabrication : la colonne « Montant » du tableau des matières n'est plus regroupée sous un en-tête de part du coût — cette part n'a jamais été calculée. Les colonnes du prix et du montant restent à leur place.
- La constante « Fabrication simplifiée » est supprimée : elle n'avait aucun effet et n'apparaissait pas dans les paramètres. Après la mise à jour, la base est restructurée.
- L'avertissement invitant à remplir à nouveau les fabrications lors d'un changement de gamme — dans la fiche article et à la validation d'une commande en production — ne tient plus compte des fabrications créées automatiquement à l'expédition : la revalidation de la vente les remplit à nouveau.
- Tests automatiques intégrés : nouveau scénario de fabrication manuelle — matières selon la gamme à la date du document, un ou plusieurs produits, produit sans gamme, avertissement sur les fabrications sans les fabrications automatiques.
### en
- Production output: filling materials by production routing — with the button of the materials table and when choosing a product — takes a single server call; previously the form also called the server for every material line. Dead code inherited from the original configuration (weight check, cost shares, purchase price lookup) is removed; the rest of the form behaves as before.
- Production output: the cost column of the materials table is no longer grouped under a cost share header — the share was never calculated. The price and cost columns stay where they were.
- The "Simplified production output" constant is removed: it had no effect and was not shown in the settings. After the update, the infobase is restructured.
- The warning to refill production outputs when a production routing changes — in the item card and when posting a production order — no longer counts outputs created automatically on shipment: reposting the sale refills them.
- Built-in automated tests: a new manual production output scenario — materials by routing on the document date, one and several products, a product without a routing, and the output warning without automatic outputs.
### es
- Fabricación: el relleno de materiales según la ruta de fabricación — con el botón de la tabla de materiales y al elegir el producto — se hace con una sola llamada al servidor; antes el formulario llamaba además al servidor por cada línea de materiales. Se retira el código inoperante heredado de la configuración original (control de peso, partes del coste, precio de compra propuesto); el resto del formulario se comporta igual.
- Fabricación: la columna del coste en la tabla de materiales ya no se agrupa bajo un encabezado de parte del coste — esa parte nunca se calculó. Las columnas del precio y del coste siguen en su sitio.
- Se elimina la constante «Fabricación simplificada»: no tenía ningún efecto y no aparecía en los ajustes. Tras la actualización, la base se reestructura.
- El aviso de volver a rellenar las fabricaciones al cambiar la ruta de fabricación — en la ficha del artículo y al contabilizar un pedido de producción — ya no tiene en cuenta las fabricaciones creadas automáticamente al enviar: las rellena la recontabilización de la venta.
- Pruebas automáticas integradas: nuevo escenario de fabricación manual — materiales por ruta en la fecha del documento, uno y varios productos, producto sin ruta y aviso de fabricaciones sin las automáticas.

## 2.0.15.22
### ru
- Автоматический выпуск при отгрузке: если материалов не хватает, реализация снова отказывает с перечнем недостающего. В 2.0.15.21 вместо этого сообщения возникала ошибка, когда в ту же секунду по этим материалам были проведены другие документы.
- Встроенные автотесты: сценарий автовыпуска проверяет выпуск по техкарте на записанном заказе — проведённый заказ не пропускает продукцию со способом «Производство» без материалов.
### fr
- Fabrication automatique à l'expédition : en cas de matières insuffisantes, la vente est de nouveau refusée avec la liste de ce qui manque. En 2.0.15.21, une erreur apparaissait à la place de ce message lorsque d'autres documents avaient été validés sur ces matières dans la même seconde.
- Tests automatiques intégrés : le scénario de fabrication automatique vérifie la fabrication selon la gamme sur une commande enregistrée — une commande validée n'accepte pas un produit en mode « Production » sans matières.
### en
- Automatic production output on shipment: when materials are short, the sale is again refused with the list of what is missing. In 2.0.15.21, an error appeared instead of this message when other documents had been posted for these materials in the same second.
- Built-in automated tests: the automatic output scenario checks output by production routing on a saved order — a posted order does not accept a product with the "Production" method without materials.
### es
- Fabricación automática al enviar: si faltan materiales, la venta vuelve a rechazarse con la lista de lo que falta. En 2.0.15.21 aparecía un error en lugar de este mensaje cuando en el mismo segundo se habían contabilizado otros documentos con esos materiales.
- Pruebas automáticas integradas: el escenario de fabricación automática comprueba la fabricación según la ruta en un pedido guardado — un pedido contabilizado no admite un producto con el método «Producción» sin materiales.

## 2.0.15.21
### ru
- Автоматический выпуск при отгрузке. Проведение реализации по заказу клиента на производство само создаёт и проводит выпуск продукции на отгружаемое количество — на секунду раньше реализации, поэтому реализация списывает готовую продукцию по ФИФО уже с себестоимостью этого выпуска. На одну реализацию — один выпуск, одинаковые позиции сводятся в одну строку.
- Материалы автовыпуска берутся по составу заказа на отгружаемое количество, а продукция без материалов в заказе — по действующей технологической карте (со способом пополнения «Оба» или «Закупка» и без карты продукция не выпускается). Сначала списываются партии закупок под этот заказ, остальное — из общего остатка склада по ФИФО; взятое из общего остатка отмечается в потребностях заказа как «Из остатка» и учитывается в стадии «Восполнение потребности», в заполнении заказа поставщику по потребности и в поступлении на основании заказа.
- Уже выпущенная по заказу продукция — ручными выпусками и автовыпусками прежних реализаций — повторно не выпускается; выпуск не превышает заказанного. Если материалов на складе не хватает, реализация не проводится, а сообщение перечисляет недостающее.
- Отмена проведения реализации распроводит её автовыпуск, повторное проведение перезаполняет тот же выпуск, пометка удаления реализации переходит на автовыпуск. Автовыпуск открывается только для просмотра со ссылкой на реализацию и не меняется вручную; у ручного выпуска основанием выбирается только заказ.
- Включается переключателем «Автоматический выпуск при продаже» в настройках раздела «Производство». Внимание: при включённом переключателе перепроведение уже проведённых реализаций по заказам на производство тоже создаёт автовыпуски. Продажи и реализации без заказа на производство работают как раньше. Права ролей не менялись: реализацию с автовыпуском проводят все роли, которые проводят реализацию.
- После обновления база перестраивается: у выпуска продукции основанием теперь может быть реализация.
### fr
- Fabrication automatique à l'expédition. La validation d'une vente sur une commande client en production crée et valide elle-même la fabrication de la quantité expédiée — une seconde avant la vente, si bien que la vente consomme les produits finis en FIFO au coût de cette fabrication. Une vente donne une seule fabrication, les lignes identiques sont regroupées.
- Les matières de la fabrication automatique suivent la composition de la commande pour la quantité expédiée ; un produit sans matières dans la commande suit la gamme de fabrication en vigueur (avec le mode d'approvisionnement « Les deux » ou « Achat », ou sans gamme, le produit n'est pas fabriqué). Les lots achetés pour cette commande sont consommés d'abord, le reste vient du stock général en FIFO ; ce qui est pris dans le stock général est noté « Pris sur le stock » dans les besoins de la commande et compté dans l'étape « Approvisionnement des besoins », dans le remplissage de la commande fournisseur selon les besoins et dans la réception sur la commande.
- Les produits déjà fabriqués pour la commande — par des fabrications manuelles ou les fabrications automatiques de ventes précédentes — ne sont pas refabriqués ; la fabrication ne dépasse pas la quantité commandée. S'il manque des matières en stock, la vente n'est pas validée et le message liste ce qui manque.
- L'annulation de la validation de la vente annule sa fabrication automatique, une nouvelle validation remplit à nouveau la même fabrication, le marquage pour suppression de la vente passe à la fabrication. La fabrication automatique s'ouvre en lecture seule avec un lien vers la vente et ne se modifie pas manuellement ; pour une fabrication manuelle, seule une commande peut servir de base.
- Elle s'active par l'interrupteur « Fabrication automatique à la vente » dans les paramètres de la section « Production ». Attention : interrupteur activé, la revalidation de ventes déjà validées sur des commandes en production crée aussi des fabrications automatiques. Les ventes sans commande en production fonctionnent comme avant. Les droits des rôles n'ont pas changé : tous les rôles qui valident les ventes valident une vente avec fabrication automatique.
- Après la mise à jour, la base est restructurée : une fabrication peut désormais avoir une vente pour base.
### en
- Automatic production output on shipment. Posting a sale for a customer production order creates and posts the production output of the shipped quantity by itself — one second before the sale, so the sale consumes the finished goods in FIFO at the cost of that output. One sale gives one output; identical lines are combined.
- Materials of the automatic output follow the order composition for the shipped quantity; a product without materials in the order follows the current production routing (a product with the "Both" or "Purchase" replenishment method, or without a routing, is not produced). Batches purchased for this order are consumed first, the rest comes from general stock in FIFO; what is taken from general stock is recorded as "From stock" in the order requirements and counted in the Replenishing requirements stage, in filling a supplier order by requirements and in a receipt based on the order.
- Products already produced for the order — by manual outputs or by automatic outputs of earlier sales — are not produced again; the output never exceeds the ordered quantity. If materials are short in stock, the sale is not posted and the message lists what is missing.
- Unposting the sale unposts its automatic output, posting it again refills the same output, and the sale's deletion mark passes to the output. The automatic output opens read-only with a link to the sale and cannot be edited manually; a manual output can only be based on an order.
- It is enabled with the "Automatic production output on sale" switch in the Production section settings. Note: with the switch on, reposting sales already posted for production orders also creates automatic outputs. Sales without a production order work as before. Role rights are unchanged: every role that posts sales posts a sale with automatic output.
- After the update, the infobase is restructured: a production output can now be based on a sale.
### es
- Fabricación automática al enviar. Al contabilizar una venta de un pedido de cliente de producción se crea y contabiliza sola la fabricación de la cantidad enviada — un segundo antes de la venta, de modo que la venta consume los productos terminados en FIFO al coste de esa fabricación. Una venta genera una sola fabricación; las líneas iguales se agrupan.
- Los materiales de la fabricación automática siguen la composición del pedido para la cantidad enviada; un producto sin materiales en el pedido sigue la ruta de fabricación vigente (con el método de reposición «Ambos» o «Compra», o sin ruta, el producto no se fabrica). Primero se consumen los lotes comprados para este pedido y el resto sale del stock general en FIFO; lo tomado del stock general se anota como «De existencias» en las necesidades del pedido y se tiene en cuenta en la etapa «Reposición de necesidades», al rellenar el pedido a proveedor por necesidades y en la recepción sobre el pedido.
- Los productos ya fabricados para el pedido — con fabricaciones manuales o con fabricaciones automáticas de ventas anteriores — no se vuelven a fabricar; la fabricación no supera lo pedido. Si faltan materiales en stock, la venta no se contabiliza y el mensaje enumera lo que falta.
- Anular la contabilización de la venta anula su fabricación automática, volver a contabilizarla rellena la misma fabricación y la marca de eliminación de la venta pasa a la fabricación. La fabricación automática se abre en solo lectura con un enlace a la venta y no se modifica a mano; una fabricación manual solo puede basarse en un pedido.
- Se activa con el interruptor «Fabricación automática al vender» en los ajustes de la sección «Producción». Atención: con el interruptor activado, recontabilizar ventas ya contabilizadas de pedidos de producción también crea fabricaciones automáticas. Las ventas sin pedido de producción funcionan como antes. Los permisos de los roles no cambian: todos los roles que contabilizan ventas contabilizan una venta con fabricación automática.
- Tras la actualización, la base se reestructura: una fabricación ahora puede basarse en una venta.

## 2.0.15.20
### ru
- У заказа клиента на производство появилась стадия, которая меняется сама по мере работы с заказом: «Черновик», «Формируется потребность», «Заказ поставщику», «Восполнение потребности», «В производстве», «Ожидает отгрузки», «Ожидает оплаты», «Выполнен». Стадию пересчитывают запись и проведение заказа, заказы поставщику, поступления и возвраты поставщику, выпуски продукции, реализации, возвраты от покупателей и оплаты. Отмена проведения документа или возврат возвращают стадию назад.
- Если заказ уже отгружен или выпущен, ранние стадии не держат его: заказ, собранный из материалов со склада без закупки, переходит к отгрузке и оплате.
- Рядом со стадией показывается индикатор из пяти кружков — обеспечение материалами, поступление материалов, выпуск, отгрузка, оплата: ○ не начато, ◐ частично, ● полностью. Индикатор виден в шапке заказа (подсказка объясняет кружки), в колонке «Индикатор» списка заказов, в панели «Детали» и в АРМ производства.
- В списке заказов черновики и выполненные заказы выделяются цветом, заказы, ожидающие оплаты, — особым цветом; картинки отгрузки и оплаты учитывают стадии. Удалено неработающее оформление списка.
- Дашборд производства учитывает стадии: выполненные и ожидающие оплаты заказы считаются завершёнными, заказы на стадиях до выпуска — в производстве. В списке реализаций выполненные заказы и заказы, ожидающие оплаты, больше не попадают в «Заказы к отгрузке».
- Отменить проведение заказа на производство можно и при проведённых закупках под него: заказ становится черновиком, закупки остаются видны в отчёте «Потребности производства».
- Заказы на продажу работают как раньше. Существующие заказы стадию не получают, пока их или связанный документ не запишут снова. После обновления база перестраивается дольше обычного: добавлены индексы в реализации, выпуске продукции и возврате от покупателя.
- Роли кассы, склада, казначея, логиста, закупок, продаж и оператора, а также интернет-магазин и мобильный клиент получили право чтения истории статусов заказов клиента: форма заказа показывает стадию без ошибки прав.
### fr
- La commande client en production reçoit une étape qui évolue d'elle-même au fil du traitement : « Brouillon », « Besoins en préparation », « Commande fournisseur », « Approvisionnement des besoins », « En production », « En attente d'expédition », « En attente de paiement », « Terminée ». L'étape est recalculée à l'enregistrement et à la validation de la commande, des commandes fournisseur, des réceptions et retours fournisseur, des productions, des ventes, des retours clients et des paiements. L'annulation de la validation d'un document ou un retour ramène l'étape en arrière.
- Une commande déjà expédiée ou produite n'est plus retenue par les étapes précédentes : une commande fabriquée avec des matières en stock sans achat passe à l'expédition et au paiement.
- À côté de l'étape s'affiche un indicateur de cinq cercles — approvisionnement en matières, réception des matières, production, expédition, paiement : ○ non commencé, ◐ partiel, ● complet. Il apparaît dans l'en-tête de la commande (l'infobulle explique les cercles), dans la colonne « Indicateur » de la liste des commandes, dans le panneau « Détails » et dans le poste de travail de production.
- Dans la liste des commandes, les brouillons et les commandes terminées sont colorés, les commandes en attente de paiement ont une couleur spéciale ; les images d'expédition et de paiement tiennent compte des étapes. La mise en forme inopérante de la liste a été supprimée.
- Le tableau de bord de production tient compte des étapes : les commandes terminées et en attente de paiement sont comptées comme achevées, celles des étapes avant la production comme en production. Dans la liste des ventes, les commandes terminées ou en attente de paiement n'apparaissent plus dans « Commandes à expédier ».
- La validation d'une commande en production peut être annulée même si des achats validés y sont liés : la commande redevient un brouillon, les achats restent visibles dans le rapport « Besoins de production ».
- Les commandes de vente fonctionnent comme avant. Les commandes existantes ne reçoivent une étape qu'au prochain enregistrement de la commande ou d'un document lié. Après la mise à jour, la restructuration de la base est plus longue que d'habitude : des index sont ajoutés aux ventes, productions et retours clients.
- Les rôles caisse, entrepôt, trésorerie, logistique, achats, ventes et opérateur, ainsi que le commerce électronique et le client mobile, peuvent lire l'historique des statuts des commandes client : le formulaire de commande affiche l'étape sans erreur de droits.
### en
- A customer production order now has a stage that changes by itself as the order progresses: Draft, Requirements being defined, Supplier order, Replenishing requirements, In production, Awaiting shipment, Awaiting payment, Completed. The stage is recalculated when the order is saved or posted and by supplier orders, receipts and returns to suppliers, production releases, sales, customer returns and payments. Unposting a document or a return moves the stage back.
- An order that is already shipped or produced is no longer held by earlier stages: an order made from materials in stock without purchasing moves on to shipment and payment.
- Next to the stage, an indicator of five circles is shown — materials ordered, materials received, production, shipment, payment: ○ not started, ◐ partial, ● complete. It appears in the order header (the tooltip explains the circles), in the Indicator column of the order list, in the Details panel and in the production workplace.
- In the order list, drafts and completed orders are colored and orders awaiting payment use a special color; the shipment and payment pictures take stages into account. Broken formatting of the list has been removed.
- The production dashboard takes stages into account: completed orders and orders awaiting payment count as finished, orders at stages before production count as in production. In the sales list, completed orders and orders awaiting payment no longer appear under Orders to ship.
- A production order can be unposted even when posted purchases are linked to it: the order becomes a draft, and the purchases stay visible in the Production requirements report.
- Sales orders work as before. Existing orders get a stage only when the order or a related document is saved again. After the update, the infobase restructuring takes longer than usual: indexes are added to sales, production releases and customer returns.
- The cashier, warehouse, treasury, logistics, purchasing, sales and operator roles, as well as e-commerce and the mobile client, can read the customer order status history: the order form shows the stage without an access rights error.
### es
- El pedido de cliente para producción tiene ahora una etapa que cambia sola a medida que avanza el pedido: «Borrador», «Necesidades en preparación», «Pedido a proveedor», «Reposición de necesidades», «En producción», «Pendiente de envío», «Pendiente de pago», «Completado». La etapa se recalcula al guardar y contabilizar el pedido y con los pedidos a proveedor, recepciones y devoluciones a proveedor, producciones, ventas, devoluciones de clientes y pagos. Anular la contabilización de un documento o una devolución hace retroceder la etapa.
- Un pedido ya enviado o producido ya no queda retenido por las etapas anteriores: un pedido fabricado con materiales en stock sin compra pasa al envío y al pago.
- Junto a la etapa se muestra un indicador de cinco círculos — abastecimiento de materiales, recepción de materiales, producción, envío, pago: ○ sin empezar, ◐ parcial, ● completo. Aparece en la cabecera del pedido (la sugerencia explica los círculos), en la columna «Indicador» de la lista de pedidos, en el panel «Detalles» y en el puesto de trabajo de producción.
- En la lista de pedidos, los borradores y los pedidos completados se muestran en color y los pendientes de pago con un color especial; las imágenes de envío y pago tienen en cuenta las etapas. Se eliminó el formato que no funcionaba en la lista.
- El panel de producción tiene en cuenta las etapas: los pedidos completados y pendientes de pago cuentan como terminados, los de etapas anteriores a la producción como en producción. En la lista de ventas, los pedidos completados o pendientes de pago ya no aparecen en «Pedidos para enviar».
- Se puede anular la contabilización de un pedido para producción aunque tenga compras contabilizadas vinculadas: el pedido vuelve a ser borrador y las compras siguen visibles en el informe «Necesidades de producción».
- Los pedidos de venta funcionan como antes. Los pedidos existentes reciben una etapa solo cuando se vuelve a guardar el pedido o un documento vinculado. Tras la actualización, la reestructuración de la base tarda más de lo habitual: se añaden índices a las ventas, producciones y devoluciones de clientes.
- Los roles de caja, almacén, tesorería, logística, compras, ventas y operador, así como el comercio electrónico y el cliente móvil, pueden leer el historial de estados de los pedidos de cliente: el formulario del pedido muestra la etapa sin error de permisos.

## 2.0.15.19
### ru
- Встроенные автотесты: проверка отчёта «Потребности производства» не учитывает итоговую строку отчёта. Для пользователей ничего не меняется.
### fr
- Tests automatiques intégrés : la vérification du rapport « Besoins de production » ne tient plus compte de la ligne de total. Rien ne change pour les utilisateurs.
### en
- Built-in automated tests: the Production requirements report check no longer counts the report total line. Nothing changes for users.
### es
- Pruebas automáticas integradas: la comprobación del informe «Necesidades de producción» ya no cuenta la línea de total. Para los usuarios no cambia nada.

## 2.0.15.18
### ru
- Встроенные автотесты: проверка отчёта «Потребности производства» сверяет строки отчёта по продукции и материалам. Для пользователей ничего не меняется.
### fr
- Tests automatiques intégrés : la vérification du rapport « Besoins de production » compare les lignes du rapport par produit et matière. Rien ne change pour les utilisateurs.
### en
- Built-in automated tests: the Production requirements report check now compares report lines by product and material. Nothing changes for users.
### es
- Pruebas automáticas integradas: la comprobación del informe «Necesidades de producción» compara las líneas del informe por producto y material. Para los usuarios no cambia nada.

## 2.0.15.17
### ru
- Исправлены ошибки версии 2.0.15.15: заказ поставщику, поступление и возврат поставщику под заказ клиента на производство не проводились из-за ошибки в запросе потребностей, а запись проведённого заказа на производство без повторного проведения завершалась ошибкой.
### fr
- Correction d'erreurs de la version 2.0.15.15 : la commande au fournisseur, la réception et le retour au fournisseur liés à une commande client en production n'étaient pas validés à cause d'une erreur dans la requête des besoins, et l'enregistrement sans nouvelle validation d'une commande en production validée échouait.
### en
- Fixed errors of version 2.0.15.15: supplier orders, receipts and returns to suppliers for a customer production order could not be posted because of an error in the requirements query, and saving a posted production order without posting failed.
### es
- Se corrigieron errores de la versión 2.0.15.15: el pedido al proveedor, la recepción y la devolución al proveedor para un pedido de cliente para producción no se contabilizaban por un error en la consulta de necesidades, y guardar sin contabilizar un pedido para producción contabilizado terminaba con error.

## 2.0.15.16
### ru
- Исправлена ошибка, из-за которой обновление на версии 2.0.15.14 и 2.0.15.15 не загружалось в базу: кнопка «Записать и закрыть» в формах заказа клиента ссылалась на команду, которой у проводимого документа нет. Кнопка работает как прежде — у заказов на продажу она главная и записывает заказ с закрытием формы.
### fr
- Correction d'une erreur qui empêchait de charger dans la base les mises à jour 2.0.15.14 et 2.0.15.15 : le bouton d'enregistrement et fermeture des formulaires de commande client utilisait une commande inexistante pour un document validable. Le bouton fonctionne comme avant : sur les commandes de vente, il reste le bouton principal et enregistre la commande en fermant le formulaire.
### en
- Fixed an error that prevented updates 2.0.15.14 and 2.0.15.15 from loading into the infobase: the Save and close button of the customer order forms referred to a command that a postable document does not have. The button works as before: on sales orders it remains the main button and saves the order and closes the form.
### es
- Se corrigió un error que impedía cargar en la base las actualizaciones 2.0.15.14 y 2.0.15.15: el botón de guardar y cerrar de los formularios de pedido de cliente usaba un comando que no existe en un documento contabilizable. El botón funciona como antes: en los pedidos de venta sigue siendo el botón principal y guarda el pedido cerrando el formulario.

## 2.0.15.15
### ru
- Проведённый заказ клиента на производство формирует потребность в материалах: сколько каждого материала нужно под каждую продукцию заказа, в базовых единицах. Закупки под заказ отмечают, сколько материала заказано и сколько пришло.
- В заказе поставщику появилось поле «Заказ клиента» и кнопка «Заполнить по потребности» над товарами: строки заполняются недостающими материалами заказа клиента на производство — потребностью за вычетом уже заказанного. Заказ поставщику, введённый на основании заказа на производство, заполняется так же; если заказ клиента не проведён, ввод отклоняется с сообщением. Ввод на основании заказа на продажу работает как раньше.
- Продукция, под которую заказан материал, хранится в колонке «Продукция» заказа поставщику; её можно показать через «Ещё → Изменить форму». Если продукция не указана, количество распределяется по продукции в порядке строк заказа клиента, а заказанное сверх потребности учитывается фактическим количеством.
- Поступление товаров и услуг можно ввести на основании заказа клиента на производство: строки заполняются материалами, которые заказаны, но ещё не пришли. Поступление по такому заказу или по заказу поставщику под него отмечает пришедшие материалы; возврат поставщику уменьшает пришедшее. В списке поступлений появилась колонка «Заказ клиента».
- Новый отчёт «Потребности производства» в разделах «Производство» и «Закупки»: по заказам, продукции и материалам — потребность, заказано, пришло, дефицит и количество к заказу, с флагом «Только дефицит».
- Проведённый заказ на производство с изменённым количеством продукции без повторного проведения не записывается — проведите заказ, чтобы обновить потребность.
- Ранее созданные заказы и закупки не перепроводятся: потребность появляется при проведении документов в новой версии. Закупки под заказы на продажу потребность не затрагивают.
### fr
- Une commande client en production validée génère un besoin en matières : la quantité de chaque matière nécessaire à chaque produit de la commande, en unités de base. Les achats liés à la commande indiquent les quantités commandées et reçues.
- La commande au fournisseur reçoit le champ « Commande client » et le bouton « Remplir selon le besoin » au-dessus des articles : les lignes sont remplies avec les matières manquantes de la commande client en production, c'est-à-dire le besoin moins ce qui est déjà commandé. Une commande au fournisseur créée à partir d'une commande en production est remplie de la même façon ; si la commande client n'est pas validée, la création est refusée avec un message. La création à partir d'une commande de vente fonctionne comme avant.
- Le produit pour lequel une matière est commandée est conservé dans la colonne « Produit » de la commande au fournisseur, affichable via « Plus → Modifier le formulaire ». Si le produit n'est pas indiqué, la quantité est répartie entre les produits dans l'ordre des lignes de la commande client, et ce qui dépasse le besoin est pris en compte pour sa quantité réelle.
- La réception de marchandises et services peut être créée à partir d'une commande client en production : les lignes reprennent les matières commandées mais pas encore reçues. Une réception sur cette commande ou sur une commande au fournisseur liée enregistre les matières reçues ; un retour au fournisseur les diminue. La liste des réceptions affiche la colonne « Commande client ».
- Nouveau rapport « Besoins de production » dans les sections « Production » et « Achats » : par commande, produit et matière — besoin, commandé, reçu, déficit et quantité à commander, avec l'option « Seulement le déficit ».
- Une commande en production validée dont la quantité de produit a changé n'est pas enregistrée sans nouvelle validation : validez la commande pour mettre à jour le besoin.
- Les commandes et achats existants ne sont pas revalidés : le besoin apparaît lors de la validation des documents dans la nouvelle version. Les achats liés aux commandes de vente ne modifient pas le besoin.
### en
- A posted customer production order now creates material requirements: how much of each material each product of the order needs, in base units. Purchases for the order record how much material is ordered and received.
- The supplier order gets a Customer order field and a Fill by requirements button above the items: lines are filled with the missing materials of the customer production order, i.e. the requirement minus what is already ordered. A supplier order created from a production order is filled the same way; if the customer order is not posted, creation is refused with a message. Creating from a sales order works as before.
- The product a material is ordered for is kept in the Product column of the supplier order, which can be shown via More → Change form. If no product is set, the quantity is distributed among the products in the order of the customer order lines, and quantities above the requirement are recorded as actually ordered.
- A goods and services receipt can be created from a customer production order: lines are filled with materials that are ordered but not yet received. A receipt for such an order, or for a supplier order placed for it, records the received materials; a return to the supplier reduces them. The receipts list shows a Customer order column.
- New Production requirements report in the Production and Purchases sections: by order, product and material — requirement, ordered, received, shortage and quantity to order, with a Shortage only option.
- A posted production order whose product quantity was changed cannot be saved without posting — post the order to update the requirements.
- Existing orders and purchases are not reposted: requirements appear when documents are posted in the new version. Purchases for sales orders do not affect requirements.
### es
- Un pedido de cliente para producción contabilizado genera necesidades de materiales: cuánto de cada material necesita cada producto del pedido, en unidades base. Las compras para el pedido registran cuánto material se ha pedido y recibido.
- El pedido al proveedor recibe el campo «Pedido de cliente» y el botón «Rellenar según necesidades» encima de los artículos: las líneas se rellenan con los materiales que faltan del pedido de cliente para producción, es decir, la necesidad menos lo ya pedido. Un pedido al proveedor creado a partir de un pedido para producción se rellena igual; si el pedido de cliente no está contabilizado, la creación se rechaza con un mensaje. La creación a partir de un pedido de venta funciona como antes.
- El producto para el que se pide un material se guarda en la columna «Producto» del pedido al proveedor, que se puede mostrar con «Más → Cambiar formulario». Si no se indica el producto, la cantidad se reparte entre los productos en el orden de las líneas del pedido de cliente, y lo pedido por encima de la necesidad se registra por su cantidad real.
- La recepción de productos y servicios se puede crear a partir de un pedido de cliente para producción: las líneas se rellenan con los materiales pedidos pero aún no recibidos. Una recepción de ese pedido, o de un pedido al proveedor hecho para él, registra los materiales recibidos; una devolución al proveedor los reduce. La lista de recepciones muestra la columna «Pedido de cliente».
- Nuevo informe «Necesidades de producción» en las secciones «Producción» y «Compras»: por pedido, producto y material — necesidad, pedido, recibido, déficit y cantidad por pedir, con la opción «Solo déficit».
- Un pedido para producción contabilizado cuya cantidad de producto ha cambiado no se guarda sin volver a contabilizar: contabilice el pedido para actualizar las necesidades.
- Los pedidos y compras existentes no se vuelven a contabilizar: las necesidades aparecen al contabilizar los documentos en la nueva versión. Las compras para pedidos de venta no afectan a las necesidades.

## 2.0.15.14
### ru
- Заказ клиента на производство теперь проводится: в форме заказа и в списке «Заказы клиентов на производство» появились «Провести и закрыть», «Провести» и «Отмена проведения», в списке — отметка проведённого заказа. Заказы на продажу по-прежнему не проводятся, кнопок проведения у них нет, заголовок и главная кнопка «Записать и закрыть» не изменились. Ранее созданные заказы остаются непроведёнными.
- При проведении заказ фиксирует состав материалов в истории технологических карт: если состав продукции отличается от её действующей карты, записывается новая версия карты с датой проведения — она становится текущей картой номенклатуры. Если состав совпадает с действующей картой, с версией карты, по которой заполнены материалы, или не менялся с прошлого проведения, новая версия не создаётся. Версия карты ставится в колонку «Техкарта» строк продукции.
- Изменить карту через заказ может только пользователь с правом на технологические карты; остальные проводят заказы с составом, совпадающим с картой.
- Заказ не проводится, если у продукции, которая только производится, нет материалов, если материал не заполнен, совпадает с самой продукцией или указан с разными упаковками, а также если у продукции уже есть карта с более поздней датой. Причина выводится сообщением.
- Если в тот же день карта продукции уже была записана с другим составом, она перезаписывается составом заказа, о чём выводится сообщение; о выпусках продукции за сегодня, проведённых по прежней карте, тоже сообщается.
- Вид операции проведённого заказа изменить нельзя — сначала отмените проведение. Если материалы проведённого заказа изменены, запись без проведения отклоняется — проведите заказ. Отмена проведения записанную карту не удаляет.
- Одновременная запись технологической карты из карточки номенклатуры, документа карты и заказа выполняется по очереди: две карты за один день больше не создаются.
### fr
- La commande client en production peut désormais être validée : le formulaire de la commande et la liste « Commandes clients en production » proposent les commandes de validation et d’annulation de la validation, et la liste marque les commandes validées. Les commandes de vente ne sont toujours pas validées : pas de commandes de validation, titre et bouton principal d’enregistrement et fermeture inchangés. Les commandes existantes restent non validées.
- À la validation, la commande fixe sa composition de matières dans l’historique des gammes de fabrication : si la composition d’un produit diffère de sa gamme en vigueur, une nouvelle version de gamme est enregistrée à la date de validation et devient la gamme courante de l’article. Si la composition correspond à la gamme en vigueur, à la version de gamme qui a servi à remplir les matières, ou n’a pas changé depuis la validation précédente, aucune version n’est créée. La version est inscrite dans la colonne « Gamme de fabrication » des lignes du produit.
- Seul un utilisateur ayant droit aux gammes de fabrication peut modifier une gamme par une commande ; les autres valident des commandes dont la composition correspond à la gamme.
- La commande n’est pas validée si un produit uniquement fabriqué n’a pas de matières, si une matière est vide, identique au produit ou saisie avec des conditionnements différents, ou si le produit a déjà une gamme à une date ultérieure. La raison est affichée dans un message.
- Si la gamme du produit a déjà été enregistrée le même jour avec une autre composition, elle est remplacée par celle de la commande et un message l’indique ; les productions du jour validées selon l’ancienne gamme sont aussi signalées.
- Le type d’opération d’une commande validée ne peut pas être modifié : annulez d’abord la validation. Si les matières d’une commande validée ont changé, l’enregistrement sans validation est refusé : validez la commande. L’annulation de la validation ne supprime pas la gamme enregistrée.
- Les enregistrements simultanés d’une gamme de fabrication depuis la fiche article, le document de gamme et une commande sont exécutés l’un après l’autre : deux gammes pour un même jour ne sont plus créées.
### en
- Customer production orders can now be posted: the order form and the Customer production orders list offer Post and close, Post and Undo posting, and the list marks posted orders. Sales orders are still not posted: they have no posting buttons, and their title and main Save and close button are unchanged. Existing orders stay unposted.
- On posting, the order records its materials in the production routing history: if a product's composition differs from its current routing, a new routing version dated on the posting day is saved and becomes the item's current routing. If the composition matches the current routing, the routing version the materials were filled from, or has not changed since the previous posting, no version is created. The version is set in the Production routing column of the product lines.
- Only a user with rights to production routings can change a routing through an order; other users post orders whose composition matches the routing.
- An order is not posted if a manufacture-only product has no materials, if a material is empty, equal to the product itself or entered with different packagings, or if the product already has a routing dated later. The reason is shown in a message.
- If the product's routing was already saved on the same day with another composition, it is overwritten with the order composition and a message says so; production issues posted today with the previous routing are reported too.
- The operation type of a posted order cannot be changed — unpost the order first. If the materials of a posted order were changed, saving without posting is rejected — post the order. Unposting does not delete the saved routing.
- Simultaneous saves of a production routing from the item card, the routing document and an order now run one after another: two routings for the same day are no longer created.
### es
- El pedido de cliente para producción ahora se contabiliza: el formulario del pedido y la lista «Pedidos de clientes para producción» ofrecen los comandos de contabilizar y anular la contabilización, y la lista marca los pedidos contabilizados. Los pedidos de venta siguen sin contabilizarse: no tienen comandos de contabilización y su título y botón principal de guardar y cerrar no cambian. Los pedidos existentes siguen sin contabilizar.
- Al contabilizar, el pedido fija su composición de materiales en el historial de rutas de fabricación: si la composición de un producto difiere de su ruta vigente, se guarda una nueva versión con la fecha de contabilización, que pasa a ser la ruta actual del artículo. Si la composición coincide con la ruta vigente, con la versión de ruta con la que se rellenaron los materiales, o no ha cambiado desde la contabilización anterior, no se crea ninguna versión. La versión se anota en la columna «Ruta de fabricación» de las líneas del producto.
- Solo un usuario con derechos sobre las rutas de fabricación puede cambiar una ruta mediante un pedido; los demás contabilizan pedidos cuya composición coincide con la ruta.
- El pedido no se contabiliza si un producto que solo se fabrica no tiene materiales, si un material está vacío, coincide con el propio producto o tiene embalajes distintos, o si el producto ya tiene una ruta con fecha posterior. El motivo se muestra en un mensaje.
- Si la ruta del producto ya se guardó el mismo día con otra composición, se sustituye por la del pedido y se muestra un mensaje; también se avisa de las producciones de hoy contabilizadas con la ruta anterior.
- El tipo de operación de un pedido contabilizado no se puede cambiar: anule primero la contabilización. Si los materiales de un pedido contabilizado han cambiado, guardar sin contabilizar se rechaza: contabilice el pedido. Anular la contabilización no elimina la ruta guardada.
- Los guardados simultáneos de una ruta de fabricación desde la ficha del artículo, el documento de ruta y un pedido se ejecutan uno tras otro: ya no se crean dos rutas para el mismo día.

## 2.0.15.13
### ru
- В заказе клиента на производство появился состав материалов: таблица «Материалы» под товарами на закладке «Товары и услуги». По умолчанию она показывает материалы текущей строки товаров, переключатель «Все материалы» — весь состав заказа.
- Кнопки «Заполнить по техкарте» (текущая строка) и «Заполнить все по техкартам» заполняют материалы по технологической карте, действующей на дату заказа. Количество материала считается от количества продукции и пересчитывается при его изменении; о производимой позиции без карты выводится сообщение.
- Заказ на производство, введённый на основании коммерческого предложения, получает материалы сразу.
- При смене номенклатуры или удалении строки товаров её материалы удаляются, копия строки получает копию материалов. Одна продукция в двух строках заказа может иметь только одинаковый состав — иначе заказ не записывается.
- Если заказ перевести из производства в продажу, материалы очищаются при записи. У заказов на продажу форма не изменилась.
- Версия технологической карты строки хранится в колонке «Техкарта»; её можно показать через «Ещё → Изменить форму».
### fr
- La commande client en production reçoit une composition de matières : le tableau « Matières » sous les articles, dans l’onglet « Marchandises et services ». Par défaut, il affiche les matières de la ligne d’articles courante ; le sélecteur « Toutes les matières » affiche toute la composition de la commande.
- Les boutons « Remplir selon la gamme de fabrication » (ligne courante) et « Tout remplir selon les gammes de fabrication » remplissent les matières selon la gamme en vigueur à la date de la commande. La quantité de matière est calculée à partir de la quantité de produit et recalculée quand celle-ci change ; un article fabriqué sans gamme fait l’objet d’un message.
- Une commande en production créée à partir d’un devis reçoit ses matières immédiatement.
- Quand l’article d’une ligne change ou que la ligne est supprimée, ses matières sont supprimées ; une ligne copiée reçoit une copie des matières. Un même produit sur deux lignes d’une commande doit avoir la même composition, sinon la commande n’est pas enregistrée.
- Si une commande en production repasse en vente, ses matières sont effacées à l’enregistrement. Le formulaire des commandes de vente est inchangé.
- La version de la gamme de fabrication de la ligne est conservée dans la colonne « Gamme de fabrication », affichable via « Plus → Modifier le formulaire ».
### en
- Customer production orders now have a materials list: the Materials table below the products on the Goods and services tab. By default it shows the materials of the current product line; the All materials switch shows the whole order composition.
- The Fill from production routing (current line) and Fill all from production routings buttons fill materials from the routing valid on the order date. Material quantity is calculated from the product quantity and recalculated when it changes; a manufactured item without a routing gets a message.
- A production order created from a quotation gets its materials straight away.
- When a line's product changes or the line is deleted, its materials are removed; a copied line gets a copy of the materials. The same product on two order lines must have the same composition, otherwise the order is not saved.
- If an order is switched from production back to sale, its materials are cleared on save. The sales order form is unchanged.
- The routing version of a line is kept in the Production routing column, which can be shown via More → Change form.
### es
- El pedido de cliente para producción tiene ahora composición de materiales: la tabla «Materiales» bajo los artículos, en la pestaña «Bienes y servicios». Por defecto muestra los materiales de la línea de artículos actual; el conmutador «Todos los materiales» muestra toda la composición del pedido.
- Los botones «Rellenar según ruta de fabricación» (línea actual) y «Rellenar todo según rutas de fabricación» rellenan los materiales según la ruta vigente en la fecha del pedido. La cantidad de material se calcula a partir de la cantidad de producto y se recalcula cuando esta cambia; un artículo fabricado sin ruta recibe un mensaje.
- Un pedido para producción creado a partir de un presupuesto recibe los materiales de inmediato.
- Al cambiar el artículo de una línea o eliminar la línea, sus materiales se eliminan; una línea copiada recibe una copia de los materiales. Un mismo producto en dos líneas del pedido debe tener la misma composición; de lo contrario, el pedido no se guarda.
- Si un pedido pasa de producción a venta, sus materiales se borran al guardar. El formulario de los pedidos de venta no cambia.
- La versión de la ruta de fabricación de la línea se guarda en la columna «Ruta de fabricación», que puede mostrarse con «Más → Cambiar formulario».

## 2.0.15.12
### ru
- Колонки «Статус» и «Долг» в списках заказов клиентов и реализаций подписаны на языке интерфейса, а не только по-русски.
### fr
- Les colonnes « Statut » et « Dette » des listes de commandes clients et de ventes sont libellées dans la langue de l’interface, et non plus seulement en russe.
### en
- The Status and Debt columns in the customer order and sales lists are now labeled in the interface language, not only in Russian.
### es
- Las columnas «Estado» y «Deuda» de las listas de pedidos de clientes y de ventas se muestran en el idioma de la interfaz y no solo en ruso.

## 2.0.15.11
### ru
- Список заказов клиентов снова показывает содержимое: закладки «Заказы» и «Коммерческие предложения» были скрыты, форма открывалась пустой — и из раздела «Продажи», и командой «Заказы клиентов на производство». Кнопка «Создать заказ» перенесена из таблицы предложений на закладку.
- Заголовок списка «Заказы клиентов на производство» больше не дублирует название списка.
- Рабочее место производства называется «Рабочее место производства» и стоит в разделе «Производство» первым.
### fr
- La liste des commandes clients affiche de nouveau son contenu : les onglets « Commandes » et « Devis » étaient masqués et le formulaire s’ouvrait vide, depuis la section « Ventes » comme par la commande « Commandes clients en production ». Le bouton « Créer la commande » a été déplacé du tableau des devis vers l’onglet.
- Le titre de la liste « Commandes clients en production » ne répète plus le nom de la liste.
- Le poste de travail s’intitule « Poste de production » et figure en premier dans la section « Production ».
### en
- The customer order list shows its content again: the Orders and Quotations tabs were hidden and the form opened empty, both from the Sales section and via the Customer production orders command. The Create order button has moved from the quotations table to the tab.
- The title of the Customer production orders list no longer repeats the list name.
- The production workplace is now called Production workstation and comes first in the Production section.
### es
- La lista de pedidos de clientes vuelve a mostrar su contenido: las pestañas «Pedidos» y «Presupuestos» estaban ocultas y el formulario se abría vacío, tanto desde la sección «Ventas» como con el comando «Pedidos de clientes para producción». El botón «Crear el pedido» se ha trasladado de la tabla de presupuestos a la pestaña.
- El título de la lista «Pedidos de clientes para producción» ya no repite el nombre de la lista.
- El puesto de trabajo se llama «Puesto de producción» y aparece en primer lugar en la sección «Producción».

## 2.0.15.10
### ru
- Исправлен ввод заказа клиента на основании коммерческого предложения: заполнение прерывалось ошибкой «Неоднозначное поле».
- У пользователей с ролью ECommerce упрощённая форма подставляется только для самого заказа клиента; остальные формы заказа открываются стандартно.
- В рабочем месте «Заказы в производстве» выбор строки заказа больше не прерывается ошибкой «Поле объекта не обнаружено (Ссылка)».
### fr
- La création d’une commande client à partir d’un devis est corrigée : le remplissage s’interrompait sur l’erreur « Champ ambigu ».
- Pour les utilisateurs ayant le rôle ECommerce, le formulaire simplifié ne remplace que celui de la commande client elle-même ; les autres formulaires de la commande s’ouvrent normalement.
- Dans le poste de travail « Commandes en production », la sélection d’une ligne de commande ne provoque plus l’erreur « Champ de l’objet introuvable (Ссылка) ».
### en
- Creating a customer order from a quotation is fixed: filling stopped with an "Ambiguous field" error.
- For users with the ECommerce role, the simplified form replaces only the customer order form itself; other order forms open as usual.
- In the Orders in production workplace, selecting an order row no longer fails with "Object field not found (Ссылка)".
### es
- Se ha corregido la creación de un pedido de cliente a partir de un presupuesto: el llenado se interrumpía con el error «Campo ambiguo».
- Para los usuarios con el rol ECommerce, el formulario simplificado solo sustituye al del propio pedido de cliente; los demás formularios del pedido se abren con normalidad.
- En el puesto de trabajo «Pedidos en producción», seleccionar una fila de pedido ya no produce el error «Campo del objeto no encontrado (Ссылка)».

## 2.0.15.9
### ru
- В заказе клиента появился вид операции: «Продажа» или «Производство». Поле видно при включённой функциональной опции «Производство»; вид операции можно сменить и у записанного заказа.
- Заказ, введённый на основании коммерческого предложения, получает вид «Производство», если хотя бы одна позиция предложения пополняется производством (в том числе «Оба»). Остальные заказы, включая заказы из кабинета партнёра и лидов, — продажи.
- Заказ на производство называется «Заказ клиента на производство» в заголовке формы, в списках и ссылках. В разделе «Производство» появилась команда «Заказы клиентов на производство»: список открывается только с такими заказами, а новый заказ из него сразу получает вид «Производство».
- В общем списке заказов клиентов добавлены колонка вида операции и тумблер «Операция» в панели фильтров. При обновлении всем существующим заказам проставляется вид «Продажа».
### fr
- La commande client dispose désormais d’un type d’opération : « Vente » ou « Production ». Le champ est visible lorsque l’option fonctionnelle « Production » est activée ; le type peut aussi être modifié sur une commande déjà enregistrée.
- Une commande créée à partir d’un devis reçoit le type « Production » si au moins un article du devis est réapprovisionné par la production (y compris « Les deux »). Les autres commandes, dont celles du portail partenaire et des prospects, sont des ventes.
- Une commande de production s’intitule « Commande client en production » dans le titre du formulaire, les listes et les liens. La section « Production » propose la commande « Commandes clients en production » : la liste n’affiche que ces commandes et toute nouvelle commande créée depuis cette liste reçoit le type « Production ».
- La liste générale des commandes clients affiche une colonne du type d’opération et un sélecteur « Opération » dans le panneau des filtres. Lors de la mise à jour, toutes les commandes existantes reçoivent le type « Vente ».
### en
- Customer orders now have an operation type: Sale or Production. The field is visible when the Production functional option is enabled; the type can also be changed on a saved order.
- An order created from a quotation gets the Production type if at least one quotation item is replenished by production (including Both). All other orders, including orders from the partner portal and from leads, are sales.
- A production order is called "Customer production order" in the form title, lists, and links. The Production section now has a Customer production orders command: the list shows only these orders, and a new order created from it gets the Production type immediately.
- The general customer order list has an operation type column and an Operation switch in the filter panel. During the update, all existing orders get the Sale type.
### es
- El pedido de cliente tiene ahora un tipo de operación: «Venta» o «Producción». El campo es visible cuando la opción funcional «Producción» está activada; el tipo también puede cambiarse en un pedido ya guardado.
- Un pedido creado a partir de un presupuesto recibe el tipo «Producción» si al menos un artículo del presupuesto se repone mediante producción (incluido «Ambos»). Los demás pedidos, incluidos los del portal de socios y los de clientes potenciales, son ventas.
- Un pedido de producción se denomina «Pedido de cliente para producción» en el título del formulario, las listas y los enlaces. La sección «Producción» incluye el comando «Pedidos de clientes para producción»: la lista muestra solo esos pedidos y un nuevo pedido creado desde ella recibe el tipo «Producción» de inmediato.
- La lista general de pedidos de clientes incluye una columna del tipo de operación y un selector «Operación» en el panel de filtros. Durante la actualización, todos los pedidos existentes reciben el tipo «Venta».

## 2.0.15.8
### ru
- Добавлен отдельный документ «Коммерческое предложение» со статусами, описанием товарных строк, фильтрами и цветовым оформлением списка.
- Заказ покупателя создаётся на основании предложения и после успешной записи переводит его в статус «Выигран». Предложение и заказ доступны в связанных документах и на общей форме списка заказов.
- Коммерческое предложение печатается существующей формой Devis A4; описание строки при записи переносится в карточку соответствующей номенклатуры.
### fr
- Un document « Devis » distinct a été ajouté avec des statuts, une description des lignes, des filtres et une mise en forme colorée de la liste.
- Une commande client peut être créée à partir du devis ; après son enregistrement réussi, le devis passe au statut « Gagné ». Le devis et la commande sont accessibles dans les documents liés et dans la liste commune des commandes.
- Le devis utilise le formulaire d’impression Devis A4 existant ; la description de la ligne est enregistrée dans la fiche de l’article correspondant.
### en
- A separate Quotation document has been added with statuses, line descriptions, filters, and status-based list colors.
- A customer order can be created from a quotation; after a successful save, the quotation changes to Won. The quotation and order are available through related documents and the shared order list.
- Quotations use the existing Devis A4 print form; saving a quotation copies each line description to the corresponding item card.
### es
- Se ha añadido un documento « Presupuesto » independiente con estados, descripciones de líneas, filtros y colores de lista según el estado.
- Se puede crear un pedido de cliente a partir del presupuesto; tras guardarlo correctamente, el presupuesto cambia a « Ganado ». Ambos documentos están disponibles entre los documentos relacionados y en la lista común de pedidos.
- El presupuesto utiliza el formulario de impresión Devis A4 existente; al guardarlo, la descripción de cada línea se copia en la ficha del artículo correspondiente.

## 2.0.15.7
### ru
- В карточке номенклатуры появился способ пополнения запаса: «Закупка», «Производство» или «Оба». Поле доступно при включённой функциональной опции «Производство».
- Для продукции и полуфабрикатов по умолчанию выбирается производство, для товаров, сырья, комплектов и услуг — закупка. При обновлении пустые значения существующей номенклатуры заполняются по тому же правилу; выбранное пользователем значение «Оба» сохраняется.
- Исправлено заполнение материалов техкарты при выключенном учёте упаковок: пустая упаковка теперь устанавливается без ошибки.
### fr
- La fiche article dispose désormais d’un mode de réapprovisionnement : « Achat », « Production » ou « Les deux ». Le champ est disponible lorsque l’option fonctionnelle « Production » est activée.
- La production est proposée par défaut pour les produits finis et semi-finis ; l’achat l’est pour les marchandises, matières premières, kits et services. Lors de la mise à jour, les valeurs vides des articles existants sont renseignées selon la même règle ; le choix manuel « Les deux » est conservé.
- Le remplissage des matières d’une gamme lorsque la gestion des unités d’emballage est désactivée ne provoque plus d’erreur.
### en
- The item card now has an inventory replenishment method: Purchase, Production, or Both. The field is available when the Production functional option is enabled.
- Production is the default for finished and semi-finished products; Purchase is the default for goods, raw materials, kits, and services. During an update, empty values for existing items are populated by the same rule; a manually selected Both value is preserved.
- Filling production routing materials no longer fails when packaging unit accounting is disabled.
### es
- La ficha del artículo ahora incluye un método de reposición de existencias: « Compra », « Producción » o « Ambos ». El campo está disponible cuando la opción funcional « Producción » está activada.
- La producción es el valor predeterminado para productos terminados y semielaborados; la compra lo es para mercancías, materias primas, kits y servicios. Durante la actualización, los valores vacíos de los artículos existentes se completan con la misma regla; se conserva la selección manual « Ambos ».
- El llenado de los materiales de la ruta de fabricación ya no falla cuando la gestión de unidades de embalaje está desactivada.

## 2.0.15.6
### ru
- Под составом техкарты название и номер документа, дата версии и кнопка истории выстроены в одну строку. Надпись «Техкарта № … от» открывает документ по щелчку; отдельная ссылка с полным представлением документа удалена.
- Колонки стоимости подписаны «Закупочная цена*» и «Себестоимость*». Сноска поясняет, что это ориентировочная себестоимость по последней закупочной цене с НДС в валюте учёта.
### fr
- Sous la composition, le nom et le numéro de la gamme, la date de version et le bouton d’historique sont alignés sur une seule ligne. Le libellé « Gamme de fabrication n° … du » ouvre le document ; le lien distinct avec sa présentation complète a été supprimé.
- Les colonnes de coût sont intitulées « Prix d’achat* » et « Coût* ». Une note précise qu’il s’agit d’un coût indicatif selon le dernier prix d’achat, TVA comprise, en devise comptable.
### en
- Below the composition, the routing name and number, version date and history button are aligned in one row. Clicking “Production routing No. … dated” opens the document; the separate link containing the full document presentation has been removed.
- The cost columns are labelled “Purchase price*” and “Cost*”. A footnote explains that this is an estimated cost based on the latest purchase price, including VAT, in the accounting currency.
### es
- Debajo de la composición, el nombre y número de la ruta, la fecha de la versión y el botón del historial se muestran en una sola fila. Al pulsar «Ruta de fabricación n.º … del» se abre el documento; se ha eliminado el enlace separado con su presentación completa.
- Las columnas de coste se denominan «Precio de compra*» y «Coste*». Una nota explica que se trata de un coste orientativo según el último precio de compra, IVA incluido, en la moneda contable.

## 2.0.15.5
### ru
- Карточка номенклатуры открывается отдельной закладкой без блокировки списка. Под составом техкарты восстановлены дата версии, ссылка на документ и кнопка истории изменений, а также блок расчётных показателей.
### fr
- La fiche article s’ouvre dans un onglet distinct sans bloquer la liste. La date de version, le lien vers la gamme, le bouton d’historique et les indicateurs calculés sont de nouveau visibles sous la composition.
### en
- The item card opens in a separate tab without blocking the list. The version date, routing document link, history button and calculated indicators are visible again below the composition table.
### es
- La ficha del artículo se abre en una pestaña independiente sin bloquear la lista. La fecha de la versión, el enlace al documento, el botón del historial y los indicadores calculados vuelven a mostrarse debajo de la composición.

## 2.0.15.4
### ru
- Исправлено открытие карточки номенклатуры с техкартой: расчёт последней цены продажи больше не обращается к отсутствующим реквизитам валюты и курса реализации. Цена берётся из фактической суммы строк с НДС в валюте учёта.
### fr
- Correction de l’ouverture de la fiche article avec une gamme : le calcul du dernier prix de vente ne fait plus référence aux champs de devise et de taux absents du document de vente. Le prix utilise le montant réel des lignes, TVA comprise, en devise comptable.
### en
- Fixed opening an item card with a production routing: the latest sale price calculation no longer refers to currency and exchange rate fields absent from the sales document. The price uses actual line amounts including VAT in the accounting currency.
### es
- Corregida la apertura de la ficha del artículo con ruta de fabricación: el cálculo del último precio de venta ya no utiliza campos de moneda y tipo de cambio inexistentes en el documento de venta. El precio se obtiene de los importes reales de las líneas con IVA en la moneda contable.

## 2.0.15.3
### ru
- Технологическая карта: при редактировании выбирается версия на указанный день. Новая дата не может быть раньше последней версии, включая будущую; повторная запись в тот же день обновляет существующую карту. Даты новых и редактируемых карт сохраняются без времени.
- При изменении карты появляется предупреждение о проведённых выпусках с этой даты: их материалы нужно перезаполнить вручную. Сохранение карточки без изменения состава не создаёт новую версию.
- В составе показаны единицы измерения, последние закупочные цены, суммы и итоги. Рассчитываются плановая себестоимость единицы, возможный выпуск по остаткам всех складов и потенциальная маржа по последней фактической продаже. Повторяющиеся материалы используют общий остаток, характеристики учитываются отдельно. При отсутствии закупочных цен выводится предупреждение; неполные себестоимость и маржа не показываются.
### fr
- Gamme de fabrication : la version à modifier est sélectionnée selon le jour indiqué. La date ne peut pas précéder la dernière version, même future ; un nouvel enregistrement le même jour met à jour la gamme existante. Les dates sont enregistrées sans heure, y compris lors des modifications.
- Un avertissement signale les productions déjà validées depuis cette date : leurs matières doivent être remplies à nouveau manuellement. Enregistrer la fiche sans modifier la composition ne crée pas de nouvelle version.
- La composition affiche les unités, les derniers prix d’achat, les montants et les totaux. Le coût prévisionnel unitaire, la production possible avec les stocks de tous les entrepôts et la marge potentielle selon la dernière vente réelle sont calculés. Les matières répétées partagent le stock ; les caractéristiques sont traitées séparément. Si des prix d’achat manquent, un avertissement remplace le coût et la marge incomplets.
### en
- Production routing: editing selects the version for the specified day. The date cannot precede the latest version, including a future version; saving again on the same day updates the existing routing. New and edited routing dates are stored without a time component.
- A warning identifies posted production issues from that date: their materials must be refilled manually. Saving the item card without changing its composition does not create a new version.
- The composition shows units, latest purchase prices, amounts and totals. Planned unit cost, possible output from stock across all warehouses and potential margin based on the latest actual sale are calculated. Repeated materials share available stock; characteristics are handled separately. Missing purchase prices trigger a warning, and incomplete cost and margin are hidden.
### es
- Ruta de fabricación: al editar se selecciona la versión del día indicado. La fecha no puede ser anterior a la última versión, aunque sea futura; guardar de nuevo el mismo día actualiza la ruta existente. Las fechas de rutas nuevas y editadas se guardan sin hora.
- Un aviso señala las producciones contabilizadas desde esa fecha: sus materiales deben rellenarse de nuevo manualmente. Guardar la ficha sin cambiar la composición no crea otra versión.
- La composición muestra unidades, últimos precios de compra, importes y totales. Se calculan el coste unitario previsto, la producción posible con existencias de todos los almacenes y el margen potencial según la última venta real. Los materiales repetidos comparten las existencias; las características se tratan por separado. Si faltan precios de compra, se muestra un aviso y se ocultan el coste y el margen incompletos.

## 2.0.15.2
### ru
- Технологические карты хранят историю состава. В карточке номенклатуры можно задать дату действия, просмотреть версию и открыть историю; очистка состава отменяет карту, запись без изменения состава не создаёт новую версию.
- При обновлении прежние карты номенклатуры автоматически переносятся в документы с датой создания товара (если дата отсутствует — с 01.01.2000). Повторный запуск не создаёт дубли и сохраняет уже заведённые карты, включая будущие версии, отмены и черновики.
- Выпуск продукции и распределение себестоимости используют карту на дату документа. Исправлено заполнение материалов выпуска по техкарте при работе с характеристиками.
- В настройках номенклатуры добавлен переключатель «Использовать упаковку». По умолчанию он выключен: упаковка из техкарты не подставляется в выпуск. Колонки упаковки и характеристик состава показываются по соответствующим настройкам.
- Карточка номенклатуры стала единой для всех ролей, включая ECommerce: страница «Технологическая карта» доступна при включённом производстве для продукции и полуфабрикатов. Страница и команды переведены на все языки интерфейса.
### fr
- Les gammes de fabrication conservent l'historique de leur composition. La fiche article permet de définir la date d'effet, de consulter la version et d'ouvrir l'historique. Vider la composition annule la gamme de fabrication ; enregistrer sans modifier la composition ne crée pas de nouvelle version.
- Lors de la mise à jour, les anciennes gammes de fabrication sont transférées automatiquement vers des documents datés de la création de l'article (ou du 01/01/2000 si la date manque). Une nouvelle exécution ne crée pas de doublons et préserve les versions existantes, y compris futures, annulées et les brouillons.
- La production et la répartition du coût utilisent la gamme de fabrication applicable à la date du document. Le remplissage des matières à partir de la gamme de fabrication a été corrigé pour les caractéristiques.
- L'option « Utiliser les conditionnements » a été ajoutée aux paramètres des articles. Désactivée par défaut, elle empêche la reprise du conditionnement de la gamme de fabrication dans la production. Les colonnes de conditionnement et de caractéristiques suivent leurs paramètres respectifs.
- La fiche article est commune à tous les rôles, y compris ECommerce. La page « Gamme de fabrication » est disponible pour les produits finis et semi-finis lorsque la production est activée. La page et ses commandes sont traduites dans toutes les langues de l'interface.
### en
- Production routings now keep version history. The item card lets you set an effective date, view the version and open its history. Clearing the materials cancels the production routing; saving an unchanged composition does not create another version.
- On update, existing item production routings are automatically transferred to documents dated from the item's creation (or January 1, 2000 if no date is available). Rerunning the migration creates no duplicates and preserves existing versions, including future versions, cancellations and drafts.
- Production issues and cost allocation use the production routing effective on the document date. Material filling from production routings has been corrected for item characteristics.
- A “Use packaging” option has been added to item settings. It is off by default, so packaging from the production routing is not filled into production issues. Packaging and characteristic columns follow their respective settings.
- The item card is shared by all roles, including ECommerce. The “Production routing” page is available for finished and semi-finished products when production is enabled. The page and its commands are translated into all interface languages.
### es
- Las rutas de fabricación conservan el historial de su composición. La ficha del artículo permite indicar la fecha de vigencia, consultar la versión y abrir el historial. Vaciar la composición anula la ruta de fabricación; guardar sin modificarla no crea una nueva versión.
- Al actualizar, las rutas de fabricación existentes se trasladan automáticamente a documentos con la fecha de creación del artículo (o el 01/01/2000 si falta la fecha). Repetir el traslado no crea duplicados y conserva las versiones existentes, incluidas las futuras, las anulaciones y los borradores.
- La producción y el reparto del coste utilizan la ruta de fabricación vigente en la fecha del documento. Se ha corregido el llenado de materiales desde la ruta de fabricación al utilizar características.
- Se ha añadido la opción «Usar embalajes» en los ajustes de artículos. Está desactivada por defecto, por lo que el embalaje de la ruta de fabricación no se rellena en la producción. Las columnas de embalaje y características siguen sus respectivos ajustes.
- La ficha del artículo es común para todos los roles, incluido ECommerce. La página «Ruta de fabricación» está disponible para productos terminados y semielaborados cuando la producción está activada. La página y sus comandos están traducidos a todos los idiomas de la interfaz.

## 2.0.15.1
### ru
- Список поступлений товаров и услуг снова показывает поступления: запрос списка был подменён запросом соседней закладки заказов поставщику, из-за чего колонки списка оставались без данных.
- АРМ производства: щелчок по заказу и его открытие двойным щелчком больше не прерываются ошибкой «Поле объекта не обнаружено (Ссылка)».
### fr
- La liste des réceptions de biens et services affiche de nouveau les réceptions : la requête de la liste avait été remplacée par celle de l'onglet voisin des commandes fournisseur, et les colonnes restaient sans données.
- Poste de production : cliquer sur une commande et l'ouvrir par double-clic n'échoue plus avec l'erreur « Champ d'objet introuvable (Référence) ».
### en
- The goods and services receipt list shows receipts again: the list query had been replaced with the query of the neighbouring supplier orders tab, leaving the list columns without data.
- Production workplace: clicking an order and opening it with a double click no longer fails with "Object field not found (Ref)".
### es
- La lista de recepciones de bienes y servicios vuelve a mostrar recepciones: la consulta de la lista había sido sustituida por la de la pestaña vecina de pedidos a proveedores y las columnas quedaban sin datos.
- Puesto de producción: al pulsar sobre un pedido y abrirlo con doble clic ya no aparece el error «Campo del objeto no encontrado (Referencia)».

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
