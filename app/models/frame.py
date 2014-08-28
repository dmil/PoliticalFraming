from app import app, db
import os, sys
from peewee import *

class Frame(db.Model):
    id = PrimaryKeyField(null=True, db_column='id')
    name = CharField(null=True)
    description = TextField(null=True)
    generation = IntegerField(null=True)
    seed_word = CharField(null=True)
    word_count = IntegerField(null=True)
    word_string = TextField(null=True)

    class Meta:
        db_table = 'frames'


def get_frame(id=None):
    return Frame.get(Frame.id == id)


@app.route('/frames/download/dummy_frames')
def populate_frames_dummy_data():

    root = os.path.dirname(os.path.realpath(__file__))
    frames = [

        ('christianity','anglican papacy founded Saint welfare religious disciples uphold papist father young redemptive sovereignty Day belonging wished Calvin christianly practicing missionary washing Sabbath Episcopal steeple communicant George spiritual godly japanese hindu Eddy doctrines christ Orthodox ecumenism churches public movement body justification christian water Redeemer healing groups English active divinity strong teacher Byzantine stresses redemption receive Quakers social baptistic Religious nicene named Jew morals wesleyan texts follower Book Communion sermon opposes episcopalian papal Congregational opposed separated predestinarians hamadryad Anabaptist holy immersion muse American adult savior antichrist adventist inerrancy word Pope science originally believer believes freedom believed Pentecostal Protestantism fundamentalist patron methodist stressing accept high ascension methodism council fundamentalism Christmas absolute siren Calvinists cardinal daemon sacred deification simplicity attend believers southern emphasizes Roman Baptistic man infallibility advocated Anglicanism purify greek advocates transubstantiate congregationalist restriction interpretation office expects scientist including Nazareth hell deity worship Trinity revivalism Catholics chosen abbey saxon founders holiday good calvinism orthodox practice Rome foot echo day cursed term feast truth messianic characterized Saints principles Saviour society cathedral living Presbyterian god scriptural paradise belief lutheranism apotheosize idealize presbyterianism patriarchate ancestry schismatic obligation Being Jesus place Puritans shaker messiahship anglicanism jesus pleiades minster Arianism separation service rejects baptised assumption saint white friend reawaken western Christianity grace thetis Manichaeism gentile marriage aether contrasted basilica tongues God Baptist Gods catholic conversion Christian latter anglo evangelicalism experienced Luther transfiguration adonis Coptic evangelism ultramontanism evangelical Saturday incomplete pope Catholic earth supporter based godlike presbyterian adherent mormon de baptist creed godliness common coptic gospel preach Methodists observes blameless individual led concern Good banns approach Protestants Bible amen incarnation deliver denomination opposition article christendom dualism goddess Greek disestablish called personal roman semitic messiah Christ bell puritan coexistence nonconformist Nazarene Ireland church antipope mortification Adventism catholicism literal communion life eastern pentecostalism dramatic euphrosyne expounded romanism Anglican conception plain churchly Church dryad property apostle primacy century separatist Easter protestantism communal perform member followers Oxford entitled practitioner centuries Uniate evil sacraments tradition annunciation celtic practiced anabaptist salvation theology thought person practices mother Jerusalem anabaptism christly United being mennonite human Churches Christendom discipline Inquisition christlike Calvinism nonJewish character save easter real aspects omnipotence Supreme redeem descendant Alexandria Methodist celibacy LatterDay avatar unitarianism old people advent belonged authority immortal born nestorian New pentecostal Mary canonically teachings legal religion christmas theological Protestant medieval Baker refused hesperides puritanism Xmas faith Mennonite compatible mutually simplification trinitarianism emperor presence Latter administer mormonism doctrine sovereign christianity errancy heresy war immaculate complete exterminated russian protestant characteristic official Africa baptism beliefs possession supreme defined Deliverer again divine adventism crypt offensive members formed Shepherd AngloSaxon dunker Testament building Tracts assume pamphlets Reformation mass'),
        ('crime','chain rob resistance gang holdout defraud shanghai violation breach housebreaking sinking paying woman inciting advantage agitating induce appropriation accuse abduction prevents molesting shipboard altering heist offender small undercover forged force offenders persuade run helpless implemented cargo barratry lawful capital public inducement jury interrupting commercial agreement protection making deceit appears molestation engage brutal unwanted smuggle transit bribery discrediting armed confidence criminals injure illegal passport vehicle injury minor plagiarize entrance statutes disruption robbing hold pretense capturing rights car cybercrime control scam agent high mayhem offense locale breaking rape court illicit acts oppose intended shoplift collection perjury depriving date invasion law extortion misleads malevolent retail attempt crippling larceny unlawfully progressively enter representation order Islam operations executed distributors consent misdemeanor seizing embezzlement shakedown committed bunco sleightofhand tending thuggery police personal mail criminal undermines embezzling greater rake indigenous owned Social articles execute classified stopped hijack entitled harm nakedness crimes engaging comprises kidnapping entering stealing girl inflated sexual living intercourse unlawful highway commits threatened free complicated pilferage Security card care created wrong hindering place threat divorce concealments entrusted extrinsic render punishable victimless corporations lawsuits vulgar forgery attack master legally scheme store plunderage highjacking punish misleading plane outlaw mutilation transgression stalk cards oath declare false investors prostitution extorting occupied sell kidnap offering extorted divulge assailant trespassing funds finding willful committing advances rapist assault involving knowingly intrinsic payment arson considered attacking fact cheat participate caper judges resisting knowledge true crime conduct perpetrating repose theft burglary pellet swindle alteration taxes quarrels common steal result threats attempting bootleg mug contraband knowing premises felony distribution disorderly contract duty indecent battery improper agents trust worthless instrument arises subjecting great swindling plants contexts expanded loot property apprehend sting ransom capture trial patent pay concealing member grand party shell raid evil statutory documents purpose injures racketeering opportunity identity transaction programs falsification weapon punishment person contact claims arousing excessive perpetration money valuable violent purchasing victim facts omissions marketeer marrying alternate arrest disparity overthrow disrupt kick victims government rules offence game traffic swiz judge divert plundering rustle officer robbery transgress rustling imprisonment back authority incriminate felonious election home gangsters avoid legal carjacking scalp judgment commandeer business blackmail constructive punishments hiding goods actual violence mugging commit efforts road statements shoplifting obtaining parties deception submit war building buy form attempted bigamy failure gain aggravated persisting fraud wholesale wife amounts factum display mails guesses speculators gunpoint wartime skimming ship operation physical willingly thugs piracy deadly peace offensive carjack valid holding income gambling forcing abducted reckless artificially bribe reached includes intent rolling equitable spouse slang exposure extort vice established intentionally fraudulent presenting treason push intentional'),
        ('finance','managed issued cooperative abundant votes pensions voted merchant overgrowth overplus legislators risk refinance regional account fat appropriation difference pooled impressive profligacy level list large depositors excellence depositories depository accumulation pork direct batch street exuberant copiousness investment index lavishness investing sum bearish shares boodle current greenness capital public simultaneously exchange ingratiate teemingness operating excess represented spendthrift thrift bellyful convert engage difficulty brilliant withdrawing losses credit simultaneous involves named exorbitance family lending extravagancy extravagance pyramid kind market fee wealth distinct coins campaign markets company St federally underwriter abundance keeping highlife work freedom strategies closing quaestor control meant reserved activities Federal attribute agent high currency association Parliament acts copious earnings Stock stock intended slush British redundancy designed law purchase short counter deposit fundamental banks pleasure rankness comfort constituents redeposit paper tendency monitor Exchange personal decorum teeming permanent impressiveness expansiveness inordinateness greater richness killer arbitrageur rank flotation bank excessiveness token moneyer characterized bond development financial depositor society depositing year requesting merchants bullish borrowed quality encourage revolving issue hedged small unwanted members card receipts fixed benefits buys longterm conducted prodigal undesirable probability owned improvements electronic legislative management leverage service bears coiner plentiful listed percentage interests prolificacy institution improvidence financing target bee amplitude budget providing profuse comfortable seed sells mint mortgages potential luxury sufficiency vegetation grandness transactions price regular plenty services intrinsic payment Reserve give sale face enterprise barrel technical reserve retire chartered businesses fifth profligate ratio transact proportion syndicate York rich regularly gains bonds expectation unethical affluent banking implication fertility national officials acquirer concern fails shinplaster federal profuseness state conditions notice terms plenteous commercial takeover debt legislature overabundant protect limits deregulation region foreign traded supply wall loan allocated trust flourishing petty union political subsidy extravagant combined firm life senses worker great fund demand prices appearance cash promotes property pound backing expenses economics finance capture pay member complex higher sterling overweening purpose ownership expand spent analysis States savings corporate United excessive money glut competitive subsidization lavish overabundance informal pecuniary royal deposits issuing pile board ample government checking advances bid loaned redeem abound bribing devises incidental securities individuals lose security statechartered immoderation arbitrage deal people back growth home specific scale lead separate exceeding trustees unit replenished stateliness truth business slight equivalent processing monetary withdrawals loans renew cornucopia citizens accepts luxuriance involving banker insufficient wilderness fisc civil communication skilled accounts accumulated extremely long minter deposited fiscal medium offer funds differences repeatedly larger analyst buying amplify shortterm waste Wall affluence fruitfulness trading engaging stages profusion sinking bankable curb floating prodigality mutual transacting floor corporation unneeded gaining ampleness invested stocks building deluxe assets workers required institutions profit Street pension quantity'),
        ('sex','restraining forbidden foul sleep porno pornographic physiological inbreeding hump whoredom masculine merchant activities woman garden compassion servicing mixing harlot encounter transmission gender marry nonwhite tenderness anal attracting enjoy spiritual porn streets lechery erotic street ardent casual aphrodisiac organisms man fetish fetishize body simultaneously fertilization men excess active sexy unrestrained recessive boy search engage condoms fond prior virility involves love disposition feelings follower aberrant working illegal beneficence cattiness call smuttiness films loving trait purposes adult penis producing women crosses animals genitalia cuddle making male indulgence process fuck bestiality honey occur dissimilar turn comfort bawdy smut bawd loyalty depriving mankind filthy man varieties attracts Japanese sodomy pleasure wind gratification over benevolence yearn experiments committed carnal lovingness attraction production zoophilia femaleness pederasty practice bang penetration kiss pregnant enjoyer paraphilia lasting conceiving harlotry generation ejaculation beneficent abnormal abuse society sexually temporary girl sexual intercourse unlawful disassortative laid darling jacking prostitutes exhibitionism intensely tempt warmhearted care exposing womans bisexuality illicit lie produce Mendels swing stimulate frequent emotion feel fancy lovable pornographer wench AIDS filial genotype service unknown relations autoeroticism stimulation vagina cocotte witnessing drool white monohybrid anus voyeurism foreplay practiced orgasm handcuffs assortative bed shower others marriage reproduction lover feeling devotion God pornography arousal organs sell screw Christian hymen self interferes rupturing eff urge play promiscuous measures pair genital inserted class prostitute latex implications disease organism masturbation affair walking perversion determined partners envy crime deepest androgyny agape ardor procreation closely nasty streetwalker reproductive organ married dearest common activity husband multiplying physically sex venerate arouse voluntary pictures away score smutty snogging filthiness promiscuity nature sold attention indiscriminate distinguish reverse freely heterosexuality sexes receives obscenity hybrids allegiance walk incest War capable panky extramarital uncritically cords aphrodisiacal defloration idol spermatozoon affectionate life fetishism cruddy excite races prostitution dote child plants soixante handling conception reciprocal fornicate sexuality behavior property cock indulging unquestioningly characteristics rubbing lascivious adultery partner whore sucking intense seduce romance hank safe slave forced enjoyment restraint fucker persons selfless simulates bondage caressing enamored theology person contact telephone testcross excessive sporting warmheartedness maleness fornication ovum informal passive hay parents beloved excited hybridization customers homozygous showing inversion know lady fondling desire profound manual homosexuality specific individuals night virginity crowd people creation showman traits dear bonk perverse avoid passion copulation inserting cunnilingus object fellatio intimate erotica properties fondness idolize involving stand vaginal cyprian vulva miscegenation respectable frottage female outercourse demimondaine heterosexual adolescent pairing form genitals admiration hop characteristic wife attached heartstrings adore lesbianism affection bearing single mutual copulate personnel role clitoris puppy roll tart amorousness genetics bodily friends slang pedophilia coupling vice mating maliciously together lovemaking offspring oral'),
        ('war','limited serviceman activated resistance jihad captain injure zone musketry spearhead dressing pilot friendly sniper adviser fatigues blockade rearguard minute room policeman compassionate prolonged flyover pullback science quick biological force escalation picket blitz battle pass hutment bacteria bomber outpost nonoperational colonel section uniform occupation movement draftee collateral full bandsman men active change naval involved smoke defeat action military struggle campaign win ensign psychological color armed crisis unit standing warship illegal objectives arms germ chief call vehicle assessment artillery holy materiel company sortie flag train commissioned olive commander chaplain high animals toxins car column drill unconditional control spy firing patrol infantry states unarmed wardroom dress ceremony information united court damage machine hot Muslims militainment mess chiefs plane fatigue militarism law militarise readiness effective caisson headquarters bashing shore infidels wing mission radar noncommissioned chemical police platform absence flank food arsenal break commodore half detach day drop capability slacker quarter side square gun firepower navy phalanx operation contend leave armor open blitzkrieg unarmored issue salute maneuver umbrella siege base formation proxy mobilize marine training yard hostile area major grade waged rank strategic guardhouse chevron electronic engineer horse salient service system attack station master enforcement shell academy hut rifle commence warfare nations subaltern briefing marines garrison armored deserter occupier infiltration demonstration amphibious agency standdown peacekeeping reservist squad conscription forces objective destroy combat track harmful assault regular eight commanding services surprising camp cover order nuclear reserve sector armament incapacitate commissary participate staff taps drumbeat drumhead operational entities achieve quartering hostility de joint competing silo flanker enemy troop logistic intelligence national redoubt deactivation defense sea seal close wire trench weapons state emplacement warrior screen attention barrack censorship installation country drug foreign reveille tactical commando duty midshipman attache battery agents petty mobilization west territorial strategy commission combined basic paratroops spit drugs gas aviation volunteer tank warrant air instigated aid reconnaissance echelon hardware inspector opponents technology tattoo coastguard wound conflict militaristic extended stripe destruction countermarch task center weapon fighting without command position hospital bearer rocket executive quarters kill polish staging field point contractor rangers retreat hat adversaries advocate game sapper desk judge world rear morale militarize manual roll specific platoon officer viruses inter deal martial warring home transport leader contingent power regimentals lieutenant post adversary mechanized actual latrine army hostilities carrier militia chow marshal cadet civil guard parties pentagon countermine submarine support fight factions war head generalship landing striker line promote junior tactics muster sprog insignia accoutered expedition plunderer general provost warning file disengagement ship trip casualty cavalry personnel boot fire minefield sick billet remilitarize peacekeeper warplane drab brass weekend deterrence fighter mass time expeditionary adjutant'),
        ('common_words','the of to and a in is it you that he was for on are with as I his they be at one have this from or had by hot but some what there we can out other were all your when up use word how said an each she which do their time if will way about many then them would write like so these her long make thing see him two has look more day could go come did my sound no most number who over know water than call first people may down side been now find any new work part take get place made live where after back little only round man year came show every good me give our under name very through just form much great think say help low line before turn cause same mean differ move right boy old too does tell sentence set three want air well also play small end put home read hand port large spell add even land here must big high such follow act why ask men change went light kind off need house picture try us again animal point mother world near build self earth father head stand own page should country found answer school grow study still learn plant cover food sun four thought let keep eye never last door between city tree cross since hard start might story saw far sea draw left late run dont while press close night real life few stop open seem together next white children begin got walk example ease paper often always music those both mark book letter until mile river car feet care second group carry took rain eat room friend began idea fish mountain north once base hear horse cut sure watch color face wood main enough plain girl usual young ready above ever red list though feel talk bird soon body dog family direct pose leave song measure state product black short numeral class wind question happen complete ship area half rock order fire south problem piece told knew pass farm top whole king size heard best hour better true during hundred am remember step early hold west ground interest reach fast five sing listen six table travel less morning ten simple several vowel toward war lay against pattern slow center love person money serve appear road map science rule govern pull cold notice voice fall power town fine certain fly unit lead cry dark machine note wait plan figure star box noun field rest correct able pound done beauty drive stood contain front teach week final'),

        ('christianity2', open(root + '/frames/christianity2.txt').read()),
        ('crime2', open(root + '/frames/crime2.txt').read()),
        ('finance2', open(root + '/frames/finance2.txt').read()),
        ('sex2', open(root + '/frames/sex2.txt').read()),
        ('war2', open(root + '/frames/war2.txt').read()),
        ('common_words2', open(root + '/frames/common_words2.txt').read()),

    ]

    for n, frame in enumerate(frames):
        Frame.create(name=frames[n][0],
            description='frame about ' + frames[n][0],
            generation = 1, seed_word=frames[n][0],
            word_string=frames[n][1],
            word_count= len(frames[n][1].split()))
        print 'created frame : ' + frames[n][0]
    return "populated frames dummy data"