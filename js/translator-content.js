var dictionary = {
    'en' : {
        'page-name': 'Alexander Dovnar professional profile page',
        'home-i-m' : "Here you can find",
    },
};

var translator = Translator({
    language : 'en',
    dictionary : dictionary,
    autostart : true,
    htmlfriendly : true,
});

function dictionaryRu(){
    var myDict = [];
    myDict['page-name'] = 'Профессиональная страница Довнара Александра'
    myDict['home-i-m'] = 'Я есть';
    translator.addTranslation('ru', myDict);
}
