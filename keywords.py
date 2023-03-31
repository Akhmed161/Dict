pattern = {
    #в основном для хелпера
    'вебим': ['wibim', 'vebim', 'webim', 'вэбим', 'вибим'],
    'инвойс': ['инвойс\w*', 'invoic(.)?' 'invoic(.)? clients', 'invoic(.)? Admin', 'invoic(.)? Inventory', 'inventory', 'инвойс админ', 'инвойс инвентори', 'инвойс клиент', 'invoice_clients'],
    'хелпдэск': ['help desk', 'helpdesk', 'хэлпдеск'],
    'скайп': ['skype', 'lync', 'линк(.)?', 'skype for business', 'скайп для бизнеса'],
    'почта': ['out look', 'outlok', 'аутлук', 'корп(\.)? почта', 'корп(\.)?почта', 'outlook'],
    'вебмейл': ['webmail', 'вэбмейл', 'вэб-мейл', 'веб-мейл'],
    'облачный офис': ['ofice 365', 'office 365', 'офис 365', 'teams', 'word', 'excel', 'oneNote', 'access'],
    'авайя': ['avaya', 'авайка', 'авая'],
    'сервисдеск': ['sd', 'servicedesk', 'bpmonline service desk', 'bpmonline', 'bpm', 'bpm7', 'бпм', 'bpm-servicedesk', 'bpm servicedesk', 'service desk', 'servic desk', 'servicdesk', 'бпм servicedesk', 'бпм-servicedesk', 'бпм-сервисдеск', 'бпм сервисдеск'],
    'виндоус': ['vindovs', 'windows', 'винда', 'виндовс', 'виндов'],
    'фтп': ['sftp', 'ftp'],
    'циско': ['cisco', 'циска', 'сиско', 'AnyConnect', 'Any Connect', 'cisco anyconnec', 'anyconnec'],
    'вди': ['vdi', 'инфраструктура виртуальных рабочих столов', 'виртуальный рабочий стол'],
    'администратор':['админ'],
    'файрвол': ['фаервол', 'брандмауэр', 'брендмауэр', 'firewall', 'файерволл'],
    'антивирус': ['касперский', 'kasperskii', 'kaspersky'],
    'электронная подпись': ['эцп', 'эр', 'унэп', 'укэп', 'qr', 'qr-код', 'qr код', 'эп', 'эл(\.)?подпись', 'цифровая подпись', 'кью ар код', 'кью код', 'графическая подпись'],
    'простая электронная подпись': ['ПЭП', 'ПЕП'],
    'сап': ['sар', 'sap'],
    'рдб': ['pdb', 'rdb'],
    'рдп': ['Rdp', 'рдиди', 'Remote Desktop Protocol', 'Remote Desktop', 'протокол удалённого рабочего стола', 'протокол удаленного рабочего стола'],
    'роботизация': ['rpa', 'рпа'],
    'шерпоинт': ['share point', 'sharepoint'],
    'тфс': ['tfs', 'tfc', 'team foundation server'],
    'вебдилер': ['webdealer', 'вэб дилер', 'веб дилер', 'web dealer', 'wd', 'вд'],
    'босс кадровик': ['босс-кадровик', 'boss кадровик', 'boss-кадровик'],
    'запрос на изменение': ['зни', 'rfc'],
    'дивр': ['divr'],
    'апи': ['api'],
    'кмс': ['kms', 'km'],
    'арес': ['arec', 'ares'],
    'бранч': ['brunch', 'branch'],
    'апекс': ['apeks', 'apex', 'арех', 'апекс(.)?'],
    'двх': ['dvh', 'dwh'],
    'прм': ['prm'],
    'рбт': ['pbt', 'rbt'],
    'едв': ['edv', 'edw', 'едв'],
    'срм': ['crm'],
    'гвардиум': ['гуардиум', 'guardium'],
    'бпс': ['сап bpc','сап бпс', 'sap bps', 'bpc', 'бпс', 'Business Planning and Consolidation', 'Business Planning Consolidation', 'Business Planning', 'Planning Consolidation', 'Business Consolidation'],
    'ерп': ['сап erp', 'сап ерп','sap erp', 'erp', 'ерп', 'Enterprise Resource Planning', 'Enterprise Resource', 'Enterprise Planning', 'Resource Planning'],
    'сард': ['sard'],
    'определение смс центр': ['smsc', 'смсц', 'sms-центр', 'смс-центр'],
    'определение ммс центр': ['mmsc', 'ммсц', 'mms-центр', 'ммс-центр'],
    'определение юссд центр': ['юссдц', 'ussd-центр', 'ussdc', 'юссд-центр'],
    'есб': ['esb', 'еэсби'],
    'чикаго': ['chicago'],
    'найс': ['nice'],
    'спейс': ['space'],
    'забикс': ['zabix', 'zabiks', 'zabbix'],
    'айти ландшафт': ['it landscape', 'it ландшафт', 'it-landscape', 'ИТ-ландшафт'],
    'колл клиент': ['call-client', 'callclient', 'колл-клиент', 'коллклиент', 'СС'],
    'экспера ассп': ['экспера assp', 'expera assp', 'assp', 'ассп'],
    'экспера бргв': ['экспера brgw', 'expera brgw', 'brgw', 'бргв'],
    'экспера ссбр': ['экспера ccbr', 'expera ccbr', 'ccbr', 'ссбр'],
    'сорм': ['сорм 538','система оперативно-розыскных мероприятий', 'система розыскных мероприятий', 'система для оперативно-розыскных мероприятий', 'система для оперативных мероприятий', 'система оперативных мероприятий','Ядро' 'система Ядро'],
    'акьюмс': ['aqmc', 'aqms'],
    'мнп': ['mnp'],
    'срф': ['srf'],
    'пдф': ['pdf'],
    'бартендер'['bartender', 'bar tender'],
    'Планета земля': ['google earth'],
    'вебтутор': ['web-tutor', 'webtutor', 'вэбтьютор'],
    'лбс': ['LBC', 'lbs'],
    'лср': ['LSR', 'lcr'],
    'пиай': ['база pi', 'pi'],
    'бро': ['bro', 'портал бро'],
    'джира': ['gira', 'jira'],
    'графана': ['Grofana', 'grafana'],
    'ивр': ['ivr', 'айвр'],
    'вики': ['viki', 'wiki', 'конфлюенс', 'confluence'],
    'фиори': ['fyori', 'fiory', 'fiori'],
    'эйчар': ['hr', 'айчар'],
    'эйчар документ': ['HR-документ\w*', 'эйчар-документ\w*', 'HR документ\w*'],
    'эйчар партнер': ['hr-партнер\w*', 'hr партнер\w*', 'hr-бизнес-партнер\w*', 'hrbp', 'эйчар-партнер\w*'],
    'рфк': ['rfq', 'рфкью'],
    'рфи': ['rfi', 'рфай'],    
    'айсиси': ['icc', 'исс'],
    'имси': ['imci', 'imsi'],
    'мсисдн': ['mcicdn', 'msisdn'],
    'фса': ['FCA', 'fsa', 'ФСЭ'],
    'сса': ['SSA'],
    'аккруал': ['accruals', 'acruals', 'accrual', 'акруал', 'аккурал'],
    'капекс': ['kapex', 'capex'],
    'опекс': ['opeks', 'opex'],
    'веб': ['veb', 'web', 'вэб'],
    'юсб': ['usb'],
    'ахр': ['административно хозяйственные расходы', 'адм(\.)? хоз(\.)? расходы', 'хоз(\.)? расходы', 'административно-хозяйственные расходы', 'административные расходы', 'админ(\.)? расходы', 'хозяйственные расходы'],
    'ситрикс': ['sitrix', 'citrix', 'цитрикс'],
    'ссд': ['ssd'],
    'аналитический': ['аналит(\.)?', 'аналитич(\.)?', 'аналетическ\w*'],
    'ОНС': ['объект(.)? незавершенного строительства', 'объект(.)? неоконченного строительства', 'объект(.)? неоконченого строительства'],
    'ОКС': ['объект(.)? капитального строительства', 'капетального строительства'],
    'ГПЗУ': ['градостроительн\w* план земельн\w* участк(.)?', 'градостроительн\w* план земл(.)?', 'градостроительн\w* план участк(.)?', 'градостроительн\w* план'],
    'некапитальные': ['не капитальные'],
    'ИТО': ['инженерно-техническо\w* обеспечени(.)?', 'инженерно техническо\w* обеспечени(.)?', 'сетей инженерно-технического обеспечения', 'сети инженерно-технического обеспечения', 'сети ИТО', 'сетей ИТО'],
    'недвижимость': ['не движимость'],
    'ЕНК': ['едины(.)? недвижимы(.)? комплекс(.)?'],
    'СРО': ['саморегулируемые организаци(.)?', 'само регулируемые организаци(.)?', 'само регулируемая организаци(.)?', 'саморегулируемая организаци(.)?'],
    'капитальный ремонт': ['кап(\.)?ремонт', 'кап(\.)? ремонт', 'копетальный ремонт'],
    'ЕГРН': ['единый государственный реестр недвижимости', 'государственный реестр недвижимости', 'госреестр недвижимости', 'гос реестр недвижимости', 'реестр недвижимости'],
    'юридический': ['юр(\.)?', 'юредический', 'юредич(\.)?', 'юридич(\.)?'],
    'юр. отдел': ['юр(\.)?отдел'],
    'налог на добавленную стоимость': ['ндс', 'налог на добавочную стоимость', 'налог на доб(\.)? стоимость', 'налог на доб(\.)? стоим(\.)?', 'налог на доб(\.)? стоим-сть'],
    'незавершенное строительство': ['нзс', 'не завершенное строительство', 'не завершеное строительство'],
    'товарно материальные ценности': ['тмц', 'товарно-материальные ценности', 'материальные ценности'],
    'дебиторская задолженность': ['дз', 'дебиторская задолжность', 'дебиторка'],
    'кредиторская задолженность': ['кз', 'кредиторская задолжность', 'кредиторка'],
    'дебиторская и кредиторская задолженность': ['дз-кз', 'дебиторская и кредиторская задолжности', 'дз и кз'],
    'материальная помощь': ['мат(\.)? помощь', 'матпомощь', 'мотериальная помощь', 'денежная помощь'],
    'дополнительное соглашение': ['доп(\.)? соглашение', 'доп(\.)?соглашение', 'допалнительное соглашение', 'допник(.)?', 'дс'],
    'хозяйственный': ['хоз(\.)?', 'хазяйственны(\.)?'],
    'бухгалтерский': ['бух(\.)?'],
    'коммерческий': ['ком(\.)?', 'комерческий', 'камерческий'],
    'коммерческое предложение': ['ком(\.)?предложение', 'ком(\.)? предложение', 'кп'],
    'компьютер': ['пк', 'комп', 'компьютерное оборудование'],
    'мфу': ['многофункционально(.)? устройств(.)?', 'много функциональное устройство', 'функциональное устройство'],
    'сопроводительный': ['сопровод(\.)?'],
    'биллинг': ['biling', 'billing', 'билинг(.)?'],
    'авз': ['акты взаимозачетов с дилерами', 'акты взаимозачетов дилерами', 'акт взаимозачетов дилерами', 'акт взаимозачетов с дилерами'],
    'контактный центр': ['кц', 'контакт-центр', 'колл-центр', 'колл центр', 'звонковый центр'],
    'удаленный доступ': ['удалёнк(.)?', 'удаленк(.)?', 'удалён\w* доступ(.)?', 'удален\w* доступ(.)?', 'удален\w* работа', 'удалён\w* работа', 'работа из дома', 'работать удаленно', 'работать удалённо', 'работать на удалёнке', 'работать на удаленке'],
    'центральная функция': ['цф', 'центр(\.)? функция'],
    'служебная записка': ['сз', 'служебка'],
    'сверхурочная работа': ['сву'],
    'работа в выходной': ['рв', 'рвд', 'работа в выходной день'],
    'айти': ['it', 'айтишник(.)?' , 'it Support', 'it админ', 'it-специалист(.)?'],
    'модуль ре': ['re', 'аккруал re', 'accruals re', 'модуль re'],
    'договор ре': ['договор re', 'контракт re'],
    'модуль фи': ['FI', 'аккруал fi', 'accruals fi', 'модуль fi'],
    'модуль мм опекс': ['mm opex', 'аккруал mm opex', 'accruals mm opex', 'модуль mm opex'],
    'модуль мм капекс': ['mm capex', 'аккруал mm capex', 'accruals mm capex', 'модуль mm capex'],
    'аккруал ФИРЕ': ['fi-re', 'fi re', 'accruals fi-re', 'accrual fi-re', 'модуль fi-re'],
    'аккруал ФИММ': ['fi-mm', 'fi mm', 'accruals fi-mm', 'accrual fi-mm', 'модуль fi-mm'],
    'годовая премия': ['гп', 'год(\.)? премия'],
    'годовой бонус': ['год(\.)? бонус'],
    'общий центр обслуживания': ['оцо', 'цо', 'центр обслуживания'],
    'квартальная премия': ['scp', 'квартал(\.)? премия', 'квартальное премирование'],
    'индивидуальный план развития': ['ипр'],
    'электронное обучение': ['e learning', 'e-learning', 'эл(\.)? обучение', 'elearning'],
    'левелап': ['левел ап', 'level up', 'levelup', 'level-up'],
    'курсера': ['coursera', 'cursera', 'coursera(\.)?org'],
    'трудовая книжка': ['труд(\.)? книжка', 'тк'],
    'электронная трудовая книжка': ['эл(\.)? труд(\.)? книжка', 'этк', 'электронная трудовая'],
    'грейд': ['pl'],
    '182 н': ['182н','182-н','н-182','н182', 'справка182'],
    '2 ндфл': ['2-ндфл','2ндфл','ндфл2','ндфл-2','ндфл','ндфл 2'],
    'страхование жизни': ['сж', 'страховка жизни'],
    'несчастный случай': ['нс', 'не счастный случай'],
    'зарплата': ['зп', 'зар(\.)? плата', 'заработная плата', 'з/п'],
    'локальные нормативные акты': ['лна', 'локально-нормативные акты'],
    'видеонаблюдение': ['видео наблюдение', 'trassir', 'трассир'],
    'транспортно экспедиторское обслуживание': ['тэо', 'обслуживание транспортной экспедиции', 'обслуживание по транспортной экспедиции', 'транспортно-экспедиторское обслуживание', 'транспортную экспедицию', 'транспортная экспедиция'],
    'ФД': ['fd', 'new_fd', 'act_fd'],
    'первичный учетный документ': ['пуд', 'первичны(.)? учетны(.)? документ(.)?'],
    'вебдитейл': ['webdetail', 'вэбдитейл', 'web detail', 'вэб-дитеил', 'вэб-детализаци(.)?', 'вэб детализаци(.)?', 'вэб деталк(.)?', 'вэб-деталк(.)?'],
    'ора': ['ora', 'ora 12154: tns'],
    'презентация': ['преза', 'powerPoint', 'power point'],
    'библиотека': ['alpina digital', 'alpina', 'альпина'],
    'шэринг': ['шеринг', 'sharing'],
    'дмс': ['добровольное мед(\.)? страхование', 'дмс(.)?', 'добровольное медицинское страхование', 'мед(\.)? страхование', 'мед(\.)?страхование', 'добровольное страхование', 'мед(\.)? страховка', 'мед(\.)?страховка'],
    'правила трудового распорядка': ['правила внутреннего трудового распорядка', 'пвтр'],
    'ответственное должностное лицо': ['одл'],
    'горячая линия': ['гл'],
    'руководитель': ['рук-ль', 'начальник'],
    'эйчар эда': ['hr эда', 'айчар эда', 'filenet'],
    'хелпер': ['хэлпер', 'helper'],
    'софт': ['software', 'soft'],
    'пунто': ['punto', 'punto switcher'],
    'бар тендер': ['bar thender'],
    'адобе': ['adobe'],
    'ремотап': ['remoteapp', 'remote app', 'remote-app', 'ремотэп', 'ремотеп', 'remote ap', 'remoteap'],
    'жесткий диск': ['жёсткий диск', 'ssd', 'hdd'],
    'флешка': ['флэшк(.)?', 'flash', 'flash-накопител(.)?', 'флэш-накопител(.)?', 'флеш-накопител(.)?'],
    'соглашение о конфиденциальности': ['nda', 'нда', 'соглашение nda', 'соглашение нда'],
    'результат интеллектуальной деятельности': ['рид', 'результат интеллект(\.)? деятельности'],
    'макрорегион': ['мр', 'макро регион', 'макро'],
    'электронный документооборот': ['эдо', 'электронный документо оборот'],
    'юридически значимый документооборот': ['юридически значимый электронный документооборот', 'юздо'],
    'авансовый отчет': ['ао', 'аванс(\.)? отчет'],
    'основные средства': ['ос', 'основ(\.)? средства'],
    'единый план счетов': ['епс', 'ед(\.)? план счетов'],
    'транзакционный план счетов': ['тпс', 'транзакц(\.)? план счетов'],
    'универсальный передаточный документ': ['упд', 'универсал(\.)? передаточный документ'],
    'электронный документный архив': ['эда', 'эл(\.)? документный архив'],
    'счет фактура': ['сф', 'счет-фактур(.)?', 'счет фактур(.)?'],
    'учетная политика': ['уп', 'уч(\.)? политик(.)?'],
    'нематериальный актив': ['нма', 'не материальный актив'],
    'расходы будущих периодов': ['рбп', 'расходы буд(\.)? периодов'],
    'рар': ['rar', 'winrar'],
    'дилерская комиссия': ['дк', 'дилер(\.)? комиссия'],
    'бизнес процесс': ['бп', 'бизнес-процесс'],
    'транспортное средство': ['тс', 'транспорт(\.)? средство'],
    'лицо, ответственное за сохранность': ['лос', 'ответственного лицо за сохранность'],
    'корректирующий счет фактура': ['ксф', 'ксф+', 'ксф +', 'корректир(\.)? счет фактура', 'корректирующий счет-фактура'],
    'исправительный счет фактура': ['иссф', 'ис сф','исправит(\.)? счет фактура', 'исправительный счет-фактура'],
    'внутригрупповая операция': ['вго', 'внутри групповая операция', 'внутри-групповая операция', 'групповая операция', 'внут(\.)? групповая операция'],
    'бтл акция': ['btl-акция', 'btl акция', 'бтл-акция'],
    'инвентаризация имущества': ['3pl', '3 пл', '3 pl'],
    'начальная цена договора': ['нмц', 'начальная максимальная цена'],
    'закупка низкой стоимости': ['знс'],
    'предварительный квалификационный отбор': ['пко', 'предварительный квалифицированный отбор'],
    'федеральный закон': ['фз', 'фед(\.)? закон'],
    'план закупок': ['пз'],
    'задолженность': ['задолжность', 'за должность', 'задолженость'],
    'программа': ['прога', 'проги', 'програм(.)?'],
    'фблхн': ['fblxh'],
    'информационная безопасность': ['иб', 'информац(\.)? безопасность', 'информ(\.)? безопасность'],
    'хаб': ['USB-хаб(.)?', 'USBхаб(.)?', 'USB хаб(.)?', 'юэсби-хаб(.)?', 'юэсби хаб(.)?', 'юсб-хаб(.)?', 'юсбхаб(.)?', 'хаб(.)?'],
    'докстанция': ['док(\.)?станци(.)?', 'док(\.)? станци(.)?', 'докстанци(.)?', 'док—станци(.)?', 'док-станци(.)?'],
    'распечатать': ['распечать', 'разпечатать'],
    'скан': ['сканы'],
    'мвз': ['места возникновения затрат', 'МВЗ', 'места затрат'],
    'мвп': ['МВП', 'направление деятельности компании', 'направление деятельности кампании'],
    'маcсовая': ['маcов(\.)?'],
    
    #в основном общие
    'симка': ['sim-карт(.)?', 'сим карт\w*?', 'sim', 'симок', 'sim карт(.)?', 'сим-карт(.)?', 'сим', 'симкарт(.)?', 'simкарт(.)?'],
    'есим': ['esim', 'е-сим', 'е сим', 'e-sim', 'esim-карт(.)?', 'есим-карт(.)?', 'esim карт(.)?', 'есим карт(.)?', 'виртуальная sim', 'виртуальная сим', 'электронная сим'],
    'нано': ['nano'],
    'гигабайт': ['гб', 'gb', 'гиг(.)?', 'гигов', 'гигами', 'гбайт\w*', 'гибогайт(.)?', 'кигобайт(.)?', 'гигабвйт(.)?', 'гигобацт\w*'],
    'мегабайт': ['мегабаит(.)?', 'мега байт(.)?', 'mb', 'мб', 'мгб'],
    'килобайт': ['кб', 'kb', 'кило байт(.)?'],
    '2 джи': ['2g', '2g+', '2г', '2джи', '2-джи', '2жи', '2ж', '2 g', '2 г', '2 жи', 'edge', 'эдже', 'ешка', 'эдж'],
    '3 джи': ['3g', '3g+', '3г', '3джи', '3-джи', '3жи', '3ж', '3 g', '3 г', '3 жи', 'h+', 'h +', 'h плюс'],
    '4 джи': ['4g', '4g+', '4г', '4г+', '4джи', '4-джи', '4жи', '4ж', '4 g', '4 г', '4 жи', '4G LTE', 'LTE', 'лте', 'четыре джи'],
    '5 джи': ['5g', '5g+', '5г', '5джи', '5-джи', '5жи', '5ж', '5 g', '5 г', '5 жи'],
    'волте': ['volte', 'ims-сервис(.)?', 'ims-сервис(.)?', 'имс-сервис(.)?', 'имс сервис(.)?', 'во лте'],
    'жпрс': ['gprs', 'джипер(.)?'],
    'телефон': ['тлф', 'тилифон(.)?', 'тел'],    
    'андроид': ['adroid', 'android'],
    'гугл плей': ['google play', 'гугл плей', 'гугл плэй', 'плей маркет(.)?', 'плэй маркет(.)?', 'play market'],
    'айфон': ['ipfone', 'iphone', 'apple', 'ios'],
    'айпад': ['ipad', 'ай пад', 'айпэд', 'ай пэд'],
    'эпстор': ['appStore', 'app store', 'apple store', 'эппл store', 'эпл store'],
    'гет эпс': ['get apps', 'get aps'],
    'гугл': ['gogle', 'google', 'хром', 'chrome'],
    'вотсап': ['вац ап', 'вацап', 'ватсап(.)?', 'вассап', 'ватцап(.)?', 'ватс ап', 'whatsapp', 'whats app', 'whassup', 'whatsup', 'what`s app', 'воцап', 'ваттсап', 'вотцап(.)?'],
    'киви': ['qiwi', 'qivi'],
    'вай фай': ['wi fi', 'wi-fi', 'ви-фи', 'вифи', 'wifi', 'вай-фай', 'вайфай'],
    'пак код': ['puk-код(.)?', 'пук-код(.)?', 'puk код(.)?', 'puc код(.)?', 'пак-код(.)?', 'рuk код(.)?', 'паккод(.)?', 'пуккод(.)?', 'puk2', 'puk-2', 'пак2', 'пак-2', 'пак2 код', 'puk', 'пак', 'рак код'],
    'пин код': ['pin-код(.)?', 'pin код(.)?', 'пинкод', 'пин-код(.)?', 'pin2', 'pin-2', 'пин2', 'пин-2', 'пин 2', 'pin', 'пин'],
    'микс': ['mix(.)?', 'miks', 'михх'],
    'винк': ['wink(.)?', 'vink', 'wing'],
    'сообщение': ['сообщние', 'сообщния'],
    'смс': ['смс сообщени\w*', 'sms', 'sms сообщени\w*', 'эсэмэс\w*', 'смск(.)?', 'эсмс', 'смс-к(.)?'],
    'ммс': ['mms сообщени(.)?', 'mms', 'ммс сообщени(.)?', 'ммс-сообщение', 'mms-сообщение', 'ммск(.)?'],
    'юссд': ['ussd', 'uccd'],
    'чат бот': ['чат-бот', 'chat-bot', 'чатбот', 'чат', 'бот', 'chat', 'bot', 'онлайн помощник', 'онлайн-помощник'],
    'мнп': ['mnp'],
    'теле2': ['tele-2', 'tele2', 'теле 2', 'tele 2', 'теледва', 'теле два', 'теле'],
    'битуби': ['b2b', 'и2и', 'в2в','б2б'],
    'эмтуэм': ['m2m', 'ь2ь', 'v2v', 'м2м'],
    'айди': ['id'],
    'айди абонент': ['ID.абонент(.)?', 'ID.abonent', 'ИД.абонент(.)?', 'ID абонент(.)?', 'ИД абонент(.)?'],
    'ростелеком': ['ростеликом', 'ртк'],
    'айпи': ['IP'],
    'впн': ['vpn', 'випиэн'],
    'тариф': ['ТП', 'тараф(.)?', 'тапиф', 'ториф', 'таррив', 'тарив'],
    'говно': ['гавно', 'дермо'],
    'интернет': ['инет(.)?', 'internet', 'инт-т', 'интеренет', 'интирнет', 'ин т', 'ин-т', 'интерне'],
    'плохой интернет': ['интернет пропадает', 'интернет говно', 'интернет ужасный', 'говно ваш(.)? интернет', 'работа\w* интернет плох(.)?', 'интернет плох(.)? работа\w*', 'интернет работа\w* отстой\w*', 'интернет работа\w* плох(.)?', 'плох(.)? работа\w* интернет', 'говно у вас интернет', 'у вас интернет говно', 'интернет еле работа\w*', 'интернет еле еле работа\w*', 'интернет глючит', 'глючит интернет', 'интернет не ловит(.)?', 'не ловит(.)? вообще интернет(.)?', 'интернет постоянно прерывает\w*', 'интернет не грузит\w*'],
    'хотел бы': ['как я могу', 'как мы можем', 'каким образом я могу'],
    'интернет магазин': ['интернет-магазин', 'ИМ'],
    'мобильный': ['моб(\.)?','могильный'],
    'детализация': ['деталезаци(.)?', 'деталк(.)?', 'деталлизаци(.)?', 'дитализаци(.)?', 'дистилизаци(.)?', 'деталеровк(.)?', 'деталировк(.)?'],
    'дополнительный': ['доп(\.)?', 'дополнит(\.)?'],
    'финансовый': ['фин(\.)?', 'финансов(\.)?'],
    'административный': ['админ(\.)?', 'административ(\.)?'],
    'единственный': ['ед(\.)?', 'единств(\.)?'],
    'технический': ['тех(\.)?', 'технич(\.)?'],
    'количество': ['кол-во', 'кол во'],
    'учетная запись': ['уз', 'учетк(.)?', 'учётк(.)?', 'уч(\.)? запис(.)?', 'уч(\.)?запис(.)?', 'учетка ad', 'учетка ад'],
    'корпоративный': ['корп(\.)?', 'корпорат(\.)?'],
    'региональный': ['рег(\.)?'],
    'социальный': ['соц(\.)?', 'социал(\.)?'],
    'базовая станция': ['БС', 'баз(\.)? станци(.)?'],
    'государственный': ['гос(\.)?'],
    'государственное предприятие': ['госпредприяти(.)?', 'гос(\.)? предприяти(.)?'],
    'физический': ['физ(\.)?', 'физич(\.)?'],
    'физическое лицо': ['физ(\.)? лицо', 'фл', 'физ(\.)?лицо'],
    'электронный': ['эл(\.)?', 'электр(\.)?', 'электрон(\.)?'],
    'контентный лицевой счет': ['клс', 'кантентный лиц(.)? счет', 'контентный счет'],
    'обещанный платеж': ['обещенны(.)? платеж(.)?', 'обеденны(.)? платеж(.)?', 'обешенны(.)? платеж(.)?'],
    'другой': ['др.'],
    'исходящий': ['исх(\.)?'],
    'входящий': ['вх(\.)?'],
    'черный список': ['чс', 'чёрный список'],
    'поделиться': ['поделица', 'подилиться', 'подилится'],
    'паспортные данные': ['ПД', 'паспорт(.)? данные'],
    'личный кабинет': ['ЛК'],
    'абонентская служба': ['абонслужб\w*', 'абон(.)? служб(.)?', 'абоненслвжб'],
    'корректировка': ['корректировака', 'корректива', 'коррективка', 'корректовка'],
    'корректный': ['коректный', 'каректный'],
    'некорректный': ['некоректный', 'некаректный'],
    'платеж': ['платяж(.)?','платкж(.)?', 'платед(.)?', 'лптеж'],
    'положил': ['полоижил'],
    'рубли': ['руб(\.)?', '₽', 'р'],
    'миллион': ['милион', 'млн(\.)?', 'мллион', '1000000'],
    'миллион рублей': ['милион руб(\.)?', 'млн(\.)? руб(\.)?', 'млн.руб(\.)?'],
    'деньги': ['денги', 'лавэ'],
    'перевод денег': ['отправк(.)? денег', 'отправк(.)? денежных средств'],
    'перевести деньги': ['отправить деньги', 'отправить денежные средства'],
    'ошибочный': ['ошибный', 'ошиочнй'],
    'номер': ['елмер', 'номр'],
    'покрытия': ['покрвытичя', 'покрвтия', 'покрти(.)?', 'пркрыти(.)?', 'покрыьти(.)?', 'покртыи(.)?', 'покрпыти(.)?', 'покрвыти(.)?', 'порыти', 'поктыти(.)?', 'пкорытия'],
    'восстановить': ['восстиановит(.)?', 'восстоновт(.)?', 'восстоновит(.)?', 'восставновит(.)?', 'восстаовит(.)?', 'восстанвоит(.)?', 'восстановат(.)?', 'восстанвит(.)?', 'востоноваит(.)?', 'востановит(.)?', 'восстановитбь', 'востоноваит',],
    'восстановление': ['восстанорвлени(.)?', 'востановлерни(.)?', 'воссатновлени(.)?', 'восстанволени(.)?', 'востановдлени(.)?', 'востоновлени(.)?', 'восстанволни(.)?', 'восставнолни(.)?', 'вовтановлени(.)?', 'воссатвнолени(.)?'],
    'почините': ['прчините'],
    'ошибка': ['ашибка', 'ашипка', 'ошипка', 'ощибка'],
    'ошибочный': ['ошиочны(.)?'],
    'правильный': ['правельный'],
    'онлайн': ['онлаин', 'он-лайн'],
    'переоформление': ['переоыормлени(.)?', 'пероформлени(.)?'],
    'переоформить': ['приоформит(.)?', 'при оформит(.)?'],
    'пользователь': ['пользыватель'],
    'безлимитный': ['безлемит\w*', 'без лемит\w*', 'беслимит\w*', 'бес лимит\w*'],
    'пришло': ['пишло'],
    'приходят': ['приодят', 'призодят', 'поиходят'],
    'приходит': ['прходит'],
    'пароль': ['порол\w*'],
    'присутствие': ['присудстви(.)?'],
    'заказать': ['заказть'],
    'звонков': ['звоков'],    
    'субъект': ['субьект(.)?'],
    'Россия': ['Росия', 'рф'],
    'порядок':['правила'],

    #в основном для смоллтока
    'привет': ['hello', 'hi', 'bonjour', 'hallo', 'хай', 'салют', 'првет', 'привед', 'прмвет', 'перивет', 'приавет', 'пиривети', 'проивет', 'прывет', 'ассаламу алейкум', 'хеллоу', 'хелло', 'пирбет', 'хэй', 'йоу', 'дароу', 'фрибет', 'халоу', 'хэллоу', 'салам малейкум', 'здаров(.)?', 'преветик(.)?', 'привецтвую', 'Привет. Я.', 'привкт', 'пивет', 'приветстваю', 'ghbdtn', 'привеет', 'приивеет', 'приевт', 'приветик(.)?', 'при вед', 'привед', 'шалом', 'здвраво', 'здоров', 'здаровеньки', 'здоровеньки', 'здорова', 'п р и в е т', 'алоха', 'дарова', 'дороу', 'cалам', 'бонжур', 'бонжор', 'банжор', 'алейкум асалам', '(.)?салам алейкум', 'малейкум салам', 'хело', 'иоу', 'доров', 'двроу', 'пирвет', 'привте', 'приветствую'],
    'здравствуйте': ['здпавствуйте', 'здрайствуйте', 'здратсвуйте', 'здравствуте', 'здравствуйсте', 'здравсвуйте', 'здравствует', 'здравстауйте', 'здравтвуйте', 'здравстуите', 'дратути', 'здрауствуйте', 'здравствййте', 'здравчтвуйте', 'зчдраствуйте', 'здравмтвуйте', 'здравствите', 'здравстввйте', 'здюравствуй', 'здрастувуйте', 'здраствуфте', 'здрасвуйте', 'здрасивуйте', 'здравствейте', 'здравстувите', 'здравстувуйте', 'здравстствуйте', 'здраамтвуйте', 'зддравсивуйте', 'здоровствуйте', 'здравстуй', 'драсти', 'драсте', 'здрасти', 'сдрасти', 'хдраствуйте', 'здравствуй', 'здрасте', 'здравстуйик'],
    'добрый вечер': ['доьрыц вечер', 'добрій вечер', 'добр?й вечер', 'добрвый вечер', 'дорый вечр', 'добры вечрь', 'добрый веяер', 'добрый вечкр', 'доброе вчер', 'добры Йвечер', 'добрый весчер', 'добрый вечеп', 'добрый вечечер', 'добрый вкчер', 'доброго вечера', 'вечер добрый'],
    'добрый день': ['добрй день', 'добоый день', 'дбрый день', 'добрь день', 'доюрый день', 'добюрый день'],
    'доброе утро': ['добри уторо', 'доброе ктро', 'добрыя утро', 'добоый утро', 'доьрое утро', 'доброе утрл', 'утро лоброе'],
    'доброй ночи': ['добренькой ночи', 'добрейшей ночки', 'добротной ночечки'],
    'пока': ['адьос', 'bye', 'бай', 'покедова', 'покеда', 'аревуар', 'арревуар', 'бай-бай', 'гудбай', 'чау', 'чао', 'пака', 'до связи', 'до завтра', 'до свядания', 'досвиданья', 'досвидания', 'досвилание', 'до саидания', 'бай-бай', 'бот пока', 'поки', 'счастливо', 'спасибо.всего доброго', 'спасибо,всего доброго', 'спасибовсего доброго', 'бывай', 'поуа', 'прощай', 'бот прощай', 'досвидания бот(.)?'],
    'окей': ['ok', 'okey', 'ок', 'оки', 'оке'],
    'спасибо': ['thanks', 'thank you', 'thanks you', 'фенк ю', 'сенк ю', 'сенкью', 'спасиобо', 'смасибо', 'сбосибо', 'срасибо', 'спасиьот', 'спосиба', 'спасиблэо', 'спасыба', 'спачибо', 'сипасибо', 'сипасиба', 'смасибо', 'спасбо', 'паибо', 'спсибо', 'спксибо', 'спасиьот', 'сппсибо', 'виспасибо', 'спасмьо', 'спс', 'пасиб', 'мерси', 'спсасибо', 'спамибо', 'от души', 'ок.спасибо', 'пасибо', 'спасибки', 'cgfcb,j', 'Спосиба вам'],
    'понятно': ['понаятна', 'пончтно', 'поняятго', 'панятна', 'ясненько-понятненько', 'понел', 'панятно'],
    'конечно': ['канешна', 'ес оф кос', 'оф кос'],
    'почему': ['почиму', 'почемуттак', 'пояему', 'в связи с чем', 'связи с чем', 'с чем связан(.)?', 'с чем это связан(.)?', 'с чем это может быть связан(.)?', 'почечу', 'по чему'],
    'вы': ['ви'],
    'кино': ['кинчик'],
    'давай': ['ну-ка', 'ну ка', 'нука'],
    'зачем': ['жачем', 'зочем'],
    'чем занимаешься': ['чем маешься'],
    'посмотреть': ['позырить', 'пазырить'],
    'поболтаем': ['по болтам', 'потрищим', 'потрещим', 'го поговорим'],
    'поговорить': ['потрещать', 'потрищать'],
    'давай поболтаем': ['два поболтаем'],    
    'общаться': ['общьятся'],
    'как дела': ['как дила', 'каааак тыыы', 'как твои делища', 'какдела', 'каак вы'],
    'у меня': ['уменя'],
    'так': ['дак'],
    'зовут': ['завуд', 'завать', 'звать', 'зовус', 'зовуд'],
    'бензин': ['бенз(\.)?'],
    'пресс': ['прэсс'],
    'кэш': ['кеш'],
    'плохой': ['полохой'],
    'такси': ['таксос', 'таксо'],
    'ура': ['урааа'],
    'спокойной ночи': ['споки', 'споки ноки'],
    'испытываю': ['испываю'],
    'кайф': ['каеф'],
    'алло': ['оло', 'алле', 'алеее', 'алё', 'алее', 'олло', 'ало', 'але', 'аллоооо', 'алоооо', 'аллё'],
    'ага': ['агась'],
    'вы здесь': ['эээээй', 'ауууу', 'раз раз раз', 'вы на связи', 'куку', 'ку-ку', 'эгегей', 'Эу'],
    'нафига': ['накой фиг'],
    'фэнтези': ['фэнтэзи', 'фентези'],
    'не смешно': ['несмешно'],
    'с новым годом': ['хеппи нью еар', 'Happy New Year'],
    'триста': ['тристо'],
    'фото': ['фотк(.)?', 'фоту'],
    'работаешь': ['пашешь'],
    'не работает': ['не работки'],
    'не поступили': ['не пришли'],
    'спб': ['Питер(.)?'],
    'сири': ['siri'],
    'правила дорожного движения': ['ПДД'],
    'коронавирус': ['корона вирус', 'covid', 'covid-19', 'ковид'],
    'смешно': ['хехехе', 'хихи', 'ахаха', 'ха ха', 'хохохо', 'ха', 'аххха', 'азахвхвхв', 'xd', 'хд'],
    'да': ['yes', 'дааа', 'да-да', 'даааа'],
    'нет': ['нэт', 'ytn', 'no', 'not', 'неет'],
    'что': ['чо', 'че', 'чё', 'шо', 'што', 'чаво', 'чего', 'чиво', 'чиго', 'чидо', 'что-то', 'што-то', 'что то', 'што то'],
    'нужно': ['нужено'],
    'навыки': ['спасобнаст\w*', 'способност(.)?', 'умени(.)?' 'скил\w*'],
    'что нибудь': ['что-нибудь', 'чо нить', 'че нить', 'чё нить', 'чо нидь', 'че нидь', 'чё нидь','чидо нибуть', 'чо-нить', 'че-нить', 'чё-нить', 'чидо-нибудь'],
    'подработка': ['шабашк(.)?'],
    'музыка': ['музочк(.)?'],
    'огорчен': ['растроен'],
    'не благодари': ['не за че', 'не за чо'],
    'неправда': ['не правда'],
    'видео': ['видос(.)?'],
    'могу': ['магу'],
    'хочу': ['хачу'],
    'куда': ['гуда'],
    'меньше': ['менее'],
    'что такое': ['че такое', 'чо такое', 'чо означает'],
    'город': ['г.'],
    'виды': ['разновидност(.)?', 'клас(.)?', 'категори(.)?', 'тип(.)?'],
}
