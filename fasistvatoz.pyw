from datetime import datetime
import os.path
import random
from discord import *
from discord.ext import commands
from Vars import *
from Sözler.Hitler import *
from Sözler.Atatürk import *
from Sözler.Lenin import *
from Sözler.Stalin import *
from Sözler.Cengiz import *
from Sözler.CelalŞengör import *
from Sözler.MeteHan import *
from propaganda import *
import token_2
from bs4 import BeautifulSoup
import requests
import json

Bot = commands.Bot("!", help_command=None)
tür = "vatoz"

# moderatrör komutları

@Bot.command()
@commands.has_permissions(ban_members = True)
async def kick(ctx, member:Member, *, reason = None):
    embed = Embed(title="kicklendi", description=f"{member.mention}", color=0x8a0a01)
    await member.kick(reason = reason)
    await ctx.send(embed=embed)

@Bot.command()
@commands.has_permissions(ban_members = True)
async def yak(ctx, member : Member, *, reason = None):
    embed = Embed(title="Yakılanlar listesi", description=f"{member.mention}", color=0x8a0a01)
    await member.ban(reason = reason)
    await ctx.send(embed=embed)


# Help komutu

@Bot.command()
async def yardım(ctx):
    embed = Embed(title="Yardım", description="Yardım komutları", color=0x8a0a01)
    embed.add_field(name="!yardım", value="yardım komutlarını gösterir", inline=False)
    embed.add_field(name="!yak", value="Etiketlenen kişiyi yakar(banlar)", inline=False)
    embed.add_field(name="!kick", value="Etiketlenen kişiyi kickler", inline=False)
    embed.add_field(name="!clear", value="Belirlenen sayıda mesaj siler", inline=False)
    embed.add_field(name="!i", value="110'dan fazla gif veya resimden seçileni atar", inline=False)
    embed.add_field(name="!başvuru", value="Seçilen başvuru formunu gönderir", inline=False)
    embed.add_field(name="!ada", value="İstediğiniz bir şeyi hayalet vatoza adar", inline=False)
    embed.add_field(name="!pp", value="Yazan kişinin profil fotoğrafını atar", inline=False)
    embed.add_field(name="!ideoloji", value="16 ideoloji arasından seçilen ideolojiye geçerim", inline=False)
    embed.add_field(name="!işkence", value="Etiketlenen kişiye işkence yaparım. Fazla kullanmamaya dikkat edin", inline=False)
    embed.add_field(name="!söz", value="Rastgele bir kişinin sözünü atar", inline=False)
    embed.add_field(name="!propaganda", value="Random propaganda gönderir", inline=False)
    embed.add_field(name="!r", value="Seçilen kitap, film, şarkı, oyun, anime veya manga seçeneklerden birisi için öneride bulunur gönderir", inline=False)
    await ctx.send(embed=embed)

# gifs


@Bot.command()
async def i(ctx, *args):
    if "like" in args:
        await ctx.send(like)
    if "rage" in args:
        await ctx.send(rage)
    if "anakuzusu" in args:
        await ctx.send(anakuzusu)
    if "cry" in args:
        await ctx.send(cry)
    if "freakout" in args:
        await ctx.send(freakout)
    if "haa" in args:
        await ctx.send(haa)
    if "o7konosuba" in args:
        await ctx.send(o7konosuba)
    if "nomnom" in args:
        await ctx.send(nomnom)
    if "like2x" in args:
        await ctx.send(like2x)
    if "shock" in args:
        await ctx.send(shock)
    if "o7" in args:
        await ctx.send(o7)
    if "foksax" in args:
        await ctx.send(foksax)
    if "dwayne" in args:
        await ctx.send(dwayne)
    if "hatsoff" in args:
        await ctx.send(hatsoff)
    if "capitalism" in args:
        await ctx.send(capitalism)
    if "soviet" in args:
        await ctx.send(soviet)
    if "sikin" in args:
        await ctx.send(sikin)
    if "susamuru" in args:
        await ctx.send(susamuru)
    if "fire" in args:
        await ctx.send(fire)
    if "marcharmy" in args:
        await ctx.send(marcharmy)
    if "irumadance" in args:
        await ctx.send(irumadance)
    if "taam" in args:
        await ctx.send(taam)
    if "milf" in args:
        await ctx.send(milf)
    if "stare" in args:
        await ctx.send(stare)
    if "GreatPurge" in args:
        await ctx.send(GreatPurge)
    if "napim" in args:
        await ctx.send(napim)
    if "napimdiyeni" in args:
        await ctx.send(napimdiyeni)
    if "hatayapar" in args:
        await ctx.send(hatayapar)
    if "nazifokları" in args:
        await ctx.send(nazifokları)
    if "darkside" in args:
        await ctx.send(darkside)
    if "troll" in args:
        await ctx.send(troll)
    if "yahudiler" in args:
        await ctx.send(yahudiler)
    if "balanced" in args:
        await ctx.send(balanced)
    if "jii" in args:
        await ctx.send(jii)
    if "shipbang" in args:
        await ctx.send(shipbang)
    if "tank" in args:
        await ctx.send(tank)
    if "degil" in args:
        await ctx.send(degil)
    if "air" in args:
        await ctx.send(air)
    if "kimclap" in args:
        await ctx.send(kimclap)
    if "worry" in args:
        await ctx.send(worry)
    if "muso" in args:
        await ctx.send(muso)
    if "sob" in args:
        await ctx.send(sob)
    if "kannaeat" in args:
        await ctx.send(kannaeat)
    if "baka" in args:
        await ctx.send(baka)
    if "triggered" in args:
        await ctx.send(triggered)
    if "shinobu" in args:
        await ctx.send(shinobu)
    if "shy" in args:
        await ctx.send(shy)
    if "bang2" in args:
        await ctx.send(bang2)
    if "shutup" in args:
        await ctx.send(shutup)
    if "save" in args:
        await ctx.send(save)
    if "aah" in args:
        await ctx.send(aah)
    if "para" in args:
        await ctx.send(para)
    if "yay" in args:
        await ctx.send(yay)
    if "anlıyorum" in args:
        await ctx.send(anlıyorum)
    if "understood" in args:
        await ctx.send(understood)
    if "igetit" in args:
        await ctx.send(igetit)
    if "benzin" in args:
        await ctx.send(benzin)
    if "why" in args:
        await ctx.send(why)
    if "celebrate" in args:
        await ctx.send(celebrate)
    if "braintime" in args:
        await ctx.send(braintime)
    if "drink" in args:
        await ctx.send(drink)
    if "bb" in args:
        await ctx.send(bb)
    if "dot" in args:
        await ctx.send(dot)
    if "confused" in args:
        await ctx.send(confused)
    if "lenny" in args:
        await ctx.send(lenny)
    if "bang" in args:
        await ctx.send(bang)
    if "slap" in args:
        await ctx.send(slap)
    if "mad" in args:
        await ctx.send(mad)
    if "sob2" in args:
        await ctx.send(sob2)
    if "laugh" in args:
        await ctx.send(laugh)
    if "evilsmile" in args:
        await ctx.send(evilsmile)
    if "dissaper" in args:
        await ctx.send(dissaper)
    if "behind" in args:
        await ctx.send(behind)
    if "like3" in args:
        await ctx.send(like3)
    if "whatanime" in args:
        await ctx.send(whatanime)
    if "nomnomnom" in args:
        await ctx.send(nomnomnom)
    if "bonk" in args:
        await ctx.send(bonk)
    if "yarra" in args:
        await ctx.send(yarra)
    if "katon" in args:
        await ctx.send(katon)
    if "hug" in args:
        await ctx.send(hug)
    if "hug2" in args:
        await ctx.send(hug2)
    if "sob3" in args:
        await ctx.send(sob3)
    if "animechild" in args:
        await ctx.send(animechild)
    if "narutodance" in args:
        await ctx.send(narutodance)
    if "darkstare" in args:
        await ctx.send(darkstare)
    if "think" in args:
        await ctx.send(think)
    if "point" in args:
        await ctx.send(point)
    if "bagıs" in args:
        await ctx.send(bagıs)
    if "stalinpoint" in args:
        await ctx.send(stalinpoint)
    if "serve" in args:
        await ctx.send(serve)
    if "waku" in args:
        await ctx.send(waku)
    if "fail" in args:
        await ctx.send(fail)
    if "comunazi" in args:
        await ctx.send(comunazi)
    if "şaak" in args:
        await ctx.send(şaak)
    if "doom" in args:
        await ctx.send(doom)
    if "omori" in args:
        await ctx.send(omori)
    if "callvatoz" in args:
        await ctx.send(callvatoz)
    if "vatozlar" in args:
        await ctx.send(knowvatoz)
    if "papas" in args:
        await ctx.send(papas)
    if "hans" in args:
        await ctx.send(hans)
    if "yummy" in args:
        await ctx.send(yummy)
    if "okay" in args:
        await ctx.send(okay)
    if "what" in args:
        await ctx.send(what)
    if "sad" in args:
        await ctx.send(sad)
    if "gel" in args:
        await ctx.send(gel)
    if "ekonomi" in args:
        await ctx.send(ekonomi)
    if "mikasa" in args:
        await ctx.send(mikasa)
    if "çıldır" in args:
        await ctx.send(çıldır)
    if "kırk" in args:
        await ctx.send(kırk)
    if "drink2" in args:
        await ctx.send(drink2)
    if "fbi" in args:
        await ctx.send(fbi)
    if "want" in args:
        await ctx.send(want)
    if "want2" in args:
        await ctx.send(want2)
    if "tehe" in args:
        await ctx.send(tehe)
    if "cringe" in args:
        await ctx.send(cringe)
    if "money" in args:
        await ctx.send(money)
    if "yay2" in args:
        await ctx.send(yay2)
    if "nod" in args:
        await ctx.send(nod)
    if "tobi" in args:
        await ctx.send(tobi)
    if "yesmaster" in args:
        await ctx.send(yesmaster)
    if "nope" in args:
        await ctx.send(nope)


