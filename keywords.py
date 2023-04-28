pattern = {
    #в основном для хелпера
    'гугл': ['google', 'googl', 'gogle'],
    'яндекс': ['yandex', 'ya'],
    'маил': ['mail'],
    'диск': ['disk'],
    'прокси': ['proxy'],
    'сервер': ['server', 'сервир(\w)?'],
    'хром': ['chrome'],
    'плей': ['play', 'плэй'],
    'маркет': ['маркит(\w)?', 'market'],
    'вебим': ['wibim', 'vebim', 'webim', 'вэбим', 'вибим'],
    'инвойс': ['инвойс\w*', 'invoic(\w)?' 'invoic(\w)? clients', 'invoic(\w)? Admin', 'invoic(\w)? Inventory', 'inventory', 'инвойс админ', 'инвойс инвентори', 'инвойс клиент', 'invoice_clients'],
    'хелпдэск': ['help desk', 'helpdesk', 'хэлпдеск'],
    'скайп': ['skype', 'lync', 'линк(\w)?', 'skype for business', 'скайп для бизнеса'],
    'почта': ['out look', 'outlok', 'аутлук', 'корп(\.)? почта', 'корп(\.)?почта', 'outlook', 'outluk'],
    'вебмейл': ['webmail', 'вэбмейл', 'вэб-мейл', 'веб-мейл'],
    'облачный офис': ['ofice 365', 'office 365', 'офис 365', 'teams', 'word', 'excel', 'oneNote', 'access'],
    'майкрософт офис': ['office', 'microsoft office'],
    'авайя': ['avaya', 'авайка', 'авая', 'аваи'],
    'сервисдеск': ['sd', 'servicedesk', 'bpmonline service desk', 'bpmonline', 'bpm', 'bpm7', 'бпм', 'bpm-servicedesk', 'bpm servicedesk', 'service desk', 'servic desk', 'servicdesk', 'бпм servicedesk', 'бпм-servicedesk', 'бпм-сервисдеск', 'бпм сервисдеск'],
    'ср': ['SR'],
    'виндовс': ['vindovs', 'windows', 'винда', 'виндоус', 'виндов', 'винда'],
    'фтп': ['sftp', 'ftp', 'сфтп'],
    'циско': ['cisco', 'циска', 'сиско', 'AnyConnect', 'Any Connect', 'cisco anyconnec', 'anyconnec'],
    'ддр': ['double data rate', 'ddr', 'double rate', 'ddr sdram', 'ddr sd'],
    'ссд накопитель': ['ssd'],
    'поликом ': ['polycom'],
    'ван икс': ['One-x', 'One x'],
    'cофтфон': ['Софт фон', 'Софтфон x'],
    'вок зе ток': ['walk talk', 'walk the talk', 'walk the tolk', 'wolk the tolk', 'wolk the talk', 'вок зэ ток'],
    'забота теле2': ['Tele2 care', 'Tele2 cere'],
    'вди': ['vdi', 'инфраструктура виртуальных рабочих столов', 'виртуальный рабочий стол'],
    'администратор':['админ'],
    'файрвол': ['фаервол', 'брандмауэр', 'брендмауэр', 'firewall', 'файерволл'],
    'антивирус': ['касперский', 'kasperskii', 'kaspersky'],
    'электронная подпись': ['эцп', 'эр', 'унэп', 'укэп', 'эп', 'эл(\.)?подпись', 'цифровая подпись', 'графическая подпись'],
    'кьюар': ['qr', 'qr-код', 'qr', 'кью ар', 'кью'],
    'простая электронная подпись': ['ПЭП', 'ПЕП'],
    'сап': ['sар', 'sap'],
    'рдб': ['pdb', 'rdb'],
    'скьюл': ['sql'],
    'пинто свичер': ['punto switcher', 'пинто свитч(\w)?', 'пунто свитч(\w)?', 'punto', 'пунто'],
    '2гис': ['2GIS', '2 GIS', 'два GIS', 'ту GIS' , '2-GIS'],
    'анализис': ['analysis'],
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
    'апекс': ['apeks', 'apex', 'арех', 'апекс(\w)?'],
    'двх': ['dvh', 'dwh'],
    'прм': ['prm'],
    'рбт': ['pbt', 'rbt'],
    'едв': ['edv', 'edw', 'едв'],
    'срм': ['crm'],
    'гвардиум': ['гуардиум', 'guardium'],
    'бпс': ['сап bpc','сап бпс', 'sap bps', 'bpc', 'бпс', 'Business Planning and Consolidation', 'Business Planning Consolidation', 'Business Planning', 'Planning Consolidation', 'Business Consolidation'],
    'ерп': ['сап erp', 'сап ерп','sap erp', 'erp', 'ерп', 'Enterprise Resource Planning', 'Enterprise Resource', 'Enterprise Planning', 'Resource Planning'],
    'сард': ['sard'],
    'смс центр': ['smsc', 'смсц', 'sms-центр', 'смс-центр'],
    'ммс центр': ['mmsc', 'ммсц', 'mms-центр', 'ммс-центр'],
    'юссд центр': ['юссдц', 'ussd-центр', 'ussdc', 'юссд-центр'],
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
    'программа пдф': ['pdf', 'пдф'],
    'бартендер': ['bartender', 'bar tender', 'бар тендер', 'bar tender'],
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
    'юсб': ['usb', 'юэсб(\w)?'],
    'ахр': ['административно хозяйственные расходы', 'адм(\.)? хоз(\.)? расходы', 'хоз(\.)? расходы', 'административно-хозяйственные расходы', 'административные расходы', 'админ(\.)? расходы', 'хозяйственные расходы'],
    'ситрикс': ['sitrix', 'citrix', 'цитрикс'],
    'ссд': ['ssd'],
    'жабра': ['jabra'],
    'аналитический': ['аналит(\.)?', 'аналитич(\.)?', 'аналетическ\w*'],
    'ОНС': ['объект(\w)? незавершенного строительства', 'объект(\w)? неоконченного строительства', 'объект(\w)? неоконченого строительства'],
    'ОКС': ['объект(\w)? капитального строительства', 'капетального строительства'],
    'ГПЗУ': ['градостроительн\w* план земельн\w* участк(\w)?', 'градостроительн\w* план земл(\w)?', 'градостроительн\w* план участк(\w)?', 'градостроительн\w* план'],
    'некапитальные': ['не капитальные'],
    'ИТО': ['инженерно-техническо\w* обеспечени(\w)?', 'инженерно техническо\w* обеспечени(\w)?', 'сетей инженерно-технического обеспечения', 'сети инженерно-технического обеспечения', 'сети ИТО', 'сетей ИТО'],
    'недвижимость': ['не движимость'],
    'ЕНК': ['едины(\w)? недвижимы(\w)? комплекс(\w)?'],
    'СРО': ['саморегулируемые организаци(\w)?', 'само регулируемые организаци(\w)?', 'само регулируемая организаци(\w)?', 'саморегулируемая организаци(\w)?'],
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
    'материальная помощь': ['мат(\.)? помощь', 'матпомощь', 'мотериальная помощь', 'денежная помощь', 'мат.помощь'],
    'дополнительное соглашение': ['доп(\.)? соглашение', 'доп(\.)?соглашение', 'допалнительное соглашение', 'допник(\w)?', 'дс'],
    'хозяйственный': ['хоз(\.)?', 'хазяйственны(\.)?'],
    'бухгалтерский': ['бух(\.)?'],
    'коммерческий': ['ком(\.)?', 'комерческий', 'камерческий'],
    'коммерческое предложение': ['ком(\.)?предложение', 'ком(\.)? предложение', 'кп'],
    'компьютер': ['пк', 'комп'],
    'мфу': ['многофункционально(\w)? устройств(\w)?', 'много функциональное устройство', 'функциональное устройство'],
    'сопроводительный': ['сопровод(\.)?'],
    'биллинг': ['biling', 'billing', 'билинг(\w)?'],
    'аук': ['auc'],
    'авз': ['акты взаимозачетов с дилерами', 'акты взаимозачетов дилерами', 'акт взаимозачетов дилерами', 'акт взаимозачетов с дилерами'],
    'контактный центр': ['кц', 'контакт-центр', 'колл-центр', 'колл центр', 'звонковый центр'],
    'удаленный доступ': ['удалёнк(\w)?', 'удаленк(\w)?', 'удалён\w* доступ(\w)?', 'удален\w* доступ(\w)?'],
    'удаленная работа': ['удален\w* работа', 'удалён\w* работа', 'работа из дома', 'работать удаленно', 'работать удалённо', 'работать на удалёнке', 'работать на удаленке'],
    'центральная функция': ['цф', 'центр(\.)? функция'],
    'служебная записка': ['сз', 'служебка'],
    'сверхурочная работа': ['сву'],
    'работа в выходной': ['рв', 'рвд', 'работа в выходной день'],
    'айти': ['it', 'айтишник(\w)?', 'it админ', 'it-специалист(\w)?', 'it admin', 'айти-специалист(\w)?', 'ит-специалист(\w)?'],
    'сапорт': ['support'],
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
    '2 ндфл': ['2-ндфл','2ндфл','ндфл2','ндфл-2','ндфл','ндфл 2', '2 нддфл'],
    'страхование жизни': ['сж', 'страховка жизни'],
    'несчастный случай': ['нс', 'не счастный случай'],
    'зарплата': ['зп', 'зар(\.)? плата', 'заработная плата', 'з/п'],
    'локальные нормативные акты': ['лна', 'локально-нормативные акты'],
    'видеонаблюдение': ['видео наблюдение', 'trassir', 'трассир'],
    'транспортно экспедиторское обслуживание': ['тэо', 'обслуживание транспортной экспедиции', 'обслуживание по транспортной экспедиции', 'транспортно-экспедиторское обслуживание', 'транспортную экспедицию', 'транспортная экспедиция'],
    'ФД': ['fd', 'new_fd', 'act_fd'],
    'первичный учетный документ': ['пуд', 'первичны(\w)? учетны(\w)? документ(\w)?'],
    'вебдитейл': ['webdetail', 'вэбдитейл', 'web detail', 'вэб-дитеил', 'вэб-детализаци(\w)?', 'вэб детализаци(\w)?', 'вэб деталк(\w)?', 'вэб-деталк(\w)?'],
    'ора': ['ora', 'ora 12154: tns'],
    'презентация': ['преза', 'powerPoint', 'power point'],
    'библиотека': ['alpina digital', 'alpina', 'альпина'],
    'шэринг': ['шеринг', 'sharing'],
    'дмс': ['добровольное мед(\.)? страхование', 'дмс(\w)?', 'добровольное медицинское страхование', 'мед(\.)? страхование', 'мед(\.)?страхование', 'добровольное страхование', 'мед(\.)? страховка', 'мед(\.)?страховка'],
    'правила трудового распорядка': ['правила внутреннего трудового распорядка', 'пвтр'],
    'ответственное должностное лицо': ['одл'],
    'горячая линия': ['гл'],
    'руководитель': ['рук-ль', 'начальник'],
    'файлнэт': ['filenet'],
    'хелпер': ['хэлпер', 'helper'],
    'софт': ['software', 'soft'],
    'пунто': ['punto', 'punto switcher'],
    'адобе': ['adobe'],
    'бест': ['best'],
    'ремотап': ['remoteapp', 'remote app', 'remote-app', 'ремотэп', 'ремотеп', 'remote ap', 'remoteap'],
    'жесткий диск': ['жёсткий диск', 'hdd', 'hard disk drive', 'hard disk', 'hard drive', 'hard диск', 'хард диск', 'хард'],
    'ноутбук': ['бук\w*', 'ноут\w*'],
    'флешка': ['флэшк(\w)?', 'flash', 'flash-накопител(\w)?', 'флэш-накопител(\w)?', 'флеш-накопител(\w)?'],
    'соглашение о конфиденциальности': ['nda', 'нда', 'соглашение nda', 'соглашение нда'],
    'результат интеллектуальной деятельности': ['рид', 'результат интеллект(\.)? деятельности'],
    'макрорегион': ['мр', 'макро регион', 'макро'],
    'электронный документооборот': ['эдо', 'электронный документо оборот'],
    'юридически значимый документооборот': ['юридически значимый электронный документооборот', 'юздо'],
    'единый план счетов': ['епс', 'ед(\.)? план счетов'],
    'транзакционный план счетов': ['тпс', 'транзакц(\.)? план счетов'],
    'универсальный передаточный документ': ['упд', 'универсал(\.)? передаточный документ'],
    'электронный документный архив': ['эда', 'эл(\.)? документный архив'],
    'счет фактура': ['сф', 'счет-фактур(\w)?', 'счет фактур(\w)?'],
    'учетная политика': ['уп', 'уч(\.)? политик(\w)?'],
    'нематериальный актив': ['нма', 'не материальный актив'],
    'расходы будущих периодов': ['рбп', 'расходы буд(\.)? периодов'],
    'рар': ['rar', 'winrar'],
    'зип': ['zip'],
    'вачдок': ['watchdoc'],
    'хониуэлл': ['honeywell'],
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
    'еодин': ['e1', 'e-1', 'e1-procurement', 'e1 procurement', 'е1'],
    'предварительный квалификационный отбор': ['пко', 'предварительный квалифицированный отбор'],
    'федеральный закон': ['фз', 'фед(\.)? закон'],
    'план закупок': ['пз'],
    'задолженность': ['задолжность', 'за должность', 'задолженость'],
    'программа': ['праграмма', 'праграма', 'прога', 'проги', 'програм(\w)?'],
    'фблхн': ['fblxh'],
    'информационная безопасность': ['иб', 'информац(\.)? безопасность', 'информ(\.)? безопасность'],
    'хаб': ['хаб(\w)?', 'USBхаб(\w)?', 'юсбхаб(\w)?', 'hub'],
    'докстанция': ['док(\.)?станци(\w)?', 'док(\.)? станци(\w)?', 'докстанци(\w)?', 'док—станци(\w)?', 'док-станци(\w)?'],
    'распечатать': ['распечать', 'разпечатать'],
    'скан': ['сканы'],
    'мвз': ['места возникновения затрат', 'МВЗ', 'места затрат'],
    'мвп': ['МВП', 'направление деятельности компании', 'направление деятельности кампании'],
    'маcсовая': ['маcов(\.)?'],
    
    #в основном общие
    'симка': ['sim-карт(\w)?', 'сим карт\w*?', 'sim', 'симок', 'sim карт(\w)?', 'сим-карт(\w)?', 'сим', 'симкарт(\w)?', 'simкарт(\w)?', 'сим к(\w)?'],
    'есим': ['esim', 'е-сим', 'е сим', 'e-sim', 'esim-карт(\w)?', 'есим-карт(\w)?', 'esim карт(\w)?', 'есим карт(\w)?', 'виртуальная sim', 'виртуальная сим', 'электронная сим', 'есимк(\w)?'],
    'нано': ['nano'],
    'гигабайт': ['гб(\w)?', 'gb', 'гиг(\w)?', 'гигов', 'гигами', 'гбайт\w*', 'гибогайт(\w)?', 'кигобайт(\w)?', 'гигабвйт(\w)?', 'гегабвйт(\w)?', 'гигобацт\w*', 'гигаб', 'гега', 'гбт(\w)?'],
    'мегабайт': ['мегабаит(\w)?', 'мега байт(\w)?', 'mb', 'мб', 'мгб', 'мбат'],
    'килобайт': ['кб', 'kb', 'кило байт(\w)?'],
    '2 джи': ['2g', '2g+', '2г', '2джи', '2-джи', '2жи', '2ж', '2 g', '2 г', '2 жи', 'edge', 'эдже', 'ешка', 'эдж'],
    '3 джи': ['3g', '3g+', '3г', '3джи', '3-джи', '3жи', '3ж', '3 g', '3 г', '3 жи', 'h+', 'h +', 'h плюс'],
    '4 джи': ['4g', '4g+', '4г', '4г+', '4джи', '4-джи', '4жи', '4ж', '4 g', '4 г', '4 жи', '4G LTE', 'LTE', 'лте', 'четыре джи'],
    '5 джи': ['5g', '5g+', '5г', '5джи', '5-джи', '5жи', '5ж', '5 g', '5 г', '5 жи'],
    'волте': ['volte', 'ims-сервис(\w)?', 'ims-сервис(\w)?', 'имс-сервис(\w)?', 'имс сервис(\w)?', 'во лте'],
    'жпрс': ['gprs', 'джипер(\w)?'],
    'телефон': ['тлф', 'тилифон(\w)?', 'тел'],    
    'андроид': ['adroid', 'android'],
    'айфон': ['ipfone', 'iphone', 'apple', 'ios'],
    'айпад': ['ipad', 'ай пад', 'айпэд', 'ай пэд'],
    'эпстор': ['appStore', 'app store', 'apple store', 'эппл store', 'эпл store'],
    'гет эпс': ['get apps', 'get aps'],
    'вотсап': ['вац ап', 'вацап', 'ватсап(\w)?', 'вассап', 'ватцап(\w)?', 'ватс ап', 'whatsapp', 'whats app', 'whassup', 'whatsup', 'what`s app', 'воцап', 'ваттсап', 'вотцап(\w)?'],
    'вк': ['vkontakte', 'vk'],
    'вк музыка': ['вк музык(\w)?', 'vkmusic', 'vk music'],
    'фейсбук': ['facebook'],
    'твиттер': ['twitter', 'twiter', 'twit', 'твитер'],
    'вайбер': ['вибер', 'ваибер', 'viber'],
    'киви': ['qiwi', 'qivi'],
    'сбербанк': ['сбанк(\w)?'],
    'вай фай': ['wi fi', 'wi-fi', 'ви-фи', 'вифи', 'wifi', 'вай-фай', 'вайфай', 'ви фи'],
    'теледвагость': ['tele2guest', 'tele2 guest', 'tele2-guest', 'guest tele2'],
    'теледвакорп': ['tele2corp', 'tele2 corp', 'tele2-corp', 'сorp tele2'],
    'пак': ['puk-код(\w)?', 'puck', 'пук-код(\w)?', 'puk код(\w)?', 'puc код(\w)?', 'пак-код(\w)?', 'рuk код(\w)?', 'паккод(\w)?', 'пуккод(\w)?', 'puk2', 'puk-2', 'пак2', 'пак-2', 'пак2 код', 'puk', 'рак код', 'пук код'],
    'пин': ['pin-код(\w)?', 'pin код(\w)?', 'пинкод', 'пин-код(\w)?', 'pin2', 'pin-2', 'пин2', 'пин-2', 'пин 2', 'pin'],
    'микс': ['mix(\w)?', 'miks', 'михх', 'мих', 'миксс', 'миксит'],
    'макс': ['max'],
    'м': ['m'],
    'с': ['s'],
    'л': ['l', 'эль'],
    'хл': ['xl'],
    'винк': ['wink(\w)?', 'vink', 'wing'],
    'ютуб': ['you tub(\w)?', 'youtub(\w)?', 'ютюб'],
    'сообщение': ['сообщние', 'сообщния'],
    'смс': ['смс сообщени\w*', 'sms', 'sms сообщени\w*', 'эсэмэс\w*', 'смск(\w)?', 'эсмс', 'смс-к(\w)?'],
    'ммс': ['mms сообщени(\w)?', 'mms', 'ммс сообщени(\w)?', 'ммс-сообщение', 'mms-сообщение', 'ммск(\w)?'],
    'юссд': ['ussd', 'uccd'],
    'чат бот': ['чат-бот', 'chat-bot', 'чатбот', 'chat', 'bot', 'онлайн помощник', 'онлайн-помощник'],
    'мнп': ['mnp'],
    'фрэндс': ['friends'],
    'теле2': ['tele-2', 'tele2', 'теле 2', 'tele 2', 'теледва', 'теле два', 'теле', 'телле 2', 'телле2', 'т2'],
    'т2 мобаил': ['т2 мобайл', 'т2-мобайл', 'т2-мобаил'],
    'битуби': ['b2b', 'и2и', 'в2в','б2б'],
    'эмтуэм': ['m2m', 'ь2ь', 'v2v', 'м2м'],
    'айди': ['id'],
    'айди абонент': ['ID.абонент(\w)?', 'ID.abonent', 'ИД.абонент(\w)?', 'ID абонент(\w)?', 'ИД абонент(\w)?'],
    'ростелеком': ['ростеликом', 'ртк'],
    'айпи': ['IP'],
    'впн': ['vpn', 'випиэн'],
    'тариф': ['ТП', 'тараф(\w)?', 'тапиф', 'ториф', 'таррив(\w)?', 'тарив(\w)?', 'тариы', 'твриф', 'тартф', 'тприф', 'таариф', 'трариф', 'тармфы', 'тарий', 'тармф(\w)?', 'таиифы'],
    'тарифы': ['тарифв'],
    'говно': ['гавно', 'дермо'],
    'интернет': ['инет\w*', 'internet', 'интырнкт', 'тньернет', 'инэт', 'инт-т', 'интеренет', 'интирнет', 'ин т', 'ин-т', 'интерне', 'иньернет(\w)?', 'интернкт(\w)?', 'интенет(\w)?', 'иниернет(\w)?', 'интнрнет(\w)?', 'интернер'],
    'плохой интернет': ['интернет пропадает', 'интернет говно', 'интернет ужасный', 'говно ваш(\w)? интернет', 'работа\w* интернет плох(\w)?', 'интернет плох(\w)? работа\w*', 'интернет работа\w* отстой\w*', 'интернет работа\w* плох(\w)?', 'плох(\w)? работа\w* интернет', 'говно у вас интернет', 'у вас интернет говно', 'интернет еле работа\w*', 'интернет еле еле работа\w*', 'интернет глючит', 'глючит интернет', 'интернет не ловит(\w)?', 'не ловит(\w)? вообще интернет(\w)?', 'интернет постоянно прерывает\w*', 'интернет не грузит\w*', 'не ловит(\w)? интернет', 'интернет работает не стабильно', 'интернет не работает стабильно'],
    'хотел бы': ['как я могу', 'как мы можем', 'каким образом я могу'],
    'интернет магазин': ['интернет-магазин'],
    'девопс': ['devops'],
    'мобильный': ['моб(\.)?','могильный'],
    'детализация': ['деталезаци(\w)?', 'деталк(\w)?', 'деталлизаци(\w)?', 'дитализаци(\w)?', 'дистилизаци(\w)?', 'деталеровк(\w)?', 'деталировк(\w)?'],
    'дополнительный': ['доп(\.)?', 'дополнит(\.)?'],
    'финансовый': ['фин(\.)?', 'финансов(\.)?'],
    'административный': ['админ(\.)?', 'административ(\.)?'],
    'единственный': ['ед(\.)?', 'единств(\.)?'],
    'технический': ['тех(\.)?', 'технич(\.)?'],
    'количество': ['кол-во', 'кол во'],
    'учетная запись': ['уз', 'учетк(\w)?', 'учётк(\w)?', 'уч(\.)? запис(\w)?', 'уч(\.)?запис(\w)?', 'учетка ad', 'учетка ад', 'ad', 'active directory', 'учётка ad', 'учётка ад'],
    'корпоративный': ['корп(\.)?', 'корпорат(\.)?', 'копораимвны(\w)?'],
    'региональный': ['рег(\.)?'],
    'социальный': ['соц(\.)?', 'социал(\.)?'],
    'базовая станция': ['БС', 'баз(\.)? станци(\w)?'],
    'государственный': ['гос(\.)?'],
    'государственное предприятие': ['госпредприяти(\w)?', 'гос(\.)? предприяти(\w)?'],
    'физический': ['физ(\.)?', 'физич(\.)?'],
    'физическое лицо': ['физ(\.)? лицо', 'фл', 'физ(\.)?лицо'],
    'электронный': ['эл(\.)?', 'электр(\.)?', 'электрон(\.)?'],
    'контентный лицевой счет': ['клс', 'кантентный лиц(\w)? счет', 'контентный счет'],
    'платеж': ['платяж(\w)?','платкж(\w)?', 'платед(\w)?', 'лптеж', 'плотешь', 'плотж', 'платнж', 'платеш', 'платёш', 'платож'],
    'обещанный платеж': ['обещен\w* платеж(\w)?', 'обеден\w* платеж(\w)?', 'обешен\w* платеж(\w)?', 'обешен\w* платёж', 'обещаны(\w)? платеж(\w)?', 'обещанаия платёж', 'обещаны(\w)? платёж(\w)?', 'обнщаны(\w)? платеж(\w)?', 'оп', 'ебещан\w* платеж(\w)?', 'общен\w* платёж', 'обещин\w* платёж', 'обешан\w* платёж', 'обещае\w* платеж(\w)?', 'обещ(\.)? платеж(\w)?', 'обещ(\.)? платёж'],
    'долг': ['долк', 'долн'],
    'другой': ['др(\.)'],
    'исходящий': ['исх(\.)?'],
    'входящий': ['вх(\.)?'],
    'черный список': ['чс', 'чёрный список'],
    'поделиться': ['поделица', 'подилиться', 'подилится'],
    'паспортные данные': ['ПД', 'паспорт(\w)? данные'],
    'личный кабинет': ['ЛК'],
    'абонентская служба': ['абонслужб\w*', 'абон(\w)? служб(\w)?', 'абоненслвжб'],
    'оператор': ['апиратор(\w)?'],
    'корректировка': ['корректировака', 'корректива', 'коррективка', 'корректовка'],
    'корректный': ['коректный', 'каректный'],
    'некорректный': ['некоректный', 'некаректный'],    
    'положил': ['полоижил'],
    'рубли': ['руб(\.)?', '₽', 'р'],
    'миллион': ['милион', 'млн(\.)?', 'мллион', '1000000'],
    'миллион рублей': ['милион руб(\.)?', 'млн(\.)? руб(\.)?', 'млн.руб(\.)?'],
    'деньги': ['денги', 'лавэ', 'теньги'],
    'перевод денег': ['отправк(\w)? денег', 'отправк(\w)? денежных средств'],
    'перевести деньги': ['отправить деньги', 'отправить денежные средства'],
    'отправляются': ['отроавляются'],
    'ошибочный': ['ошибный', 'ошиочнй', 'ошиочны(\w)?'],
    'номер': ['елмер', 'номр'],
    'покрытия': ['покрвытичя', 'покрвтия', 'покрти(\w)?', 'пркрыти(\w)?', 'покрыьти(\w)?', 'покртыи(\w)?', 'покрпыти(\w)?', 'покрвыти(\w)?', 'порыти', 'поктыти(\w)?', 'пкорытия'],
    'восстановить': ['востоновит(\w)?', 'восстиановит(\w)?', 'восстоновт(\w)?', 'восстоновит(\w)?', 'восставновит(\w)?', 'восстаовит(\w)?', 'восстанвоит(\w)?', 'восстановат(\w)?', 'восстанвит(\w)?', 'востоноваит(\w)?', 'востановит(\w)?', 'восстановитбь', 'востоноваит'],
    'восстановление': ['восстанорвлени(\w)?', 'востановлерни(\w)?', 'воссатновлени(\w)?', 'восстанволени(\w)?', 'востановдлени(\w)?', 'востоновлени(\w)?', 'восстанволни(\w)?', 'восставнолни(\w)?', 'вовтановлени(\w)?', 'воссатвнолени(\w)?', 'Востанови', 'востановка', 'востанов', 'ВОСТАНОВИЧ'],
    'почините': ['прчините'],
    'ошибка': ['ашибка', 'ашипка', 'ошипка', 'ощибка', 'ожибка'],
    'правильный': ['правельный'],
    'онлайн': ['онлаин', 'он-лайн', 'он лайн'],
    'переоформление': ['переоыормлени(\w)?', 'пероформлени(\w)?'],
    'переоформить': ['приоформит(\w)?', 'при оформит(\w)?'],
    'пользователь': ['пользыватель'],
    'безлимит': ['анлим', 'unlim', 'без лимт', 'без лимит', 'безлемит'],
    'безлимитный': ['безлемит\w*', 'без лемит\w*', 'беслимит\w*', 'бес лимит\w*'],
    'пришло': ['пишло'],
    'пришел': ['пирошло'],
    'подаренные': ['пожарен(\w)?'],
    'приходят': ['приодят', 'призодят', 'поиходят', 'приходятся'],
    'приходит': ['прходит', 'приходчи'],
    'пароль': ['порол\w*'],
    'присутствие': ['присудстви(\w)?'],
    'заказать': ['заказть'],
    'звонков': ['звоков'],    
    'субъект': ['субьект(\w)?'],
    'Россия': ['Росия', 'рф', 'росий'],
    'раздача': ['расдача', 'расдяча', 'рездача', 'роздача', 'раздоча', 'раздвча', 'ращдача', 'рпздача', 'разадача', 'раздачик'],
    'не могу': ['немогу', 'немагу'],
    'включите': ['врубите'],
    'онлайн+': ['онлаин плюс', 'онлаин плюс', 'онлайн \+', 'онлаин\+', 'онлаин \+'],
    'классический': ['классичкий'],
    'списали': ['спесали'],
    'заблокировать': ['заблокироваеть', 'заблокироватб'],
    'скидка': ['скидока', 'скитка'],
    'дорого': ['дррого', 'доргго', 'дортго'],
    'автоплатеж': ['автоплатежь', 'авто платеж'],
    'дешёвый': ['не дорог\w*', 'недоро\w*', 'дёшев\w*', 'дешов\w*', 'дишов\w*', 'дешев\w*', 'дишев\w*', 'жешов\w*'],
    'абонентская': ['абанентская', 'обонентская', 'обанетская', 'абон(\w)?', 'обоненская', 'обон'],
    'вип': ['VIP'],
    'селекшен': ['Selection'],
    'не': ['нп'],
    'звонить': ['заонить'],
    'звонит': ['зиванит'],
    'мир танков': ['World of tanks'],
    'блэк': ['блейк', 'Black'],
    'стоимость': ['Стомость',],
    'абонентская плата': ['АП', 'абон(\.)?плата', 'абон(\w)? плат(\w)?', 'абанентски рлата', 'анон плат(\w)?', 'обенент плат(\w)?'],
    'разблокируйте': ['Расблоктруйте', 'Black'],
    'сколько': ['скок(\w)?', 'сколко'],
    'миа': ['мия', 'мии'],
    'подключить': ['потклучит(\w)?', 'потключит(\w)?', 'подклучит(\w)?', 'падклучит(\w)?', 'подкуличит(\w)?', 'поткючит(\w)?', 'подкл(\.)?'],
    'подключен': ['потключен'],
    'подключил': ['потключил'],
    'отключить': ['атклечить', 'отлючить', 'откл(\.)?'],
    'подписки': ['падписки', 'подпискв', 'прдаиску', 'Black'],
    'модем': ['мадем'],
    'роутер': ['раутер(\w)?'],
    'раздавать': ['раздовать', 'роздовать'],
    'кончился': ['кончилца'],
    'рекуррентный платеж': ['оэдс', 'одэс', 'рекурентны(\w)? платеж(\w)?', 'реккурентны(\w)? платеж(\w)?'],
    'анти аон': ['антиаон(\w)?'],
    'спам': ['спем'],
    'док+': ['doc\+', 'doc \+'],
    'погасить': ['пагосить'],

    #в основном для смоллтока
    'привет': ['hello', 'hi', 'bonjour', 'hallo', 'хай', 'салют', 'првет', 'привед', 'прмвет', 'перивет', 'приавет', 'пиривети', 'проивет', 'прывет', 'салам', 'ассаламу алейкум', 'хеллоу', 'хелло', 'пирбет', 'хэй', 'йоу', 'дароу', 'фрибет', 'халоу', 'хэллоу', 'салам малейкум', 'здаров(\w)?', 'преветик(\w)?', 'привецтвую', 'Привет. Я.', 'привкт', 'пивет', 'приветстваю', 'ghbdtn', 'привеет', 'приивеет', 'приевт', 'приветик(\w)?', 'при вед', 'привед', 'шалом', 'здвраво', 'здоров', 'здаровеньки', 'здоровеньки', 'здорова', 'п р и в е т', 'алоха', 'дарова', 'дороу', 'cалам', 'бонжур', 'бонжор', 'банжор', 'алейкум асалам', '(\w)?салам алейкум', 'малейкум салам', 'хело', 'иоу', 'доров', 'двроу', 'пирвет', 'привте', 'приветствую'],
    'здравствуйте': ['здпавствуйте', 'здрайствуйте', 'здратсвуйте', 'здравствуте', 'здравствуйсте', 'здравсвуйте', 'здравствует', 'здравстауйте', 'здравтвуйте', 'здравстуите', 'дратути', 'здрауствуйте', 'здравствййте', 'здравчтвуйте', 'зчдраствуйте', 'здравмтвуйте', 'здравствите', 'здравстввйте', 'здюравствуй', 'здрастувуйте', 'здраствуфте', 'здрасвуйте', 'здрасивуйте', 'здравствейте', 'здравстувите', 'здравстувуйте', 'здравстствуйте', 'здраамтвуйте', 'зддравсивуйте', 'здоровствуйте', 'здравстуй', 'драсти', 'драсте', 'здрасти', 'сдрасти', 'хдраствуйте', 'здравствуй', 'здрасте', 'здравстуйик'],
    'добрый вечер': ['доьрыц вечер', 'добрій вечер', 'добр?й вечер', 'добрвый вечер', 'дорый вечр', 'добры вечрь', 'добрый веяер', 'добрый вечкр', 'доброе вчер', 'добры Йвечер', 'добрый весчер', 'добрый вечеп', 'добрый вечечер', 'добрый вкчер', 'доброго вечера', 'вечер добрый'],
    'добрый день': ['добрй день', 'добоый день', 'дбрый день', 'добрь день', 'доюрый день', 'добюрый день'],
    'доброе утро': ['добри уторо', 'доброе ктро', 'добрыя утро', 'добоый утро', 'доьрое утро', 'доброе утрл', 'утро лоброе'],
    'доброй ночи': ['добренькой ночи', 'добрейшей ночки', 'добротной ночечки'],
    'пока': ['адьос', 'bye', 'бай', 'покедова', 'покеда', 'аревуар', 'арревуар', 'бай-бай', 'гудбай', 'чау', 'чао', 'пака', 'до связи', 'до завтра', 'до свядания', 'досвиданья', 'досвидания', 'досвилание', 'до саидания', 'бай-бай', 'бот пока', 'поки', 'счастливо оставаться', 'спасибо.всего доброго', 'спасибо,всего доброго', 'спасибовсего доброго', 'бывай', 'поуа', 'прощай', 'бот прощай', 'досвидания бот(\w)?'],
    'окей': ['ok', 'okey', 'ок', 'оки', 'оке'],
    'спасибо': ['thanks', 'thank you', 'thanks you', 'фенк ю', 'сенк ю', 'сенкью', 'спасиобо', 'смасибо', 'сбосибо', 'срасибо', 'спасиьот', 'спосиба', 'спасиблэо', 'спасыба', 'спачибо', 'сипасибо', 'сипасиба', 'смасибо', 'спасбо', 'паибо', 'спсибо', 'спксибо', 'спасиьот', 'сппсибо', 'виспасибо', 'спасмьо', 'спс', 'пасиб', 'мерси', 'спсасибо', 'спамибо', 'от души', 'ок.спасибо', 'пасибо', 'спасибки', 'cgfcb,j', 'Спосиба вам'],
    'пожалуйста': ['пжлст', 'пжл', 'пож'],
    'понятно': ['понаятна', 'пончтно', 'поняятго', 'панятна', 'ясненько-понятненько', 'понел', 'панятно'],
    'конечно': ['канешна', 'ес оф кос', 'оф кос'],
    'почему': ['пачему', 'пасему', 'посему', 'пачиму', 'почиму', 'почемуттак', 'пояему', 'в связи с чем', 'связи с чем', 'с чем связан(\w)?', 'с чем это связан(\w)?', 'с чем это может быть связан(\w)?', 'почечу', 'по чему', 'какого хрена бл'],
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
    'у вас': ['увас'],
    'так': ['дак'],
    'тут': ['тутачки', 'туточки', 'тута'],
    'зовут': ['завуд', 'завать', 'звать', 'зовус', 'зовуд'],
    'бензин': ['бенз(\.)?'],
    'пресс': ['прэсс'],
    'кэш': ['кеш'],
    'плохой': ['полохой', 'плахой'],
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
    'триста': ['тристо', 'три ста'],
    'фото': ['фотк(\w)?', 'фоту'],
    'работаешь': ['пашешь'],
    'не работает': ['не работки', 'не раьотает', 'не работать'],
    'не поступили': ['не пришли'],
    'спб': ['Питер(\w)?'],
    'сири': ['siri'],
    'правила дорожного движения': ['ПДД'],
    'ковид': ['covid', 'covid-19'],
    'смешно': ['хехехе', 'хихи', 'ахаха', 'ха ха', 'хохохо', 'ха', 'аххха', 'азахвхвхв', 'xd', 'хд'],
    'да': ['yes', 'дааа', 'да-да', 'даааа'],
    'нет': ['нэт', 'ytn', 'no', 'not', 'неет', 'неь'],
    'что': ['чо', 'че', 'чё', 'шо', 'што', 'чаво', 'чего', 'чиво', 'чиго', 'чидо', 'что-то', 'што-то', 'что то', 'што то'],
    'нужно': ['нужено', 'нада'],
    'навыки': ['спасобнаст\w*', 'способност(\w)?', 'умени(\w)?' 'скил\w*'],
    'что нибудь': ['что-нибудь', 'чо нить', 'че нить', 'чё нить', 'чо нидь', 'че нидь', 'чё нидь','чидо нибуть', 'чо-нить', 'че-нить', 'чё-нить', 'чидо-нибудь'],
    'подработка': ['шабашк(\w)?'],
    'музыка': ['музочк(\w)?', 'musik', 'music'],
    'огорчен': ['растроен'],
    'не благодари': ['не за че', 'не за чо'],
    'неправда': ['не правда'],
    'видео': ['видос(\w)?'],
    'могу': ['магу'],
    'хочу': ['хачу'],
    'куда': ['гуда', 'кудой'],
    'меньше': ['менее'],
    'что такое': ['че такое', 'чо такое', 'чо означает'],
    'перевыпустить': ['пере выпустить'],
    'подтвердить': ['потвердеть'],
    'сейчас': ['щас'],
    'можно': ['моднр'],
    'лучше': ['лутши'],
    'когда': ['какгда'],
    'нечайно': ['не чайно'],
    'еще': ['ищо', 'ище', 'ещё'],
    
    #города и страны
    'анадырь': ['анадыръ'],
    'в сша': ['вСША'],
    'абхазия': ['абзазия'],
}
