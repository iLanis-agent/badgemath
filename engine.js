// Badge Math engine: the packs a badge order takes, the lanyard bags the attendees take, the cost an attendee, and the minutes the printing takes. Exact integers, half-up on display only. No named constants; every number is the owner's own entry.
function _i(t, err, digits, lo, hi) {
  t = typeof t === "string" ? t.trim() : "";
  if (!new RegExp("^[0-9]{1," + digits + "}$").test(t)) throw new Error(err);
  var v = parseInt(t, 10);
  if (v < lo || v > hi) throw new Error(err);
  return v;
}
function _p(t, err, intDigits, places, lo, hi) {
  t = typeof t === "string" ? t.trim() : "";
  var m = new RegExp("^([0-9]{1," + intDigits + "})(?:\\.([0-9]{1," + places + "}))?$").exec(t);
  if (!m) throw new Error(err);
  var v = parseInt(m[1], 10) * Math.pow(10, places) + (m[2] ? parseInt(m[2].padEnd(places, "0"), 10) : 0);
  if (v < lo || v > hi) throw new Error(err);
  return v;
}
function _m(v) {
  var w = Math.floor(v / 100), f = String(v % 100).padStart(2, "0");
  return w + "." + f;
}
function _pl(n, one, many) { return n + (n === 1 ? one : many); }
function _v(n, one, many) { return n === 1 ? one : many; }
var _AT = "the attendees must be from 1 to 1000000 with no decimal places";
var _BP = "the badges a pack must be from 1 to 1000 with no decimal places";
var _LB = "the lanyards a bag must be from 1 to 1000 with no decimal places";
var _PK = "the packs must be from 1 to 100000 with no decimal places";
var _PR = "the pack price must be from 0.01 to 999.99 with up to 2 decimal places";
var _BM = "the badges a minute must be from 1 to 100 with no decimal places";

function packsTruth(attendees, perPack) {
  var n = _i(attendees, _AT, 7, 1, 1000000), b = _i(perPack, _BP, 4, 1, 1000);
  var k = Math.floor((n + b - 1) / b), last = n - (k - 1) * b;
  return "The " + _pl(n, " attendee", " attendees") + " at " + _pl(b, " badge", " badges") + " a pack " + _v(n, "takes", "take") + " " + _pl(k, " pack", " packs") + ", the last pack holding " + _pl(last, " badge", " badges") + ".";
}
function lanyardTruth(attendees, perBag) {
  var n = _i(attendees, _AT, 7, 1, 1000000), b = _i(perBag, _LB, 4, 1, 1000);
  var k = Math.floor((n + b - 1) / b), spare = k * b - n;
  return "The " + _pl(n, " attendee", " attendees") + " at " + _pl(b, " lanyard", " lanyards") + " a bag " + _v(n, "takes", "take") + " " + _pl(k, " bag", " bags") + ", leaving " + _pl(spare, " lanyard", " lanyards") + " spare.";
}
function costTruth(packs, price, attendees) {
  var b = _i(packs, _PK, 6, 1, 100000), p = _p(price, _PR, 3, 2, 1, 99999), n = _i(attendees, _AT, 7, 1, 1000000);
  var cc = b * p;
  var pa = Math.floor((2 * cc + n) / (2 * n));
  return "The " + _pl(b, " pack", " packs") + " at $" + _m(p) + " a pack " + _v(b, "comes", "come") + " to $" + _m(cc) + ", $" + _m(pa) + " an attendee.";
}
function timeTruth(attendees, perMinute) {
  var n = _i(attendees, _AT, 7, 1, 1000000), m = _i(perMinute, _BM, 3, 1, 100);
  var t = Math.floor((n + m - 1) / m), h = Math.floor(t / 60), r = t % 60;
  return "The " + _pl(n, " badge", " badges") + " at " + _pl(m, " badge", " badges") + " a minute " + _v(n, "takes", "take") + " " + _pl(t, " minute", " minutes") + ", " + _pl(h, " hour", " hours") + " " + _pl(r, " minute", " minutes") + ".";
}