# Bug fix
@Bot.command()
async def aki(ctx):
    print("")


@Bot.command()
async def rank(ctx):
    print("")

@Bot.command()
async def owo(ctx):
    print("")

# ekibe başvuru


@Bot.command()
async def başvuru(ctx, *args):
    if "mangaçevirmen" in args:
        tr = Embed(
            title="Manga çevirmen başvuru formu",
            description="Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nİngilizce seviyen nedir?\n\nEn çok hangi tür mangaları seviyorsun?\n\nİngilizceni değerlendiriniz(A1, A2, B1, B2, C1, C2)\n\nHaftada kaç bölüm çevirebilirsin?\n\nVe bu örnek sayfayı çevirmeni istiyoruz\n\nhttps://drive.google.com/file/d/1_qfW23Wvda94S19U3f4x8eCe6YEqFCug/view?usp=sharing\n\nSon olarak #yeni-gelenlere kanalına bakmayı unutmayın."
        )
        await ctx.send(embed=tr)
    if "mangaeditör" in args:
        ed = Embed(
            title="Manga editör başvuru formu",
            description="Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nHaftada kaç bölüm editleyebilirsin?\n\nPhotoshop seviyene 5 üzerinden puan verebilir misin?\n\nVe bu örnek sayfayı editlemeni istiyoruz\n\nhttps://drive.google.com/file/d/1-B-xLpofKmmyx86_wOuOA4ii-LfG4hb9/view?usp=sharing\n\nSon olarak #yeni-gelenlere kanalına bakmayı unutmayın")
        await ctx.send(embed=ed)
    if "webçevirmen" in args:
        wtr = Embed(
            title="Webtoon çevirmen başvuru formu",
            description="Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nİngilizce seviyen nedir?\n\nEn çok hangi tür webtoonları seviyorsun?\n\nİngilizceni değerlendiriniz(A1, A2, B1, B2, C1, C2)\n\nHaftada kaç bölüm çevirebilirsin?\n\nVe bu örnek sayfayı çevirmeni istiyoruz\nSon olarak #yeni-gelenlere kanalına bakmayı unutmayın")
        await ctx.send(embed=wtr)
    if "webeditör" in args:
        wed = Embed(
            title="Webtoon editör başvuru formu",
            description="Daha önce başka bir ekipte çalıştın mı?\n\nBağımsız da olsa deneyimin var mı?\n\nHaftada kaç bölüm editleyebilirsin?\n\nPhotoshop seviyene 5 üzerinden puan verebilir misin?\n\nVe bu örnek sayfayı editlemeni istiyoruz\n\nhttps://drive.google.com/drive/folders/12spp_Y4xTWLRJ8HxLsaom4B5Ilord0_7?usp=sharing\n\nSon olarak #yeni-gelenlere kanalına bakmayı unutmayın"
        )
        await ctx.send(embed=wed)


# Adak sistemi


@Bot.command()
async def ada(ctx, *args):
    author = str(ctx.message.author)
    ad = "adaklar/"+ author +".txt"
    if "temizle" in args:
        os.remove(ad)
        embed = Embed(title="Adağınız başarıyla temizlendi.")
        await ctx.send(embed=embed)
    if os.path.exists(ad) == True and "temizle" not in args:
        msg = Embed(title="Adağınız kabul edildi")
        await ctx.send(embed=msg)
        r = open(ad, "r")
        ar = r.read()
        ada = open(str(ad), "w")
        a = str(ar) + ", " + str(args)
        ada.write(a)
    if os.path.exists(ad) == False and "temizle" not in args:
        msg = Embed(title="Adağınız kabul edildi")
        await ctx.send(embed=msg)
        ada = open(str(ad), "x")
        ada = open(str(ad), "w")
        a = str(args)
        ada.write(a)


@Bot.command()
async def pp(ctx, Member: Member):
    await ctx.send(Member.avatar_url)


@Bot.command()
async def fok(ctx):
    tür = "fok"
    dem = open("foklar/faşist.jpg", 'rb')
    demo = dem.read()
    await Bot.change_presence(activity=Game(name="Yahudi yakıyor"))
    await Bot.user.edit(username="Faşist Vatoz", avatar=demo)
    embed = Embed(title="Artık bende bir fokum")
    await ctx.send(embed=embed)


@Bot.command()
async def vatoz(ctx):
    tür = "vatoz"
    dem = open("vatozlar/fasist_vatoz.jpg", "rb")
    demo = dem.read()
    await Bot.change_presence(activity=Game(name="Yahudi yakıyor"))
    await Bot.user.edit(usename="Faşist Vatoz", avatar=demo)
    embed = Embed(title="Artık bende bir vatozum")
    await ctx.send(embed=embed)


