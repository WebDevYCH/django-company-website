! function() {
    ! function(e, t, a, i, n, r, l) {
        e.GoogleAnalyticsObject = n, e.ga = e.ga || function() {
            (e.ga.q = e.ga.q || []).push(arguments)
        }, e.ga.l = 1 * new Date, r = t.createElement(a), l = t.getElementsByTagName(a)[0], r.async = 1, r.src = "https://www.google-analytics.com/analytics.js", l.parentNode.insertBefore(r, l)
    }(window, document, "script", 0, "ga"), ga("create", "UA-76493652-2", "auto"), ga("set", "title", "Article Player Shown"), ga("send", "pageview", location.pathname), window.parent.postMessage(JSON.stringify({ src: window.location.toString(), context: "iframe.resize", height: 80, width: 325 }), "*");
    var e, t, a = String(Math.random().toString(22).substr(2, 22)),
        n = [
            ["#progress-text", "color"],
            ["#backwards-background", "background-color"],
            ["#forwards-background", "background-color"],
            ["#play-background", "background-color"],
            ["#speed-line", "border-color"],
            ["#speed-text", "color"],
            ["#divider-line", "border-color"],
            [".arrow-triangle", "background-color"],
            [".arrow-triangle-small", "background-color"],
            ["#rectangle", "border-color"],
            ["#speed", "color"],
            ["#forwards", "color"],
            ["#duration", "color"],
            ["#listen-text", "color"],
            [".pause", "background-color"],
            ["#pulltab", "border-color"],
            ["#pulltab", "color"],
            ["#playlist", "border-color"],
            ["#playlist", "color"],
            [".playlist-entry", "border-color"]
        ],
        r = function(e, t) { return binge_body = document.getElementById("bingewith-body"), binge_body ? tabindex = `tabindex="${4*e+t}"` : tabindex = "", tabindex },
        l = function() { var e = window.location.href; return e.match("/elderecho.com|espaciopymes.com|espacioasesoria.com|efl.es|derecholocal.es/g") ? listenText = "ESCUCHA EL ARTÍCULO" : e.includes("alvarezabogadostenerife") ? listenText = "ESCUCHE EL ARTÍCULO" : listenText = "LISTEN TO THIS ARTICLE", listenText },
        s = '\n  <div id="playlist-entry-0" class="playlist-entry">\n      <div class="playlist-entry-status">\n        <div class="arrow-triangle-small left"></div>\n      </div>\n      <div class="playlist-entry-title"></div>\n      <div class="playlist-entry-duration"></div>\n    </div>\n    <div id="playlist-entry-1" class="playlist-entry">\n      <div class="playlist-entry-status" style="visibility: hidden">\n        <div class="arrow-triangle-small left"></div>\n      </div>\n      <div class="playlist-entry-title"></div>\n      <div class="playlist-entry-duration"></div>\n    </div>\n    <div id="playlist-entry-2" class="playlist-entry">\n      <div class="playlist-entry-status" style="visibility: hidden">\n        <div class="arrow-triangle-small left"></div>\n      </div>\n      <div class="playlist-entry-title"></div>\n      <div class="playlist-entry-duration"></div>\n    </div>\n    <div id="playlist-entry-3" class="playlist-entry">\n      <div class="playlist-entry-status" style="visibility: hidden">\n        <div class="arrow-triangle-small left"></div>\n      </div>\n      <div class="playlist-entry-title"></div>\n      <div class="playlist-entry-duration"></div>\n    </div>\n',
        o = '\n    <div id="pulltab" class="pulltab-collapsed">\n      <div id="pulltab-text">Playlist</div>\n    </div>\n';

    function d(e) { return `\n<div id="rectangle" style="display: none;">\n\t<div id="listen-text"> ${l()}</div>\n\t<div id="player-container" style="display: none;">\n\t\t  <button type="button" id="backwards-area" class="button" ${r(e,1)}></button>\n      <div id="backwards-background"></div>\n      <div id="backwards"></div>\n      <button type="button" id="play-area" class="button" ${r(e,2)}></button>\n      <div class="play left" id="play-outline" style="display: none">\n        <div id="play-background"></div>\n        <div id="play-graphic"></div>\n      </div>\n      <div class="play arrow-triangle left" id="play-filled" style="display: none"></div>\n      <div class="pause pause-rectangle" style="display: none;"></div>\n\t\t  <div class="pause pause-rectangle-1" style="display: none;"></div>\n      <button type="button" id="forwards-area" class="button" ${r(e,3)}></button>\n      <div id="forwards-background"></div>\n      \x3c!--<div id="divider-line"></div>--\x3e\n\t\t  <div id="forwards"></div>\n      <div id="progress">\n        <div id="progress-text">Remaining</div>\n        <div id="duration"></div>\n      </div>\n\t    <button type="button" id="speed-area" class="button" ${r(e,4)}></button>\n      <div id="speed-container">\n        \x3c!--<div id="speed-line"></div>--\x3e\n        <div id="speed-text">Speed</div>\n        <div id="speed">1X</div>\n      </div>\n  </div>\n  <div id="playlist">\n  </div>\n\t<div id="generate-audio" style="display: none;">\n\t\t<div id="generate-area"></div>\n\t\t<div id="generate-text">Click to Generate Audio</div>\n\t\t<div id="generating-text" style="display: none;">Generating audio</div>\n\t\t<div id="generate-duration"></div>\n\t</div>\n\t<div id="signup" style="display: none;">\n\t<div id="signup-text">Sign up at <a style="color: purple;" href="https://bingewith.com/about">BingeWith</a> to let your audience Listen!</p>\n\t</div>\n</div>\n` }
    if (void 0 === window.jQuery || "1.4.2" !== window.jQuery.fn.jquery) {
        var c = document.createElement("script");
        c.setAttribute("type", "text/javascript"), c.setAttribute("src", "https://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"), c.readyState ? c.onreadystatechange = function() { "complete" != this.readyState && "loaded" != this.readyState || u() } : c.onload = u, (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(c)
    } else e = window.jQuery, p();

    function p() {
        if (void 0 === window.playerjs) {
            var e = document.createElement("script");
            e.setAttribute("type", "text/javascript"), e.setAttribute("src", "//cdn.embed.ly/player-0.1.0.js"), e.readyState ? e.onreadystatechange = function() { "complete" != this.readyState && "loaded" != this.readyState || y() } : e.onload = y, (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(e)
        } else t = window.playerjs, v()
    }

    function u() { e = window.jQuery.noConflict(!0), p() }

    function y() { t = window.playerjs, v() }

    function g(e) {
        var t = window.location.href;
        t.includes("blog-stag.heroku.com") && (t = t.replace("blog-stag.heroku.com", "blog.heroku.com"));
        var a = document.getElementsByTagName("script");
        currentScript = a[a.length - 1];
        var i = e[0].dataset.href;
        return testing_param = currentScript.getAttribute("testing"), testing_param && (t = testing_param), i && (t = i), t
    }

    function v() {
        e(document).ready(function(r) {
            r('<link rel="stylesheet" href="https://bingewith.com/assets/css/affiliate_player_clean.css">').appendTo("head"), r('<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">').appendTo("head"), r('<meta name="viewport" content="width=device-width, initial-scale=1.0">').appendTo("head");
            var l = window.location.href,
                c = "https://bingewith.com";

            function p(e, t) {
                var i = new Date;
                i = i.toLocaleString("en-US").replace(",", "");
                e = [a, i, e, encodeURIComponent(t)].join(",");
                r.get(c + "/logger?event=" + e)
            }(l.includes("bingewith.com") || l.includes("localhost")) && (c = "");
            var u = function(t) {
                    var a = r("#player", t)[0];
                    Number.isNaN(a.duration) || e("#duration", t).html(w(a.duration))
                },
                y = function(t) {
                    var a = r("#player", t)[0];
                    Number.isNaN(a.duration) || e("#duration", t).html(w(a.duration - a.currentTime))
                },
                v = function(e, t) {
                    if (t.length > 1)
                        for (i = 0; i < t.length; i++) {
                            var a = "#playlist-entry-" + i;
                            r(a, e).find(".playlist-entry-title").text(t[i][1]), r(a + " .playlist-entry-duration", e).text(t[i][3].replace(/^0+(\d)/, "$1")), r(a, e).attr("data-href", t[i][0]), r(a, e).attr("data-title", t[i][1]), r(a, e).attr("data-duration", t[i][3])
                        } else r("#pulltab", e).hide(), r("#playlist", e).hide()
                },
                h = async function(e, t, a) {
                    var i = e;
                    v(a, i);
                    var n = e[0],
                        l = await storage_prefix + n[0],
                        s = await n[1],
                        o = (await n[2], await n[3]);
                    r("#rectangle", a).hide(), r("#generate-audio", a).hide(), r("#player-container", a).prepend('<audio id="player"><source type="audio/mp3"></audio>'), r("#player", a).attr("title", s);
                    r("#player", a)[0];
                    await T(t, a);
                    try { r("#duration", a).html(o.replace(/^0+/, "")) } catch (e) {}
                    return r("#player-container", a).show(), r("#rectangle", a).show(), r("#player", a).attr("data-playlist_index", 0), r("#player", a).attr("data-playlist_articles", JSON.stringify(i)), r("#player", a).attr("data-href", l), r("#player", a).attr("data-title", s), r("#player", a).attr("data-duration", o), window.parent.postMessage(JSON.stringify({ src: window.location.toString(), context: "player_loaded" }), "*"), l
                },
                f = async function(e, a) {
                    ga("send", "pageview", "Article Generate Button", e), ga("send", "event", "Article Generated", e);
                    const i = await

                    function(e, t) {
                        return new Promise(function(a, i) {
                            var n = g(t);
                            n.includes("bingewith.com/article/") || n.includes("localhost:3000/article/") || n.includes("localhost:3000"), r.get(c + "/get_mp3_url?url=" + e, function(e) {
                                try {
                                    var t = JSON.parse(e);
                                    a(t)
                                } catch (e) {}
                            })
                        })
                    }(e, a), n = i[0];
                    v(a, i);
                    var l = await storage_prefix + n[0],
                        s = await n[1];
                    await n[2];
                    r("#generate-audio", a).hide(), r("#player-container", a).prepend('<audio id="player"><source type="audio/mp3"></audio>'), r("#player", a).attr("title", s);
                    var o = r("#player", a)[0];
                    return await T(e, a), o.addEventListener("timeupdate", function() { y(a) }), o.addEventListener("durationchange", function() { u(a) }), o.addEventListener("ended", function() { u(a), player = r("#player", a)[0], !0 === player.paused && E(a) }), o.addEventListener("loadedmetadata", function() { r("#player-container", a).show(), p("shown", e) }), o.src = l, t.HTML5Adapter(o).ready(), l
                },
                w = function(e) {
                    var t = Math.floor(e / 60),
                        a = Math.floor(e % 60);
                    if (a < 10) var i = "0" + a.toFixed(0).toString();
                    else i = a.toFixed(0).toString();
                    return t + ":" + i
                };
            bingewith_players = document.getElementsByClassName("bingewith-players"), 0 === bingewith_players.length && (bp = document.getElementById("bingewith-player"), bp && (bingewith_players = [bp]));
            for (let e = 0; e < bingewith_players.length; e++) {
                const t = r(bingewith_players[e]);
                t.find("#rectangle").remove(), t[0].innerHTML += d(e), r(t).attr("class").includes("micro") || (t.find("#playlist")[0].innerHTML += s, t.find("#player-container")[0].innerHTML += o), player = r("#player", t)[0], playBtn = r("#play-area", t)[0], backBtn = r("#backwards-area", t)[0], ffwBtn = r("#forwards-area", t)[0], speedBtn = r("#speed-area", t)[0], generateBtn = r("#generate-area", t)[0], playlistBtn = r("#pulltab", t)[0], playlistEntryBtn = r(".playlist-entry", t), storage_prefix = "https://storage.googleapis.com/tvchat-mp3/", storage_suffix = ".mp3";
                var m = r(".button", t)[0];
                for (let e = 0; e < m.length; e++) m[e].addEventListener("mousedown", function() { m[e].classList.add("using-mouse") }), m[e].addEventListener("keydown", function() { m[e].classList.remove("using-mouse") });
                null != playBtn && playBtn.addEventListener("click", function() { S(t) }), null != ffwBtn && ffwBtn.addEventListener("click", function() { L(t) }), null != backBtn && backBtn.addEventListener("click", function() { k(t) }), null != generateBtn && generateBtn.addEventListener("click", function() {}), null != speedBtn && speedBtn.addEventListener("click", function() { B(t) }), null != playlistBtn && playlistBtn.addEventListener("click", function() { r(".pulltab-collapsed", t)[0] ? (window.parent.postMessage(JSON.stringify({ src: window.location.toString(), context: "iframe.resize", height: 235, width: 100 }), "*"), r("#pulltab", t).removeClass("pulltab-collapsed"), r("#pulltab", t).addClass("pulltab-expanded"), r("#playlist", t).show()) : r(".pulltab-expanded", t)[0] && (r("#pulltab", t).removeClass("pulltab-expanded"), r("#pulltab", t).addClass("pulltab-collapsed"), r("#playlist", t).hide(), window.parent.postMessage(JSON.stringify({ src: window.location.toString(), context: "iframe.resize", height: 80, width: 100 }), "*")) }), null != playlistEntryBtn && playlistEntryBtn.toArray().forEach(e => {
                    e.addEventListener("click", function() {
                        var a = e.getAttribute("id").split("-")[2];
                        r("#player", t).attr("data-playlist_index", a);
                        r("#player", t)[0];
                        r(".playlist-entry-status", t).toArray().forEach(e => { r(e).css("visibility", "hidden") }), r(".playlist-entry-status", e).css("visibility", "visible"), r("#player", t).attr("data-href", storage_prefix + r(e).attr("data-href")), r("#player", t).attr("data-duration", r(e).attr("data-duration")), r("#player", t).attr("data-title", r(e).attr("data-title")), _(t), S(t)
                    })
                })
            }
            var b = {},
                x = function(t) {
                    var a = 90;
                    t in b && (a = b[t]), a > 0 ? (a -= 1, e("#generate-duration", t).html(a + " seconds left"), setTimeout(x, 1e3, t)) : (a = 0, e("#generate-duration", t).html("a little longer")), b[t] = a
                };

            function E(e) { r(".play", e).show(), r(".pause-rectangle", e).hide(), r(".pause-rectangle-1", e).hide(), r("#play-area", e).removeClass("pause") }

            function _(e) {
                var a = r("#player", e).attr("data-href"),
                    i = (r("#player", e).attr("data-title"), r("#player", e).attr("data-duration").replace(/^0+/, "")),
                    n = r("#player", e)[0];
                n.src = a, r("#duration", e).html(i), n.addEventListener("timeupdate", function() { y(e) }), n.addEventListener("durationchange", function() { u(e) }), n.addEventListener("ended", function() {
                    u(e), player = r("#player", e)[0], !0 === player.paused && E(e);
                    var t = JSON.parse(r("#player", e).attr("data-playlist_articles")),
                        l = parseInt(r("#player", e).attr("data-playlist_index"));
                    r(r(".playlist-entry-status", e)[l]).css("visibility", "hidden"), (l += 1) >= t.length && (l = 0), r(r(".playlist-entry-status", e)[l]).css("visibility", "visible"), r("#player", e).attr("data-playlist_index", l), a = storage_prefix + t[l][0], t[l][1], author = t[l][2], i = t[l][3], n.src = a;
                    try { r("#duration", e).html(i) } catch (e) {}
                    0 != l && (! function(e) { r(".play", e).hide(), r(".pause-rectangle", e).show(), r(".pause-rectangle-1", e).show(), r("#play-area", e).addClass("pause") }(e), r("#listen-text", e).text("Playing the next article"), setTimeout(function() { n.play() }, 4e3))
                }), n.addEventListener("loadedmetadata", function() { r("#player-container", e).show(), r("#rectangle", e).show(), p("shown", l) }), t.HTML5Adapter(n).ready()
            }

            function S(e) {
                if (player = r("#player", e)[0], (t = r(e).attr("class")).includes("micro")) var t = "size=micro";
                else t = "size=normal";
                if (r("#player", e)[0].src || _(e), !1 === player.paused) {
                    player.pause(), E(e);
                    ga("send", "event", "Article Pause - Big Player", r("#player", e).attr("title"), window.location.href + "&" + t), p("pause", window.location.href + "&" + t)
                } else {
                    for (let e = 0; e < bingewith_players.length; e++) {
                        const t = r(bingewith_players[e]),
                            a = r("#player", t)[0];
                        player !== a && (a.pause(), E(t))
                    }
                    player.play(), r(".play", e).hide(), r(".pause-rectangle", e).show(), r(".pause-rectangle-1", e).show();
                    r("#play-area", e).addClass("pause"), ga("send", "event", "Article Play - Big Player", r("#player", e).attr("title"), window.location.href + "&" + t), p("play", window.location.href + "&" + t), window.parent.postMessage(JSON.stringify({ src: window.location.toString(), context: "player_played" }), "*")
                }
            }

            function k(e) {
                player = r("#player", e)[0];
                var t = player.currentTime;
                player.currentTime = t - 15
            }

            function L(e) {
                player = r("#player", e)[0];
                var t = player.currentTime;
                player.currentTime = t + 15
            }

            function B(t) {
                player = r("#player", t)[0];
                var a = r("#speed", t)[0].textContent;
                (a = parseFloat(a.split("X")[0])) < 2.2 ? a += .3 : a = .7, e("#speed", t).html(a.toFixed(1) + "X"), player.playbackRate = a
            }
            async function T(e, t) {
                if (!e.includes("page=preferences")) {
                    var a = await

                    function(e) {
                        return new Promise(function(t, a) {
                            r.get(c + "/get_color?url=" + e, function(e) {
                                var a = JSON.parse(e);
                                t(a)
                            })
                        })
                    }(e), [i, l, s, o, d] = a;
                    n.forEach(function(e) { r(e[0], t).css(e[1], i) }), l && r("#listen-text", t).css("font-family", l), "outline" === s ? (r("#play-outline", t).show(), r(".pause", t).css("border", "1.5px solid " + i), r(".pause", t).css("background-color", "white"), r("#play-filled", t).remove()) : (r("#play-filled", t).show(), r(".pause", t).css("border", "1.5px solid " + i), r("#play-outline", t).remove()), "no" === d && r("#listen-text", t).remove()
                }
            }
            async function N(e, t) {
                var a = e;
                e.includes("?referrer=") && (a = e.split("?referrer=")[1]), r.get(c + "/mp3_ready?url=" + e, function(i) {
                    var n = JSON.parse(i);
                    if ("medium app" == n) r("#rectangle", t).remove(), t.remove(), r("#bingewith-body").remove(), window.parent.postMessage(JSON.stringify({ src: window.location.toString(), context: "iframe.resize", height: 1, width: 1 }), "*");
                    else if ("no result" == n) { r("#player-container", t).hide(), T(a, t), r("#generate-audio", t).show(), r("#generate-area", t)[0].addEventListener("click", function() { r("#generate-text", t).hide(), r("#generating-text", t).show(), x(t), f(e, t) }), r("#rectangle", t).show() } else "signup" == n ? (r("#player-container", t).hide(), T("https://bingewith.com", t), r("#signup", t).show(), r("#rectangle", t).show()) : (h(n, a, t), r("#rectangle", t).show())
                })
            }
            async function A(e) {
                if (!e.hasClass("micro") || e[0].dataset.href) {
                    var t, a = g(e);
                    if (e.css("color", "white"), r(".bingewith-iframe").show(), e.show(), a.includes("/article/")) {
                        var i = a.split("/article/")[1];
                        if (i.includes("&testing=bingewith") && (i = i.split("&testing=bingewith")[0]), i.includes("?") && (i = i.split("?")[0]), i.includes("::_wp")) {
                            var n = i.split("&permalink=")[1];
                            r.get(c + "/mp3_ready?url=" + n, function(t) { var a = JSON.parse(t); "medium app" == a ? (r("#rectangle", e).remove(), e.remove(), r("#bingewith-body").remove()) : "no result" == a ? (r("#player-container", e).hide(), T(n, e), r("#generate-audio", e).show(), r("#rectangle", e).show()) : "signup" == a ? (r("#player-container", e).hide(), T("https://bingewith.com", e), r("#signup", e).show(), r("#rectangle", e).show()) : (h(a, n, e), r("#rectangle", e).show()), r("#generate-area", e)[0].addEventListener("click", function() { r("#generate-text", e).hide(), r("#generating-text", e).show(), x(e), f(n, e) }) })
                        } else if (i.includes("::_Generate_Audio")) N(a, e);
                        else {
                            const n = await (t = i + storage_suffix, new Promise(function(e, a) {
                                r.get("/static/app/js/test.mp3", function(t) {
                                    var a = JSON.parse(t);
                                    e(a)
                                })
                            }));
                            h(n, a, e), r("#rectangle", e).show()
                        }
                    } else N(a, e)
                }
            }
            for (let e = 0; e < bingewith_players.length; e++) A(r(bingewith_players[e]))
        })
    }
}();