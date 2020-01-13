! function (e) {
    function t(r) {
        if (n[r]) return n[r].exports;
        var i = n[r] = {
            "i": r,
            "l": !1,
            "exports": {}
        };
        return e[r].call(i.exports, i, i.exports, t), i.l = !0, i.exports
    }
    var n = {};
    t.m = e, t.c = n, t.d = function (e, n, r) {
        t.o(e, n) || Object.defineProperty(e, n, {
            "configurable": !1,
            "enumerable": !0,
            "get": r
        })
    }, t.n = function (e) {
        var n = e && e.__esModule ? function () {
            return e["default"]
        } : function () {
            return e
        };
        return t.d(n, "a", n), n
    }, t.o = function (e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }, t.p = "", t(t.s = 0)
}({
    "./node_modules/jquery/dist/jquery.js": function (e, t, n) {
        var r, i;
        /*!
         * jQuery JavaScript Library v1.12.4
         * http://jquery.com/
         *
         * Includes Sizzle.js
         * http://sizzlejs.com/
         *
         * Copyright jQuery Foundation and other contributors
         * Released under the MIT license
         * http://jquery.org/license
         *
         * Date: 2016-05-20T17:17Z
         */
        ! function (t, n) {
            "object" == typeof e && "object" == typeof e.exports ? e.exports = t.document ? n(t, !0) : function (e) {
                if (!e.document) throw new Error("jQuery requires a window with a document");
                return n(e)
            } : n(t)
        }("undefined" != typeof window ? window : this, function (n, o) {
            function a(e) {
                var t = !!e && "length" in e && e.length,
                    n = ve.type(e);
                return "function" !== n && !ve.isWindow(e) && ("array" === n || 0 === t || "number" == typeof t && t > 0 && t - 1 in e)
            }

            function s(e, t, n) {
                if (ve.isFunction(t)) return ve.grep(e, function (e, r) {
                    return !!t.call(e, r, e) !== n
                });
                if (t.nodeType) return ve.grep(e, function (e) {
                    return e === t !== n
                });
                if ("string" == typeof t) {
                    if (_e.test(t)) return ve.filter(t, e, n);
                    t = ve.filter(t, e)
                }
                return ve.grep(e, function (e) {
                    return ve.inArray(e, t) > -1 !== n
                })
            }

            function l(e, t) {
                do {
                    e = e[t]
                } while (e && 1 !== e.nodeType);
                return e
            }

            function u(e) {
                var t = {};
                return ve.each(e.match(De) || [], function (e, n) {
                    t[n] = !0
                }), t
            }

            function c() {
                se.addEventListener ? (se.removeEventListener("DOMContentLoaded", d), n.removeEventListener("load", d)) : (se.detachEvent("onreadystatechange", d), n.detachEvent("onload", d))
            }

            function d() {
                (se.addEventListener || "load" === n.event.type || "complete" === se.readyState) && (c(), ve.ready())
            }

            function f(e, t, n) {
                if (void 0 === n && 1 === e.nodeType) {
                    var r = "data-" + t.replace(Oe, "-$1").toLowerCase();
                    if ("string" == typeof (n = e.getAttribute(r))) {
                        try {
                            n = "true" === n || "false" !== n && ("null" === n ? null : +n + "" === n ? +n : He.test(n) ? ve.parseJSON(n) : n)
                        } catch (i) {}
                        ve.data(e, t, n)
                    } else n = void 0
                }
                return n
            }

            function p(e) {
                var t;
                for (t in e)
                    if (("data" !== t || !ve.isEmptyObject(e[t])) && "toJSON" !== t) return !1;
                return !0
            }

            function h(e, t, n, r) {
                if (qe(e)) {
                    var i, o, a = ve.expando,
                        s = e.nodeType,
                        l = s ? ve.cache : e,
                        u = s ? e[a] : e[a] && a;
                    if (u && l[u] && (r || l[u].data) || void 0 !== n || "string" != typeof t) return u || (u = s ? e[a] = ae.pop() || ve.guid++ : a), l[u] || (l[u] = s ? {} : {
                        "toJSON": ve.noop
                    }), "object" != typeof t && "function" != typeof t || (r ? l[u] = ve.extend(l[u], t) : l[u].data = ve.extend(l[u].data, t)), o = l[u], r || (o.data || (o.data = {}), o = o.data), void 0 !== n && (o[ve.camelCase(t)] = n), "string" == typeof t ? null == (i = o[t]) && (i = o[ve.camelCase(t)]) : i = o, i
                }
            }

            function g(e, t, n) {
                if (qe(e)) {
                    var r, i, o = e.nodeType,
                        a = o ? ve.cache : e,
                        s = o ? e[ve.expando] : ve.expando;
                    if (a[s]) {
                        if (t && (r = n ? a[s] : a[s].data)) {
                            ve.isArray(t) ? t = t.concat(ve.map(t, ve.camelCase)) : t in r ? t = [t] : (t = ve.camelCase(t), t = t in r ? [t] : t.split(" ")), i = t.length;
                            for (; i--;) delete r[t[i]];
                            if (n ? !p(r) : !ve.isEmptyObject(r)) return
                        }(n || (delete a[s].data, p(a[s]))) && (o ? ve.cleanData([e], !0) : ge.deleteExpando || a != a.window ? delete a[s] : a[s] = void 0)
                    }
                }
            }

            function v(e, t, n, r) {
                var i, o = 1,
                    a = 20,
                    s = r ? function () {
                        return r.cur()
                    } : function () {
                        return ve.css(e, t, "")
                    },
                    l = s(),
                    u = n && n[3] || (ve.cssNumber[t] ? "" : "px"),
                    c = (ve.cssNumber[t] || "px" !== u && +l) && Pe.exec(ve.css(e, t));
                if (c && c[3] !== u) {
                    u = u || c[3], n = n || [], c = +l || 1;
                    do {
                        o = o || ".5", c /= o, ve.style(e, t, c + u)
                    } while (o !== (o = s() / l) && 1 !== o && --a)
                }
                return n && (c = +c || +l || 0, i = n[1] ? c + (n[1] + 1) * n[2] : +n[2], r && (r.unit = u, r.start = c, r.end = i)), i
            }

            function m(e) {
                var t = Ue.split("|"),
                    n = e.createDocumentFragment();
                if (n.createElement)
                    for (; t.length;) n.createElement(t.pop());
                return n
            }

            function y(e, t) {
                var n, r, i = 0,
                    o = void 0 !== e.getElementsByTagName ? e.getElementsByTagName(t || "*") : void 0 !== e.querySelectorAll ? e.querySelectorAll(t || "*") : void 0;
                if (!o)
                    for (o = [], n = e.childNodes || e; null != (r = n[i]); i++)!t || ve.nodeName(r, t) ? o.push(r) : ve.merge(o, y(r, t));
                return void 0 === t || t && ve.nodeName(e, t) ? ve.merge([e], o) : o
            }

            function b(e, t) {
                for (var n, r = 0; null != (n = e[r]); r++) ve._data(n, "globalEval", !t || ve._data(t[r], "globalEval"))
            }

            function x(e) {
                We.test(e.type) && (e.defaultChecked = e.checked)
            }

            function w(e, t, n, r, i) {
                for (var o, a, s, l, u, c, d, f = e.length, p = m(t), h = [], g = 0; g < f; g++)
                    if ((a = e[g]) || 0 === a)
                        if ("object" === ve.type(a)) ve.merge(h, a.nodeType ? [a] : a);
                        else if (Ge.test(a)) {
                    for (l = l || p.appendChild(t.createElement("div")), u = (Be.exec(a) || ["", ""])[1].toLowerCase(), d = Ve[u] || Ve._default, l.innerHTML = d[1] + ve.htmlPrefilter(a) + d[2], o = d[0]; o--;) l = l.lastChild;
                    if (!ge.leadingWhitespace && Xe.test(a) && h.push(t.createTextNode(Xe.exec(a)[0])), !ge.tbody)
                        for (a = "table" !== u || Ye.test(a) ? "<table>" !== d[1] || Ye.test(a) ? 0 : l : l.firstChild, o = a && a.childNodes.length; o--;) ve.nodeName(c = a.childNodes[o], "tbody") && !c.childNodes.length && a.removeChild(c);
                    for (ve.merge(h, l.childNodes), l.textContent = ""; l.firstChild;) l.removeChild(l.firstChild);
                    l = p.lastChild
                } else h.push(t.createTextNode(a));
                for (l && p.removeChild(l), ge.appendChecked || ve.grep(y(h, "input"), x), g = 0; a = h[g++];)
                    if (r && ve.inArray(a, r) > -1) i && i.push(a);
                    else if (s = ve.contains(a.ownerDocument, a), l = y(p.appendChild(a), "script"), s && b(l), n)
                    for (o = 0; a = l[o++];) ze.test(a.type || "") && n.push(a);
                return l = null, p
            }

            function T() {
                return !0
            }

            function C() {
                return !1
            }

            function k() {
                try {
                    return se.activeElement
                } catch (e) {}
            }

            function E(e, t, n, r, i, o) {
                var a, s;
                if ("object" == typeof t) {
                    "string" != typeof n && (r = r || n, n = void 0);
                    for (s in t) E(e, s, n, r, t[s], o);
                    return e
                }
                if (null == r && null == i ? (i = n, r = n = void 0) : null == i && ("string" == typeof n ? (i = r, r = void 0) : (i = r, r = n, n = void 0)), !1 === i) i = C;
                else if (!i) return e;
                return 1 === o && (a = i, i = function (e) {
                    return ve().off(e), a.apply(this, arguments)
                }, i.guid = a.guid || (a.guid = ve.guid++)), e.each(function () {
                    ve.event.add(this, t, i, r, n)
                })
            }

            function _(e, t) {
                return ve.nodeName(e, "table") && ve.nodeName(11 !== t.nodeType ? t : t.firstChild, "tr") ? e.getElementsByTagName("tbody")[0] || e.appendChild(e.ownerDocument.createElement("tbody")) : e
            }

            function N(e) {
                return e.type = (null !== ve.find.attr(e, "type")) + "/" + e.type, e
            }

            function S(e) {
                var t = at.exec(e.type);
                return t ? e.type = t[1] : e.removeAttribute("type"), e
            }

            function j(e, t) {
                if (1 === t.nodeType && ve.hasData(e)) {
                    var n, r, i, o = ve._data(e),
                        a = ve._data(t, o),
                        s = o.events;
                    if (s) {
                        delete a.handle, a.events = {};
                        for (n in s)
                            for (r = 0, i = s[n].length; r < i; r++) ve.event.add(t, n, s[n][r])
                    }
                    a.data && (a.data = ve.extend({}, a.data))
                }
            }

            function A(e, t) {
                var n, r, i;
                if (1 === t.nodeType) {
                    if (n = t.nodeName.toLowerCase(), !ge.noCloneEvent && t[ve.expando]) {
                        i = ve._data(t);
                        for (r in i.events) ve.removeEvent(t, r, i.handle);
                        t.removeAttribute(ve.expando)
                    }
                    "script" === n && t.text !== e.text ? (N(t).text = e.text, S(t)) : "object" === n ? (t.parentNode && (t.outerHTML = e.outerHTML), ge.html5Clone && e.innerHTML && !ve.trim(t.innerHTML) && (t.innerHTML = e.innerHTML)) : "input" === n && We.test(e.type) ? (t.defaultChecked = t.checked = e.checked, t.value !== e.value && (t.value = e.value)) : "option" === n ? t.defaultSelected = t.selected = e.defaultSelected : "input" !== n && "textarea" !== n || (t.defaultValue = e.defaultValue)
                }
            }

            function D(e, t, n, r) {
                t = ue.apply([], t);
                var i, o, a, s, l, u, c = 0,
                    d = e.length,
                    f = d - 1,
                    p = t[0],
                    h = ve.isFunction(p);
                if (h || d > 1 && "string" == typeof p && !ge.checkClone && ot.test(p)) return e.each(function (i) {
                    var o = e.eq(i);
                    h && (t[0] = p.call(this, i, o.html())), D(o, t, n, r)
                });
                if (d && (u = w(t, e[0].ownerDocument, !1, e, r), i = u.firstChild, 1 === u.childNodes.length && (u = i), i || r)) {
                    for (s = ve.map(y(u, "script"), N), a = s.length; c < d; c++) o = u, c !== f && (o = ve.clone(o, !0, !0), a && ve.merge(s, y(o, "script"))), n.call(e[c], o, c);
                    if (a)
                        for (l = s[s.length - 1].ownerDocument, ve.map(s, S), c = 0; c < a; c++) o = s[c], ze.test(o.type || "") && !ve._data(o, "globalEval") && ve.contains(l, o) && (o.src ? ve._evalUrl && ve._evalUrl(o.src) : ve.globalEval((o.text || o.textContent || o.innerHTML || "").replace(st, "")));
                    u = i = null
                }
                return e
            }

            function L(e, t, n) {
                for (var r, i = t ? ve.filter(t, e) : e, o = 0; null != (r = i[o]); o++) n || 1 !== r.nodeType || ve.cleanData(y(r)), r.parentNode && (n && ve.contains(r.ownerDocument, r) && b(y(r, "script")), r.parentNode.removeChild(r));
                return e
            }

            function $(e, t) {
                var n = ve(t.createElement(e)).appendTo(t.body),
                    r = ve.css(n[0], "display");
                return n.detach(), r
            }

            function q(e) {
                var t = se,
                    n = dt[e];
                return n || (n = $(e, t), "none" !== n && n || (ct = (ct || ve("<iframe frameborder='0' width='0' height='0'/>")).appendTo(t.documentElement), t = (ct[0].contentWindow || ct[0].contentDocument).document, t.write(), t.close(), n = $(e, t), ct.detach()), dt[e] = n), n
            }

            function H(e, t) {
                return {
                    "get": function () {
                        return e() ? void delete this.get : (this.get = t).apply(this, arguments)
                    }
                }
            }

            function O(e) {
                if (e in _t) return e;
                for (var t = e.charAt(0).toUpperCase() + e.slice(1), n = Et.length; n--;)
                    if ((e = Et[n] + t) in _t) return e
            }

            function M(e, t) {
                for (var n, r, i, o = [], a = 0, s = e.length; a < s; a++) r = e[a], r.style && (o[a] = ve._data(r, "olddisplay"), n = r.style.display, t ? (o[a] || "none" !== n || (r.style.display = ""), "" === r.style.display && Re(r) && (o[a] = ve._data(r, "olddisplay", q(r.nodeName)))) : (i = Re(r), (n && "none" !== n || !i) && ve._data(r, "olddisplay", i ? n : ve.css(r, "display"))));
                for (a = 0; a < s; a++) r = e[a], r.style && (t && "none" !== r.style.display && "" !== r.style.display || (r.style.display = t ? o[a] || "" : "none"));
                return e
            }

            function P(e, t, n) {
                var r = Tt.exec(t);
                return r ? Math.max(0, r[1] - (n || 0)) + (r[2] || "px") : t
            }

            function F(e, t, n, r, i) {
                for (var o = n === (r ? "border" : "content") ? 4 : "width" === t ? 1 : 0, a = 0; o < 4; o += 2) "margin" === n && (a += ve.css(e, n + Fe[o], !0, i)), r ? ("content" === n && (a -= ve.css(e, "padding" + Fe[o], !0, i)), "margin" !== n && (a -= ve.css(e, "border" + Fe[o] + "Width", !0, i))) : (a += ve.css(e, "padding" + Fe[o], !0, i), "padding" !== n && (a += ve.css(e, "border" + Fe[o] + "Width", !0, i)));
                return a
            }

            function R(e, t, n) {
                var r = !0,
                    i = "width" === t ? e.offsetWidth : e.offsetHeight,
                    o = vt(e),
                    a = ge.boxSizing && "border-box" === ve.css(e, "boxSizing", !1, o);
                if (i <= 0 || null == i) {
                    if (i = mt(e, t, o), (i < 0 || null == i) && (i = e.style[t]), pt.test(i)) return i;
                    r = a && (ge.boxSizingReliable() || i === e.style[t]), i = parseFloat(i) || 0
                }
                return i + F(e, t, n || (a ? "border" : "content"), r, o) + "px"
            }

            function I(e, t, n, r, i) {
                return new I.prototype.init(e, t, n, r, i)
            }

            function W() {
                return n.setTimeout(function () {
                    Nt = void 0
                }), Nt = ve.now()
            }

            function B(e, t) {
                var n, r = {
                        "height": e
                    },
                    i = 0;
                for (t = t ? 1 : 0; i < 4; i += 2 - t) n = Fe[i], r["margin" + n] = r["padding" + n] = e;
                return t && (r.opacity = r.width = e), r
            }

            function z(e, t, n) {
                for (var r, i = (V.tweeners[t] || []).concat(V.tweeners["*"]), o = 0, a = i.length; o < a; o++)
                    if (r = i[o].call(n, t, e)) return r
            }

            function X(e, t, n) {
                var r, i, o, a, s, l, u, c = this,
                    d = {},
                    f = e.style,
                    p = e.nodeType && Re(e),
                    h = ve._data(e, "fxshow");
                n.queue || (s = ve._queueHooks(e, "fx"), null == s.unqueued && (s.unqueued = 0, l = s.empty.fire, s.empty.fire = function () {
                    s.unqueued || l()
                }), s.unqueued++, c.always(function () {
                    c.always(function () {
                        s.unqueued--, ve.queue(e, "fx").length || s.empty.fire()
                    })
                })), 1 === e.nodeType && ("height" in t || "width" in t) && (n.overflow = [f.overflow, f.overflowX, f.overflowY], u = ve.css(e, "display"), "inline" === ("none" === u ? ve._data(e, "olddisplay") || q(e.nodeName) : u) && "none" === ve.css(e, "float") && (ge.inlineBlockNeedsLayout && "inline" !== q(e.nodeName) ? f.zoom = 1 : f.display = "inline-block")), n.overflow && (f.overflow = "hidden", ge.shrinkWrapBlocks() || c.always(function () {
                    f.overflow = n.overflow[0], f.overflowX = n.overflow[1], f.overflowY = n.overflow[2]
                }));
                for (r in t)
                    if (i = t[r], jt.exec(i)) {
                        if (delete t[r], o = o || "toggle" === i, i === (p ? "hide" : "show")) {
                            if ("show" !== i || !h || void 0 === h[r]) continue;
                            p = !0
                        }
                        d[r] = h && h[r] || ve.style(e, r)
                    } else u = void 0;
                if (ve.isEmptyObject(d)) "inline" === ("none" === u ? q(e.nodeName) : u) && (f.display = u);
                else {
                    h ? "hidden" in h && (p = h.hidden) : h = ve._data(e, "fxshow", {}), o && (h.hidden = !p), p ? ve(e).show() : c.done(function () {
                        ve(e).hide()
                    }), c.done(function () {
                        var t;
                        ve._removeData(e, "fxshow");
                        for (t in d) ve.style(e, t, d[t])
                    });
                    for (r in d) a = z(p ? h[r] : 0, r, c), r in h || (h[r] = a.start, p && (a.end = a.start, a.start = "width" === r || "height" === r ? 1 : 0))
                }
            }

            function U(e, t) {
                var n, r, i, o, a;
                for (n in e)
                    if (r = ve.camelCase(n), i = t[r], o = e[n], ve.isArray(o) && (i = o[1], o = e[n] = o[0]), n !== r && (e[r] = o, delete e[n]), (a = ve.cssHooks[r]) && "expand" in a) {
                        o = a.expand(o), delete e[r];
                        for (n in o) n in e || (e[n] = o[n], t[n] = i)
                    } else t[r] = i
            }

            function V(e, t, n) {
                var r, i, o = 0,
                    a = V.prefilters.length,
                    s = ve.Deferred().always(function () {
                        delete l.elem
                    }),
                    l = function () {
                        if (i) return !1;
                        for (var t = Nt || W(), n = Math.max(0, u.startTime + u.duration - t), r = n / u.duration || 0, o = 1 - r, a = 0, l = u.tweens.length; a < l; a++) u.tweens[a].run(o);
                        return s.notifyWith(e, [u, o, n]), o < 1 && l ? n : (s.resolveWith(e, [u]), !1)
                    },
                    u = s.promise({
                        "elem": e,
                        "props": ve.extend({}, t),
                        "opts": ve.extend(!0, {
                            "specialEasing": {},
                            "easing": ve.easing._default
                        }, n),
                        "originalProperties": t,
                        "originalOptions": n,
                        "startTime": Nt || W(),
                        "duration": n.duration,
                        "tweens": [],
                        "createTween": function (t, n) {
                            var r = ve.Tween(e, u.opts, t, n, u.opts.specialEasing[t] || u.opts.easing);
                            return u.tweens.push(r), r
                        }, "stop": function (t) {
                            var n = 0,
                                r = t ? u.tweens.length : 0;
                            if (i) return this;
                            for (i = !0; n < r; n++) u.tweens[n].run(1);
                            return t ? (s.notifyWith(e, [u, 1, 0]), s.resolveWith(e, [u, t])) : s.rejectWith(e, [u, t]), this
                        }
                    }),
                    c = u.props;
                for (U(c, u.opts.specialEasing); o < a; o++)
                    if (r = V.prefilters[o].call(u, e, c, u.opts)) return ve.isFunction(r.stop) && (ve._queueHooks(u.elem, u.opts.queue).stop = ve.proxy(r.stop, r)), r;
                return ve.map(c, z, u), ve.isFunction(u.opts.start) && u.opts.start.call(e, u), ve.fx.timer(ve.extend(l, {
                    "elem": e,
                    "anim": u,
                    "queue": u.opts.queue
                })), u.progress(u.opts.progress).done(u.opts.done, u.opts.complete).fail(u.opts.fail).always(u.opts.always)
            }

            function G(e) {
                return ve.attr(e, "class") || ""
            }

            function Y(e) {
                return function (t, n) {
                    "string" != typeof t && (n = t, t = "*");
                    var r, i = 0,
                        o = t.toLowerCase().match(De) || [];
                    if (ve.isFunction(n))
                        for (; r = o[i++];) "+" === r.charAt(0) ? (r = r.slice(1) || "*", (e[r] = e[r] || []).unshift(n)) : (e[r] = e[r] || []).push(n)
                }
            }

            function J(e, t, n, r) {
                function i(s) {
                    var l;
                    return o[s] = !0, ve.each(e[s] || [], function (e, s) {
                        var u = s(t, n, r);
                        return "string" != typeof u || a || o[u] ? a ? !(l = u) : void 0 : (t.dataTypes.unshift(u), i(u), !1)
                    }), l
                }
                var o = {},
                    a = e === en;
                return i(t.dataTypes[0]) || !o["*"] && i("*")
            }

            function K(e, t) {
                var n, r, i = ve.ajaxSettings.flatOptions || {};
                for (r in t) void 0 !== t[r] && ((i[r] ? e : n || (n = {}))[r] = t[r]);
                return n && ve.extend(!0, e, n), e
            }

            function Q(e, t, n) {
                for (var r, i, o, a, s = e.contents, l = e.dataTypes;
                    "*" === l[0];) l.shift(), void 0 === i && (i = e.mimeType || t.getResponseHeader("Content-Type"));
                if (i)
                    for (a in s)
                        if (s[a] && s[a].xpathTest(i)) {
                            l.unshift(a);
                            break
                        }
                if (l[0] in n) o = l[0];
                else {
                    for (a in n) {
                        if (!l[0] || e.converters[a + " " + l[0]]) {
                            o = a;
                            break
                        }
                        r || (r = a)
                    }
                    o = o || r
                } if (o) return o !== l[0] && l.unshift(o), n[o]
            }

            function Z(e, t, n, r) {
                var i, o, a, s, l, u = {},
                    c = e.dataTypes.slice();
                if (c[1])
                    for (a in e.converters) u[a.toLowerCase()] = e.converters[a];
                for (o = c.shift(); o;)
                    if (e.responseFields[o] && (n[e.responseFields[o]] = t), !l && r && e.dataFilter && (t = e.dataFilter(t, e.dataType)), l = o, o = c.shift())
                        if ("*" === o) o = l;
                        else if ("*" !== l && l !== o) {
                    if (!(a = u[l + " " + o] || u["* " + o]))
                        for (i in u)
                            if (s = i.split(" "), s[1] === o && (a = u[l + " " + s[0]] || u["* " + s[0]])) {
                                !0 === a ? a = u[i] : !0 !== u[i] && (o = s[0], c.unshift(s[1]));
                                break
                            }
                    if (!0 !== a)
                        if (a && e["throws"]) t = a(t);
                        else try {
                            t = a(t)
                        } catch (d) {
                            return {
                                "state": "parsererror",
                                "error": a ? d : "No conversion from " + l + " to " + o
                            }
                        }
                }
                return {
                    "state": "success",
                    "data": t
                }
            }

            function ee(e) {
                return e.style && e.style.display || ve.css(e, "display")
            }

            function te(e) {
                if (!ve.contains(e.ownerDocument || se, e)) return !0;
                for (; e && 1 === e.nodeType;) {
                    if ("none" === ee(e) || "hidden" === e.type) return !0;
                    e = e.parentNode
                }
                return !1
            }

            function ne(e, t, n, r) {
                var i;
                if (ve.isArray(t)) ve.each(t, function (t, i) {
                    n || an.test(e) ? r(e, i) : ne(e + "[" + ("object" == typeof i && null != i ? t : "") + "]", i, n, r)
                });
                else if (n || "object" !== ve.type(t)) r(e, t);
                else
                    for (i in t) ne(e + "[" + i + "]", t[i], n, r)
            }

            function re() {
                try {
                    return new n.XMLHttpRequest
                } catch (e) {}
            }

            function ie() {
                try {
                    return new n.ActiveXObject("Microsoft.XMLHTTP")
                } catch (e) {}
            }

            function oe(e) {
                return ve.isWindow(e) ? e : 9 === e.nodeType && (e.defaultView || e.parentWindow)
            }
            var ae = [],
                se = n.document,
                le = ae.slice,
                ue = ae.concat,
                ce = ae.push,
                de = ae.indexOf,
                fe = {},
                pe = fe.toString,
                he = fe.hasOwnProperty,
                ge = {},
                ve = function (e, t) {
                    return new ve.fn.init(e, t)
                },
                me = /^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,
                ye = /^-ms-/,
                be = /-([\da-z])/gi,
                xe = function (e, t) {
                    return t.toUpperCase()
                };
            ve.fn = ve.prototype = {
                "jquery": "1_冬季电动车儿童护膝保暖骑车加厚摩托车挡风被防水布男女小孩护腿.html.12.4",
                "constructor": ve,
                "selector": "",
                "length": 0,
                "toArray": function () {
                    return le.call(this)
                }, "get": function (e) {
                    return null != e ? e < 0 ? this[e + this.length] : this[e] : le.call(this)
                }, "pushStack": function (e) {
                    var t = ve.merge(this.constructor(), e);
                    return t.prevObject = this, t.context = this.context, t
                }, "each": function (e) {
                    return ve.each(this, e)
                }, "map": function (e) {
                    return this.pushStack(ve.map(this, function (t, n) {
                        return e.call(t, n, t)
                    }))
                }, "slice": function () {
                    return this.pushStack(le.apply(this, arguments))
                }, "first": function () {
                    return this.eq(0)
                }, "last": function () {
                    return this.eq(-1)
                }, "eq": function (e) {
                    var t = this.length,
                        n = +e + (e < 0 ? t : 0);
                    return this.pushStack(n >= 0 && n < t ? [this[n]] : [])
                }, "end": function () {
                    return this.prevObject || this.constructor()
                }, "push": ce,
                "sort": ae.sort,
                "splice": ae.splice
            }, ve.extend = ve.fn.extend = function () {
                var e, t, n, r, i, o, a = arguments[0] || {},
                    s = 1,
                    l = arguments.length,
                    u = !1;
                for ("boolean" == typeof a && (u = a, a = arguments[s] || {}, s++), "object" == typeof a || ve.isFunction(a) || (a = {}), s === l && (a = this, s--); s < l; s++)
                    if (null != (i = arguments[s]))
                        for (r in i) e = a[r], n = i[r], a !== n && (u && n && (ve.isPlainObject(n) || (t = ve.isArray(n))) ? (t ? (t = !1, o = e && ve.isArray(e) ? e : []) : o = e && ve.isPlainObject(e) ? e : {}, a[r] = ve.extend(u, o, n)) : void 0 !== n && (a[r] = n));
                return a
            }, ve.extend({
                "expando": "jQuery" + ("1_冬季电动车儿童护膝保暖骑车加厚摩托车挡风被防水布男女小孩护腿.html.12.4" + Math.random()).replace(/\D/g, ""),
                "isReady": !0,
                "error": function (e) {
                    throw new Error(e)
                }, "noop": function () {}, "isFunction": function (e) {
                    return "function" === ve.type(e)
                }, "isArray": Array.isArray || function (e) {
                    return "array" === ve.type(e)
                }, "isWindow": function (e) {
                    return null != e && e == e.window
                }, "isNumeric": function (e) {
                    var t = e && e.toString();
                    return !ve.isArray(e) && t - parseFloat(t) + 1 >= 0
                }, "isEmptyObject": function (e) {
                    var t;
                    for (t in e) return !1;
                    return !0
                }, "isPlainObject": function (e) {
                    var t;
                    if (!e || "object" !== ve.type(e) || e.nodeType || ve.isWindow(e)) return !1;
                    try {
                        if (e.constructor && !he.call(e, "constructor") && !he.call(e.constructor.prototype, "isPrototypeOf")) return !1
                    } catch (n) {
                        return !1
                    }
                    if (!ge.ownFirst)
                        for (t in e) return he.call(e, t);
                    for (t in e);
                    return void 0 === t || he.call(e, t)
                }, "type": function (e) {
                    return null == e ? e + "" : "object" == typeof e || "function" == typeof e ? fe[pe.call(e)] || "object" : typeof e
                }, "globalEval": function (e) {
                    e && ve.trim(e) && (n.execScript || function (e) {
                        n["eval"].call(n, e)
                    })(e)
                }, "camelCase": function (e) {
                    return e.replace(ye, "ms-").replace(be, xe)
                }, "nodeName": function (e, t) {
                    return e.nodeName && e.nodeName.toLowerCase() === t.toLowerCase()
                }, "each": function (e, t) {
                    var n, r = 0;
                    if (a(e))
                        for (n = e.length; r < n && !1 !== t.call(e[r], r, e[r]); r++);
                    else
                        for (r in e)
                            if (!1 === t.call(e[r], r, e[r])) break; return e
                }, "trim": function (e) {
                    return null == e ? "" : (e + "").replace(me, "")
                }, "makeArray": function (e, t) {
                    var n = t || [];
                    return null != e && (a(Object(e)) ? ve.merge(n, "string" == typeof e ? [e] : e) : ce.call(n, e)), n
                }, "inArray": function (e, t, n) {
                    var r;
                    if (t) {
                        if (de) return de.call(t, e, n);
                        for (r = t.length, n = n ? n < 0 ? Math.max(0, r + n) : n : 0; n < r; n++)
                            if (n in t && t[n] === e) return n
                    }
                    return -1
                }, "merge": function (e, t) {
                    for (var n = +t.length, r = 0, i = e.length; r < n;) e[i++] = t[r++];
                    if (n !== n)
                        for (; void 0 !== t[r];) e[i++] = t[r++];
                    return e.length = i, e
                }, "grep": function (e, t, n) {
                    for (var r = [], i = 0, o = e.length, a = !n; i < o; i++)!t(e[i], i) !== a && r.push(e[i]);
                    return r
                }, "map": function (e, t, n) {
                    var r, i, o = 0,
                        s = [];
                    if (a(e))
                        for (r = e.length; o < r; o++) null != (i = t(e[o], o, n)) && s.push(i);
                    else
                        for (o in e) null != (i = t(e[o], o, n)) && s.push(i);
                    return ue.apply([], s)
                }, "guid": 1,
                "proxy": function (e, t) {
                    var n, r, i;
                    if ("string" == typeof t && (i = e[t], t = e, e = i), ve.isFunction(e)) return n = le.call(arguments, 2), r = function () {
                        return e.apply(t || this, n.concat(le.call(arguments)))
                    }, r.guid = e.guid = e.guid || ve.guid++, r
                }, "now": function () {
                    return +new Date
                }, "support": ge
            }), "function" == typeof Symbol && (ve.fn[Symbol.iterator] = ae[Symbol.iterator]), ve.each("Boolean Number String Function Array Date RegExp Object Error Symbol".split(" "), function (e, t) {
                fe["[object " + t + "]"] = t.toLowerCase()
            });
            var we =
                /*!
                 * Sizzle CSS Selector Engine v2.2.1
                 * http://sizzlejs.com/
                 *
                 * Copyright jQuery Foundation and other contributors
                 * Released under the MIT license
                 * http://jquery.org/license
                 *
                 * Date: 2015-10-17
                 */
                function (e) {
                    function t(e, t, n, r) {
                        var i, o, a, s, u, d, f, p, h = t && t.ownerDocument,
                            g = t ? t.nodeType : 9;
                        if (n = n || [], "string" != typeof e || !e || 1 !== g && 9 !== g && 11 !== g) return n;
                        if (!r && ((t ? t.ownerDocument || t : P) !== A && j(t), t = t || A, L)) {
                            if (11 !== g && (d = ge.exec(e)))
                                if (i = d[1]) {
                                    if (9 === g) {
                                        if (!(a = t.getElementById(i))) return n;
                                        if (a.id === i) return n.push(a), n
                                    } else if (h && (a = h.getElementById(i)) && O(t, a) && a.id === i) return n.push(a), n
                                } else {
                                    if (d[2]) return J.apply(n, t.getElementsByTagName(e)), n;
                                    if ((i = d[3]) && b.getElementsByClassName && t.getElementsByClassName) return J.apply(n, t.getElementsByClassName(i)), n
                                }
                            if (b.qsa && !B[e + " "] && (!$ || !$.xpathTest(e))) {
                                if (1 !== g) h = t, p = e;
                                else if ("object" !== t.nodeName.toLowerCase()) {
                                    for ((s = t.getAttribute("id")) ? s = s.replace(me, "\\$&") : t.setAttribute("id", s = M), f = C(e), o = f.length, u = ce.test(s) ? "#" + s : "[id='" + s + "']"; o--;) f[o] = u + " " + c(f[o]);
                                    p = f.join(","), h = ve.test(e) && l(t.parentNode) || t
                                }
                                if (p) try {
                                    return J.apply(n, h.querySelectorAll(p)), n
                                } catch (v) {} finally {
                                    s === M && t.removeAttribute("id")
                                }
                            }
                        }
                        return E(e.replace(oe, "$1"), t, n, r)
                    }

                    function n() {
                        function e(n, r) {
                            return t.push(n + " ") > x.cacheLength && delete e[t.shift()], e[n + " "] = r
                        }
                        var t = [];
                        return e
                    }

                    function r(e) {
                        return e[M] = !0, e
                    }

                    function i(e) {
                        var t = A.createElement("div");
                        try {
                            return !!e(t)
                        } catch (n) {
                            return !1
                        } finally {
                            t.parentNode && t.parentNode.removeChild(t), t = null
                        }
                    }

                    function o(e, t) {
                        for (var n = e.split("|"), r = n.length; r--;) x.attrHandle[n[r]] = t
                    }

                    function a(e, t) {
                        var n = t && e,
                            r = n && 1 === e.nodeType && 1 === t.nodeType && (~t.sourceIndex || X) - (~e.sourceIndex || X);
                        if (r) return r;
                        if (n)
                            for (; n = n.nextSibling;)
                                if (n === t) return -1;
                        return e ? 1 : -1
                    }

                    function s(e) {
                        return r(function (t) {
                            return t = +t, r(function (n, r) {
                                for (var i, o = e([], n.length, t), a = o.length; a--;) n[i = o[a]] && (n[i] = !(r[i] = n[i]))
                            })
                        })
                    }

                    function l(e) {
                        return e && void 0 !== e.getElementsByTagName && e
                    }

                    function u() {}

                    function c(e) {
                        for (var t = 0, n = e.length, r = ""; t < n; t++) r += e[t].value;
                        return r
                    }

                    function d(e, t, n) {
                        var r = t.dir,
                            i = n && "parentNode" === r,
                            o = R++;
                        return t.first ? function (t, n, o) {
                            for (; t = t[r];)
                                if (1 === t.nodeType || i) return e(t, n, o)
                        } : function (t, n, a) {
                            var s, l, u, c = [F, o];
                            if (a) {
                                for (; t = t[r];)
                                    if ((1 === t.nodeType || i) && e(t, n, a)) return !0
                            } else
                                for (; t = t[r];)
                                    if (1 === t.nodeType || i) {
                                        if (u = t[M] || (t[M] = {}), l = u[t.uniqueID] || (u[t.uniqueID] = {}), (s = l[r]) && s[0] === F && s[1] === o) return c[2] = s[2];
                                        if (l[r] = c, c[2] = e(t, n, a)) return !0
                                    }
                        }
                    }

                    function f(e) {
                        return e.length > 1 ? function (t, n, r) {
                            for (var i = e.length; i--;)
                                if (!e[i](t, n, r)) return !1;
                            return !0
                        } : e[0]
                    }

                    function p(e, n, r) {
                        for (var i = 0, o = n.length; i < o; i++) t(e, n[i], r);
                        return r
                    }

                    function h(e, t, n, r, i) {
                        for (var o, a = [], s = 0, l = e.length, u = null != t; s < l; s++)(o = e[s]) && (n && !n(o, r, i) || (a.push(o), u && t.push(s)));
                        return a
                    }

                    function g(e, t, n, i, o, a) {
                        return i && !i[M] && (i = g(i)), o && !o[M] && (o = g(o, a)), r(function (r, a, s, l) {
                            var u, c, d, f = [],
                                g = [],
                                v = a.length,
                                m = r || p(t || "*", s.nodeType ? [s] : s, []),
                                y = !e || !r && t ? m : h(m, f, e, s, l),
                                b = n ? o || (r ? e : v || i) ? [] : a : y;
                            if (n && n(y, b, s, l), i)
                                for (u = h(b, g), i(u, [], s, l), c = u.length; c--;)(d = u[c]) && (b[g[c]] = !(y[g[c]] = d));
                            if (r) {
                                if (o || e) {
                                    if (o) {
                                        for (u = [], c = b.length; c--;)(d = b[c]) && u.push(y[c] = d);
                                        o(null, b = [], u, l)
                                    }
                                    for (c = b.length; c--;)(d = b[c]) && (u = o ? Q(r, d) : f[c]) > -1 && (r[u] = !(a[u] = d))
                                }
                            } else b = h(b === a ? b.splice(v, b.length) : b), o ? o(null, a, b, l) : J.apply(a, b)
                        })
                    }

                    function v(e) {
                        for (var t, n, r, i = e.length, o = x.relative[e[0].type], a = o || x.relative[" "], s = o ? 1 : 0, l = d(function (e) {
                            return e === t
                        }, a, !0), u = d(function (e) {
                            return Q(t, e) > -1
                        }, a, !0), p = [
                            function (e, n, r) {
                                var i = !o && (r || n !== _) || ((t = n).nodeType ? l(e, n, r) : u(e, n, r));
                                return t = null, i
                            }
                        ]; s < i; s++)
                            if (n = x.relative[e[s].type]) p = [d(f(p), n)];
                            else {
                                if (n = x.filter[e[s].type].apply(null, e[s].matches), n[M]) {
                                    for (r = ++s; r < i && !x.relative[e[r].type]; r++);
                                    return g(s > 1 && f(p), s > 1 && c(e.slice(0, s - 1).concat({
                                        "value": " " === e[s - 2].type ? "*" : ""
                                    })).replace(oe, "$1"), n, s < r && v(e.slice(s, r)), r < i && v(e = e.slice(r)), r < i && c(e))
                                }
                                p.push(n)
                            }
                        return f(p)
                    }

                    function m(e, n) {
                        var i = n.length > 0,
                            o = e.length > 0,
                            a = function (r, a, s, l, u) {
                                var c, d, f, p = 0,
                                    g = "0",
                                    v = r && [],
                                    m = [],
                                    y = _,
                                    b = r || o && x.find["TAG"]("*", u),
                                    w = F += null == y ? 1 : Math.random() || .1,
                                    T = b.length;
                                for (u && (_ = a === A || a || u); g !== T && null != (c = b[g]); g++) {
                                    if (o && c) {
                                        for (d = 0, a || c.ownerDocument === A || (j(c), s = !L); f = e[d++];)
                                            if (f(c, a || A, s)) {
                                                l.push(c);
                                                break
                                            }
                                        u && (F = w)
                                    }
                                    i && ((c = !f && c) && p--, r && v.push(c))
                                }
                                if (p += g, i && g !== p) {
                                    for (d = 0; f = n[d++];) f(v, m, a, s);
                                    if (r) {
                                        if (p > 0)
                                            for (; g--;) v[g] || m[g] || (m[g] = G.call(l));
                                        m = h(m)
                                    }
                                    J.apply(l, m), u && !r && m.length > 0 && p + n.length > 1 && t.uniqueSort(l)
                                }
                                return u && (F = w, _ = y), v
                            };
                        return i ? r(a) : a
                    }
                    var y, b, x, w, T, C, k, E, _, N, S, j, A, D, L, $, q, H, O, M = "sizzle" + 1 * new Date,
                        P = e.document,
                        F = 0,
                        R = 0,
                        I = n(),
                        W = n(),
                        B = n(),
                        z = function (e, t) {
                            return e === t && (S = !0), 0
                        },
                        X = 1 << 31,
                        U = {}.hasOwnProperty,
                        V = [],
                        G = V.pop,
                        Y = V.push,
                        J = V.push,
                        K = V.slice,
                        Q = function (e, t) {
                            for (var n = 0, r = e.length; n < r; n++)
                                if (e[n] === t) return n;
                            return -1
                        },
                        Z = "checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped",
                        ee = "[\\x20\\t\\r\\n\\f]",
                        te = "(?:\\\\.|[\\w-]|[^\\x00-\\xa0])+",
                        ne = "\\[" + ee + "*(" + te + ")(?:" + ee + "*([*^$|!~]?=)" + ee + "*(?:'((?:\\\\.|[^\\\\'])*)'|\"((?:\\\\.|[^\\\\\"])*)\"|(" + te + "))|)" + ee + "*\\]",
                        re = ":(" + te + ")(?:\\((('((?:\\\\.|[^\\\\'])*)'|\"((?:\\\\.|[^\\\\\"])*)\")|((?:\\\\.|[^\\\\()[\\]]|" + ne + ")*)|.*)\\)|)",
                        ie = new RegExp(ee + "+", "g"),
                        oe = new RegExp("^" + ee + "+|((?:^|[^\\\\])(?:\\\\.)*)" + ee + "+$", "g"),
                        ae = new RegExp("^" + ee + "*," + ee + "*"),
                        se = new RegExp("^" + ee + "*([>+~]|" + ee + ")" + ee + "*"),
                        le = new RegExp("=" + ee + "*([^\\]'\"]*?)" + ee + "*\\]", "g"),
                        ue = new RegExp(re),
                        ce = new RegExp("^" + te + "$"),
                        de = {
                            "ID": new RegExp("^#(" + te + ")"),
                            "CLASS": new RegExp("^\\.(" + te + ")"),
                            "TAG": new RegExp("^(" + te + "|[*])"),
                            "ATTR": new RegExp("^" + ne),
                            "PSEUDO": new RegExp("^" + re),
                            "CHILD": new RegExp("^:(only|first|last|nth|nth-last)-(child|of-type)(?:\\(" + ee + "*(even|odd|(([+-]|)(\\d*)n|)" + ee + "*(?:([+-]|)" + ee + "*(\\d+)|))" + ee + "*\\)|)", "i"),
                            "bool": new RegExp("^(?:" + Z + ")$", "i"),
                            "needsContext": new RegExp("^" + ee + "*[>+~]|:(even|odd|eq|gt|lt|nth|first|last)(?:\\(" + ee + "*((?:-\\d)?\\d*)" + ee + "*\\)|)(?=[^-]|$)", "i")
                        },
                        fe = /^(?:input|select|textarea|button)$/i,
                        pe = /^h\d$/i,
                        he = /^[^{]+\{\s*\[native \w/,
                        ge = /^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/,
                        ve = /[+~]/,
                        me = /'|\\/g,
                        ye = new RegExp("\\\\([\\da-f]{1,6}" + ee + "?|(" + ee + ")|.)", "ig"),
                        be = function (e, t, n) {
                            var r = "0x" + t - 65536;
                            return r !== r || n ? t : r < 0 ? String.fromCharCode(r + 65536) : String.fromCharCode(r >> 10 | 55296, 1023 & r | 56320)
                        },
                        xe = function () {
                            j()
                        };
                    try {
                        J.apply(V = K.call(P.childNodes), P.childNodes), V[P.childNodes.length].nodeType
                    } catch (we) {
                        J = {
                            "apply": V.length ? function (e, t) {
                                Y.apply(e, K.call(t))
                            } : function (e, t) {
                                for (var n = e.length, r = 0; e[n++] = t[r++];);
                                e.length = n - 1
                            }
                        }
                    }
                    b = t.support = {}, T = t.isXML = function (e) {
                        var t = e && (e.ownerDocument || e).documentElement;
                        return !!t && "HTML" !== t.nodeName
                    }, j = t.setDocument = function (e) {
                        var t, n, r = e ? e.ownerDocument || e : P;
                        return r !== A && 9 === r.nodeType && r.documentElement ? (A = r, D = A.documentElement, L = !T(A), (n = A.defaultView) && n.top !== n && (n.addEventListener ? n.addEventListener("unload", xe, !1) : n.attachEvent && n.attachEvent("onunload", xe)), b.attributes = i(function (e) {
                            return e.className = "i", !e.getAttribute("className")
                        }), b.getElementsByTagName = i(function (e) {
                            return e.appendChild(A.createComment("")), !e.getElementsByTagName("*").length
                        }), b.getElementsByClassName = he.test(A.getElementsByClassName), b.getById = i(function (e) {
                            return D.appendChild(e).id = M, !A.getElementsByName || !A.getElementsByName(M).length
                        }), b.getById ? (x.find["ID"] = function (e, t) {
                            if (void 0 !== t.getElementById && L) {
                                var n = t.getElementById(e);
                                return n ? [n] : []
                            }
                        }, x.filter["ID"] = function (e) {
                            var t = e.replace(ye, be);
                            return function (e) {
                                return e.getAttribute("id") === t
                            }
                        }) : (delete x.find["ID"], x.filter["ID"] = function (e) {
                            var t = e.replace(ye, be);
                            return function (e) {
                                var n = void 0 !== e.getAttributeNode && e.getAttributeNode("id");
                                return n && n.value === t
                            }
                        }), x.find["TAG"] = b.getElementsByTagName ? function (e, t) {
                            return void 0 !== t.getElementsByTagName ? t.getElementsByTagName(e) : b.qsa ? t.querySelectorAll(e) : void 0
                        } : function (e, t) {
                            var n, r = [],
                                i = 0,
                                o = t.getElementsByTagName(e);
                            if ("*" === e) {
                                for (; n = o[i++];) 1 === n.nodeType && r.push(n);
                                return r
                            }
                            return o
                        }, x.find["CLASS"] = b.getElementsByClassName && function (e, t) {
                            if (void 0 !== t.getElementsByClassName && L) return t.getElementsByClassName(e)
                        }, q = [], $ = [], (b.qsa = he.test(A.querySelectorAll)) && (i(function (e) {
                            D.appendChild(e).innerHTML = "<a id='" + M + "'></a><select id='" + M + "-\r\\' msallowcapture=''><option selected=''></option></select>", e.querySelectorAll("[msallowcapture^='']").length && $.push("[*^$]=" + ee + "*(?:''|\"\")"), e.querySelectorAll("[selected]").length || $.push("\\[" + ee + "*(?:value|" + Z + ")"), e.querySelectorAll("[id~=" + M + "-]").length || $.push("~="), e.querySelectorAll(":checked").length || $.push(":checked"), e.querySelectorAll("a#" + M + "+*").length || $.push(".#.+[+~]")
                        }), i(function (e) {
                            var t = A.createElement("input");
                            t.setAttribute("type", "hidden"), e.appendChild(t).setAttribute("name", "D"), e.querySelectorAll("[name=d]").length && $.push("name" + ee + "*[*^$|!~]?="), e.querySelectorAll(":enabled").length || $.push(":enabled", ":disabled"), e.querySelectorAll("*,:x"), $.push(",.*:")
                        })), (b.matchesSelector = he.test(H = D.matches || D.webkitMatchesSelector || D.mozMatchesSelector || D.oMatchesSelector || D.msMatchesSelector)) && i(function (e) {
                            b.disconnectedMatch = H.call(e, "div"), H.call(e, "[s!='']:x"), q.push("!=", re)
                        }), $ = $.length && new RegExp($.join("|")), q = q.length && new RegExp(q.join("|")), t = he.test(D.compareDocumentPosition), O = t || he.test(D.contains) ? function (e, t) {
                            var n = 9 === e.nodeType ? e.documentElement : e,
                                r = t && t.parentNode;
                            return e === r || !(!r || 1 !== r.nodeType || !(n.contains ? n.contains(r) : e.compareDocumentPosition && 16 & e.compareDocumentPosition(r)))
                        } : function (e, t) {
                            if (t)
                                for (; t = t.parentNode;)
                                    if (t === e) return !0;
                            return !1
                        }, z = t ? function (e, t) {
                            if (e === t) return S = !0, 0;
                            var n = !e.compareDocumentPosition - !t.compareDocumentPosition;
                            return n || (n = (e.ownerDocument || e) === (t.ownerDocument || t) ? e.compareDocumentPosition(t) : 1, 1 & n || !b.sortDetached && t.compareDocumentPosition(e) === n ? e === A || e.ownerDocument === P && O(P, e) ? -1 : t === A || t.ownerDocument === P && O(P, t) ? 1 : N ? Q(N, e) - Q(N, t) : 0 : 4 & n ? -1 : 1)
                        } : function (e, t) {
                            if (e === t) return S = !0, 0;
                            var n, r = 0,
                                i = e.parentNode,
                                o = t.parentNode,
                                s = [e],
                                l = [t];
                            if (!i || !o) return e === A ? -1 : t === A ? 1 : i ? -1 : o ? 1 : N ? Q(N, e) - Q(N, t) : 0;
                            if (i === o) return a(e, t);
                            for (n = e; n = n.parentNode;) s.unshift(n);
                            for (n = t; n = n.parentNode;) l.unshift(n);
                            for (; s[r] === l[r];) r++;
                            return r ? a(s[r], l[r]) : s[r] === P ? -1 : l[r] === P ? 1 : 0
                        }, A) : A
                    }, t.matches = function (e, n) {
                        return t(e, null, null, n)
                    }, t.matchesSelector = function (e, n) {
                        if ((e.ownerDocument || e) !== A && j(e), n = n.replace(le, "='$1']"), b.matchesSelector && L && !B[n + " "] && (!q || !q.xpathTest(n)) && (!$ || !$.xpathTest(n))) try {
                            var r = H.call(e, n);
                            if (r || b.disconnectedMatch || e.document && 11 !== e.document.nodeType) return r
                        } catch (we) {}
                        return t(n, A, null, [e]).length > 0
                    }, t.contains = function (e, t) {
                        return (e.ownerDocument || e) !== A && j(e), O(e, t)
                    }, t.attr = function (e, t) {
                        (e.ownerDocument || e) !== A && j(e);
                        var n = x.attrHandle[t.toLowerCase()],
                            r = n && U.call(x.attrHandle, t.toLowerCase()) ? n(e, t, !L) : void 0;
                        return void 0 !== r ? r : b.attributes || !L ? e.getAttribute(t) : (r = e.getAttributeNode(t)) && r.specified ? r.value : null
                    }, t.error = function (e) {
                        throw new Error("Syntax error, unrecognized expression: " + e)
                    }, t.uniqueSort = function (e) {
                        var t, n = [],
                            r = 0,
                            i = 0;
                        if (S = !b.detectDuplicates, N = !b.sortStable && e.slice(0), e.sort(z), S) {
                            for (; t = e[i++];) t === e[i] && (r = n.push(i));
                            for (; r--;) e.splice(n[r], 1)
                        }
                        return N = null, e
                    }, w = t.getText = function (e) {
                        var t, n = "",
                            r = 0,
                            i = e.nodeType;
                        if (i) {
                            if (1 === i || 9 === i || 11 === i) {
                                if ("string" == typeof e.textContent) return e.textContent;
                                for (e = e.firstChild; e; e = e.nextSibling) n += w(e)
                            } else if (3 === i || 4 === i) return e.nodeValue
                        } else
                            for (; t = e[r++];) n += w(t);
                        return n
                    }, x = t.selectors = {
                        "cacheLength": 50,
                        "createPseudo": r,
                        "match": de,
                        "attrHandle": {},
                        "find": {},
                        "relative": {
                            ">": {
                                "dir": "parentNode",
                                "first": !0
                            },
                            " ": {
                                "dir": "parentNode"
                            },
                            "+": {
                                "dir": "previousSibling",
                                "first": !0
                            },
                            "~": {
                                "dir": "previousSibling"
                            }
                        },
                        "preFilter": {
                            "ATTR": function (e) {
                                return e[1] = e[1].replace(ye, be), e[3] = (e[3] || e[4] || e[5] || "").replace(ye, be), "~=" === e[2] && (e[3] = " " + e[3] + " "), e.slice(0, 4)
                            }, "CHILD": function (e) {
                                return e[1] = e[1].toLowerCase(), "nth" === e[1].slice(0, 3) ? (e[3] || t.error(e[0]), e[4] = +(e[4] ? e[5] + (e[6] || 1) : 2 * ("even" === e[3] || "odd" === e[3])), e[5] = +(e[7] + e[8] || "odd" === e[3])) : e[3] && t.error(e[0]), e
                            }, "PSEUDO": function (e) {
                                var t, n = !e[6] && e[2];
                                return de["CHILD"].test(e[0]) ? null : (e[3] ? e[2] = e[4] || e[5] || "" : n && ue.test(n) && (t = C(n, !0)) && (t = n.indexOf(")", n.length - t) - n.length) && (e[0] = e[0].slice(0, t), e[2] = n.slice(0, t)), e.slice(0, 3))
                            }
                        },
                        "filter": {
                            "TAG": function (e) {
                                var t = e.replace(ye, be).toLowerCase();
                                return "*" === e ? function () {
                                    return !0
                                } : function (e) {
                                    return e.nodeName && e.nodeName.toLowerCase() === t
                                }
                            }, "CLASS": function (e) {
                                var t = I[e + " "];
                                return t || (t = new RegExp("(^|" + ee + ")" + e + "(" + ee + "|$)")) && I(e, function (e) {
                                    return t.test("string" == typeof e.className && e.className || void 0 !== e.getAttribute && e.getAttribute("class") || "")
                                })
                            }, "ATTR": function (e, n, r) {
                                return function (i) {
                                    var o = t.attr(i, e);
                                    return null == o ? "!=" === n : !n || (o += "", "=" === n ? o === r : "!=" === n ? o !== r : "^=" === n ? r && 0 === o.indexOf(r) : "*=" === n ? r && o.indexOf(r) > -1 : "$=" === n ? r && o.slice(-r.length) === r : "~=" === n ? (" " + o.replace(ie, " ") + " ").indexOf(r) > -1 : "|=" === n && (o === r || o.slice(0, r.length + 1) === r + "-"))
                                }
                            }, "CHILD": function (e, t, n, r, i) {
                                var o = "nth" !== e.slice(0, 3),
                                    a = "last" !== e.slice(-4),
                                    s = "of-type" === t;
                                return 1 === r && 0 === i ? function (e) {
                                    return !!e.parentNode
                                } : function (t, n, l) {
                                    var u, c, d, f, p, h, g = o !== a ? "nextSibling" : "previousSibling",
                                        v = t.parentNode,
                                        m = s && t.nodeName.toLowerCase(),
                                        y = !l && !s,
                                        b = !1;
                                    if (v) {
                                        if (o) {
                                            for (; g;) {
                                                for (f = t; f = f[g];)
                                                    if (s ? f.nodeName.toLowerCase() === m : 1 === f.nodeType) return !1;
                                                h = g = "only" === e && !h && "nextSibling"
                                            }
                                            return !0
                                        }
                                        if (h = [a ? v.firstChild : v.lastChild], a && y) {
                                            for (f = v, d = f[M] || (f[M] = {}), c = d[f.uniqueID] || (d[f.uniqueID] = {}), u = c[e] || [], p = u[0] === F && u[1], b = p && u[2], f = p && v.childNodes[p]; f = ++p && f && f[g] || (b = p = 0) || h.pop();)
                                                if (1 === f.nodeType && ++b && f === t) {
                                                    c[e] = [F, p, b];
                                                    break
                                                }
                                        } else if (y && (f = t, d = f[M] || (f[M] = {}), c = d[f.uniqueID] || (d[f.uniqueID] = {}), u = c[e] || [], p = u[0] === F && u[1], b = p), !1 === b)
                                            for (;
                                                (f = ++p && f && f[g] || (b = p = 0) || h.pop()) && ((s ? f.nodeName.toLowerCase() !== m : 1 !== f.nodeType) || !++b || (y && (d = f[M] || (f[M] = {}), c = d[f.uniqueID] || (d[f.uniqueID] = {}), c[e] = [F, b]), f !== t)););
                                        return (b -= i) === r || b % r == 0 && b / r >= 0
                                    }
                                }
                            }, "PSEUDO": function (e, n) {
                                var i, o = x.pseudos[e] || x.setFilters[e.toLowerCase()] || t.error("unsupported pseudo: " + e);
                                return o[M] ? o(n) : o.length > 1 ? (i = [e, e, "", n], x.setFilters.hasOwnProperty(e.toLowerCase()) ? r(function (e, t) {
                                    for (var r, i = o(e, n), a = i.length; a--;) r = Q(e, i[a]), e[r] = !(t[r] = i[a])
                                }) : function (e) {
                                    return o(e, 0, i)
                                }) : o
                            }
                        },
                        "pseudos": {
                            "not": r(function (e) {
                                var t = [],
                                    n = [],
                                    i = k(e.replace(oe, "$1"));
                                return i[M] ? r(function (e, t, n, r) {
                                    for (var o, a = i(e, null, r, []), s = e.length; s--;)(o = a[s]) && (e[s] = !(t[s] = o))
                                }) : function (e, r, o) {
                                    return t[0] = e, i(t, null, o, n), t[0] = null, !n.pop()
                                }
                            }),
                            "has": r(function (e) {
                                return function (n) {
                                    return t(e, n).length > 0
                                }
                            }),
                            "contains": r(function (e) {
                                return e = e.replace(ye, be),
                                    function (t) {
                                        return (t.textContent || t.innerText || w(t)).indexOf(e) > -1
                                    }
                            }),
                            "lang": r(function (e) {
                                return ce.test(e || "") || t.error("unsupported lang: " + e), e = e.replace(ye, be).toLowerCase(),
                                    function (t) {
                                        var n;
                                        do {
                                            if (n = L ? t.lang : t.getAttribute("xml:lang") || t.getAttribute("lang")) return (n = n.toLowerCase()) === e || 0 === n.indexOf(e + "-")
                                        } while ((t = t.parentNode) && 1 === t.nodeType);
                                        return !1
                                    }
                            }),
                            "target": function (t) {
                                var n = e.location && e.location.hash;
                                return n && n.slice(1) === t.id
                            }, "root": function (e) {
                                return e === D
                            }, "focus": function (e) {
                                return e === A.activeElement && (!A.hasFocus || A.hasFocus()) && !!(e.type || e.href || ~e.tabIndex)
                            }, "enabled": function (e) {
                                return !1 === e.disabled
                            }, "disabled": function (e) {
                                return !0 === e.disabled
                            }, "checked": function (e) {
                                var t = e.nodeName.toLowerCase();
                                return "input" === t && !!e.checked || "option" === t && !!e.selected
                            }, "selected": function (e) {
                                return e.parentNode && e.parentNode.selectedIndex, !0 === e.selected
                            }, "empty": function (e) {
                                for (e = e.firstChild; e; e = e.nextSibling)
                                    if (e.nodeType < 6) return !1;
                                return !0
                            }, "parent": function (e) {
                                return !x.pseudos["empty"](e)
                            }, "header": function (e) {
                                return pe.test(e.nodeName)
                            }, "input": function (e) {
                                return fe.test(e.nodeName)
                            }, "button": function (e) {
                                var t = e.nodeName.toLowerCase();
                                return "input" === t && "button" === e.type || "button" === t
                            }, "text": function (e) {
                                var t;
                                return "input" === e.nodeName.toLowerCase() && "text" === e.type && (null == (t = e.getAttribute("type")) || "text" === t.toLowerCase())
                            }, "first": s(function () {
                                return [0]
                            }),
                            "last": s(function (e, t) {
                                return [t - 1]
                            }),
                            "eq": s(function (e, t, n) {
                                return [n < 0 ? n + t : n]
                            }),
                            "even": s(function (e, t) {
                                for (var n = 0; n < t; n += 2) e.push(n);
                                return e
                            }),
                            "odd": s(function (e, t) {
                                for (var n = 1; n < t; n += 2) e.push(n);
                                return e
                            }),
                            "lt": s(function (e, t, n) {
                                for (var r = n < 0 ? n + t : n; --r >= 0;) e.push(r);
                                return e
                            }),
                            "gt": s(function (e, t, n) {
                                for (var r = n < 0 ? n + t : n; ++r < t;) e.push(r);
                                return e
                            })
                        }
                    }, x.pseudos["nth"] = x.pseudos["eq"];
                    for (y in {
                        "radio": !0,
                        "checkbox": !0,
                        "file": !0,
                        "password": !0,
                        "image": !0
                    }) x.pseudos[y] = function (e) {
                        return function (t) {
                            return "input" === t.nodeName.toLowerCase() && t.type === e
                        }
                    }(y);
                    for (y in {
                        "submit": !0,
                        "reset": !0
                    }) x.pseudos[y] = function (e) {
                        return function (t) {
                            var n = t.nodeName.toLowerCase();
                            return ("input" === n || "button" === n) && t.type === e
                        }
                    }(y);
                    return u.prototype = x.filters = x.pseudos, x.setFilters = new u, C = t.tokenize = function (e, n) {
                        var r, i, o, a, s, l, u, c = W[e + " "];
                        if (c) return n ? 0 : c.slice(0);
                        for (s = e, l = [], u = x.preFilter; s;) {
                            r && !(i = ae.exec(s)) || (i && (s = s.slice(i[0].length) || s), l.push(o = [])), r = !1, (i = se.exec(s)) && (r = i.shift(), o.push({
                                "value": r,
                                "type": i[0].replace(oe, " ")
                            }), s = s.slice(r.length));
                            for (a in x.filter)!(i = de[a].exec(s)) || u[a] && !(i = u[a](i)) || (r = i.shift(), o.push({
                                "value": r,
                                "type": a,
                                "matches": i
                            }), s = s.slice(r.length));
                            if (!r) break
                        }
                        return n ? s.length : s ? t.error(e) : W(e, l).slice(0)
                    }, k = t.compile = function (e, t) {
                        var n, r = [],
                            i = [],
                            o = B[e + " "];
                        if (!o) {
                            for (t || (t = C(e)), n = t.length; n--;) o = v(t[n]), o[M] ? r.push(o) : i.push(o);
                            o = B(e, m(i, r)), o.selector = e
                        }
                        return o
                    }, E = t.select = function (e, t, n, r) {
                        var i, o, a, s, u, d = "function" == typeof e && e,
                            f = !r && C(e = d.selector || e);
                        if (n = n || [], 1 === f.length) {
                            if (o = f[0] = f[0].slice(0), o.length > 2 && "ID" === (a = o[0]).type && b.getById && 9 === t.nodeType && L && x.relative[o[1].type]) {
                                if (!(t = (x.find["ID"](a.matches[0].replace(ye, be), t) || [])[0])) return n;
                                d && (t = t.parentNode), e = e.slice(o.shift().value.length)
                            }
                            for (i = de["needsContext"].test(e) ? 0 : o.length; i-- && (a = o[i], !x.relative[s = a.type]);)
                                if ((u = x.find[s]) && (r = u(a.matches[0].replace(ye, be), ve.test(o[0].type) && l(t.parentNode) || t))) {
                                    if (o.splice(i, 1), !(e = r.length && c(o))) return J.apply(n, r), n;
                                    break
                                }
                        }
                        return (d || k(e, f))(r, t, !L, n, !t || ve.test(e) && l(t.parentNode) || t), n
                    }, b.sortStable = M.split("").sort(z).join("") === M, b.detectDuplicates = !!S, j(), b.sortDetached = i(function (e) {
                        return 1 & e.compareDocumentPosition(A.createElement("div"))
                    }), i(function (e) {
                        return e.innerHTML = "<a href='#'></a>", "#" === e.firstChild.getAttribute("href")
                    }) || o("type|href|height|width", function (e, t, n) {
                        if (!n) return e.getAttribute(t, "type" === t.toLowerCase() ? 1 : 2)
                    }), b.attributes && i(function (e) {
                        return e.innerHTML = "<input/>", e.firstChild.setAttribute("value", ""), "" === e.firstChild.getAttribute("value")
                    }) || o("value", function (e, t, n) {
                        if (!n && "input" === e.nodeName.toLowerCase()) return e.defaultValue
                    }), i(function (e) {
                        return null == e.getAttribute("disabled")
                    }) || o(Z, function (e, t, n) {
                        var r;
                        if (!n) return !0 === e[t] ? t.toLowerCase() : (r = e.getAttributeNode(t)) && r.specified ? r.value : null
                    }), t
                }(n);
            ve.find = we, ve.expr = we.selectors, ve.expr[":"] = ve.expr.pseudos, ve.uniqueSort = ve.unique = we.uniqueSort, ve.text = we.getText, ve.isXMLDoc = we.isXML, ve.contains = we.contains;
            var Te = function (e, t, n) {
                    for (var r = [], i = void 0 !== n;
                        (e = e[t]) && 9 !== e.nodeType;)
                        if (1 === e.nodeType) {
                            if (i && ve(e).is(n)) break;
                            r.push(e)
                        }
                    return r
                },
                Ce = function (e, t) {
                    for (var n = []; e; e = e.nextSibling) 1 === e.nodeType && e !== t && n.push(e);
                    return n
                },
                ke = ve.expr.match.needsContext,
                Ee = /^<([\w-]+)\s*\/?>(?:<\/\1>|)$/,
                _e = /^.[^:#\[\.,]*$/;
            ve.filter = function (e, t, n) {
                var r = t[0];
                return n && (e = ":not(" + e + ")"), 1 === t.length && 1 === r.nodeType ? ve.find.matchesSelector(r, e) ? [r] : [] : ve.find.matches(e, ve.grep(t, function (e) {
                    return 1 === e.nodeType
                }))
            }, ve.fn.extend({
                "find": function (e) {
                    var t, n = [],
                        r = this,
                        i = r.length;
                    if ("string" != typeof e) return this.pushStack(ve(e).filter(function () {
                        for (t = 0; t < i; t++)
                            if (ve.contains(r[t], this)) return !0
                    }));
                    for (t = 0; t < i; t++) ve.find(e, r[t], n);
                    return n = this.pushStack(i > 1 ? ve.unique(n) : n), n.selector = this.selector ? this.selector + " " + e : e, n
                }, "filter": function (e) {
                    return this.pushStack(s(this, e || [], !1))
                }, "not": function (e) {
                    return this.pushStack(s(this, e || [], !0))
                }, "is": function (e) {
                    return !!s(this, "string" == typeof e && ke.xpathTest(e) ? ve(e) : e || [], !1).length
                }
            });
            var Ne, Se = /^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]*))$/;
            (ve.fn.init = function (e, t, n) {
                var r, i;
                if (!e) return this;
                if (n = n || Ne, "string" == typeof e) {
                    if (!(r = "<" === e.charAt(0) && ">" === e.charAt(e.length - 1) && e.length >= 3 ? [null, e, null] : Se.exec(e)) || !r[1] && t) return !t || t.jquery ? (t || n).find(e) : this.constructor(t).find(e);
                    if (r[1]) {
                        if (t = t instanceof ve ? t[0] : t, ve.merge(this, ve.parseHTML(r[1], t && t.nodeType ? t.ownerDocument || t : se, !0)), Ee.test(r[1]) && ve.isPlainObject(t))
                            for (r in t) ve.isFunction(this[r]) ? this[r](t[r]) : this.attr(r, t[r]);
                        return this
                    }
                    if ((i = se.getElementById(r[2])) && i.parentNode) {
                        if (i.id !== r[2]) return Ne.find(e);
                        this.length = 1, this[0] = i
                    }
                    return this.context = se, this.selector = e, this
                }
                return e.nodeType ? (this.context = this[0] = e, this.length = 1, this) : ve.isFunction(e) ? void 0 !== n.ready ? n.ready(e) : e(ve) : (void 0 !== e.selector && (this.selector = e.selector, this.context = e.context), ve.makeArray(e, this))
            }).prototype = ve.fn, Ne = ve(se);
            var je = /^(?:parents|prev(?:Until|All))/,
                Ae = {
                    "children": !0,
                    "contents": !0,
                    "next": !0,
                    "prev": !0
                };
            ve.fn.extend({
                "has": function (e) {
                    var t, n = ve(e, this),
                        r = n.length;
                    return this.filter(function () {
                        for (t = 0; t < r; t++)
                            if (ve.contains(this, n[t])) return !0
                    })
                }, "closest": function (e, t) {
                    for (var n, r = 0, i = this.length, o = [], a = ke.xpathTest(e) || "string" != typeof e ? ve(e, t || this.context) : 0; r < i; r++)
                        for (n = this[r]; n && n !== t; n = n.parentNode)
                            if (n.nodeType < 11 && (a ? a.index(n) > -1 : 1 === n.nodeType && ve.find.matchesSelector(n, e))) {
                                o.push(n);
                                break
                            }
                    return this.pushStack(o.length > 1 ? ve.uniqueSort(o) : o)
                }, "index": function (e) {
                    return e ? "string" == typeof e ? ve.inArray(this[0], ve(e)) : ve.inArray(e.jquery ? e[0] : e, this) : this[0] && this[0].parentNode ? this.first().prevAll().length : -1
                }, "add": function (e, t) {
                    return this.pushStack(ve.uniqueSort(ve.merge(this.get(), ve(e, t))))
                }, "addBack": function (e) {
                    return this.add(null == e ? this.prevObject : this.prevObject.filter(e))
                }
            }), ve.each({
                "parent": function (e) {
                    var t = e.parentNode;
                    return t && 11 !== t.nodeType ? t : null
                }, "parents": function (e) {
                    return Te(e, "parentNode")
                }, "parentsUntil": function (e, t, n) {
                    return Te(e, "parentNode", n)
                }, "next": function (e) {
                    return l(e, "nextSibling")
                }, "prev": function (e) {
                    return l(e, "previousSibling")
                }, "nextAll": function (e) {
                    return Te(e, "nextSibling")
                }, "prevAll": function (e) {
                    return Te(e, "previousSibling")
                }, "nextUntil": function (e, t, n) {
                    return Te(e, "nextSibling", n)
                }, "prevUntil": function (e, t, n) {
                    return Te(e, "previousSibling", n)
                }, "siblings": function (e) {
                    return Ce((e.parentNode || {}).firstChild, e)
                }, "children": function (e) {
                    return Ce(e.firstChild)
                }, "contents": function (e) {
                    return ve.nodeName(e, "iframe") ? e.contentDocument || e.contentWindow.document : ve.merge([], e.childNodes)
                }
            }, function (e, t) {
                ve.fn[e] = function (n, r) {
                    var i = ve.map(this, t, n);
                    return "Until" !== e.slice(-5) && (r = n), r && "string" == typeof r && (i = ve.filter(r, i)), this.length > 1 && (Ae[e] || (i = ve.uniqueSort(i)), je.test(e) && (i = i.reverse())), this.pushStack(i)
                }
            });
            var De = /\S+/g;
            ve.Callbacks = function (e) {
                e = "string" == typeof e ? u(e) : ve.extend({}, e);
                var t, n, r, i, o = [],
                    a = [],
                    s = -1,
                    l = function () {
                        for (i = e.once, r = t = !0; a.length; s = -1)
                            for (n = a.shift(); ++s < o.length;)!1 === o[s].apply(n[0], n[1]) && e.stopOnFalse && (s = o.length, n = !1);
                        e.memory || (n = !1), t = !1, i && (o = n ? [] : "")
                    },
                    c = {
                        "add": function () {
                            return o && (n && !t && (s = o.length - 1, a.push(n)), function r(t) {
                                ve.each(t, function (t, n) {
                                    ve.isFunction(n) ? e.unique && c.has(n) || o.push(n) : n && n.length && "string" !== ve.type(n) && r(n)
                                })
                            }(arguments), n && !t && l()), this
                        }, "remove": function () {
                            return ve.each(arguments, function (e, t) {
                                for (var n;
                                    (n = ve.inArray(t, o, n)) > -1;) o.splice(n, 1), n <= s && s--
                            }), this
                        }, "has": function (e) {
                            return e ? ve.inArray(e, o) > -1 : o.length > 0
                        }, "empty": function () {
                            return o && (o = []), this
                        }, "disable": function () {
                            return i = a = [], o = n = "", this
                        }, "disabled": function () {
                            return !o
                        }, "lock": function () {
                            return i = !0, n || c.disable(), this
                        }, "locked": function () {
                            return !!i
                        }, "fireWith": function (e, n) {
                            return i || (n = n || [], n = [e, n.slice ? n.slice() : n], a.push(n), t || l()), this
                        }, "fire": function () {
                            return c.fireWith(this, arguments), this
                        }, "fired": function () {
                            return !!r
                        }
                    };
                return c
            }, ve.extend({
                "Deferred": function (e) {
                    var t = [
                            ["resolve", "done", ve.Callbacks("once memory"), "resolved"],
                            ["reject", "fail", ve.Callbacks("once memory"), "rejected"],
                            ["notify", "progress", ve.Callbacks("memory")]
                        ],
                        n = "pending",
                        r = {
                            "state": function () {
                                return n
                            }, "always": function () {
                                return i.done(arguments).fail(arguments), this
                            }, "then": function () {
                                var e = arguments;
                                return ve.Deferred(function (n) {
                                    ve.each(t, function (t, o) {
                                        var a = ve.isFunction(e[t]) && e[t];
                                        i[o[1]](function () {
                                            var e = a && a.apply(this, arguments);
                                            e && ve.isFunction(e.promise) ? e.promise().progress(n.notify).done(n.resolve).fail(n.reject) : n[o[0] + "With"](this === r ? n.promise() : this, a ? [e] : arguments)
                                        })
                                    }), e = null
                                }).promise()
                            }, "promise": function (e) {
                                return null != e ? ve.extend(e, r) : r
                            }
                        },
                        i = {};
                    return r.pipe = r.then, ve.each(t, function (e, o) {
                        var a = o[2],
                            s = o[3];
                        r[o[1]] = a.add, s && a.add(function () {
                            n = s
                        }, t[1 ^ e][2].disable, t[2][2].lock), i[o[0]] = function () {
                            return i[o[0] + "With"](this === i ? r : this, arguments), this
                        }, i[o[0] + "With"] = a.fireWith
                    }), r.promise(i), e && e.call(i, i), i
                }, "when": function (e) {
                    var t, n, r, i = 0,
                        o = le.call(arguments),
                        a = o.length,
                        s = 1 !== a || e && ve.isFunction(e.promise) ? a : 0,
                        l = 1 === s ? e : ve.Deferred(),
                        u = function (e, n, r) {
                            return function (i) {
                                n[e] = this, r[e] = arguments.length > 1 ? le.call(arguments) : i, r === t ? l.notifyWith(n, r) : --s || l.resolveWith(n, r)
                            }
                        };
                    if (a > 1)
                        for (t = new Array(a), n = new Array(a), r = new Array(a); i < a; i++) o[i] && ve.isFunction(o[i].promise) ? o[i].promise().progress(u(i, n, t)).done(u(i, r, o)).fail(l.reject) : --s;
                    return s || l.resolveWith(r, o), l.promise()
                }
            });
            var Le;
            ve.fn.ready = function (e) {
                return ve.ready.promise().done(e), this
            }, ve.extend({
                "isReady": !1,
                "readyWait": 1,
                "holdReady": function (e) {
                    e ? ve.readyWait++ : ve.ready(!0)
                }, "ready": function (e) {
                    (!0 === e ? --ve.readyWait : ve.isReady) || (ve.isReady = !0, !0 !== e && --ve.readyWait > 0 || (Le.resolveWith(se, [ve]), ve.fn.triggerHandler && (ve(se).triggerHandler("ready"), ve(se).off("ready"))))
                }
            }), ve.ready.promise = function (e) {
                if (!Le)
                    if (Le = ve.Deferred(), "complete" === se.readyState || "loading" !== se.readyState && !se.documentElement.doScroll) n.setTimeout(ve.ready);
                    else if (se.addEventListener) se.addEventListener("DOMContentLoaded", d), n.addEventListener("load", d);
                else {
                    se.attachEvent("onreadystatechange", d), n.attachEvent("onload", d);
                    var t = !1;
                    try {
                        t = null == n.frameElement && se.documentElement
                    } catch (r) {}
                    t && t.doScroll && function i() {
                        if (!ve.isReady) {
                            try {
                                t.doScroll("left")
                            } catch (r) {
                                return n.setTimeout(i, 50)
                            }
                            c(), ve.ready()
                        }
                    }()
                }
                return Le.promise(e)
            }, ve.ready.promise();
            var $e;
            for ($e in ve(ge)) break;
            ge.ownFirst = "0" === $e, ge.inlineBlockNeedsLayout = !1, ve(function () {
                    var e, t, n, r;
                    (n = se.getElementsByTagName("body")[0]) && n.style && (t = se.createElement("div"), r = se.createElement("div"), r.style.cssText = "position:absolute;border:0;width:0;height:0;top:0;left:-9999px", n.appendChild(r).appendChild(t), void 0 !== t.style.zoom && (t.style.cssText = "display:inline;margin:0;border:0;padding:1px;width:1px;zoom:1", ge.inlineBlockNeedsLayout = e = 3 === t.offsetWidth, e && (n.style.zoom = 1)), n.removeChild(r))
                }),
                function () {
                    var e = se.createElement("div");
                    ge.deleteExpando = !0;
                    try {
                        delete e.xpathTest
                    } catch (t) {
                        ge.deleteExpando = !1
                    }
                    e = null
                }();
            var qe = function (e) {
                    var t = ve.noData[(e.nodeName + " ").toLowerCase()],
                        n = +e.nodeType || 1;
                    return (1 === n || 9 === n) && (!t || !0 !== t && e.getAttribute("classid") === t)
                },
                He = /^(?:\{[\w\W]*\}|\[[\w\W]*\])$/,
                Oe = /([A-Z])/g;
            ve.extend({
                    "cache": {},
                    "noData": {
                        "applet ": !0,
                        "embed ": !0,
                        "object ": "clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
                    },
                    "hasData": function (e) {
                        return !!(e = e.nodeType ? ve.cache[e[ve.expando]] : e[ve.expando]) && !p(e)
                    }, "data": function (e, t, n) {
                        return h(e, t, n)
                    }, "removeData": function (e, t) {
                        return g(e, t)
                    }, "_data": function (e, t, n) {
                        return h(e, t, n, !0)
                    }, "_removeData": function (e, t) {
                        return g(e, t, !0)
                    }
                }), ve.fn.extend({
                    "data": function (e, t) {
                        var n, r, i, o = this[0],
                            a = o && o.attributes;
                        if (void 0 === e) {
                            if (this.length && (i = ve.data(o), 1 === o.nodeType && !ve._data(o, "parsedAttrs"))) {
                                for (n = a.length; n--;) a[n] && (r = a[n].name, 0 === r.indexOf("data-") && (r = ve.camelCase(r.slice(5)), f(o, r, i[r])));
                                ve._data(o, "parsedAttrs", !0)
                            }
                            return i
                        }
                        return "object" == typeof e ? this.each(function () {
                            ve.data(this, e)
                        }) : arguments.length > 1 ? this.each(function () {
                            ve.data(this, e, t)
                        }) : o ? f(o, e, ve.data(o, e)) : void 0
                    }, "removeData": function (e) {
                        return this.each(function () {
                            ve.removeData(this, e)
                        })
                    }
                }), ve.extend({
                    "queue": function (e, t, n) {
                        var r;
                        if (e) return t = (t || "fx") + "queue", r = ve._data(e, t), n && (!r || ve.isArray(n) ? r = ve._data(e, t, ve.makeArray(n)) : r.push(n)), r || []
                    }, "dequeue": function (e, t) {
                        t = t || "fx";
                        var n = ve.queue(e, t),
                            r = n.length,
                            i = n.shift(),
                            o = ve._queueHooks(e, t),
                            a = function () {
                                ve.dequeue(e, t)
                            };
                        "inprogress" === i && (i = n.shift(), r--), i && ("fx" === t && n.unshift("inprogress"), delete o.stop, i.call(e, a, o)), !r && o && o.empty.fire()
                    }, "_queueHooks": function (e, t) {
                        var n = t + "queueHooks";
                        return ve._data(e, n) || ve._data(e, n, {
                            "empty": ve.Callbacks("once memory").add(function () {
                                ve._removeData(e, t + "queue"), ve._removeData(e, n)
                            })
                        })
                    }
                }), ve.fn.extend({
                    "queue": function (e, t) {
                        var n = 2;
                        return "string" != typeof e && (t = e, e = "fx", n--), arguments.length < n ? ve.queue(this[0], e) : void 0 === t ? this : this.each(function () {
                            var n = ve.queue(this, e, t);
                            ve._queueHooks(this, e), "fx" === e && "inprogress" !== n[0] && ve.dequeue(this, e)
                        })
                    }, "dequeue": function (e) {
                        return this.each(function () {
                            ve.dequeue(this, e)
                        })
                    }, "clearQueue": function (e) {
                        return this.queue(e || "fx", [])
                    }, "promise": function (e, t) {
                        var n, r = 1,
                            i = ve.Deferred(),
                            o = this,
                            a = this.length,
                            s = function () {
                                --r || i.resolveWith(o, [o])
                            };
                        for ("string" != typeof e && (t = e, e = void 0), e = e || "fx"; a--;)(n = ve._data(o[a], e + "queueHooks")) && n.empty && (r++, n.empty.add(s));
                        return s(), i.promise(t)
                    }
                }),
                function () {
                    var e;
                    ge.shrinkWrapBlocks = function () {
                        if (null != e) return e;
                        e = !1;
                        var t, n, r;
                        return (n = se.getElementsByTagName("body")[0]) && n.style ? (t = se.createElement("div"), r = se.createElement("div"), r.style.cssText = "position:absolute;border:0;width:0;height:0;top:0;left:-9999px", n.appendChild(r).appendChild(t), void 0 !== t.style.zoom && (t.style.cssText = "-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box;display:block;margin:0;border:0;padding:1px;width:1px;zoom:1", t.appendChild(se.createElement("div")).style.width = "5px", e = 3 !== t.offsetWidth), n.removeChild(r), e) : void 0
                    }
                }();
            var Me = /[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source,
                Pe = new RegExp("^(?:([+-])=|)(" + Me + ")([a-z%]*)$", "i"),
                Fe = ["Top", "Right", "Bottom", "Left"],
                Re = function (e, t) {
                    return e = t || e, "none" === ve.css(e, "display") || !ve.contains(e.ownerDocument, e)
                },
                Ie = function (e, t, n, r, i, o, a) {
                    var s = 0,
                        l = e.length,
                        u = null == n;
                    if ("object" === ve.type(n)) {
                        i = !0;
                        for (s in n) Ie(e, t, s, n[s], !0, o, a)
                    } else if (void 0 !== r && (i = !0, ve.isFunction(r) || (a = !0), u && (a ? (t.call(e, r), t = null) : (u = t, t = function (e, t, n) {
                        return u.call(ve(e), n)
                    })), t))
                        for (; s < l; s++) t(e[s], n, a ? r : r.call(e[s], s, t(e[s], n)));
                    return i ? e : u ? t.call(e) : l ? t(e[0], n) : o
                },
                We = /^(?:checkbox|radio)$/i,
                Be = /<([\w:-]+)/,
                ze = /^$|\/(?:java|ecma)script/i,
                Xe = /^\s+/,
                Ue = "abbr|article|aside|audio|bdi|canvas|data|datalist|details|dialog|figcaption|figure|footer|header|hgroup|main|mark|meter|nav|output|picture|progress|section|summary|template|time|video";
            ! function () {
                var e = se.createElement("div"),
                    t = se.createDocumentFragment(),
                    n = se.createElement("input");
                e.innerHTML = "  <link/><table></table><a href='/a'>a</a><input type='checkbox'/>", ge.leadingWhitespace = 3 === e.firstChild.nodeType, ge.tbody = !e.getElementsByTagName("tbody").length, ge.htmlSerialize = !!e.getElementsByTagName("link").length, ge.html5Clone = "<:nav></:nav>" !== se.createElement("nav").cloneNode(!0).outerHTML, n.type = "checkbox", n.checked = !0, t.appendChild(n), ge.appendChecked = n.checked, e.innerHTML = "<textarea>x</textarea>", ge.noCloneChecked = !!e.cloneNode(!0).lastChild.defaultValue, t.appendChild(e), n = se.createElement("input"), n.setAttribute("type", "radio"), n.setAttribute("checked", "checked"), n.setAttribute("name", "t"), e.appendChild(n), ge.checkClone = e.cloneNode(!0).cloneNode(!0).lastChild.checked, ge.noCloneEvent = !!e.addEventListener, e[ve.expando] = 1, ge.attributes = !e.getAttribute(ve.expando)
            }();
            var Ve = {
                "option": [1, "<select multiple='multiple'>", "</select>"],
                "legend": [1, "<fieldset>", "</fieldset>"],
                "area": [1, "<map>", "</map>"],
                "param": [1, "<object>", "</object>"],
                "thead": [1, "<table>", "</table>"],
                "tr": [2, "<table><tbody>", "</tbody></table>"],
                "col": [2, "<table><tbody></tbody><colgroup>", "</colgroup></table>"],
                "td": [3, "<table><tbody><tr>", "</tr></tbody></table>"],
                "_default": ge.htmlSerialize ? [0, "", ""] : [1, "X<div>", "</div>"]
            };
            Ve.optgroup = Ve.option, Ve.tbody = Ve.tfoot = Ve.colgroup = Ve.caption = Ve.thead, Ve.th = Ve.td;
            var Ge = /<|&#?\w+;/,
                Ye = /<tbody/i;
            ! function () {
                var e, t, r = se.createElement("div");
                for (e in {
                    "submit": !0,
                    "change": !0,
                    "focusin": !0
                }) t = "on" + e, (ge[e] = t in n) || (r.setAttribute(t, "t"), ge[e] = !1 === r.attributes[t].expando);
                r = null
            }();
            var Je = /^(?:input|select|textarea)$/i,
                Ke = /^key/,
                Qe = /^(?:mouse|pointer|contextmenu|drag|drop)|click/,
                Ze = /^(?:focusinfocus|focusoutblur)$/,
                et = /^([^.]*)(?:\.(.+)|)/;
            ve.event = {
                "global": {},
                "add": function (e, t, n, r, i) {
                    var o, a, s, l, u, c, d, f, p, h, g, v = ve._data(e);
                    if (v) {
                        for (n.handler && (l = n, n = l.handler, i = l.selector), n.guid || (n.guid = ve.guid++), (a = v.events) || (a = v.events = {}), (c = v.handle) || (c = v.handle = function (e) {
                            return void 0 === ve || e && ve.event.triggered === e.type ? void 0 : ve.event.dispatch.apply(c.elem, arguments)
                        }, c.elem = e), t = (t || "").match(De) || [""], s = t.length; s--;) o = et.exec(t[s]) || [], p = g = o[1], h = (o[2] || "").split(".").sort(), p && (u = ve.event.special[p] || {}, p = (i ? u.delegateType : u.bindType) || p, u = ve.event.special[p] || {}, d = ve.extend({
                            "type": p,
                            "origType": g,
                            "data": r,
                            "handler": n,
                            "guid": n.guid,
                            "selector": i,
                            "needsContext": i && ve.expr.match.needsContext.xpathTest(i),
                            "namespace": h.join(".")
                        }, l), (f = a[p]) || (f = a[p] = [], f.delegateCount = 0, u.setup && !1 !== u.setup.call(e, r, h, c) || (e.addEventListener ? e.addEventListener(p, c, !1) : e.attachEvent && e.attachEvent("on" + p, c))), u.add && (u.add.call(e, d), d.handler.guid || (d.handler.guid = n.guid)), i ? f.splice(f.delegateCount++, 0, d) : f.push(d), ve.event.global[p] = !0);
                        e = null
                    }
                }, "remove": function (e, t, n, r, i) {
                    var o, a, s, l, u, c, d, f, p, h, g, v = ve.hasData(e) && ve._data(e);
                    if (v && (c = v.events)) {
                        for (t = (t || "").match(De) || [""], u = t.length; u--;)
                            if (s = et.exec(t[u]) || [], p = g = s[1], h = (s[2] || "").split(".").sort(), p) {
                                for (d = ve.event.special[p] || {}, p = (r ? d.delegateType : d.bindType) || p, f = c[p] || [], s = s[2] && new RegExp("(^|\\.)" + h.join("\\.(?:.*\\.|)") + "(\\.|$)"), l = o = f.length; o--;) a = f[o], !i && g !== a.origType || n && n.guid !== a.guid || s && !s.test(a.namespace) || r && r !== a.selector && ("**" !== r || !a.selector) || (f.splice(o, 1), a.selector && f.delegateCount--, d.remove && d.remove.call(e, a));
                                l && !f.length && (d.teardown && !1 !== d.teardown.call(e, h, v.handle) || ve.removeEvent(e, p, v.handle), delete c[p])
                            } else
                                for (p in c) ve.event.remove(e, p + t[u], n, r, !0);
                        ve.isEmptyObject(c) && (delete v.handle, ve._removeData(e, "events"))
                    }
                }, "trigger": function (e, t, r, i) {
                    var o, a, s, l, u, c, d, f = [r || se],
                        p = he.call(e, "type") ? e.type : e,
                        h = he.call(e, "namespace") ? e.namespace.split(".") : [];
                    if (s = c = r = r || se, 3 !== r.nodeType && 8 !== r.nodeType && !Ze.test(p + ve.event.triggered) && (p.indexOf(".") > -1 && (h = p.split("."), p = h.shift(), h.sort()), a = p.indexOf(":") < 0 && "on" + p, e = e[ve.expando] ? e : new ve.Event(p, "object" == typeof e && e), e.isTrigger = i ? 2 : 3, e.namespace = h.join("."), e.rnamespace = e.namespace ? new RegExp("(^|\\.)" + h.join("\\.(?:.*\\.|)") + "(\\.|$)") : null, e.result = void 0, e.target || (e.target = r), t = null == t ? [e] : ve.makeArray(t, [e]), u = ve.event.special[p] || {}, i || !u.trigger || !1 !== u.trigger.apply(r, t))) {
                        if (!i && !u.noBubble && !ve.isWindow(r)) {
                            for (l = u.delegateType || p, Ze.test(l + p) || (s = s.parentNode); s; s = s.parentNode) f.push(s), c = s;
                            c === (r.ownerDocument || se) && f.push(c.defaultView || c.parentWindow || n)
                        }
                        for (d = 0;
                            (s = f[d++]) && !e.isPropagationStopped();) e.type = d > 1 ? l : u.bindType || p, o = (ve._data(s, "events") || {})[e.type] && ve._data(s, "handle"), o && o.apply(s, t), (o = a && s[a]) && o.apply && qe(s) && (e.result = o.apply(s, t), !1 === e.result && e.preventDefault());
                        if (e.type = p, !i && !e.isDefaultPrevented() && (!u._default || !1 === u._default.apply(f.pop(), t)) && qe(r) && a && r[p] && !ve.isWindow(r)) {
                            c = r[a], c && (r[a] = null), ve.event.triggered = p;
                            try {
                                r[p]()
                            } catch (g) {}
                            ve.event.triggered = void 0, c && (r[a] = c)
                        }
                        return e.result
                    }
                }, "dispatch": function (e) {
                    e = ve.event.fix(e);
                    var t, n, r, i, o, a = [],
                        s = le.call(arguments),
                        l = (ve._data(this, "events") || {})[e.type] || [],
                        u = ve.event.special[e.type] || {};
                    if (s[0] = e, e.delegateTarget = this, !u.preDispatch || !1 !== u.preDispatch.call(this, e)) {
                        for (a = ve.event.handlers.call(this, e, l), t = 0;
                            (i = a[t++]) && !e.isPropagationStopped();)
                            for (e.currentTarget = i.elem, n = 0;
                                (o = i.handlers[n++]) && !e.isImmediatePropagationStopped();) e.rnamespace && !e.rnamespace.xpathTest(o.namespace) || (e.handleObj = o, e.data = o.data, void 0 !== (r = ((ve.event.special[o.origType] || {}).handle || o.handler).apply(i.elem, s)) && !1 === (e.result = r) && (e.preventDefault(), e.stopPropagation()));
                        return u.postDispatch && u.postDispatch.call(this, e), e.result
                    }
                }, "handlers": function (e, t) {
                    var n, r, i, o, a = [],
                        s = t.delegateCount,
                        l = e.target;
                    if (s && l.nodeType && ("click" !== e.type || isNaN(e.button) || e.button < 1))
                        for (; l != this; l = l.parentNode || this)
                            if (1 === l.nodeType && (!0 !== l.disabled || "click" !== e.type)) {
                                for (r = [], n = 0; n < s; n++) o = t[n], i = o.selector + " ", void 0 === r[i] && (r[i] = o.needsContext ? ve(i, this).index(l) > -1 : ve.find(i, this, null, [l]).length), r[i] && r.push(o);
                                r.length && a.push({
                                    "elem": l,
                                    "handlers": r
                                })
                            }
                    return s < t.length && a.push({
                        "elem": this,
                        "handlers": t.slice(s)
                    }), a
                }, "fix": function (e) {
                    if (e[ve.expando]) return e;
                    var t, n, r, i = e.type,
                        o = e,
                        a = this.fixHooks[i];
                    for (a || (this.fixHooks[i] = a = Qe.test(i) ? this.mouseHooks : Ke.test(i) ? this.keyHooks : {}), r = a.props ? this.props.concat(a.props) : this.props, e = new ve.Event(o), t = r.length; t--;) n = r[t], e[n] = o[n];
                    return e.target || (e.target = o.srcElement || se), 3 === e.target.nodeType && (e.target = e.target.parentNode), e.metaKey = !!e.metaKey, a.filter ? a.filter(e, o) : e
                }, "props": "altKey bubbles cancelable ctrlKey currentTarget detail eventPhase metaKey relatedTarget shiftKey target timeStamp view which".split(" "),
                "fixHooks": {},
                "keyHooks": {
                    "props": "char charCode key keyCode".split(" "),
                    "filter": function (e, t) {
                        return null == e.which && (e.which = null != t.charCode ? t.charCode : t.keyCode), e
                    }
                },
                "mouseHooks": {
                    "props": "button buttons clientX clientY fromElement offsetX offsetY pageX pageY screenX screenY toElement".split(" "),
                    "filter": function (e, t) {
                        var n, r, i, o = t.button,
                            a = t.fromElement;
                        return null == e.pageX && null != t.clientX && (r = e.target.ownerDocument || se, i = r.documentElement, n = r.body, e.pageX = t.clientX + (i && i.scrollLeft || n && n.scrollLeft || 0) - (i && i.clientLeft || n && n.clientLeft || 0), e.pageY = t.clientY + (i && i.scrollTop || n && n.scrollTop || 0) - (i && i.clientTop || n && n.clientTop || 0)), !e.relatedTarget && a && (e.relatedTarget = a === e.target ? t.toElement : a), e.which || void 0 === o || (e.which = 1 & o ? 1 : 2 & o ? 3 : 4 & o ? 2 : 0), e
                    }
                },
                "special": {
                    "load": {
                        "noBubble": !0
                    },
                    "focus": {
                        "trigger": function () {
                            if (this !== k() && this.focus) try {
                                return this.focus(), !1
                            } catch (e) {}
                        }, "delegateType": "focusin"
                    },
                    "blur": {
                        "trigger": function () {
                            if (this === k() && this.blur) return this.blur(), !1
                        }, "delegateType": "focusout"
                    },
                    "click": {
                        "trigger": function () {
                            if (ve.nodeName(this, "input") && "checkbox" === this.type && this.click) return this.click(), !1
                        }, "_default": function (e) {
                            return ve.nodeName(e.target, "a")
                        }
                    },
                    "beforeunload": {
                        "postDispatch": function (e) {
                            void 0 !== e.result && e.originalEvent && (e.originalEvent.returnValue = e.result)
                        }
                    }
                },
                "simulate": function (e, t, n) {
                    var r = ve.extend(new ve.Event, n, {
                        "type": e,
                        "isSimulated": !0
                    });
                    ve.event.trigger(r, null, t), r.isDefaultPrevented() && n.preventDefault()
                }
            }, ve.removeEvent = se.removeEventListener ? function (e, t, n) {
                e.removeEventListener && e.removeEventListener(t, n)
            } : function (e, t, n) {
                var r = "on" + t;
                e.detachEvent && (void 0 === e[r] && (e[r] = null), e.detachEvent(r, n))
            }, ve.Event = function (e, t) {
                if (!(this instanceof ve.Event)) return new ve.Event(e, t);
                e && e.type ? (this.originalEvent = e, this.type = e.type, this.isDefaultPrevented = e.defaultPrevented || void 0 === e.defaultPrevented && !1 === e.returnValue ? T : C) : this.type = e, t && ve.extend(this, t), this.timeStamp = e && e.timeStamp || ve.now(), this[ve.expando] = !0
            }, ve.Event.prototype = {
                "constructor": ve.Event,
                "isDefaultPrevented": C,
                "isPropagationStopped": C,
                "isImmediatePropagationStopped": C,
                "preventDefault": function () {
                    var e = this.originalEvent;
                    this.isDefaultPrevented = T, e && (e.preventDefault ? e.preventDefault() : e.returnValue = !1)
                }, "stopPropagation": function () {
                    var e = this.originalEvent;
                    this.isPropagationStopped = T, e && !this.isSimulated && (e.stopPropagation && e.stopPropagation(), e.cancelBubble = !0)
                }, "stopImmediatePropagation": function () {
                    var e = this.originalEvent;
                    this.isImmediatePropagationStopped = T, e && e.stopImmediatePropagation && e.stopImmediatePropagation(), this.stopPropagation()
                }
            }, ve.each({
                "mouseenter": "mouseover",
                "mouseleave": "mouseout",
                "pointerenter": "pointerover",
                "pointerleave": "pointerout"
            }, function (e, t) {
                ve.event.special[e] = {
                    "delegateType": t,
                    "bindType": t,
                    "handle": function (e) {
                        var n, r = this,
                            i = e.relatedTarget,
                            o = e.handleObj;
                        return i && (i === r || ve.contains(r, i)) || (e.type = o.origType, n = o.handler.apply(this, arguments), e.type = t), n
                    }
                }
            }), ge.submit || (ve.event.special.submit = {
                "setup": function () {
                    if (ve.nodeName(this, "form")) return !1;
                    ve.event.add(this, "click._submit keypress._submit", function (e) {
                        var t = e.target,
                            n = ve.nodeName(t, "input") || ve.nodeName(t, "button") ? ve.prop(t, "form") : void 0;
                        n && !ve._data(n, "submit") && (ve.event.add(n, "submit._submit", function (e) {
                            e._submitBubble = !0
                        }), ve._data(n, "submit", !0))
                    })
                }, "postDispatch": function (e) {
                    e._submitBubble && (delete e._submitBubble, this.parentNode && !e.isTrigger && ve.event.simulate("submit", this.parentNode, e))
                }, "teardown": function () {
                    if (ve.nodeName(this, "form")) return !1;
                    ve.event.remove(this, "._submit")
                }
            }), ge.change || (ve.event.special.change = {
                "setup": function () {
                    if (Je.test(this.nodeName)) return "checkbox" !== this.type && "radio" !== this.type || (ve.event.add(this, "propertychange._change", function (e) {
                        "checked" === e.originalEvent.propertyName && (this._justChanged = !0)
                    }), ve.event.add(this, "click._change", function (e) {
                        this._justChanged && !e.isTrigger && (this._justChanged = !1), ve.event.simulate("change", this, e)
                    })), !1;
                    ve.event.add(this, "beforeactivate._change", function (e) {
                        var t = e.target;
                        Je.test(t.nodeName) && !ve._data(t, "change") && (ve.event.add(t, "change._change", function (e) {
                            !this.parentNode || e.isSimulated || e.isTrigger || ve.event.simulate("change", this.parentNode, e)
                        }), ve._data(t, "change", !0))
                    })
                }, "handle": function (e) {
                    var t = e.target;
                    if (this !== t || e.isSimulated || e.isTrigger || "radio" !== t.type && "checkbox" !== t.type) return e.handleObj.handler.apply(this, arguments)
                }, "teardown": function () {
                    return ve.event.remove(this, "._change"), !Je.test(this.nodeName)
                }
            }), ge.focusin || ve.each({
                "focus": "focusin",
                "blur": "focusout"
            }, function (e, t) {
                var n = function (e) {
                    ve.event.simulate(t, e.target, ve.event.fix(e))
                };
                ve.event.special[t] = {
                    "setup": function () {
                        var r = this.ownerDocument || this,
                            i = ve._data(r, t);
                        i || r.addEventListener(e, n, !0), ve._data(r, t, (i || 0) + 1)
                    }, "teardown": function () {
                        var r = this.ownerDocument || this,
                            i = ve._data(r, t) - 1;
                        i ? ve._data(r, t, i) : (r.removeEventListener(e, n, !0), ve._removeData(r, t))
                    }
                }
            }), ve.fn.extend({
                "on": function (e, t, n, r) {
                    return E(this, e, t, n, r)
                }, "one": function (e, t, n, r) {
                    return E(this, e, t, n, r, 1)
                }, "off": function (e, t, n) {
                    var r, i;
                    if (e && e.preventDefault && e.handleObj) return r = e.handleObj, ve(e.delegateTarget).off(r.namespace ? r.origType + "." + r.namespace : r.origType, r.selector, r.handler), this;
                    if ("object" == typeof e) {
                        for (i in e) this.off(i, t, e[i]);
                        return this
                    }
                    return !1 !== t && "function" != typeof t || (n = t, t = void 0), !1 === n && (n = C), this.each(function () {
                        ve.event.remove(this, e, n, t)
                    })
                }, "trigger": function (e, t) {
                    return this.each(function () {
                        ve.event.trigger(e, t, this)
                    })
                }, "triggerHandler": function (e, t) {
                    var n = this[0];
                    if (n) return ve.event.trigger(e, t, n, !0)
                }
            });
            var tt = / jQuery\d+="(?:null|\d+)"/g,
                nt = new RegExp("<(?:" + Ue + ")[\\s/>]", "i"),
                rt = /<(?!area|br|col|embed|hr|img|input|link|meta|param)(([\w:-]+)[^>]*)\/>/gi,
                it = /<script|<style|<link/i,
                ot = /checked\s*(?:[^=]|=\s*.checked.)/i,
                at = /^true\/(.*)/,
                st = /^\s*<!(?:\[CDATA\[|--)|(?:\]\]|--)>\s*$/g,
                lt = m(se),
                ut = lt.appendChild(se.createElement("div"));
            ve.extend({
                "htmlPrefilter": function (e) {
                    return e.replace(rt, "<$1></$2>")
                }, "clone": function (e, t, n) {
                    var r, i, o, a, s, l = ve.contains(e.ownerDocument, e);
                    if (ge.html5Clone || ve.isXMLDoc(e) || !nt.test("<" + e.nodeName + ">") ? o = e.cloneNode(!0) : (ut.innerHTML = e.outerHTML, ut.removeChild(o = ut.firstChild)), !(ge.noCloneEvent && ge.noCloneChecked || 1 !== e.nodeType && 11 !== e.nodeType || ve.isXMLDoc(e)))
                        for (r = y(o), s = y(e), a = 0; null != (i = s[a]); ++a) r[a] && A(i, r[a]);
                    if (t)
                        if (n)
                            for (s = s || y(e), r = r || y(o), a = 0; null != (i = s[a]); a++) j(i, r[a]);
                        else j(e, o);
                    return r = y(o, "script"), r.length > 0 && b(r, !l && y(e, "script")), r = s = i = null, o
                }, "cleanData": function (e, t) {
                    for (var n, r, i, o, a = 0, s = ve.expando, l = ve.cache, u = ge.attributes, c = ve.event.special; null != (n = e[a]); a++)
                        if ((t || qe(n)) && (i = n[s], o = i && l[i])) {
                            if (o.events)
                                for (r in o.events) c[r] ? ve.event.remove(n, r) : ve.removeEvent(n, r, o.handle);
                            l[i] && (delete l[i], u || void 0 === n.removeAttribute ? n[s] = void 0 : n.removeAttribute(s), ae.push(i))
                        }
                }
            }), ve.fn.extend({
                "domManip": D,
                "detach": function (e) {
                    return L(this, e, !0)
                }, "remove": function (e) {
                    return L(this, e)
                }, "text": function (e) {
                    return Ie(this, function (e) {
                        return void 0 === e ? ve.text(this) : this.empty().append((this[0] && this[0].ownerDocument || se).createTextNode(e))
                    }, null, e, arguments.length)
                }, "append": function () {
                    return D(this, arguments, function (e) {
                        if (1 === this.nodeType || 11 === this.nodeType || 9 === this.nodeType) {
                            _(this, e).appendChild(e)
                        }
                    })
                }, "prepend": function () {
                    return D(this, arguments, function (e) {
                        if (1 === this.nodeType || 11 === this.nodeType || 9 === this.nodeType) {
                            var t = _(this, e);
                            t.insertBefore(e, t.firstChild)
                        }
                    })
                }, "before": function () {
                    return D(this, arguments, function (e) {
                        this.parentNode && this.parentNode.insertBefore(e, this)
                    })
                }, "after": function () {
                    return D(this, arguments, function (e) {
                        this.parentNode && this.parentNode.insertBefore(e, this.nextSibling)
                    })
                }, "empty": function () {
                    for (var e, t = 0; null != (e = this[t]); t++) {
                        for (1 === e.nodeType && ve.cleanData(y(e, !1)); e.firstChild;) e.removeChild(e.firstChild);
                        e.options && ve.nodeName(e, "select") && (e.options.length = 0)
                    }
                    return this
                }, "clone": function (e, t) {
                    return e = null != e && e, t = null == t ? e : t, this.map(function () {
                        return ve.clone(this, e, t)
                    })
                }, "html": function (e) {
                    return Ie(this, function (e) {
                        var t = this[0] || {},
                            n = 0,
                            r = this.length;
                        if (void 0 === e) return 1 === t.nodeType ? t.innerHTML.replace(tt, "") : void 0;
                        if ("string" == typeof e && !it.test(e) && (ge.htmlSerialize || !nt.test(e)) && (ge.leadingWhitespace || !Xe.test(e)) && !Ve[(Be.exec(e) || ["", ""])[1].toLowerCase()]) {
                            e = ve.htmlPrefilter(e);
                            try {
                                for (; n < r; n++) t = this[n] || {}, 1 === t.nodeType && (ve.cleanData(y(t, !1)), t.innerHTML = e);
                                t = 0
                            } catch (i) {}
                        }
                        t && this.empty().append(e)
                    }, null, e, arguments.length)
                }, "replaceWith": function () {
                    var e = [];
                    return D(this, arguments, function (t) {
                        var n = this.parentNode;
                        ve.inArray(this, e) < 0 && (ve.cleanData(y(this)), n && n.replaceChild(t, this))
                    }, e)
                }
            }), ve.each({
                "appendTo": "append",
                "prependTo": "prepend",
                "insertBefore": "before",
                "insertAfter": "after",
                "replaceAll": "replaceWith"
            }, function (e, t) {
                ve.fn[e] = function (e) {
                    for (var n, r = 0, i = [], o = ve(e), a = o.length - 1; r <= a; r++) n = r === a ? this : this.clone(!0), ve(o[r])[t](n), ce.apply(i, n.get());
                    return this.pushStack(i)
                }
            });
            var ct, dt = {
                    "HTML": "block",
                    "BODY": "block"
                },
                ft = /^margin/,
                pt = new RegExp("^(" + Me + ")(?!px)[a-z%]+$", "i"),
                ht = function (e, t, n, r) {
                    var i, o, a = {};
                    for (o in t) a[o] = e.style[o], e.style[o] = t[o];
                    i = n.apply(e, r || []);
                    for (o in t) e.style[o] = a[o];
                    return i
                },
                gt = se.documentElement;
            ! function () {
                function e() {
                    var e, c, d = se.documentElement;
                    d.appendChild(l), u.style.cssText = "-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;display:block;margin:auto;border:1px;padding:1px;top:1%;width:50%", t = i = s = !1, r = a = !0, n.getComputedStyle && (c = n.getComputedStyle(u), t = "1%" !== (c || {}).top, s = "2px" === (c || {}).marginLeft, i = "4px" === (c || {
                        "width": "4px"
                    }).width, u.style.marginRight = "50%", r = "4px" === (c || {
                        "marginRight": "4px"
                    }).marginRight, e = u.appendChild(se.createElement("div")), e.style.cssText = u.style.cssText = "-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box;display:block;margin:0;border:0;padding:0", e.style.marginRight = e.style.width = "0", u.style.width = "1px", a = !parseFloat((n.getComputedStyle(e) || {}).marginRight), u.removeChild(e)), u.style.display = "none", o = 0 === u.getClientRects().length, o && (u.style.display = "", u.innerHTML = "<table><tr><td></td><td>t</td></tr></table>", u.childNodes[0].style.borderCollapse = "separate", e = u.getElementsByTagName("td"), e[0].style.cssText = "margin:0;border:0;padding:0;display:none", (o = 0 === e[0].offsetHeight) && (e[0].style.display = "", e[1].style.display = "none", o = 0 === e[0].offsetHeight)), d.removeChild(l)
                }
                var t, r, i, o, a, s, l = se.createElement("div"),
                    u = se.createElement("div");
                u.style && (u.style.cssText = "float:left;opacity:.5", ge.opacity = "0.5" === u.style.opacity, ge.cssFloat = !!u.style.cssFloat, u.style.backgroundClip = "content-box", u.cloneNode(!0).style.backgroundClip = "", ge.clearCloneStyle = "content-box" === u.style.backgroundClip, l = se.createElement("div"), l.style.cssText = "border:0;width:8px;height:0;top:0;left:-9999px;padding:0;margin-top:1px;position:absolute", u.innerHTML = "", l.appendChild(u), ge.boxSizing = "" === u.style.boxSizing || "" === u.style.MozBoxSizing || "" === u.style.WebkitBoxSizing, ve.extend(ge, {
                    "reliableHiddenOffsets": function () {
                        return null == t && e(), o
                    }, "boxSizingReliable": function () {
                        return null == t && e(), i
                    }, "pixelMarginRight": function () {
                        return null == t && e(), r
                    }, "pixelPosition": function () {
                        return null == t && e(), t
                    }, "reliableMarginRight": function () {
                        return null == t && e(), a
                    }, "reliableMarginLeft": function () {
                        return null == t && e(), s
                    }
                }))
            }();
            var vt, mt, yt = /^(top|right|bottom|left)$/;
            n.getComputedStyle ? (vt = function (e) {
                var t = e.ownerDocument.defaultView;
                return t && t.opener || (t = n), t.getComputedStyle(e)
            }, mt = function (e, t, n) {
                var r, i, o, a, s = e.style;
                return n = n || vt(e), a = n ? n.getPropertyValue(t) || n[t] : void 0, "" !== a && void 0 !== a || ve.contains(e.ownerDocument, e) || (a = ve.style(e, t)), n && !ge.pixelMarginRight() && pt.test(a) && ft.test(t) && (r = s.width, i = s.minWidth, o = s.maxWidth, s.minWidth = s.maxWidth = s.width = a, a = n.width, s.width = r, s.minWidth = i, s.maxWidth = o), void 0 === a ? a : a + ""
            }) : gt.currentStyle && (vt = function (e) {
                return e.currentStyle
            }, mt = function (e, t, n) {
                var r, i, o, a, s = e.style;
                return n = n || vt(e), a = n ? n[t] : void 0, null == a && s && s[t] && (a = s[t]), pt.test(a) && !yt.test(t) && (r = s.left, i = e.runtimeStyle, o = i && i.left, o && (i.left = e.currentStyle.left), s.left = "fontSize" === t ? "1em" : a, a = s.pixelLeft + "px", s.left = r, o && (i.left = o)), void 0 === a ? a : a + "" || "auto"
            });
            var bt = /alpha\([^)]*\)/i,
                xt = /opacity\s*=\s*([^)]*)/i,
                wt = /^(none|table(?!-c[ea]).+)/,
                Tt = new RegExp("^(" + Me + ")(.*)$", "i"),
                Ct = {
                    "position": "absolute",
                    "visibility": "hidden",
                    "display": "block"
                },
                kt = {
                    "letterSpacing": "0",
                    "fontWeight": "400"
                },
                Et = ["Webkit", "O", "Moz", "ms"],
                _t = se.createElement("div").style;
            ve.extend({
                "cssHooks": {
                    "opacity": {
                        "get": function (e, t) {
                            if (t) {
                                var n = mt(e, "opacity");
                                return "" === n ? "1_冬季电动车儿童护膝保暖骑车加厚摩托车挡风被防水布男女小孩护腿.html" : n
                            }
                        }
                    }
                },
                "cssNumber": {
                    "animationIterationCount": !0,
                    "columnCount": !0,
                    "fillOpacity": !0,
                    "flexGrow": !0,
                    "flexShrink": !0,
                    "fontWeight": !0,
                    "lineHeight": !0,
                    "opacity": !0,
                    "order": !0,
                    "orphans": !0,
                    "widows": !0,
                    "zIndex": !0,
                    "zoom": !0
                },
                "cssProps": {
                    "float": ge.cssFloat ? "cssFloat" : "styleFloat"
                },
                "style": function (e, t, n, r) {
                    if (e && 3 !== e.nodeType && 8 !== e.nodeType && e.style) {
                        var i, o, a, s = ve.camelCase(t),
                            l = e.style;
                        if (t = ve.cssProps[s] || (ve.cssProps[s] = O(s) || s), a = ve.cssHooks[t] || ve.cssHooks[s], void 0 === n) return a && "get" in a && void 0 !== (i = a.get(e, !1, r)) ? i : l[t];
                        if (o = typeof n, "string" === o && (i = Pe.exec(n)) && i[1] && (n = v(e, t, i), o = "number"), null != n && n === n && ("number" === o && (n += i && i[3] || (ve.cssNumber[s] ? "" : "px")), ge.clearCloneStyle || "" !== n || 0 !== t.indexOf("background") || (l[t] = "inherit"), !(a && "set" in a && void 0 === (n = a.set(e, n, r))))) try {
                            l[t] = n
                        } catch (u) {}
                    }
                }, "css": function (e, t, n, r) {
                    var i, o, a, s = ve.camelCase(t);
                    return t = ve.cssProps[s] || (ve.cssProps[s] = O(s) || s), a = ve.cssHooks[t] || ve.cssHooks[s], a && "get" in a && (o = a.get(e, !0, n)), void 0 === o && (o = mt(e, t, r)), "normal" === o && t in kt && (o = kt[t]), "" === n || n ? (i = parseFloat(o), !0 === n || isFinite(i) ? i || 0 : o) : o
                }
            }), ve.each(["height", "width"], function (e, t) {
                ve.cssHooks[t] = {
                    "get": function (e, n, r) {
                        if (n) return wt.test(ve.css(e, "display")) && 0 === e.offsetWidth ? ht(e, Ct, function () {
                            return R(e, t, r)
                        }) : R(e, t, r)
                    }, "set": function (e, n, r) {
                        var i = r && vt(e);
                        return P(e, n, r ? F(e, t, r, ge.boxSizing && "border-box" === ve.css(e, "boxSizing", !1, i), i) : 0)
                    }
                }
            }), ge.opacity || (ve.cssHooks.opacity = {
                "get": function (e, t) {
                    return xt.test((t && e.currentStyle ? e.currentStyle.filter : e.style.filter) || "") ? .01 * parseFloat(RegExp.$1) + "" : t ? "1_冬季电动车儿童护膝保暖骑车加厚摩托车挡风被防水布男女小孩护腿.html" : ""
                }, "set": function (e, t) {
                    var n = e.style,
                        r = e.currentStyle,
                        i = ve.isNumeric(t) ? "alpha(opacity=" + 100 * t + ")" : "",
                        o = r && r.filter || n.filter || "";
                    n.zoom = 1, (t >= 1 || "" === t) && "" === ve.trim(o.replace(bt, "")) && n.removeAttribute && (n.removeAttribute("filter"), "" === t || r && !r.filter) || (n.filter = bt.test(o) ? o.replace(bt, i) : o + " " + i)
                }
            }), ve.cssHooks.marginRight = H(ge.reliableMarginRight, function (e, t) {
                if (t) return ht(e, {
                    "display": "inline-block"
                }, mt, [e, "marginRight"])
            }), ve.cssHooks.marginLeft = H(ge.reliableMarginLeft, function (e, t) {
                if (t) return (parseFloat(mt(e, "marginLeft")) || (ve.contains(e.ownerDocument, e) ? e.getBoundingClientRect().left - ht(e, {
                    "marginLeft": 0
                }, function () {
                    return e.getBoundingClientRect().left
                }) : 0)) + "px"
            }), ve.each({
                "margin": "",
                "padding": "",
                "border": "Width"
            }, function (e, t) {
                ve.cssHooks[e + t] = {
                    "expand": function (n) {
                        for (var r = 0, i = {}, o = "string" == typeof n ? n.split(" ") : [n]; r < 4; r++) i[e + Fe[r] + t] = o[r] || o[r - 2] || o[0];
                        return i
                    }
                }, ft.test(e) || (ve.cssHooks[e + t].set = P)
            }), ve.fn.extend({
                "css": function (e, t) {
                    return Ie(this, function (e, t, n) {
                        var r, i, o = {},
                            a = 0;
                        if (ve.isArray(t)) {
                            for (r = vt(e), i = t.length; a < i; a++) o[t[a]] = ve.css(e, t[a], !1, r);
                            return o
                        }
                        return void 0 !== n ? ve.style(e, t, n) : ve.css(e, t)
                    }, e, t, arguments.length > 1)
                }, "show": function () {
                    return M(this, !0)
                }, "hide": function () {
                    return M(this)
                }, "toggle": function (e) {
                    return "boolean" == typeof e ? e ? this.show() : this.hide() : this.each(function () {
                        Re(this) ? ve(this).show() : ve(this).hide()
                    })
                }
            }), ve.Tween = I, I.prototype = {
                "constructor": I,
                "init": function (e, t, n, r, i, o) {
                    this.elem = e, this.prop = n, this.easing = i || ve.easing._default, this.options = t, this.start = this.now = this.cur(), this.end = r, this.unit = o || (ve.cssNumber[n] ? "" : "px")
                }, "cur": function () {
                    var e = I.propHooks[this.prop];
                    return e && e.get ? e.get(this) : I.propHooks._default.get(this)
                }, "run": function (e) {
                    var t, n = I.propHooks[this.prop];
                    return this.options.duration ? this.pos = t = ve.easing[this.easing](e, this.options.duration * e, 0, 1, this.options.duration) : this.pos = t = e, this.now = (this.end - this.start) * t + this.start, this.options.step && this.options.step.call(this.elem, this.now, this), n && n.set ? n.set(this) : I.propHooks._default.set(this), this
                }
            }, I.prototype.init.prototype = I.prototype, I.propHooks = {
                "_default": {
                    "get": function (e) {
                        var t;
                        return 1 !== e.elem.nodeType || null != e.elem[e.prop] && null == e.elem.style[e.prop] ? e.elem[e.prop] : (t = ve.css(e.elem, e.prop, ""), t && "auto" !== t ? t : 0)
                    }, "set": function (e) {
                        ve.fx.step[e.prop] ? ve.fx.step[e.prop](e) : 1 !== e.elem.nodeType || null == e.elem.style[ve.cssProps[e.prop]] && !ve.cssHooks[e.prop] ? e.elem[e.prop] = e.now : ve.style(e.elem, e.prop, e.now + e.unit)
                    }
                }
            }, I.propHooks.scrollTop = I.propHooks.scrollLeft = {
                "set": function (e) {
                    e.elem.nodeType && e.elem.parentNode && (e.elem[e.prop] = e.now)
                }
            }, ve.easing = {
                "linear": function (e) {
                    return e
                }, "swing": function (e) {
                    return .5 - Math.cos(e * Math.PI) / 2
                }, "_default": "swing"
            }, ve.fx = I.prototype.init, ve.fx.step = {};
            var Nt, St, jt = /^(?:toggle|show|hide)$/,
                At = /queueHooks$/;
            ve.Animation = ve.extend(V, {
                    "tweeners": {
                        "*": [
                            function (e, t) {
                                var n = this.createTween(e, t);
                                return v(n.elem, e, Pe.exec(t), n), n
                            }
                        ]
                    },
                    "tweener": function (e, t) {
                        ve.isFunction(e) ? (t = e, e = ["*"]) : e = e.match(De);
                        for (var n, r = 0, i = e.length; r < i; r++) n = e[r], V.tweeners[n] = V.tweeners[n] || [], V.tweeners[n].unshift(t)
                    }, "prefilters": [X],
                    "prefilter": function (e, t) {
                        t ? V.prefilters.unshift(e) : V.prefilters.push(e)
                    }
                }), ve.speed = function (e, t, n) {
                    var r = e && "object" == typeof e ? ve.extend({}, e) : {
                        "complete": n || !n && t || ve.isFunction(e) && e,
                        "duration": e,
                        "easing": n && t || t && !ve.isFunction(t) && t
                    };
                    return r.duration = ve.fx.off ? 0 : "number" == typeof r.duration ? r.duration : r.duration in ve.fx.speeds ? ve.fx.speeds[r.duration] : ve.fx.speeds._default, null != r.queue && !0 !== r.queue || (r.queue = "fx"), r.old = r.complete, r.complete = function () {
                        ve.isFunction(r.old) && r.old.call(this), r.queue && ve.dequeue(this, r.queue)
                    }, r
                }, ve.fn.extend({
                    "fadeTo": function (e, t, n, r) {
                        return this.filter(Re).css("opacity", 0).show().end().animate({
                            "opacity": t
                        }, e, n, r)
                    }, "animate": function (e, t, n, r) {
                        var i = ve.isEmptyObject(e),
                            o = ve.speed(t, n, r),
                            a = function () {
                                var t = V(this, ve.extend({}, e), o);
                                (i || ve._data(this, "finish")) && t.stop(!0)
                            };
                        return a.finish = a, i || !1 === o.queue ? this.each(a) : this.queue(o.queue, a)
                    }, "stop": function (e, t, n) {
                        var r = function (e) {
                            var t = e.stop;
                            delete e.stop, t(n)
                        };
                        return "string" != typeof e && (n = t, t = e, e = void 0), t && !1 !== e && this.queue(e || "fx", []), this.each(function () {
                            var t = !0,
                                i = null != e && e + "queueHooks",
                                o = ve.timers,
                                a = ve._data(this);
                            if (i) a[i] && a[i].stop && r(a[i]);
                            else
                                for (i in a) a[i] && a[i].stop && At.test(i) && r(a[i]);
                            for (i = o.length; i--;) o[i].elem !== this || null != e && o[i].queue !== e || (o[i].anim.stop(n), t = !1, o.splice(i, 1));
                            !t && n || ve.dequeue(this, e)
                        })
                    }, "finish": function (e) {
                        return !1 !== e && (e = e || "fx"), this.each(function () {
                            var t, n = ve._data(this),
                                r = n[e + "queue"],
                                i = n[e + "queueHooks"],
                                o = ve.timers,
                                a = r ? r.length : 0;
                            for (n.finish = !0, ve.queue(this, e, []), i && i.stop && i.stop.call(this, !0), t = o.length; t--;) o[t].elem === this && o[t].queue === e && (o[t].anim.stop(!0), o.splice(t, 1));
                            for (t = 0; t < a; t++) r[t] && r[t].finish && r[t].finish.call(this);
                            delete n.finish
                        })
                    }
                }), ve.each(["toggle", "show", "hide"], function (e, t) {
                    var n = ve.fn[t];
                    ve.fn[t] = function (e, r, i) {
                        return null == e || "boolean" == typeof e ? n.apply(this, arguments) : this.animate(B(t, !0), e, r, i)
                    }
                }), ve.each({
                    "slideDown": B("show"),
                    "slideUp": B("hide"),
                    "slideToggle": B("toggle"),
                    "fadeIn": {
                        "opacity": "show"
                    },
                    "fadeOut": {
                        "opacity": "hide"
                    },
                    "fadeToggle": {
                        "opacity": "toggle"
                    }
                }, function (e, t) {
                    ve.fn[e] = function (e, n, r) {
                        return this.animate(t, e, n, r)
                    }
                }), ve.timers = [], ve.fx.tick = function () {
                    var e, t = ve.timers,
                        n = 0;
                    for (Nt = ve.now(); n < t.length; n++)(e = t[n])() || t[n] !== e || t.splice(n--, 1);
                    t.length || ve.fx.stop(), Nt = void 0
                }, ve.fx.timer = function (e) {
                    ve.timers.push(e), e() ? ve.fx.start() : ve.timers.pop()
                }, ve.fx.interval = 13, ve.fx.start = function () {
                    St || (St = n.setInterval(ve.fx.tick, ve.fx.interval))
                }, ve.fx.stop = function () {
                    n.clearInterval(St), St = null
                }, ve.fx.speeds = {
                    "slow": 600,
                    "fast": 200,
                    "_default": 400
                }, ve.fn.delay = function (e, t) {
                    return e = ve.fx ? ve.fx.speeds[e] || e : e, t = t || "fx", this.queue(t, function (t, r) {
                        var i = n.setTimeout(t, e);
                        r.stop = function () {
                            n.clearTimeout(i)
                        }
                    })
                },
                function () {
                    var e, t = se.createElement("input"),
                        n = se.createElement("div"),
                        r = se.createElement("select"),
                        i = r.appendChild(se.createElement("option"));
                    n = se.createElement("div"), n.setAttribute("className", "t"), n.innerHTML = "  <link/><table></table><a href='/a'>a</a><input type='checkbox'/>", e = n.getElementsByTagName("a")[0], t.setAttribute("type", "checkbox"), n.appendChild(t), e = n.getElementsByTagName("a")[0], e.style.cssText = "top:1px", ge.getSetAttribute = "t" !== n.className, ge.style = /top/.test(e.getAttribute("style")), ge.hrefNormalized = "/a" === e.getAttribute("href"), ge.checkOn = !!t.value, ge.optSelected = i.selected, ge.enctype = !!se.createElement("form").enctype, r.disabled = !0, ge.optDisabled = !i.disabled, t = se.createElement("input"), t.setAttribute("value", ""), ge.input = "" === t.getAttribute("value"), t.value = "t", t.setAttribute("type", "radio"), ge.radioValue = "t" === t.value
                }();
            var Dt = /\r/g,
                Lt = /[\x20\t\r\n\f]+/g;
            ve.fn.extend({
                "val": function (e) {
                    var t, n, r, i = this[0]; {
                        if (arguments.length) return r = ve.isFunction(e), this.each(function (n) {
                            var i;
                            1 === this.nodeType && (i = r ? e.call(this, n, ve(this).val()) : e, null == i ? i = "" : "number" == typeof i ? i += "" : ve.isArray(i) && (i = ve.map(i, function (e) {
                                return null == e ? "" : e + ""
                            })), (t = ve.valHooks[this.type] || ve.valHooks[this.nodeName.toLowerCase()]) && "set" in t && void 0 !== t.set(this, i, "value") || (this.value = i))
                        });
                        if (i) return (t = ve.valHooks[i.type] || ve.valHooks[i.nodeName.toLowerCase()]) && "get" in t && void 0 !== (n = t.get(i, "value")) ? n : (n = i.value, "string" == typeof n ? n.replace(Dt, "") : null == n ? "" : n)
                    }
                }
            }), ve.extend({
                "valHooks": {
                    "option": {
                        "get": function (e) {
                            var t = ve.find.attr(e, "value");
                            return null != t ? t : ve.trim(ve.text(e)).replace(Lt, " ")
                        }
                    },
                    "select": {
                        "get": function (e) {
                            for (var t, n, r = e.options, i = e.selectedIndex, o = "select-one" === e.type || i < 0, a = o ? null : [], s = o ? i + 1 : r.length, l = i < 0 ? s : o ? i : 0; l < s; l++)
                                if (n = r[l], (n.selected || l === i) && (ge.optDisabled ? !n.disabled : null === n.getAttribute("disabled")) && (!n.parentNode.disabled || !ve.nodeName(n.parentNode, "optgroup"))) {
                                    if (t = ve(n).val(), o) return t;
                                    a.push(t)
                                }
                            return a
                        }, "set": function (e, t) {
                            for (var n, r, i = e.options, o = ve.makeArray(t), a = i.length; a--;)
                                if (r = i[a], ve.inArray(ve.valHooks.option.get(r), o) > -1) try {
                                    r.selected = n = !0
                                } catch (s) {
                                    r.scrollHeight
                                } else r.selected = !1;
                            return n || (e.selectedIndex = -1), i
                        }
                    }
                }
            }), ve.each(["radio", "checkbox"], function () {
                ve.valHooks[this] = {
                    "set": function (e, t) {
                        if (ve.isArray(t)) return e.checked = ve.inArray(ve(e).val(), t) > -1
                    }
                }, ge.checkOn || (ve.valHooks[this].get = function (e) {
                    return null === e.getAttribute("value") ? "on" : e.value
                })
            });
            var $t, qt, Ht = ve.expr.attrHandle,
                Ot = /^(?:checked|selected)$/i,
                Mt = ge.getSetAttribute,
                Pt = ge.input;
            ve.fn.extend({
                "attr": function (e, t) {
                    return Ie(this, ve.attr, e, t, arguments.length > 1)
                }, "removeAttr": function (e) {
                    return this.each(function () {
                        ve.removeAttr(this, e)
                    })
                }
            }), ve.extend({
                "attr": function (e, t, n) {
                    var r, i, o = e.nodeType;
                    if (3 !== o && 8 !== o && 2 !== o) return void 0 === e.getAttribute ? ve.prop(e, t, n) : (1 === o && ve.isXMLDoc(e) || (t = t.toLowerCase(), i = ve.attrHooks[t] || (ve.expr.match.bool.xpathTest(t) ? qt : $t)), void 0 !== n ? null === n ? void ve.removeAttr(e, t) : i && "set" in i && void 0 !== (r = i.set(e, n, t)) ? r : (e.setAttribute(t, n + ""), n) : i && "get" in i && null !== (r = i.get(e, t)) ? r : (r = ve.find.attr(e, t), null == r ? void 0 : r))
                }, "attrHooks": {
                    "type": {
                        "set": function (e, t) {
                            if (!ge.radioValue && "radio" === t && ve.nodeName(e, "input")) {
                                var n = e.value;
                                return e.setAttribute("type", t), n && (e.value = n), t
                            }
                        }
                    }
                }, "removeAttr": function (e, t) {
                    var n, r, i = 0,
                        o = t && t.match(De);
                    if (o && 1 === e.nodeType)
                        for (; n = o[i++];) r = ve.propFix[n] || n, ve.expr.match.bool.xpathTest(n) ? Pt && Mt || !Ot.test(n) ? e[r] = !1 : e[ve.camelCase("default-" + n)] = e[r] = !1 : ve.attr(e, n, ""), e.removeAttribute(Mt ? n : r)
                }
            }), qt = {
                "set": function (e, t, n) {
                    return !1 === t ? ve.removeAttr(e, n) : Pt && Mt || !Ot.test(n) ? e.setAttribute(!Mt && ve.propFix[n] || n, n) : e[ve.camelCase("default-" + n)] = e[n] = !0, n
                }
            }, ve.each(ve.expr.match.bool.source.match(/\w+/g), function (e, t) {
                var n = Ht[t] || ve.find.attr;
                Pt && Mt || !Ot.test(t) ? Ht[t] = function (e, t, r) {
                    var i, o;
                    return r || (o = Ht[t], Ht[t] = i, i = null != n(e, t, r) ? t.toLowerCase() : null, Ht[t] = o), i
                } : Ht[t] = function (e, t, n) {
                    if (!n) return e[ve.camelCase("default-" + t)] ? t.toLowerCase() : null
                }
            }), Pt && Mt || (ve.attrHooks.value = {
                "set": function (e, t, n) {
                    if (!ve.nodeName(e, "input")) return $t && $t.set(e, t, n);
                    e.defaultValue = t
                }
            }), Mt || ($t = {
                "set": function (e, t, n) {
                    var r = e.getAttributeNode(n);
                    if (r || e.setAttributeNode(r = e.ownerDocument.createAttribute(n)), r.value = t += "", "value" === n || t === e.getAttribute(n)) return t
                }
            }, Ht.id = Ht.name = Ht.coords = function (e, t, n) {
                var r;
                if (!n) return (r = e.getAttributeNode(t)) && "" !== r.value ? r.value : null
            }, ve.valHooks.button = {
                "get": function (e, t) {
                    var n = e.getAttributeNode(t);
                    if (n && n.specified) return n.value
                }, "set": $t.set
            }, ve.attrHooks.contenteditable = {
                "set": function (e, t, n) {
                    $t.set(e, "" !== t && t, n)
                }
            }, ve.each(["width", "height"], function (e, t) {
                ve.attrHooks[t] = {
                    "set": function (e, n) {
                        if ("" === n) return e.setAttribute(t, "auto"), n
                    }
                }
            })), ge.style || (ve.attrHooks.style = {
                "get": function (e) {
                    return e.style.cssText || void 0
                }, "set": function (e, t) {
                    return e.style.cssText = t + ""
                }
            });
            var Ft = /^(?:input|select|textarea|button|object)$/i,
                Rt = /^(?:a|area)$/i;
            ve.fn.extend({
                "prop": function (e, t) {
                    return Ie(this, ve.prop, e, t, arguments.length > 1)
                }, "removeProp": function (e) {
                    return e = ve.propFix[e] || e, this.each(function () {
                        try {
                            this[e] = void 0, delete this[e]
                        } catch (t) {}
                    })
                }
            }), ve.extend({
                "prop": function (e, t, n) {
                    var r, i, o = e.nodeType;
                    if (3 !== o && 8 !== o && 2 !== o) return 1 === o && ve.isXMLDoc(e) || (t = ve.propFix[t] || t, i = ve.propHooks[t]), void 0 !== n ? i && "set" in i && void 0 !== (r = i.set(e, n, t)) ? r : e[t] = n : i && "get" in i && null !== (r = i.get(e, t)) ? r : e[t]
                }, "propHooks": {
                    "tabIndex": {
                        "get": function (e) {
                            var t = ve.find.attr(e, "tabindex");
                            return t ? parseInt(t, 10) : Ft.test(e.nodeName) || Rt.test(e.nodeName) && e.href ? 0 : -1
                        }
                    }
                }, "propFix": {
                    "for": "htmlFor",
                    "class": "className"
                }
            }), ge.hrefNormalized || ve.each(["href", "src"], function (e, t) {
                ve.propHooks[t] = {
                    "get": function (e) {
                        return e.getAttribute(t, 4)
                    }
                }
            }), ge.optSelected || (ve.propHooks.selected = {
                "get": function (e) {
                    var t = e.parentNode;
                    return t && (t.selectedIndex, t.parentNode && t.parentNode.selectedIndex), null
                }, "set": function (e) {
                    var t = e.parentNode;
                    t && (t.selectedIndex, t.parentNode && t.parentNode.selectedIndex)
                }
            }), ve.each(["tabIndex", "readOnly", "maxLength", "cellSpacing", "cellPadding", "rowSpan", "colSpan", "useMap", "frameBorder", "contentEditable"], function () {
                ve.propFix[this.toLowerCase()] = this
            }), ge.enctype || (ve.propFix.enctype = "encoding");
            var It = /[\t\r\n\f]/g;
            ve.fn.extend({
                "addClass": function (e) {
                    var t, n, r, i, o, a, s, l = 0;
                    if (ve.isFunction(e)) return this.each(function (t) {
                        ve(this).addClass(e.call(this, t, G(this)))
                    });
                    if ("string" == typeof e && e)
                        for (t = e.match(De) || []; n = this[l++];)
                            if (i = G(n), r = 1 === n.nodeType && (" " + i + " ").replace(It, " ")) {
                                for (a = 0; o = t[a++];) r.indexOf(" " + o + " ") < 0 && (r += o + " ");
                                s = ve.trim(r), i !== s && ve.attr(n, "class", s)
                            }
                    return this
                }, "removeClass": function (e) {
                    var t, n, r, i, o, a, s, l = 0;
                    if (ve.isFunction(e)) return this.each(function (t) {
                        ve(this).removeClass(e.call(this, t, G(this)))
                    });
                    if (!arguments.length) return this.attr("class", "");
                    if ("string" == typeof e && e)
                        for (t = e.match(De) || []; n = this[l++];)
                            if (i = G(n), r = 1 === n.nodeType && (" " + i + " ").replace(It, " ")) {
                                for (a = 0; o = t[a++];)
                                    for (; r.indexOf(" " + o + " ") > -1;) r = r.replace(" " + o + " ", " ");
                                s = ve.trim(r), i !== s && ve.attr(n, "class", s)
                            }
                    return this
                }, "toggleClass": function (e, t) {
                    var n = typeof e;
                    return "boolean" == typeof t && "string" === n ? t ? this.addClass(e) : this.removeClass(e) : ve.isFunction(e) ? this.each(function (n) {
                        ve(this).toggleClass(e.call(this, n, G(this), t), t)
                    }) : this.each(function () {
                        var t, r, i, o;
                        if ("string" === n)
                            for (r = 0, i = ve(this), o = e.match(De) || []; t = o[r++];) i.hasClass(t) ? i.removeClass(t) : i.addClass(t);
                        else void 0 !== e && "boolean" !== n || (t = G(this), t && ve._data(this, "__className__", t), ve.attr(this, "class", t || !1 === e ? "" : ve._data(this, "__className__") || ""))
                    })
                }, "hasClass": function (e) {
                    var t, n, r = 0;
                    for (t = " " + e + " "; n = this[r++];)
                        if (1 === n.nodeType && (" " + G(n) + " ").replace(It, " ").indexOf(t) > -1) return !0;
                    return !1
                }
            }), ve.each("blur focus focusin focusout load resize scroll unload click dblclick mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave change select submit keydown keypress keyup error contextmenu".split(" "), function (e, t) {
                ve.fn[t] = function (e, n) {
                    return arguments.length > 0 ? this.on(t, null, e, n) : this.trigger(t)
                }
            }), ve.fn.extend({
                "hover": function (e, t) {
                    return this.mouseenter(e).mouseleave(t || e)
                }
            });
            var Wt = n.location,
                Bt = ve.now(),
                zt = /\?/,
                Xt = /(,)|(\[|{)|(}|])|"(?:[^"\\\r\n]|\\["\\\/bfnrt]|\\u[\da-fA-F]{4})*"\s*:?|true|false|null|-?(?!0\d)\d+(?:\.\d+|)(?:[eE][+-]?\d+|)/g;
            ve.parseJSON = function (e) {
                if (n.JSON && n.JSON.parse) return n.JSON.parse(e + "");
                var t, r = null,
                    i = ve.trim(e + "");
                return i && !ve.trim(i.replace(Xt, function (e, n, i, o) {
                    return t && n && (r = 0), 0 === r ? e : (t = i || n, r += !o - !i, "")
                })) ? Function("return " + i)() : ve.error("Invalid JSON: " + e)
            }, ve.parseXML = function (e) {
                var t, r;
                if (!e || "string" != typeof e) return null;
                try {
                    n.DOMParser ? (r = new n.DOMParser, t = r.parseFromString(e, "text/xml")) : (t = new n.ActiveXObject("Microsoft.XMLDOM"), t.async = "false", t.loadXML(e))
                } catch (i) {
                    t = void 0
                }
                return t && t.documentElement && !t.getElementsByTagName("parsererror").length || ve.error("Invalid XML: " + e), t
            };
            var Ut = /#.*$/,
                Vt = /([?&])_=[^&]*/,
                Gt = /^(.*?):[ \t]*([^\r\n]*)\r?$/gm,
                Yt = /^(?:about|app|app-storage|.+-extension|file|res|widget):$/,
                Jt = /^(?:GET|HEAD)$/,
                Kt = /^\/\//,
                Qt = /^([\w.+-]+:)(?:\/\/(?:[^\/?#]*@|)([^\/?#:]*)(?::(\d+)|)|)/,
                Zt = {},
                en = {},
                tn = "*/".concat("*"),
                nn = Wt.href,
                rn = Qt.exec(nn.toLowerCase()) || [];
            ve.extend({
                "active": 0,
                "lastModified": {},
                "etag": {},
                "ajaxSettings": {
                    "url": nn,
                    "type": "GET",
                    "isLocal": Yt.test(rn[1]),
                    "global": !0,
                    "processData": !0,
                    "async": !0,
                    "contentType": "application/x-www-form-urlencoded; charset=UTF-8",
                    "accepts": {
                        "*": tn,
                        "text": "text/plain",
                        "html": "text/html",
                        "xml": "application/xml, text/xml",
                        "json": "application/json, text/javascript"
                    },
                    "contents": {
                        "xml": /\bxml\b/,
                        "html": /\bhtml/,
                        "json": /\bjson\b/
                    },
                    "responseFields": {
                        "xml": "responseXML",
                        "text": "responseText",
                        "json": "responseJSON"
                    },
                    "converters": {
                        "* text": String,
                        "text html": !0,
                        "text json": ve.parseJSON,
                        "text xml": ve.parseXML
                    },
                    "flatOptions": {
                        "url": !0,
                        "context": !0
                    }
                },
                "ajaxSetup": function (e, t) {
                    return t ? K(K(e, ve.ajaxSettings), t) : K(ve.ajaxSettings, e)
                }, "ajaxPrefilter": Y(Zt),
                "ajaxTransport": Y(en),
                "ajax": function (e, t) {
                    function r(e, t, r, i) {
                        var o, d, y, b, w, C = t;
                        2 !== x && (x = 2, l && n.clearTimeout(l), c = void 0, s = i || "", T.readyState = e > 0 ? 4 : 0, o = e >= 200 && e < 300 || 304 === e, r && (b = Q(f, T, r)), b = Z(f, b, T, o), o ? (f.ifModified && (w = T.getResponseHeader("Last-Modified"), w && (ve.lastModified[a] = w), (w = T.getResponseHeader("etag")) && (ve.etag[a] = w)), 204 === e || "HEAD" === f.type ? C = "nocontent" : 304 === e ? C = "notmodified" : (C = b.state, d = b.data, y = b.error, o = !y)) : (y = C, !e && C || (C = "error", e < 0 && (e = 0))), T.status = e, T.statusText = (t || C) + "", o ? g.resolveWith(p, [d, C, T]) : g.rejectWith(p, [T, C, y]), T.statusCode(m), m = void 0, u && h.trigger(o ? "ajaxSuccess" : "ajaxError", [T, f, o ? d : y]), v.fireWith(p, [T, C]), u && (h.trigger("ajaxComplete", [T, f]), --ve.active || ve.event.trigger("ajaxStop")))
                    }
                    "object" == typeof e && (t = e, e = void 0), t = t || {};
                    var i, o, a, s, l, u, c, d, f = ve.ajaxSetup({}, t),
                        p = f.context || f,
                        h = f.context && (p.nodeType || p.jquery) ? ve(p) : ve.event,
                        g = ve.Deferred(),
                        v = ve.Callbacks("once memory"),
                        m = f.statusCode || {},
                        y = {},
                        b = {},
                        x = 0,
                        w = "canceled",
                        T = {
                            "readyState": 0,
                            "getResponseHeader": function (e) {
                                var t;
                                if (2 === x) {
                                    if (!d)
                                        for (d = {}; t = Gt.exec(s);) d[t[1].toLowerCase()] = t[2];
                                    t = d[e.toLowerCase()]
                                }
                                return null == t ? null : t
                            }, "getAllResponseHeaders": function () {
                                return 2 === x ? s : null
                            }, "setRequestHeader": function (e, t) {
                                var n = e.toLowerCase();
                                return x || (e = b[n] = b[n] || e, y[e] = t), this
                            }, "overrideMimeType": function (e) {
                                return x || (f.mimeType = e), this
                            }, "statusCode": function (e) {
                                var t;
                                if (e)
                                    if (x < 2)
                                        for (t in e) m[t] = [m[t], e[t]];
                                    else T.always(e[T.status]);
                                return this
                            }, "abort": function (e) {
                                var t = e || w;
                                return c && c.abort(t), r(0, t), this
                            }
                        };
                    if (g.promise(T).complete = v.add, T.success = T.done, T.error = T.fail, f.url = ((e || f.url || nn) + "").replace(Ut, "").replace(Kt, rn[1] + "//"), f.type = t.method || t.type || f.method || f.type, f.dataTypes = ve.trim(f.dataType || "*").toLowerCase().match(De) || [""], null == f.crossDomain && (i = Qt.exec(f.url.toLowerCase()), f.crossDomain = !(!i || i[1] === rn[1] && i[2] === rn[2] && (i[3] || ("http:" === i[1] ? "80" : "443")) === (rn[3] || ("http:" === rn[1] ? "80" : "443")))), f.data && f.processData && "string" != typeof f.data && (f.data = ve.param(f.data, f.traditional)), J(Zt, f, t, T), 2 === x) return T;
                    u = ve.event && f.global, u && 0 == ve.active++ && ve.event.trigger("ajaxStart"), f.type = f.type.toUpperCase(), f.hasContent = !Jt.test(f.type), a = f.url, f.hasContent || (f.data && (a = f.url += (zt.test(a) ? "&" : "?") + f.data, delete f.data), !1 === f.cache && (f.url = Vt.test(a) ? a.replace(Vt, "$1_=" + Bt++) : a + (zt.test(a) ? "&" : "?") + "_=" + Bt++)), f.ifModified && (ve.lastModified[a] && T.setRequestHeader("If-Modified-Since", ve.lastModified[a]), ve.etag[a] && T.setRequestHeader("If-None-Match", ve.etag[a])), (f.data && f.hasContent && !1 !== f.contentType || t.contentType) && T.setRequestHeader("Content-Type", f.contentType), T.setRequestHeader("Accept", f.dataTypes[0] && f.accepts[f.dataTypes[0]] ? f.accepts[f.dataTypes[0]] + ("*" !== f.dataTypes[0] ? ", " + tn + "; q=0.01" : "") : f.accepts["*"]);
                    for (o in f.headers) T.setRequestHeader(o, f.headers[o]);
                    if (f.beforeSend && (!1 === f.beforeSend.call(p, T, f) || 2 === x)) return T.abort();
                    w = "abort";
                    for (o in {
                        "success": 1,
                        "error": 1,
                        "complete": 1
                    }) T[o](f[o]);
                    if (c = J(en, f, t, T)) {
                        if (T.readyState = 1, u && h.trigger("ajaxSend", [T, f]), 2 === x) return T;
                        f.async && f.timeout > 0 && (l = n.setTimeout(function () {
                            T.abort("timeout")
                        }, f.timeout));
                        try {
                            x = 1, c.send(y, r)
                        } catch (C) {
                            if (!(x < 2)) throw C;
                            r(-1, C)
                        }
                    } else r(-1, "No Transport");
                    return T
                }, "getJSON": function (e, t, n) {
                    return ve.get(e, t, n, "json")
                }, "getScript": function (e, t) {
                    return ve.get(e, void 0, t, "script")
                }
            }), ve.each(["get", "post"], function (e, t) {
                ve[t] = function (e, n, r, i) {
                    return ve.isFunction(n) && (i = i || r, r = n, n = void 0), ve.ajax(ve.extend({
                        "url": e,
                        "type": t,
                        "dataType": i,
                        "data": n,
                        "success": r
                    }, ve.isPlainObject(e) && e))
                }
            }), ve._evalUrl = function (e) {
                return ve.ajax({
                    "url": e,
                    "type": "GET",
                    "dataType": "script",
                    "cache": !0,
                    "async": !1,
                    "global": !1,
                    "throws": !0
                })
            }, ve.fn.extend({
                "wrapAll": function (e) {
                    if (ve.isFunction(e)) return this.each(function (t) {
                        ve(this).wrapAll(e.call(this, t))
                    });
                    if (this[0]) {
                        var t = ve(e, this[0].ownerDocument).eq(0).clone(!0);
                        this[0].parentNode && t.insertBefore(this[0]), t.map(function () {
                            for (var e = this; e.firstChild && 1 === e.firstChild.nodeType;) e = e.firstChild;
                            return e
                        }).append(this)
                    }
                    return this
                }, "wrapInner": function (e) {
                    return ve.isFunction(e) ? this.each(function (t) {
                        ve(this).wrapInner(e.call(this, t))
                    }) : this.each(function () {
                        var t = ve(this),
                            n = t.contents();
                        n.length ? n.wrapAll(e) : t.append(e)
                    })
                }, "wrap": function (e) {
                    var t = ve.isFunction(e);
                    return this.each(function (n) {
                        ve(this).wrapAll(t ? e.call(this, n) : e)
                    })
                }, "unwrap": function () {
                    return this.parent().each(function () {
                        ve.nodeName(this, "body") || ve(this).replaceWith(this.childNodes)
                    }).end()
                }
            }), ve.expr.filters.hidden = function (e) {
                return ge.reliableHiddenOffsets() ? e.offsetWidth <= 0 && e.offsetHeight <= 0 && !e.getClientRects().length : te(e)
            }, ve.expr.filters.visible = function (e) {
                return !ve.expr.filters.hidden(e)
            };
            var on = /%20/g,
                an = /\[\]$/,
                sn = /\r?\n/g,
                ln = /^(?:submit|button|image|reset|file)$/i,
                un = /^(?:input|select|textarea|keygen)/i;
            ve.param = function (e, t) {
                var n, r = [],
                    i = function (e, t) {
                        t = ve.isFunction(t) ? t() : null == t ? "" : t, r[r.length] = encodeURIComponent(e) + "=" + encodeURIComponent(t)
                    };
                if (void 0 === t && (t = ve.ajaxSettings && ve.ajaxSettings.traditional), ve.isArray(e) || e.jquery && !ve.isPlainObject(e)) ve.each(e, function () {
                    i(this.name, this.value)
                });
                else
                    for (n in e) ne(n, e[n], t, i);
                return r.join("&").replace(on, "+")
            }, ve.fn.extend({
                "serialize": function () {
                    return ve.param(this.serializeArray())
                }, "serializeArray": function () {
                    return this.map(function () {
                        var e = ve.prop(this, "elements");
                        return e ? ve.makeArray(e) : this
                    }).filter(function () {
                        var e = this.type;
                        return this.name && !ve(this).is(":disabled") && un.test(this.nodeName) && !ln.test(e) && (this.checked || !We.test(e))
                    }).map(function (e, t) {
                        var n = ve(this).val();
                        return null == n ? null : ve.isArray(n) ? ve.map(n, function (e) {
                            return {
                                "name": t.name,
                                "value": e.replace(sn, "\r\n")
                            }
                        }) : {
                            "name": t.name,
                            "value": n.replace(sn, "\r\n")
                        }
                    }).get()
                }
            }), ve.ajaxSettings.xhr = void 0 !== n.ActiveXObject ? function () {
                return this.isLocal ? ie() : se.documentMode > 8 ? re() : /^(get|post|head|put|delete|options)$/i.test(this.type) && re() || ie()
            } : re;
            var cn = 0,
                dn = {},
                fn = ve.ajaxSettings.xhr();
            n.attachEvent && n.attachEvent("onunload", function () {
                for (var e in dn) dn[e](void 0, !0)
            }), ge.cors = !!fn && "withCredentials" in fn, fn = ge.ajax = !!fn, fn && ve.ajaxTransport(function (e) {
                if (!e.crossDomain || ge.cors) {
                    var t;
                    return {
                        "send": function (r, i) {
                            var o, a = e.xhr(),
                                s = ++cn;
                            if (a.open(e.type, e.url, e.async, e.username, e.password), e.xhrFields)
                                for (o in e.xhrFields) a[o] = e.xhrFields[o];
                            e.mimeType && a.overrideMimeType && a.overrideMimeType(e.mimeType), e.crossDomain || r["X-Requested-With"] || (r["X-Requested-With"] = "XMLHttpRequest");
                            for (o in r) void 0 !== r[o] && a.setRequestHeader(o, r[o] + "");
                            a.send(e.hasContent && e.data || null), t = function (n, r) {
                                var o, l, u;
                                if (t && (r || 4 === a.readyState))
                                    if (delete dn[s], t = void 0, a.onreadystatechange = ve.noop, r) 4 !== a.readyState && a.abort();
                                    else {
                                        u = {}, o = a.status, "string" == typeof a.responseText && (u.text = a.responseText);
                                        try {
                                            l = a.statusText
                                        } catch (c) {
                                            l = ""
                                        }
                                        o || !e.isLocal || e.crossDomain ? 1223 === o && (o = 204) : o = u.text ? 200 : 404
                                    }
                                u && i(o, l, u, a.getAllResponseHeaders())
                            }, e.async ? 4 === a.readyState ? n.setTimeout(t) : a.onreadystatechange = dn[s] = t : t()
                        }, "abort": function () {
                            t && t(void 0, !0)
                        }
                    }
                }
            }), ve.ajaxSetup({
                "accepts": {
                    "script": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript"
                },
                "contents": {
                    "script": /\b(?:java|ecma)script\b/
                },
                "converters": {
                    "text script": function (e) {
                        return ve.globalEval(e), e
                    }
                }
            }), ve.ajaxPrefilter("script", function (e) {
                void 0 === e.cache && (e.cache = !1), e.crossDomain && (e.type = "GET", e.global = !1)
            }), ve.ajaxTransport("script", function (e) {
                if (e.crossDomain) {
                    var t, n = se.head || ve("head")[0] || se.documentElement;
                    return {
                        "send": function (r, i) {
                            t = se.createElement("script"), t.async = !0, e.scriptCharset && (t.charset = e.scriptCharset), t.src = e.url, t.onload = t.onreadystatechange = function (e, n) {
                                (n || !t.readyState || /loaded|complete/.test(t.readyState)) && (t.onload = t.onreadystatechange = null, t.parentNode && t.parentNode.removeChild(t), t = null, n || i(200, "success"))
                            }, n.insertBefore(t, n.firstChild)
                        }, "abort": function () {
                            t && t.onload(void 0, !0)
                        }
                    }
                }
            });
            var pn = [],
                hn = /(=)\?(?=&|$)|\?\?/;
            ve.ajaxSetup({
                "jsonp": "callback",
                "jsonpCallback": function () {
                    var e = pn.pop() || ve.expando + "_" + Bt++;
                    return this[e] = !0, e
                }
            }), ve.ajaxPrefilter("json jsonp", function (e, t, r) {
                var i, o, a, s = !1 !== e.jsonp && (hn.test(e.url) ? "url" : "string" == typeof e.data && 0 === (e.contentType || "").indexOf("application/x-www-form-urlencoded") && hn.test(e.data) && "data");
                if (s || "jsonp" === e.dataTypes[0]) return i = e.jsonpCallback = ve.isFunction(e.jsonpCallback) ? e.jsonpCallback() : e.jsonpCallback, s ? e[s] = e[s].replace(hn, "$1" + i) : !1 !== e.jsonp && (e.url += (zt.test(e.url) ? "&" : "?") + e.jsonp + "=" + i), e.converters["script json"] = function () {
                    return a || ve.error(i + " was not called"), a[0]
                }, e.dataTypes[0] = "json", o = n[i], n[i] = function () {
                    a = arguments
                }, r.always(function () {
                    void 0 === o ? ve(n).removeProp(i) : n[i] = o, e[i] && (e.jsonpCallback = t.jsonpCallback, pn.push(i)), a && ve.isFunction(o) && o(a[0]), a = o = void 0
                }), "script"
            }), ve.parseHTML = function (e, t, n) {
                if (!e || "string" != typeof e) return null;
                "boolean" == typeof t && (n = t, t = !1), t = t || se;
                var r = Ee.exec(e),
                    i = !n && [];
                return r ? [t.createElement(r[1])] : (r = w([e], t, i), i && i.length && ve(i).remove(), ve.merge([], r.childNodes))
            };
            var gn = ve.fn.load;
            ve.fn.load = function (e, t, n) {
                if ("string" != typeof e && gn) return gn.apply(this, arguments);
                var r, i, o, a = this,
                    s = e.indexOf(" ");
                return s > -1 && (r = ve.trim(e.slice(s, e.length)), e = e.slice(0, s)), ve.isFunction(t) ? (n = t, t = void 0) : t && "object" == typeof t && (i = "POST"), a.length > 0 && ve.ajax({
                    "url": e,
                    "type": i || "GET",
                    "dataType": "html",
                    "data": t
                }).done(function (e) {
                    o = arguments, a.html(r ? ve("<div>").append(ve.parseHTML(e)).find(r) : e)
                }).always(n && function (e, t) {
                    a.each(function () {
                        n.apply(this, o || [e.responseText, t, e])
                    })
                }), this
            }, ve.each(["ajaxStart", "ajaxStop", "ajaxComplete", "ajaxError", "ajaxSuccess", "ajaxSend"], function (e, t) {
                ve.fn[t] = function (e) {
                    return this.on(t, e)
                }
            }), ve.expr.filters.animated = function (e) {
                return ve.grep(ve.timers, function (t) {
                    return e === t.elem
                }).length
            }, ve.offset = {
                "setOffset": function (e, t, n) {
                    var r, i, o, a, s, l, u, c = ve.css(e, "position"),
                        d = ve(e),
                        f = {};
                    "static" === c && (e.style.position = "relative"), s = d.offset(), o = ve.css(e, "top"), l = ve.css(e, "left"), u = ("absolute" === c || "fixed" === c) && ve.inArray("auto", [o, l]) > -1, u ? (r = d.position(), a = r.top, i = r.left) : (a = parseFloat(o) || 0, i = parseFloat(l) || 0), ve.isFunction(t) && (t = t.call(e, n, ve.extend({}, s))), null != t.top && (f.top = t.top - s.top + a), null != t.left && (f.left = t.left - s.left + i), "using" in t ? t.using.call(e, f) : d.css(f)
                }
            }, ve.fn.extend({
                "offset": function (e) {
                    if (arguments.length) return void 0 === e ? this : this.each(function (t) {
                        ve.offset.setOffset(this, e, t)
                    });
                    var t, n, r = {
                            "top": 0,
                            "left": 0
                        },
                        i = this[0],
                        o = i && i.ownerDocument;
                    if (o) return t = o.documentElement, ve.contains(t, i) ? (void 0 !== i.getBoundingClientRect && (r = i.getBoundingClientRect()), n = oe(o), {
                        "top": r.top + (n.pageYOffset || t.scrollTop) - (t.clientTop || 0),
                        "left": r.left + (n.pageXOffset || t.scrollLeft) - (t.clientLeft || 0)
                    }) : r
                }, "position": function () {
                    if (this[0]) {
                        var e, t, n = {
                                "top": 0,
                                "left": 0
                            },
                            r = this[0];
                        return "fixed" === ve.css(r, "position") ? t = r.getBoundingClientRect() : (e = this.offsetParent(), t = this.offset(), ve.nodeName(e[0], "html") || (n = e.offset()), n.top += ve.css(e[0], "borderTopWidth", !0), n.left += ve.css(e[0], "borderLeftWidth", !0)), {
                            "top": t.top - n.top - ve.css(r, "marginTop", !0),
                            "left": t.left - n.left - ve.css(r, "marginLeft", !0)
                        }
                    }
                }, "offsetParent": function () {
                    return this.map(function () {
                        for (var e = this.offsetParent; e && !ve.nodeName(e, "html") && "static" === ve.css(e, "position");) e = e.offsetParent;
                        return e || gt
                    })
                }
            }), ve.each({
                "scrollLeft": "pageXOffset",
                "scrollTop": "pageYOffset"
            }, function (e, t) {
                var n = /Y/.test(t);
                ve.fn[e] = function (r) {
                    return Ie(this, function (e, r, i) {
                        var o = oe(e);
                        if (void 0 === i) return o ? t in o ? o[t] : o.document.documentElement[r] : e[r];
                        o ? o.scrollTo(n ? ve(o).scrollLeft() : i, n ? i : ve(o).scrollTop()) : e[r] = i
                    }, e, r, arguments.length, null)
                }
            }), ve.each(["top", "left"], function (e, t) {
                ve.cssHooks[t] = H(ge.pixelPosition, function (e, n) {
                    if (n) return n = mt(e, t), pt.test(n) ? ve(e).position()[t] + "px" : n
                })
            }), ve.each({
                "Height": "height",
                "Width": "width"
            }, function (e, t) {
                ve.each({
                    "padding": "inner" + e,
                    "content": t,
                    "": "outer" + e
                }, function (n, r) {
                    ve.fn[r] = function (r, i) {
                        var o = arguments.length && (n || "boolean" != typeof r),
                            a = n || (!0 === r || !0 === i ? "margin" : "border");
                        return Ie(this, function (t, n, r) {
                            var i;
                            return ve.isWindow(t) ? t.document.documentElement["client" + e] : 9 === t.nodeType ? (i = t.documentElement, Math.max(t.body["scroll" + e], i["scroll" + e], t.body["offset" + e], i["offset" + e], i["client" + e])) : void 0 === r ? ve.css(t, n, a) : ve.style(t, n, r, a)
                        }, t, o ? r : void 0, o, null)
                    }
                })
            }), ve.fn.extend({
                "bind": function (e, t, n) {
                    return this.on(e, null, t, n)
                }, "unbind": function (e, t) {
                    return this.off(e, null, t)
                }, "delegate": function (e, t, n, r) {
                    return this.on(t, e, n, r)
                }, "undelegate": function (e, t, n) {
                    return 1 === arguments.length ? this.off(e, "**") : this.off(t, e || "**", n)
                }
            }), ve.fn.size = function () {
                return this.length
            }, ve.fn.andSelf = ve.fn.addBack, r = [], void 0 !== (i = function () {
                return ve
            }.apply(t, r)) && (e.exports = i);
            var vn = n.jQuery,
                mn = n.$;
            return ve.noConflict = function (e) {
                return n.$ === ve && (n.$ = mn), e && n.jQuery === ve && (n.jQuery = vn), ve
            }, o || (n.jQuery = n.$ = ve), ve
        })
    }, "./resources/assets/js/account/base.js": function (e, t) {
        var n = {
            "ajax": function (e) {
                var t = e.success;
                e.data = e.data || {}, e.data["_t"] = (new Date).getTime(), e.success = function (e, n, r) {
                    if (100 == e.code) return void(document.location.href = "/login?url=" + encodeURIComponent(document.location.href));
                    t(e, n, r)
                }, $.ajax(e)
            }, "cookie": {
                "get": function (e) {
                    var t = (e = RegExp("(^| )" + e + "=([^;]*)(;|$)").exec(document.cookie)) ? e[2] : null;
                    return decodeURIComponent(t)
                }, "set": function (e, t, n) {
                    var r;
                    n.expires && (r = new Date, r.setTime(r.getTime() + n.s)), document.cookie = e + "=" + t + (n.domain ? "; domain=" + n.domain : "") + (n.path ? "; path=" + n.path : "") + (r ? "; expires=" + r.toGMTString() : "") + (n.wb ? "; secure" : "")
                }
            }, "account": {
                "phone": {
                    "get": function () {
                        var e = $("#areacode"),
                            t = $("#phone");
                        return e = e.length && "+86" != e.val() ? e.val().replace("+", "") + " " : "", {
                            "self": t[0],
                            "value": e + t.val()
                        }
                    }
                },
                "email": {
                    "get": function () {
                        var e = $("#email");
                        return {
                            "self": e[0],
                            "value": e.val()
                        }
                    }
                }
            }, "regular": {
                "phone": /(^1(\d{10})$)|(^[\d]{1,4} [\d]{7,11}$)/,
                "username": /^(?![0-9]{11}$)[A-Za-z\d_\u4e00-\u9fa5]{4,16}$/,
                "pwd": /^[A-Za-z0-9~!@#$%\^&\*\(\)_\+\[\]\\{\}\|;':",\.\/<>\?]{6,16}$/,
                "email": /^\w+([-+.]\w+)*@\w+([-.]\w+)*.\w+([-.]\w+)*$/,
                "code": /^(\d{6})$/,
                "username_phone": /^(([a-zA-Z\d_\u4e00-\u9fa5]{2,16})|(1(\d{10})))$/,
                "login_user": /^[^\n]{2,32}$/,
                "login_pwd": /^[^\n]{6,32}$/
            }, "prompts": {
                "phone": "手机号格错误，请重新输入",
                "user": "用户名不正确，请重新输入[字母,数字,汉字,下划线 4-16字符。不能为11位纯数字]",
                "pwd": "密码格式错误，请重新输入[字母,数字,符号 6-16字节]",
                "email": "邮箱格式错误，请重新输入",
                "code": "验证码错误，请重新输入",
                "confirm_pwd": "两次密码不同，请重新输入",
                "gee": "验证出错，请重新验证",
                "username_phone": "用户名或手机号格式不正确，请重新输入",
                "login_user": "用户名不正确，请重新输入[字母,数字,汉字,下划线 2-32字符]",
                "login_pwd": "密码格式错误，请重新输入[字母,数字,符号 6-32字节]",
                "required": "不能为空"
            }, "validate": function (e, t, n, i) {
                return !0 === t || !1 !== t && t.xpathTest(e) ? (r(i, !0, n), !0) : (r(i, !1, n), !1)
            }, "validateForm": function (e) {
                this.valid = function (t) {
                    var n = !0,
                        r = {};
                    if (t)
                        for (var i in t) {
                            var o = t[i];
                            r[o] = e[o]
                        } else r = e;
                    for (var a in r) {
                        var s = !1,
                            l = e[a];
                        !1 === l.valid ? s = !1 : void 0 === l.valid ? ($("#" + a).trigger("valid"), s = l.valid) : s = !0 === l.valid, n = n && s
                    }
                    return n
                };
                for (var t in e)! function (t) {
                    var i = e[t];
                    $("#" + t).on("blur valid", function (e) {
                        var t = $(this);
                        if (i.required && "" === t.val()) return r(this, !1, i.requiredMsg ? i.requiredMsg : n.prompts.required), i.valid = !1, !1;
                        if ("function" == typeof i.validate.check) return i.valid = i.validate.check(i), n.validate(null, i.valid, i.validate.msg, this), i.valid;
                        var o = n.validate(t.val(), i.validate.preg, i.validate.msg, this);
                        return i.valid = o, o
                    })
                }(t);
                return this
            }, "alert": function (e, t) {
                t = t || 1500, $("#msg_alert").length ? $("#msg_alert").show(160).text(e) : $("body").append('<div class="msg-alert" id="msg_alert">' + e + "</div>"), $("#msg_alert").show(160), setTimeout(function () {
                    $("#msg_alert").hide(160), setTimeout(function () {
                        $("#msg_alert").remove()
                    }, 160)
                }, t)
            }, "submit": function (e, t, r, i, o) {
                n.ajax({
                    "url": t,
                    "type": o || "post",
                    "dataType": "json",
                    "data": e,
                    "success": function (e) {
                        "function" == typeof r && r(e)
                    }, "error": function (e) {
                        "function" == typeof i && i(e)
                    }
                })
            }, "adjustScroll": function () {
                var e, t;
                t = setInterval(function () {
                    e = document.documentElement.scrollTop || document.body.scrollTop, e -= 1, window.scrollTo(0, e), e += 1, window.scrollTo(0, e), clearInterval(t)
                }, 1)
            }, "browser": {
                "versions": function () {
                    var e = navigator.userAgent;
                    navigator.appVersion;
                    return {
                        "trident": e.indexOf("Trident") > -1,
                        "presto": e.indexOf("Presto") > -1,
                        "webKit": e.indexOf("AppleWebKit") > -1,
                        "gecko": e.indexOf("Gecko") > -1 && -1 == e.indexOf("KHTML"),
                        "mobile": !!e.match(/AppleWebKit.*Mobile.*/) || !!e.match(/AppleWebKit/),
                        "ios": !!e.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/),
                        "android": e.indexOf("Android") > -1 || e.indexOf("Linux") > -1,
                        "iPhone": e.indexOf("iPhone") > -1,
                        "iPad": e.indexOf("iPad") > -1,
                        "webApp": -1 == e.indexOf("Safari"),
                        "winphone": e.indexOf("Windows Phone") > -1
                    }
                }()
            }, "runParty": {
                "party": "",
                "backWxParty": function (e) {
                    var t = n.cookie.get("__backurl");
                    if (t) {
                        wx.miniProgram.postMessage({
                            "data": {
                                "status": 1,
                                "user": e
                            }
                        });
                        switch (t.split("?")[0].toLowerCase()) {
                        case "/pages/stack/list":
                        case "/pages/index/index":
                        case "/pages/ucenter/index":
                        case "/pages/ustack/write":
                            wx.miniProgram.switchTab({
                                "url": t
                            });
                            break;
                        default:
                            wx.miniProgram.redirectTo({
                                "url": t
                            })
                        }
                    } else alert("登录页面已过期，请返回重新登录")
                }
            }
        };
        $(window).load(function () {
            try {
                wx.miniProgram.getEnv(function (e) {
                    e.miniprogram ? (n.runParty.party = "wx", wx.miniProgram.postMessage({
                        "data": {
                            "status": 1,
                            "user": []
                        }
                    })) : n.runParty.party = ""
                })
            } catch (e) {}
        }), $(function () {
            /Mac OS X/.test(navigator.userAgent) && $("body").on("blur", "input[type=text],input[type=password],textarea", function () {
                n.adjustScroll()
            })
        });
        var r = function (e, t, n) {
            var r = $(e),
                i = r.parents(".inp_box"),
                o = $("[for=" + r.attr("id") + "]");
            t ? (i.removeClass("inp_box_error"), o.length && o.hide()) : (i.addClass("inp_box_error"), o.length && o.html(n).show() || i.after('<div class="error">' + n + "</div>"))
        };
        e.exports = {
            "util": n
        }
    }, "./resources/assets/js/account/captcha.js": function (e, t, n) {
        n("./resources/assets/js/components/gt.js");
        var r = n("./resources/assets/js/account/base.js"),
            i = r.util,
            o = function (e) {
                this.captchatype = e, this._send = function (t, n, r) {
                    var o = "";
                    switch (e) {
                    case 1:
                        o = "/captcha/phone";
                        break;
                    case 2:
                        o = "/captcha/email"
                    }
                    i.submit(t, o, function (e) {
                        n(e)
                    }, r)
                }
            },
            a = function () {
                o.call(this, 1), this.send = function (e, t, n) {
                    this._send(e, t, n)
                }
            },
            s = function () {
                o.call(this, 2), this.send = function (e, t, n) {
                    this._send(e, t, n)
                }
            },
            l = {
                "init": function (e) {
                    $.ajax({
                        "url": "/captcha/slide?t=" + (new Date).getTime(),
                        "type": "get",
                        "dataType": "json",
                        "success": function (t) {
                            initGeetest({
                                "gt": t.gt,
                                "challenge": t.challenge,
                                "new_captcha": t.new_captcha,
                                "product": "embed",
                                "offline": !t.success
                            }, function (t) {
                                t.appendTo("#embed-captcha"), t.onReady(function () {
                                    $("#wait")[0].className = "hide"
                                }).validate(function () {
                                    return e()
                                }).onSuccess(function () {
                                    i.validate("", !0, i.prompts.gee, $("#embed-captcha"))
                                }), window.geeCaptcha = t
                            })
                        }
                    })
                }
            };
        e.exports = {
            "phone": a,
            "email": s,
            "gee": l
        }
    }, "./resources/assets/js/account/captchaButton.js": function (e, t, n) {
        var r = n("./resources/assets/js/account/base.js"),
            i = r.util,
            o = n("./resources/assets/js/account/captcha.js"),
            a = function () {
                var e = [];
                return e.push('<input class="code_btn" id="btnCode" value="获取验证码" type="button">'), e = e.join(""), this.html = function () {
                    return e
                }, this
            },
            s = function (e) {
                var t = $("#btnCode");
                if (200 == e.code) {
                    t.attr("disabled", "disabled").addClass("disabled");
                    var n = 60,
                        r = setInterval(function () {
                            n > 0 ? (n--, t.val(n + "s")) : (clearInterval(r), t.val("获取验证码").removeAttr("disabled").removeClass("disabled"))
                        }, 1e3)
                } else i.alert(e.msg), t.removeAttr("disabled"), geeCaptcha.reset()
            },
            l = function (e) {
                i.alert("系统异常，请稍后再试"), $("#btnCode").removeAttr("disabled")
            },
            u = function (e, t) {
                switch ($("#btnCode").attr("disabled", "disabled"), e) {
                case 1:
                    (new o.phone).send(t, s, l);
                    break;
                case 2:
                    (new o.email).send(t, s, l)
                }
            };
        e.exports = {
            "init": a,
            "send": u
        }
    }, "./resources/assets/js/account/login.js": function (e, t, n) {
        window.$ = window.jQuery = n("./node_modules/jquery/dist/jquery.js");
        var r = n("./resources/assets/js/account/base.js"),
            i = r.util,
            o = n("./resources/assets/js/account/captcha.js"),
            a = n("./resources/assets/js/account/captchaButton.js"),
            s = n("./resources/assets/js/components/phone.js"),
            l = !0;
        $("#login_ways a").on("click", function () {
            var e = $(this);
            if (!e.hasClass("here")) {
                var t = parseInt(e.attr("type"));
                $("#login_ways a").removeClass("here"), e.addClass("here");
                var n = $("#slide_code"),
                    r = $("form .list"),
                    i = $("form .login-qrcode");
                switch (t) {
                case 1:
                    var o = new s.init(!0, !0),
                        l = new a.init;
                    n.prevAll(".form-item").remove().end().before('<li class="form-item">\n    <div class="inp_box">\n        <div class="inp_box_1"><span class="phone"></span>\n' + o.html() + '        </div>\n    </div><div class="error hide" for="phone"></div>\n</li>'), n.nextAll(".form-item").remove().end().after('<li class="form-item">\n    <div class="inp_box">\n        <div class="inp_box_1"><span class="phone2"></span>\n            <input value="" placeholder="手机验证码" id="code" maxlength="6" type="text" class="inp">\n            ' + l.html() + '        </div>\n    </div><div class="error hide" for="code"></div>\n</li>'), o.bindEvent();
                    break;
                case 3:
                    if ("micromessenger" == window.navigator.userAgent.toLowerCase().match(/MicroMessenger/i)) return void(window.location.href = "https://account.itpub.net/thirdParty/wechat/wxAuthUrl");
                    new WxLogin({
                        "self_redirect": !0,
                        "id": "wxlogin",
                        "appid": "undefined" == typeof wx_login_appid ? "" : wx_login_appid,
                        "scope": "snsapi_login",
                        "redirect_uri": encodeURIComponent("https://account.itpub.net/thirdParty/wechat/login/scan"),
                        "state": (new Date).getTime(),
                        "style": "",
                        "href": encodeURIComponent("https://account.itpub.net/static/css/wxlogin.css")
                    });
                    break;
                case 2:
                    n.prevAll(".form-item").remove().end().before('<li class="form-item">\n    <div class="inp_box">\n        <div class="inp_box_1"><span class="user"></span>\n            <input value="" placeholder="用户名/手机号" id="username" maxlength="32" type="text" class="inp">\n        </div>\n    </div><div class="error hide" for="username"></div>\n</li>\n<li class="form-item">\n    <div class="inp_box">\n        <div class="inp_box_1"><span class="password"></span>\n            <input value="" placeholder="密码" id="password" maxlength="32" type="password" class="inp">\n        </div>\n    </div><div class="error hide" for="password"></div>\n</li>'), n.nextAll(".form-item").remove()
                }
                switch (t) {
                case 1:
                    r.show(), u(), n.show(), i.hide();
                    break;
                case 2:
                    r.show(), 0 == needverify && n.hide(), i.hide();
                    break;
                case 3:
                    r.hide(), i.show()
                }
            }
        });
        var u = function () {
            l && ($("#slide_code").show(), o.gee.init(function () {
                var e = !1;
                switch (parseInt($("#login_ways a.here").attr("type"))) {
                case 1:
                case 3:
                    var t = i.account.phone.get();
                    e = i.validate(t.value, i.regular.phone, i.prompts.phone, t.self);
                    break;
                case 2:
                    var n = $("#username"),
                        r = $("#password");
                    e = i.validate(n.val(), i.regular.login_user, i.prompts.login_user, n[0]) && i.validate(r.val(), i.regular.login_pwd, i.prompts.login_pwd, r[0])
                }
                return e
            })), l = !1
        };
        $(function () {
            $("form").on("click", "#btnCode", function () {
                var e = !1,
                    t = {},
                    n = i.account.phone.get();
                if (!(e = i.validate(n.value, i.regular.phone, i.prompts.phone, n.self))) return !1;
                var r = geeCaptcha.getValidate();
                r ? (e = !0, t.geetest_challenge = r.geetest_challenge, t.geetest_validate = r.geetest_validate, t.geetest_seccode = r.geetest_seccode) : (e = !1, i.validate("", !1, i.prompts.gee, $("#embed-captcha"))), e && (t.phone = n.value, a.send(1, t))
            }), (i.browser.versions.android || i.browser.versions.iPhone || i.browser.versions.winphone || i.browser.versions.iPad) && "micromessenger" != window.navigator.userAgent.toLowerCase().match(/MicroMessenger/i) || $(".wx_btn").show()
        }), $(function () {
            $("form").on("blur", "#phone", function () {
                var e = i.account.phone.get();
                i.validate(e.value, i.regular.phone, i.prompts.phone, e.self)
            }), $("form").on("blur", "#code", function () {
                var e = $(this).val();
                i.validate(e, i.regular.code, i.prompts.code, this)
            }), $("form").on("blur", "#username", function () {
                var e = $(this).val();
                i.validate(e, i.regular.login_user, i.prompts.login_user, this)
            }), $("form").on("blur", "#password", function () {
                var e = $(this).val();
                i.validate(e, i.regular.login_pwd, i.prompts.login_pwd, this)
            }), $(document).keydown(function (e) {
                e && 13 == e.keyCode && $("#btnSubmit").trigger("click")
            }), $("#btnSubmit").click(function () {
                var e = $(this),
                    t = !1,
                    n = {},
                    r = "/login/phone",
                    o = parseInt($("#login_ways a.here").attr("type"));
                switch (o) {
                case 1:
                case 3:
                    var a = i.account.phone.get(),
                        s = $("#code");
                    t = i.validate(a.value, i.regular.phone, i.prompts.phone, a.self) && i.validate(s.val(), i.regular.code, i.prompts.code, s[0]), n.phone = a.value, n.code = s.val();
                    break;
                case 2:
                    var l = $("#username"),
                        c = $("#password");
                    t = i.validate(l.val(), i.regular.login_user, i.prompts.login_user, l[0]) && i.validate(c.val(), i.regular.login_pwd, i.prompts.login_pwd, c[0]), n.username = l.val(), n.password = c.val(), r = "/login/login"
                }
                if (2 == o && 1 == needverify) {
                    var d = geeCaptcha.getValidate();
                    d ? (n.geetest_challenge = d.geetest_challenge, n.geetest_validate = d.geetest_validate, n.geetest_seccode = d.geetest_seccode) : i.validate("", !1, i.prompts.gee, $("#embed-captcha")), t = !!d
                }
                t && (n._token = $("input[name=_token]").val(), e.val("登录中...").attr("disabled", "disabled"), i.submit(n, r, function (t) {
                    200 == t.code ? (i.alert("登录成功，即将跳转页面"), setTimeout(function () {
                        e.val("登录").removeAttr("disabled"), document.location.href = t.data.url
                    }, 1500)) : (i.alert(t.msg), e.val("登录").removeAttr("disabled"), 2 == o && (needverify = t.data.needverify ? 1 : 0, needverify && u(), needverify && "undefined" != typeof geeCaptcha && geeCaptcha.reset()))
                }, function (t) {
                    e.val("登录").removeAttr("disabled"), i.alert("系统异常，请稍后再试")
                }))
            }), needverify && u()
        }), window.thirdLogin = function (e, t, n) {
            window.location.href = n
        }, e.exports = {}
    }, "./resources/assets/js/components/gt.js": function (e, t) {
        var n = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (e) {
            return typeof e
        } : function (e) {
            return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
        };
        ! function (e, t) {
            "use strict";
            ! function (e, t) {
                function r(e) {
                    this._obj = e
                }

                function i(e) {
                    var t = this;
                    new r(e)._each(function (e, n) {
                        t[e] = n
                    })
                }
                if (void 0 === e) throw new Error("Geetest requires browser environment");
                var o = e.document,
                    a = e.Math,
                    s = o.getElementsByTagName("head")[0];
                r.prototype = {
                    "_each": function (e) {
                        var t = this._obj;
                        for (var n in t) t.hasOwnProperty(n) && e(n, t[n]);
                        return this
                    }
                }, i.prototype = {
                    "api_server": "api.geetest.com",
                    "protocol": "http://",
                    "type_path": "/gettype.php",
                    "fallback_config": {
                        "slide": {
                            "static_servers": ["static.geetest.com", "dn-staticdown.qbox.me"],
                            "type": "slide",
                            "slide": "/static/js/geetest.0.0.0.js"
                        },
                        "fullpage": {
                            "static_servers": ["static.geetest.com", "dn-staticdown.qbox.me"],
                            "type": "fullpage",
                            "fullpage": "/static/js/fullpage.0.0.0.js"
                        }
                    },
                    "_get_fallback_config": function () {
                        var e = this;
                        return u(e.type) ? e.fallback_config[e.type] : e.new_captcha ? e.fallback_config.fullpage : e.fallback_config.slide
                    }, "_extend": function (e) {
                        var t = this;
                        new r(e)._each(function (e, n) {
                            t[e] = n
                        })
                    }
                };
                var l = function (e) {
                        return "number" == typeof e
                    },
                    u = function (e) {
                        return "string" == typeof e
                    },
                    c = function (e) {
                        return "boolean" == typeof e
                    },
                    d = function (e) {
                        return "object" === (void 0 === e ? "undefined" : n(e)) && null !== e
                    },
                    f = function (e) {
                        return "function" == typeof e
                    },
                    p = {},
                    h = {},
                    g = function () {
                        return parseInt(1e4 * a.random()) + (new Date).valueOf()
                    },
                    v = function (e, t) {
                        var n = o.createElement("script");
                        n.charset = "UTF-8", n.async = !0, n.onerror = function () {
                            t(!0)
                        };
                        var r = !1;
                        n.onload = n.onreadystatechange = function () {
                            r || n.readyState && "loaded" !== n.readyState && "complete" !== n.readyState || (r = !0, setTimeout(function () {
                                t(!1)
                            }, 0))
                        }, n.src = e, s.appendChild(n)
                    },
                    m = function (e) {
                        return e.replace(/^https?:\/\/|\/$/g, "")
                    },
                    y = function (e) {
                        return e = e.replace(/\/+/g, "/"), 0 !== e.indexOf("/") && (e = "/" + e), e
                    },
                    b = function (e) {
                        if (!e) return "";
                        var t = "?";
                        return new r(e)._each(function (e, n) {
                            (u(n) || l(n) || c(n)) && (t = t + encodeURIComponent(e) + "=" + encodeURIComponent(n) + "&")
                        }), "?" === t && (t = ""), t.replace(/&$/, "")
                    },
                    x = function (e, t, n, r) {
                        t = m(t);
                        var i = y(n) + b(r);
                        return t && (i = e + t + i), i
                    },
                    w = function (e, t, n, r, i) {
                        ! function o(a) {
                            var s = x(e, t[a], n, r);
                            v(s, function (e) {
                                e ? a >= t.length - 1 ? i(!0) : o(a + 1) : i(!1)
                            })
                        }(0)
                    },
                    T = function (t, n, r, i) {
                        if (d(r.getLib)) return r._extend(r.getLib), void i(r);
                        if (r.offline) return void i(r._get_fallback_config());
                        var o = "geetest_" + g();
                        e[o] = function (t) {
                            i("success" === t.status ? t.data : t.status ? r._get_fallback_config() : t), e[o] = void 0;
                            try {
                                delete e[o]
                            } catch (n) {}
                        }, w(r.protocol, t, n, {
                            "gt": r.gt,
                            "callback": o
                        }, function (e) {
                            e && i(r._get_fallback_config())
                        })
                    },
                    C = function (e, t) {
                        var n = {
                            "networkError": "网络错误"
                        };
                        if ("function" != typeof t.onError) throw new Error(n[e]);
                        t.onError(n[e])
                    };
                (function () {
                    return !!e.Geetest
                })() && (h.slide = "loaded");
                var k = function (t, n) {
                    var r = new i(t);
                    t.https ? r.protocol = "https://" : t.protocol || (r.protocol = e.location.protocol + "//"), T([r.api_server || r.apiserver], r.type_path, r, function (t) {
                        var i = t.type,
                            o = function () {
                                r._extend(t), n(new e.Geetest(r))
                            };
                        p[i] = p[i] || [];
                        var a = h[i] || "init";
                        "init" === a ? (h[i] = "loading", p[i].push(o), w(r.protocol, t.static_servers || t.domains, t[i] || t.path, null, function (e) {
                            if (e) h[i] = "fail", C("networkError", r);
                            else {
                                h[i] = "loaded";
                                for (var t = p[i], n = 0, o = t.length; n < o; n += 1) {
                                    var a = t[n];
                                    f(a) && a()
                                }
                                p[i] = []
                            }
                        })) : "loaded" === a ? o() : "fail" === a ? C("networkError", r) : "loading" === a && p[i].push(o)
                    })
                };
                e.initGeetest = k
            }(e)
        }("undefined" != typeof window ? window : this)
    }, "./resources/assets/js/components/phone.js": function (e, t) {
        var n = [{
                "code": "+86",
                "area": "中国"
            }, {
                "code": "+852",
                "area": "中国香港特别行政区"
            }, {
                "code": "+853",
                "area": "中国澳门特别行政区"
            }, {
                "code": "+886",
                "area": "中国台湾"
            }, {
                "code": "+1",
                "area": "美国"
            }, {
                "code": "+81",
                "area": "日本"
            }, {
                "code": "+82",
                "area": "韩国"
            }],
            r = function (e, t) {
                var r = [];
                if (e = e && !0 === e, e && (r.push('<div class="area-code" id="area-code">'), r.push('<input value="' + (!0 === t ? "+86" : "+852") + '" placeholder="" type="text" readonly="readonly" id="areacode">'), r.push("</div>")), r.push('<input value="" placeholder="手机号码" id="phone" name="phone" maxlength="11" type="text"  pattern="[0-9]*" class="' + (e ? "inp2" : "inp") + '">'), e) {
                    r.push('<ul class="areacode-select">');
                    for (var i in n) {
                        var o = n[i];
                        !0 !== t && "+86" === o.code || r.push('<li data-value="' + o.code + '"><i>' + o.code + "</i>" + o.area + "</li>")
                    }
                    r.push("</ul>")
                }
                r = r.join(""), this.html = function () {
                    return r
                }, this.bindEvent = function () {
                    var e = $(".areacode-select");
                    $("form").on("click", "#area-code", function (t) {
                        e.slideDown(), t.stopPropagation()
                    }), $("body").on("click", function () {
                        e.slideUp()
                    }), e.find("li").on("click", function () {
                        $("#areacode").val($(this).attr("data-value"))
                    })
                }
            };
        e.exports = {
            "init": r
        }
    }, "0": function (e, t, n) {
        e.exports = n("./resources/assets/js/account/login.js")
    }
});