@Bot.command()
async def ideoloji(ctx, *args):
    if tür == "vatoz":
        if "ak4747" in args:
            dem = open("vatozlar/ak4747.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Etrafa sıkıyor"))
            await Bot.user.edit(username="AK-4747 Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bir can karşılığında bir can. Bence mantıklı bir anlaşma")
            await ctx.send(embed=embed)
        if "almanya" in args:
            dem = open("vatozlar/almanya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşıyor"))
            await Bot.user.edit(username="Alman Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Alman oldum")
        if "anarşist" in args:
            fas = open("vatozlar/anarşist.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Otoriteye küfür ediyor"))
            await Bot.user.edit(username="Anarşist Vatoz", avatar=fasc)
            vatoz = "anarşist"
            print(vatoz)
            embed = Embed(title="Otoritede ne?")
            await ctx.send(embed=embed)
        if "anarkoilkel" in args:
            ail = open("vatozlar/Anarko-ilkelcilik_vatoz.jpg", 'rb')
            ailk = ail.read()
            await Bot.change_presence(activity=Game(name="Hayvan avlıyor"))
            await Bot.user.edit(username="Anarko-ilkelci Vatoz", avatar=fasc)
            vatoz = "anarko ilkelci"
            print(vatoz)
            embed = Embed(title="Yeni dünya boş asıl olay geçmişte var")
            await ctx.send(embed=embed)
        if "anarkokapitalist" in args:
            fas = open("vatozlar/Anarko-kapitalist_vatoz.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Tüccarlık yapıyor"))
            await Bot.user.edit(username="Anarko Vatoz", avatar=fasc)
            vatoz = "anarko kapitalist"
            print(vatoz)
            embed = Embed(title="Serbest piyasasında tüccarlık yapacağım")
            await ctx.send(embed=embed)
        if "Avusturya" in args:
            dem = open("vatozlar/Avusturya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Avusturyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Avusturyalı oldum")
            await ctx.send(embed=embed)
        if "azerbeycan" in args:
            dem = open("vatozlar/azerbeycan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Azerbeycanlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Türk oldum")
            await ctx.send(embed=embed)
        if "Belarus" in args:
            dem = open("vatozlar/Belarus.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Belaruslu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Belaruslu oldum")
            await ctx.send(embed=embed)
        if "Belçika" in args:
            dem = open("vatozlar/Belçika.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Belçikalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Belçikalı oldum")
            await ctx.send(embed=embed)
        if "BosnaHersek" in args:
            dem = open("vatozlar/bosna.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bosnalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bosnalı oldum")
            await ctx.send(embed=embed)
        if "Bulgaristan" in args:
            dem = open("vatozlar/Bulgaristan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bulgar Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Bulgar oldum")
            await ctx.send(embed=embed)
        if "Çek" in args:
            dem = open("vatozlar/Çek.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Çekli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Çekli oldum")
            await ctx.send(embed=embed)
        if "demokrat" in args:
            dem = open("vatozlar/demokrat.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Oy saymaca"))
            await Bot.user.edit(username="Demokrat Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Herkes istiklalimde eşit özgür olacak")
            await ctx.send(embed=embed)
        if "Danimarka" in args:
            dem = open("vatozlar/denmark.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Danimarkalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Danimarkalı oldum")
            await ctx.send(embed=embed)
        if "ermenistan" in args:
            dem = open("vatozlar/ermenistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Eremeni Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Ermeni oldum")
        if "Estonya" in args:
            dem = open("vatozlar/estonya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Estonyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Estonyalı oldum")
            await ctx.send(embed=embed)
        if "fabrika" in args:
            fas = open("vatozlar/fabrika_vatoz.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Edit yapıyor"))
            await Bot.user.edit(username="Fabrika Vatoz", avatar=fasc)
            vatoz = "fabrika"
            print(vatoz)
            embed = Embed(title="İdeolojileri boş verdim ben edit yapacağım")
            await ctx.send(embed=embed)
        if "faşist" in args:
            fas = open("vatozlar/fasist_vatoz.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Yahudi yakmaca"))
            await Bot.user.edit(username="Faşist Vatoz", avatar=fasc)
            vatoz = "faşist"
            embed = Embed(title="Köklerime döndüm")
            await ctx.send(embed=embed)
        if "finlandiya" in args:
            dem = open("vatozlar/finland.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Finlandiyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Finlandiyalı oldum")
            await ctx.send(embed=embed)
        if "fransa" in args:
            dem = open("vatozlar/fransa.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Fransız Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Fransız oldum")
        if "gürcistan" in args:
            dem = open("vatozlar/Gürcistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Gürci Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Gürcistanlı oldum")
            await ctx.send(embed=embed)
        if "hırvatistan" in args:
            dem = open("vatozlar/Hırvatistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Hırvat Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Hırvat oldum")
            await ctx.send(embed=embed)
        if "irlanda" in args:
            dem = open("vatozlar/İrlanda.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İrlandalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İrlandalı oldum")
            await ctx.send(embed=embed)
        if "İspanya" in args:
            dem = open("vatozlar/ispanya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İspanyol Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İspanyol oldum")
            await ctx.send(embed=embed)
        if "İtalya" in args:
            dem = open("vatozlar/italya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İtalyan Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İtalyan oldum")
            await ctx.send(embed=embed)
        if "izlanda" in args:
            dem = open("vatozlar/izlanda.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İzlandalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İzlandalı oldum")
        if "karadağ" in args:
            dem = open("vatozlar/Karadağ.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Karadağlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Karadağlı oldum")
            await ctx.send(embed=embed)
        if "kazakistan" in args:
            dem = open("vatozlar/kazakistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Kazak Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kazak oldum")
        if "kıbrıs" in args:
            dem = open("vatozlar/kıbrıs.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Kıbrıslı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kıbrıslı oldum")
        if "kuma" in args:
            fas = open("vatozlar/kuma vatoz.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Dünyayı kumalıyor"))
            await Bot.user.edit(username="Kuma Vatoz", avatar=fasc)
            vatoz = "kuma"
            print(vatoz)
            embed = Embed(title="Kuma kuma kuma bear izleyip geldim")
            await ctx.send(embed=embed)
        if "kuzey kıbrıs" in args:
            dem = open("vatozlar/kuzey-kıbrıs.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Kuzey kıbrıslı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Kuzey kıbrıslı oldum")
        if "makedonya" in args:
            dem = open("vatozlar/kuzey-makedonya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Makedonyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Makedonyalı oldum")
        if "letonya" in args:
            dem = open("vatozlar/Latvia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Letonyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Letonyalı oldum")
        if "liberteryanist" in args:
            fas = open("vatozlar/librteryenist.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Özgürlüğün dibine vuruyor"))
            await Bot.user.edit(username="Liberteryanist Vatoz", avatar=fasc)
            vatoz = "liberteryanist"
            print(vatoz)
            embed = Embed(title="Özgürlük, özgürlük ve daha fazla özgürlük")
            await ctx.send(embed=embed)
        if "liechtenstein" in args:
            dem = open("vatozlar/Liechtenstein.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Liechtensteinlı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Liechtensteinlı oldum")
        if "litvanya" in args:
            dem = open("vatozlar/lithuania.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Litvanyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Litvanyalı oldum")
            await ctx.send(embed=embed)
        if "lüksemburg" in args:
            dem = open("vatozlar/Lüksemburg.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Lüksemburglu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Lüksemburglu oldum")
            await ctx.send(embed=embed)
        if "Macaristan" in args:
            dem = open("vatozlar/Macaristan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Macar Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Macar oldum")
            await ctx.send(embed=embed)
        if "mao" in args:
            fas = open("vatozlar/maocu.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Kırlarda hazırlanıyor"))
            await Bot.user.edit(username="Maocu Vatoz", avatar=fasc)
            vatoz = "maocu"
            print(vatoz)
            embed = Embed(title="马克思主义者认为，只有人们的社会实践，才是人们对于外界认识的真理性的标准。……判定认识或理论之是否真理，不是依主观上觉得如何而定，而是依客观上社会实践的结果如何而定。真理的标准只能是社会的实践。")
            await ctx.send(embed=embed)
        if "moldova" in args:
            dem = open("vatozlar/moldovo.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Moldovalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Moldovalı oldum")
            await ctx.send(embed=embed)
        if "monako" in args:
            dem = open("vatozlar/Monaco.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Monakolu Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Monakolu oldum")
            await ctx.send(embed=embed)
        if "norveç" in args:
            dem = open("vatozlar/norway.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Norveçli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Norveçli oldum")
            await ctx.send(embed=embed)
        if "onee-san" in args:
            dem = open("vatozlar/onee-san.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Minoru-kun'la yaşıyor"))
            await Bot.user.edit(username="Onee-san Vatoz", avatar=demo)
            vatoz = "oppai"
            print(vatoz)
            embed = Embed(title="MINORYU-KYUNNNN!!!")
            await ctx.send(embed=embed)
        if "polonya" in args:
            dem = open("vatozlar/poland.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Polonyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Polonyalı oldum")
            await ctx.send(embed=embed)
        if "radyoaktif" in args:
            fas = open("vatozlar/radyoaktif.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="α ışıması yapıyor"))
            await Bot.user.edit(username="Radyoaktif Vatoz", avatar=fasc)
            vatoz = "radyoaktif"
            print(vatoz)
            embed = Embed(title="Yanlışlıkla Uranyuma dokundum umarım sıkıntı olmaz")
            await ctx.send(embed=embed)
        if "romanya" in args:
            dem = open("vatozlar/romania.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Romanyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Romanyalı oldum")
            await ctx.send(embed=embed)
        if "rus" in args:
            dem = open("vatozlar/russia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Rus Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Rus oldum")
            await ctx.send(embed=embed)
        if "sırbistan" in args:
            dem = open("vatozlar/Serbia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Sırp Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Sırp oldum")
            await ctx.send(embed=embed)
        if "slovakya" in args:
            dem = open("vatozlar/slovakia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Slovakyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Slovakyalı oldum")
            await ctx.send(embed=embed)
        if "slovenya" in args:
            dem = open("vatozlar/slovenia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Slovenyalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Slovenyalı oldum")
            await ctx.send(embed=embed)
        if "stalin" in args:
            dem = open("vatozlar/Stalin.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Stalin Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Россия - священная наша держава")
            await ctx.send(embed=embed)
        if "isveç" in args:
            dem = open("vatozlar/sweden.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İsveçli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İsveçli oldum")
            await ctx.send(embed=embed)
        if "isviçre" in args:
            dem = open("vatozlar/switzerland.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İsviçreli Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İsviçreli oldum")
            await ctx.send(embed=embed)
        if "turan" in args:
            fas = open("vatozlar/turancı.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Haritayı açık maviye boyuyor"))
            await Bot.user.edit(username="Turancı Vatoz", avatar=fasc)
            vatoz = "turancı"
            print(vatoz)
            embed = Embed(title="Türkler üstün ırktır ve ben de görevim olan cihan fethini gerçekleştireceğim")
            await ctx.send(embed=embed)
        if "türk" in args:
            fas = open("vatozlar/Türkiye.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Yaşayamıyor"))
            await Bot.user.edit(username="Türk Vatoz", avatar=fasc)
            vatoz = "turancı"
            print(vatoz)
            embed = Embed(title="Ne mutlu Türküm diyene!")
            await ctx.send(embed=embed)
        if "ukrayna" in args:
            dem = open("vatozlar/ukrayna.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Ukraynalı Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Ukraynalı oldum")
        if "İngiltere" in args:
            dem = open("vatozlar/Unitend-kingdom.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İngiliz Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="İngiliz oldum")
            await ctx.send(embed=embed)
        if "yunanistan" in args:
            dem = open("vatozlar/yunanistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Yunan Vatoz", avatar=demo)
            vatoz = "demokrat"
            print(vatoz)
            embed = Embed(title="Yunan oldum")
            await ctx.send(embed=embed)
    if tür == "fok":
                
        if "ak4747" in args:
            dem = open("foklar/ak4747.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Etrafa sıkıyor"))
            await Bot.user.edit(username="AK-4747 fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Bir can karşılığında bir can. Bence mantıklı bir anlaşma")
            await ctx.send(embed=embed)
        if "almanya" in args:
            dem = open("foklar/almanya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşıyor"))
            await Bot.user.edit(username="Alman fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Alman oldum")
        if "anarşist" in args:
            fas = open("foklar/anarşist.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Otoriteye küfür ediyor"))
            await Bot.user.edit(username="Anarşist fok", avatar=fasc)
            fok = "anarşist"
            print(fok)
            embed = Embed(title="Otoritede ne?")
            await ctx.send(embed=embed)
        if "anarkoilkel" in args:
            ail = open("foklar/Anarko-ilkelcilik.jpg", 'rb')
            ailk = ail.read()
            await Bot.change_presence(activity=Game(name="Hayvan avlıyor"))
            await Bot.user.edit(username="Anarko-ilkelci fok", avatar=fasc)
            fok = "anarko ilkelci"
            print(fok)
            embed = Embed(title="Yeni dünya boş asıl olay geçmişte var")
            await ctx.send(embed=embed)
        if "anarkokapitalist" in args:
            fas = open("foklar/Anarko-kapitalist.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Tüccarlık yapıyor"))
            await Bot.user.edit(username="Anarko fok", avatar=fasc)
            fok = "anarko kapitalist"
            print(fok)
            embed = Embed(title="Serbest piyasasında tüccarlık yapacağım")
            await ctx.send(embed=embed)
        if "Avusturya" in args:
            dem = open("foklar/Avusturya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Avusturyalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Avusturyalı oldum")
            await ctx.send(embed=embed)
        if "azerbeycan" in args:
            dem = open("foklar/azerbeycan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Azerbeycanlı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Türk oldum")
            await ctx.send(embed=embed)
        if "Belarus" in args:
            dem = open("foklar/Belarus.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Belaruslu fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Belaruslu oldum")
            await ctx.send(embed=embed)
        if "Belçika" in args:
            dem = open("foklar/Belçika.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Belçikalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Belçikalı oldum")
            await ctx.send(embed=embed)
        if "BosnaHersek" in args:
            dem = open("foklar/bosna.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bosnalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Bosnalı oldum")
            await ctx.send(embed=embed)
        if "Bulgaristan" in args:
            dem = open("foklar/Bulgaristan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Bulgar fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Bulgar oldum")
            await ctx.send(embed=embed)
        if "Çek" in args:
            dem = open("foklar/Çek.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Çekli fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Çekli oldum")
            await ctx.send(embed=embed)
        if "demokrat" in args:
            dem = open("foklar/demokrat.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Oy saymaca"))
            await Bot.user.edit(username="Demokrat fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Herkes istiklalimde eşit özgür olacak")
            await ctx.send(embed=embed)
        if "Danimarka" in args:
            dem = open("foklar/denmark.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Danimarkalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Danimarkalı oldum")
            await ctx.send(embed=embed)
        if "ermenistan" in args:
            dem = open("foklar/ermenistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Eremeni fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Ermeni oldum")
        if "Estonya" in args:
            dem = open("foklar/estonya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Estonyalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Estonyalı oldum")
            await ctx.send(embed=embed)
        if "fabrika" in args:
            fas = open("foklar/fabrika_fok.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Edit yapıyor"))
            await Bot.user.edit(username="Fabrika fok", avatar=fasc)
            fok = "fabrika"
            print(fok)
            embed = Embed(title="İdeolojileri boş verdim ben edit yapacağım")
            await ctx.send(embed=embed)
        if "faşist" in args:
            fas = open("foklar/fasist_fok.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Yahudi yakmaca"))
            await Bot.user.edit(username="Faşist fok", avatar=fasc)
            fok = "faşist"
            embed = Embed(title="Köklerime döndüm")
            await ctx.send(embed=embed)
        if "finlandiya" in args:
            dem = open("foklar/finland.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Finlandiyalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Finlandiyalı oldum")
            await ctx.send(embed=embed)
        if "fransa" in args:
            dem = open("foklar/fransa.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Fransız fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Fransız oldum")
        if "gürcistan" in args:
            dem = open("foklar/Gürcistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Gürci fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Gürcistanlı oldum")
            await ctx.send(embed=embed)
        if "hırvatistan" in args:
            dem = open("foklar/Hırvatistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Hırvat fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Hırvat oldum")
            await ctx.send(embed=embed)
        if "irlanda" in args:
            dem = open("foklar/İrlanda.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İrlandalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="İrlandalı oldum")
            await ctx.send(embed=embed)
        if "İspanya" in args:
            dem = open("foklar/ispanya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İspanyol fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="İspanyol oldum")
            await ctx.send(embed=embed)
        if "İtalya" in args:
            dem = open("foklar/italya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İtalyan fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="İtalyan oldum")
            await ctx.send(embed=embed)
        if "izlanda" in args:
            dem = open("foklar/izlanda.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İzlandalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="İzlandalı oldum")
        if "karadağ" in args:
            dem = open("foklar/Karadağ.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Karadağlı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Karadağlı oldum")
            await ctx.send(embed=embed)
        if "kazakistan" in args:
            dem = open("foklar/kazakistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Kazak fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Kazak oldum")
        if "kıbrıs" in args:
            dem = open("foklar/kıbrıs.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Kıbrıslı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Kıbrıslı oldum")
        if "kuma" in args:
            fas = open("foklar/kuma fok.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Dünyayı kumalıyor"))
            await Bot.user.edit(username="Kuma fok", avatar=fasc)
            fok = "kuma"
            print(fok)
            embed = Embed(title="Kuma kuma kuma bear izleyip geldim")
            await ctx.send(embed=embed)
        if "kuzey kıbrıs" in args:
            dem = open("foklar/kuzey-kıbrıs.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Kuzey kıbrıslı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Kuzey kıbrıslı oldum")
        if "makedonya" in args:
            dem = open("foklar/kuzey-makedonya.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Makedonyalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Makedonyalı oldum")
        if "letonya" in args:
            dem = open("foklar/Latvia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Letonyalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Letonyalı oldum")
        if "liberteryanist" in args:
            fas = open("foklar/librteryenist.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Özgürlüğün dibine vuruyor"))
            await Bot.user.edit(username="Liberteryanist fok", avatar=fasc)
            fok = "liberteryanist"
            print(fok)
            embed = Embed(title="Özgürlük, özgürlük ve daha fazla özgürlük")
            await ctx.send(embed=embed)
        if "liechtenstein" in args:
            dem = open("foklar/Liechtenstein.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Liechtensteinlı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Liechtensteinlı oldum")
        if "litvanya" in args:
            dem = open("foklar/lithuania.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Litvanyalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Litvanyalı oldum")
            await ctx.send(embed=embed)
        if "lüksemburg" in args:
            dem = open("foklar/Lüksemburg.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Lüksemburglu fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Lüksemburglu oldum")
            await ctx.send(embed=embed)
        if "Macaristan" in args:
            dem = open("foklar/Macaristan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Macar fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Macar oldum")
            await ctx.send(embed=embed)
        if "mao" in args:
            fas = open("foklar/maocu.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Kırlarda hazırlanıyor"))
            await Bot.user.edit(username="Maocu fok", avatar=fasc)
            fok = "maocu"
            print(fok)
            embed = Embed(title="马克思主义者认为，只有人们的社会实践，才是人们对于外界认识的真理性的标准。……判定认识或理论之是否真理，不是依主观上觉得如何而定，而是依客观上社会实践的结果如何而定。真理的标准只能是社会的实践。")
            await ctx.send(embed=embed)
        if "moldova" in args:
            dem = open("foklar/moldovo.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Moldovalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Moldovalı oldum")
            await ctx.send(embed=embed)
        if "monako" in args:
            dem = open("foklar/Monaco.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Monakolu fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Monakolu oldum")
            await ctx.send(embed=embed)
        if "norveç" in args:
            dem = open("foklar/norway.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Norveçli fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Norveçli oldum")
            await ctx.send(embed=embed)
        if "onee-san" in args:
            dem = open("foklar/onee-san.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Minoru-kun'la yaşıyor"))
            await Bot.user.edit(username="Onee-san fok", avatar=demo)
            fok = "oppai"
            print(fok)
            embed = Embed(title="MINORYU-KYUNNNN!!!")
            await ctx.send(embed=embed)
        if "polonya" in args:
            dem = open("foklar/poland.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Polonyalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Polonyalı oldum")
            await ctx.send(embed=embed)
        if "radyoaktif" in args:
            fas = open("foklar/radyoaktif.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="α ışıması yapıyor"))
            await Bot.user.edit(username="Radyoaktif fok", avatar=fasc)
            fok = "radyoaktif"
            print(fok)
            embed = Embed(title="Yanlışlıkla Uranyuma dokundum umarım sıkıntı olmaz")
            await ctx.send(embed=embed)
        if "romanya" in args:
            dem = open("foklar/romania.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Romanyalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Romanyalı oldum")
            await ctx.send(embed=embed)
        if "rus" in args:
            dem = open("foklar/russia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Rus fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Rus oldum")
            await ctx.send(embed=embed)
        if "sırbistan" in args:
            dem = open("foklar/Serbia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Sırp fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Sırp oldum")
            await ctx.send(embed=embed)
        if "slovakya" in args:
            dem = open("foklar/slovakia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Slovakyalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Slovakyalı oldum")
            await ctx.send(embed=embed)
        if "slovenya" in args:
            dem = open("foklar/slovenia.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Slovenyalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Slovenyalı oldum")
            await ctx.send(embed=embed)
        if "stalin" in args:
            dem = open("foklar/Stalin.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Stalin fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Россия - священная наша держава")
            await ctx.send(embed=embed)
        if "isveç" in args:
            dem = open("foklar/sweden.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İsveçli fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="İsveçli oldum")
            await ctx.send(embed=embed)
        if "isviçre" in args:
            dem = open("foklar/switzerland.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İsviçreli fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="İsviçreli oldum")
            await ctx.send(embed=embed)
        if "turan" in args:
            fas = open("foklar/turancı.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Haritayı açık maviye boyuyor"))
            await Bot.user.edit(username="Turancı fok", avatar=fasc)
            fok = "turancı"
            print(fok)
            embed = Embed(title="Türkler üstün ırktır ve ben de görevim olan cihan fethini gerçekleştireceğim")
            await ctx.send(embed=embed)
        if "türk" in args:
            fas = open("foklar/Türkiye.jpg", 'rb')
            fasc = fas.read()
            await Bot.change_presence(activity=Game(name="Yaşayamıyor"))
            await Bot.user.edit(username="Türk fok", avatar=fasc)
            fok = "turancı"
            print(fok)
            embed = Embed(title="Ne mutlu Türküm diyene!")
            await ctx.send(embed=embed)
        if "ukrayna" in args:
            dem = open("foklar/ukrayna.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Ukraynalı fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Ukraynalı oldum")
        if "İngiltere" in args:
            dem = open("foklar/Unitend-kingdom.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="İngiliz fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="İngiliz oldum")
            await ctx.send(embed=embed)
        if "yunanistan" in args:
            dem = open("foklar/yunanistan.jpg", 'rb')
            demo = dem.read()
            await Bot.change_presence(activity=Game(name="Yaşamaya çalışıyor"))
            await Bot.user.edit(username="Yunan fok", avatar=demo)
            fok = "demokrat"
            print(fok)
            embed = Embed(title="Yunan oldum")
            await ctx.send(embed=embed)


# Work

@Bot.command()
async def work(ctx, *args):
    au = str(ctx.author)
    wa = "work/" + au + ".txt"
    if "profil" not in args:
        if os.path.exists(wa) ==  True:
            with open(str(wa), 'r') as f:
                a = str(f.read())
                a = int(a)
                a = a + 150
                a = str(a)
            with open(str(wa), 'w') as f:
                f.write(str(a))
                embed = Embed(title="Çalışman sonucunda 150₺ kazandın")
                await ctx.send(embed=embed)
        if os.path.exists(wa) == False:
            with open(str(wa), 'x') as fe:
                with open(str(wa), "w") as fea:
                    fea.write('150')
                    embed = Embed(title="Çalışman sonucunda 150₺ kazandın\nVarlık: yok")
                    await ctx.send(embed=embed)
    if "profil" in args:
        t = au + " Profili"
        p = open(str(wa), 'r')
        a = str(p.read())
        a = int(a)
        embed = Embed(title=t, description="Para : "+str(a))
        embed.add_field(value="yok", name="Varlık")
        await ctx.send(embed=embed)


# Söz

@Bot.command()
async def söz(ctx):
    l = random.randint(1, 7)
    if l == 1:
        Hitlerlist = [Hitler1,Hitler2,Hitler3, Hitler4, Hitler5, Hitler6, Hitler7, Hitler8, Hitler9, Hitler10, Hitler11, Hitler12, Hitler13, Hitler14, Hitler15, Hitler16, Hitler17, Hitler18, Hitler19, Hitler20, Hitler21, Hitler22, Hitler23, Hitler24, Hitler25, Hitler26, Hitler27, Hitler28, Hitler29, Hitler30, Hitler31, Hitler32, Hitler33, Hitler34, Hitler35, Hitler36, Hitler37, Hitler38, Hitler39, Hitler40, Hitler41, Hitler42, Hitler43, Hitler44, Hitler45, Hitler46, Hitler47, Hitler48, Hitler49, Hitler50, Hitler51, Hitler52, Hitler53, Hitler54, Hitler55, Hitler56, Hitler57, Hitler58, Hitler59, Hitler60, Hitler61, Hitler62, Hitler63, Hitler64, Hitler65, Hitler66, Hitler67, Hitler68, Hitler69, Hitler70, Hitler71, Hitler72, Hitler73, Hitler74, Hitler75, Hitler76, Hitler77, Hitler78, Hitler79, Hitler80, Hitler81, Hitler82, Hitler83, Hitler84, Hitler85, Hitler86, Hitler87, Hitler88, Hitler89, Hitler90, Hitler91, Hitler92, Hitler93, Hitler94, Hitler95, Hitler96, Hitler97, Hitler98, Hitler99, Hitler100, Hitler101, Hitler102, Hitler103, Hitler104, Hitler105, Hitler106, Hitler107, Hitler108, Hitler109, Hitler110, Hitler111, Hitler112, Hitler113, Hitler114, Hitler115, Hitler116, Hitler117, Hitler118, Hitler119, Hitler120, Hitler121, Hitler122, Hitler123, Hitler124, Hitler125, Hitler126, Hitler127, Hitler128, Hitler129, Hitler130, Hitler131, Hitler132, Hitler133, Hitler134, Hitler135, Hitler136, Hitler137, Hitler138, Hitler139, Hitler140, Hitler141, Hitler142, Hitler143, Hitler144, Hitler145, Hitler146, Hitler147, Hitler148, Hitler149, Hitler150, Hitler151, Hitler152, Hitler153, Hitler154, Hitler155, Hitler156, Hitler157, Hitler158, Hitler159, Hitler160, Hitler161, Hitler162, Hitler163, Hitler164, Hitler165, Hitler166, Hitler167, Hitler168, Hitler169, Hitler170, Hitler171, Hitler172, Hitler173, Hitler174, Hitler175, Hitler176, Hitler177, Hitler178, Hitler179, Hitler180, Hitler181, Hitler182, Hitler183, Hitler184, Hitler185, Hitler186, Hitler187, Hitler188, Hitler189, Hitler190, Hitler191, Hitler192, Hitler193, Hitler194, Hitler195, Hitler196, Hitler197, Hitler198, Hitler199, Hitler200, Hitler201, Hitler202, Hitler203, Hitler204, Hitler205, Hitler206, Hitler207, Hitler208, Hitler209, Hitler210, Hitler211, Hitler212, Hitler213, Hitler214, Hitler215, Hitler216, Hitler217, Hitler218, Hitler219, Hitler220, Hitler221, Hitler222, Hitler223, Hitler224, Hitler225, Hitler226, Hitler227, Hitler228, Hitler229, Hitler230, Hitler231, Hitler232, Hitler233, Hitler234, Hitler235, Hitler236, Hitler237, Hitler238, Hitler239, Hitler240, Hitler241, Hitler242, Hitler243, Hitler244, Hitler245, Hitler246, Hitler247, Hitler248, Hitler249, Hitler250, Hitler251, Hitler252, Hitler253, Hitler254, Hitler255, Hitler256, Hitler257]
        f = random.choice(Hitlerlist)
        embed = Embed(title="Hitler derki", description=f)
        await ctx.send(embed=embed)
    if l == 2:
        Ataturklist = [Ataturk1, Ataturk2, Ataturk3, Ataturk4, Ataturk5, Ataturk6, Ataturk7, Ataturk8, Ataturk9, Ataturk10, Ataturk11, Ataturk12, Ataturk13, Ataturk14, Ataturk15, Ataturk16, Ataturk17, Ataturk18, Ataturk19, Ataturk20, Ataturk21, Ataturk22, Ataturk23, Ataturk24, Ataturk25, Ataturk26, Ataturk27, Ataturk28, Ataturk29, Ataturk30, Ataturk31, Ataturk32, Ataturk33, Ataturk34, Ataturk35, Ataturk36, Ataturk37, Ataturk38, Ataturk39, Ataturk40, Ataturk41, Ataturk42, Ataturk43, Ataturk44, Ataturk45, Ataturk46, Ataturk47, Ataturk48, Ataturk49, Ataturk50, Ataturk51, Ataturk52, Ataturk53, Ataturk54, Ataturk55, Ataturk56, Ataturk57, Ataturk58, Ataturk59, Ataturk60, Ataturk61, Ataturk62, Ataturk63, Ataturk64, Ataturk65, Ataturk66, Ataturk67, Ataturk68, Ataturk69, Ataturk70, Ataturk71, Ataturk72, Ataturk73, Ataturk74, Ataturk75, Ataturk76, Ataturk77, Ataturk78, Ataturk79, Ataturk80, Ataturk81, Ataturk82, Ataturk83, Ataturk84, Ataturk85, Ataturk86, Ataturk87, Ataturk88, Ataturk89, Ataturk90, Ataturk91, Ataturk92, Ataturk93, Ataturk94, Ataturk95, Ataturk96, Ataturk97, Ataturk98, Ataturk99, Ataturk100, Ataturk101, Ataturk102, Ataturk103, Ataturk104, Ataturk105, Ataturk106, Ataturk107, Ataturk108, Ataturk109, Ataturk110, Ataturk111, Ataturk112, Ataturk113, Ataturk114, Ataturk115, Ataturk116, Ataturk117, Ataturk118, Ataturk119, Ataturk120, Ataturk121, Ataturk122, Ataturk123, Ataturk124, Ataturk125, Ataturk126, Ataturk127, Ataturk128, Ataturk129, Ataturk130, Ataturk131, Ataturk132, Ataturk133, Ataturk134, Ataturk135, Ataturk136, Ataturk137, Ataturk138, Ataturk139, Ataturk140, Ataturk141, Ataturk142, Ataturk143, Ataturk144, Ataturk145, Ataturk146, Ataturk147, Ataturk148, Ataturk149, Ataturk150, Ataturk151, Ataturk152, Ataturk153, Ataturk154, Ataturk155, Ataturk156, Ataturk157, Ataturk158, Ataturk159, Ataturk160, Ataturk161, Ataturk162, Ataturk163, Ataturk164, Ataturk165, Ataturk166, Ataturk167, Ataturk168, Ataturk169, Ataturk170, Ataturk171, Ataturk172, Ataturk173, Ataturk174, Ataturk175, Ataturk176, Ataturk177, Ataturk178, Ataturk179, Ataturk180, Ataturk181, Ataturk182, Ataturk183, Ataturk184, Ataturk185, Ataturk186, Ataturk187]
        f = random.choice(Ataturklist)
        embed = Embed(title="Atatürk derki", description=f)
        await ctx.send(embed=embed)
    if l == 3:
        Leninlist = [Lenin1, Lenin2, Lenin3, Lenin4, Lenin5, Lenin6, Lenin7, Lenin8, Lenin9, Lenin10, Lenin11, Lenin12, Lenin13, Lenin14, Lenin15, Lenin16, Lenin17, Lenin18, Lenin19, Lenin20, Lenin21]
        f = random.choice(Leninlist)
        embed = Embed(title="Lenin derki", description=f)
        await ctx.send(embed=embed)
    if l == 4:
        Stalinlist = [Stalin1, Stalin2, Stalin3, Stalin4, Stalin5, Stalin6, Stalin7, Stalin8, Stalin9, Stalin10, Stalin11, Stalin12, Stalin13, Stalin14, Stalin15, Stalin16, Stalin17, Stalin18, Stalin19, Stalin20, Stalin21, Stalin22, Stalin23, Stalin24, Stalin25]
        f = random.choice(Stalinlist)
        embed = Embed(title="Stalin derki", description=f)
        await ctx.send(embed=embed)
    if l == 5:
        Cengizlist = [CengizHan1, CengizHan2, CengizHan3, CengizHan4, CengizHan5, CengizHan6, CengizHan7, CengizHan8, CengizHan9]
        f = random.choice(Cengizlist)
        embed = Embed(title="Cengiz Han derki", description=f)
        await ctx.send(embed=embed)
    if l == 6:
        CelalŞengörlist = [Celal1, Celal2, Celal3, Celal4, Celal5, Celal6, Celal7, Celal8, Celal9, Celal10, Celal11, Celal12, Celal13, Celal14, Celal15, Celal16, Celal17, Celal18, Celal19, Celal20, Celal21, Celal22, Celal23, Celal24, Celal25, Celal26, Celal27, Celal28, Celal29, Celal30, Celal31, Celal32, Celal33, Celal34, Celal35, Celal36, Celal37, Celal38, Celal39, Celal40, Celal41, Celal42, Celal43]
        f = random.choice(CelalŞengörlist)
        embed = Embed(title="Celal Şengör derki", description=f)
        await ctx.send(embed=embed)
    if l == 7: # TODO 2.7 Eklenecek
        Metehanlist = [Metehan1, Metehan2, Metehan3, Metehan4, Metehan5, Metehan6, Metehan7]
        f = random.choice(Metehanlist)
        embed = Embed(title="Metehan derki", description=f)
        await ctx.send(embed=embed)


# Konuşma

@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return
    # 日本語
    if 'こんにちは' == message.content and message.author != Bot.user:
        await message.channel.send(f"こんにちは{message.author.name}、お名前は何ですか？")
    if "私は" in message.content and message.author != Bot.user and "こんにちは" not in message.content:
        a = message.content.replace("私は",'')
        b = a.replace("です",'')
        await message.channel.send(f"よろしくお願いします{b}－さん、俺はファシストエイですよろしくお願いします。")
    if "おはよう" in message.content and message.author != Bot.user:
        await message.channel.send(f"おはよう{message.author.name}、お名前は何ですか？")
    if "こんばんは" in message.content and message.author != Bot.user:
        await message.channel.send(f"こんばんは{message.author.name}ーさん。")
    if "おやすみ" in message.content and message.author != Bot.user:
        await message.channel.send(f"おやすみございます{message.author.name}ーさん。")
    if "元気ですか" in message.content and message.author != Bot.user:
        await message.channel.send(f"大丈夫です。あなたは元気ですか？")
    if "職業はなんですか" in message.content and message.author != Bot.user:
        await message.channel.send(f"俺は楽しいベースのDiscordボットで、!yardımコマンドを使用してコマンドを表示できます")
    # English
    if "hello" in message.content and message.author != Bot.user:
        await message.channel.send(f"hello {message.author.name} what is your name?")
    if "my name is" in message.content and message.author != Bot.user and "hello" not in message.content:
        a = message.content.replace("my name is",'')
        await message.channel.send(f"hello {a} nice to meet you, I am")
    if "good morning" in message.content and message.author != Bot.user:
        await message.channel.send(f"good morning {message.author.name}")
    if "good evening" in message.content and message.author != Bot.user:
        await message.channel.send(f"good evening {message.author.name}")
    if "good night" in message.content and message.author != Bot.user:
        await message.channel.send(f"good night {message.author.name}")
    if "good bye" in message.content and message.author != Bot.user:
        await message.channel.send(f"good bye {message.author.name}")
    if "how are you" in message.content and message.author != Bot.user:
        await message.channel.send(f"I am fine, how are you {message.author.name}")
    if "what is your job" in message.content and message.author != Bot.user:
        await message.channel.send(f"I am a entertainment based Discord bot, I can show you commands with !yardım command")
    # Deutsch
    if "hallo" in message.content and message.author != Bot.user:
        await message.channel.send(f"hallo {message.author.name} was ist dein name?")
    if "mein name ist" in message.content and message.author != Bot.user and "hallo" not in message.content:
        a = message.content.replace("mein name ist",'')
        await message.channel.send(f"hallo {a} schön dich kennen zu lernen, ich bin")
    if "guten morgen" in message.content and message.author != Bot.user:
        await message.channel.send(f"guten morgen {message.author.name}")
    if "guten abend" in message.content and message.author != Bot.user:
        await message.channel.send(f"guten abend {message.author.name}")
    if "gute nacht" in message.content and message.author != Bot.user:
        await message.channel.send(f"gute nacht {message.author.name}")
    if "Bis später" in message.content and message.author != Bot.user:
        await message.channel.send(f"Bis später {message.author.name}")
    if "wie gehts" in message.content and message.author != Bot.user:
        await message.channel.send(f"Ich bin gut, wie geht's {message.author.name}")
    if "was ist dein job" in message.content and message.author != Bot.user:
        await message.channel.send(f"Ich bin ein Entertainment basiertes Discord Bot, ich kann dir mit !yardım kommandos anzeigen")
    # 한국인
    if "안녕" in message.content and message.author != Bot.user:
        await message.channel.send(f"안녕하세요 이름이 뭐에 요?")
    if "내 이름은" in message.content and message.author != Bot.user and "안녕" not in message.content:
        a = message.content.replace("내 이름은",'')
        await message.channel.send(f"안녕 {a} 안녕하세요, 저는 파시스트 가오리")
    if "오전 잘 지내요" in message.content and message.author != Bot.user:
        await message.channel.send(f"오전 잘 지내요 {message.author.name}")
    if "저녁 잘 지내요" in message.content and message.author != Bot.user:
        await message.channel.send(f"저녁 잘 지내요 {message.author.name}")
    if "나중에 봐요" in message.content and message.author != Bot.user:
        await message.channel.send(f"나중에 봐요 {message.author.name}")
    if "잘 지내고 있나요" in message.content and message.author != Bot.user:
        await message.channel.send(f"전 잘 지냅니다. 당신은 어떤가요?")
    if "너 뭐하니" in message.content and message.author != Bot.user:
        await message.channel.send(f"나는 재미를 위한 Discord 봇입니다! !yardım 명령을 사용하여 내 명령을 볼 수 있습니다.")
    else:
        await Bot.process_commands(message)
    # Küfür filtre TODO
    if "Puşt" in message.content and message.author != Bot.user:
        await message.delete()


@Bot.command()
async def propaganda(ctx):
    propagandalist = [Propaganda1, Propaganda2, Propaganda3, Propaganda4, Propaganda5, Propaganda6, Propaganda7, Propaganda8, Propaganda9, Propaganda10, Propaganda11, Propaganda12, Propaganda13, Propaganda14, Propaganda15, Propaganda16, Propaganda17, Propaganda18, Propaganda19, Propaganda20, Propaganda21, Propaganda22, Propaganda23, Propaganda24, Propaganda25, Propaganda26, Propaganda27, Propaganda28, Propaganda29, Propaganda30, Propaganda31, Propaganda32, Propaganda33, Propaganda34, Propaganda35, Propaganda36, Propaganda37, Propaganda38, Propaganda39, Propaganda40, Propaganda41, Propaganda42, Propaganda43, Propaganda44, Propaganda45, Propaganda46, Propaganda47, Propaganda48, Propaganda49, Propaganda50, Propaganda51, Propaganda52, Propaganda53, Propaganda54, Propaganda55, Propaganda56, Propaganda57, Propaganda58, Propaganda59, Propaganda60, Propaganda61]
    await ctx.send(random.choice(propagandalist))


@Bot.command()
async def r(ctx, *args):
    if "kitap" in args:
        page = requests.get("https://www.generatormix.com/random-book-generator")
        soup = BeautifulSoup(page.text, "lxml")
        a = soup.find("div", class_="col-7")
        b = a.text.replace("Get it on Amazon US", "")
        c = b.replace("Fiction", "Kurgu")
        d = c.replace("keywords", "Anahtar Kelimeler")
        e = d.replace("\n\n", "\n")
        f = e.replace("\nby ", "Yazar: ")
        embed = Embed(title="Random Kitap Önerisi", description=f, color=0x00ff00)
        await ctx.send(embed=embed)
    if "film" in args:
        page = requests.get("https://www.generatormix.com/random-movie-generator")
        soup = BeautifulSoup(page.text, "lxml")
        a = soup.find("div", class_="thumbnail-col-3 tile-block-inner marg-top first")
        b = a.text.replace("Watch trailer", "")
        d = c.replace("Get it on Amazon US", "")
        embed = Embed(title="Random Film Önerisi", description=d, color=0x00ff00)
        await ctx.send(embed=embed)
    if "şarkı" in args:
        page = requests.get("https://www.generatormix.com/random-spotify-songs-generator")
        soup = BeautifulSoup(page.text, "lxml")
        a = soup.find("div", class_="thumbnail-col-3 tile-block-inner marg-top first")
        z = soup.find("a", class_="btn btn-default col-10 no-float btn-spotify marg-top")["href"]
        b = a.text.replace("No preview available.", "")
        c = b.replace(" Get track on Spotify", z)
        d = c.replace("Get it on Amazon US", "")
        embed = Embed(title="Random Şarkı Önerisi", description=str(d), color=0x00ff00)
        await ctx.send(embed=embed)
    if "oyun" in args:
        page = requests.get("https://www.generatormix.com/random-steam-games-generator")
        soup = BeautifulSoup(page.text, "lxml")
        a = soup.find("a", class_="btn btn-steam marg-bottom col-12")["href"]
        await ctx.send(a)
    if "anime" in args:
        query = '''
        query ($id: Int) { # Define which variables will be used in the query (id)
        Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
            id
            title {
            romaji
            }
        }
        }
        '''
        l = random.randint(1, 9999)
        variables = {
            'id': l
        }
        url = 'https://graphql.anilist.co'
        response = requests.post(url, json={'query': query, 'variables': variables})
        a = json.loads(response.text)
        url = 'https://anilist.co/anime/' + str(l)
        u = a.get('data').get('Media').get('title').get('romaji')
        embed = Embed(title=u, description=url, color=0x00ff00)
        await ctx.send(embed=embed)
    if "manga" in args:
        l = random.randint(1, 20700)
        url = 'https://myanimelist.net/manga/' + str(l)
        embed = Embed(title="Random manga önerisi" ,description=url)
        await ctx.send(embed=embed)


@Bot.command()
async def zar(ctx, u):
    z = random.randint(1, 6)
    embed = Embed(title="Zar atıldı!", description=z , color=0x00ff00)
    await ctx.send(embed=embed)


@Bot.command()
async def Kapat(ctx):
    au = ctx.author.id
    if au == 618214247742308361:
        await ctx.send("Kapatılıyor...")
        exit()
    if au != 618214247742308361:
        await ctx.send("Kapatma yetkiniz yok")


Bot.run(token_2.token)
