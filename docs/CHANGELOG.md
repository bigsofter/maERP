# Список изменений maERP

Секции переносятся сюда из общего макета `ОписаниеИзменений` при публикации CF
(правило в `docs/RELEASING.md`). Внутри релиза секции идут по сборкам, от новых
к старым, на всех языках конфигурации — ровно так, как их видел владелец в окне
«Что нового».

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
