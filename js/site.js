// Theme toggle (light = default) and reveal-on-scroll.
(function () {
  var root = document.documentElement;
  var btn = document.querySelector('.theme-toggle');
  var sun = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
  var moon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';

  function render() {
    if (!btn) return;
    var dark = root.getAttribute('data-theme') === 'dark';
    btn.innerHTML = (dark ? sun : moon) + '<span>' + (dark ? 'LIGHT' : 'DARK') + '</span>';
    btn.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
    btn.setAttribute('aria-pressed', dark ? 'true' : 'false');
  }
  if (btn) {
    btn.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
      render();
    });
    render();
  }

  var items = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    items.forEach(function (el) { el.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  items.forEach(function (el) { io.observe(el); });
})();

// Homepage boot-up: type the name, scramble the readout values, then mark the session as booted.
(function () {
  var root = document.documentElement;
  if (!root.classList.contains('boot')) return;
  try { sessionStorage.setItem('booted', '1'); } catch (e) {}
  var h1 = document.querySelector('.hero h1');
  if (h1) {
    var lines = h1.innerHTML.split(/<br\s*\/?>/i).map(function (t) { return t.replace(/<[^>]+>/g, '').trim(); });
    h1.setAttribute('aria-label', lines.join(' '));
    h1.innerHTML = '';
    var spans = [];
    lines.forEach(function (line, li) {
      if (li) h1.appendChild(document.createElement('br'));
      line.split('').forEach(function (ch) {
        var s = document.createElement('span'); s.textContent = ch; s.style.visibility = 'hidden';
        s.setAttribute('aria-hidden', 'true'); h1.appendChild(s); spans.push(s);
      });
    });
    var caret = document.createElement('span'); caret.className = 'type-caret'; caret.setAttribute('aria-hidden', 'true');
    h1.style.animation = 'none'; h1.style.visibility = 'visible';
    var i = 0;
    setTimeout(function step() {
      if (i < spans.length) {
        spans[i].style.visibility = 'visible';
        spans[i].after(caret);
        i++; setTimeout(step, 120);
      } else {
        setTimeout(function () { caret.remove(); }, 1200);
      }
    }, 435);
  }
  var glyphs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#/<>';
  document.querySelectorAll('[data-scramble]').forEach(function (el, k) {
    var final = el.textContent, frame = 0, total = 14;
    setTimeout(function tick() {
      frame++;
      var settled = Math.floor(final.length * frame / total);
      el.textContent = final.split('').map(function (c, j) {
        return j < settled || c === ' ' ? c : glyphs[Math.floor(Math.random() * glyphs.length)];
      }).join('');
      if (frame < total) setTimeout(tick, 87); else el.textContent = final;
    }, 1845 + k * 345);
  });
  setTimeout(function () { root.classList.remove('boot'); }, 7800);
})();

// Photo viewer: click any project photo to view it large; arrows/keys to flip, Esc to close.
(function () {
  var links = Array.prototype.filter.call(document.querySelectorAll('.lfig a, .gallery a'), function (a) {
    return /\.(jpe?g|png|gif|webp)$/i.test(a.getAttribute('href') || '');
  });
  if (!links.length) return;
  var lb = document.createElement('div');
  lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', 'Photo viewer');
  lb.innerHTML = '<span class="lb-count"></span><button class="lb-close" type="button" aria-label="Close">✕</button>' +
    '<button class="lb-prev" type="button" aria-label="Previous photo">‹</button><button class="lb-next" type="button" aria-label="Next photo">›</button>' +
    '<figure><img alt=""><figcaption></figcaption></figure>';
  document.body.appendChild(lb);
  var img = lb.querySelector('img'), cap = lb.querySelector('figcaption'), count = lb.querySelector('.lb-count'), idx = 0, last = null;
  function show(i) {
    idx = (i + links.length) % links.length;
    var a = links[idx], fig = a.closest('figure'), fc = fig && fig.querySelector('figcaption'), im = a.querySelector('img');
    img.src = a.getAttribute('href'); img.alt = im ? im.alt : '';
    cap.textContent = fc ? fc.textContent : ''; cap.hidden = !cap.textContent;
    count.textContent = (idx + 1) + ' / ' + links.length;
  }
  function open(i) { last = document.activeElement; show(i); lb.classList.add('open'); document.body.classList.add('lb-lock'); lb.querySelector('.lb-close').focus(); }
  function close() { lb.classList.remove('open'); document.body.classList.remove('lb-lock'); img.src = ''; if (last) last.focus(); }
  links.forEach(function (a, i) { a.addEventListener('click', function (e) { e.preventDefault(); open(i); }); });
  lb.querySelector('.lb-close').addEventListener('click', close);
  lb.querySelector('.lb-prev').addEventListener('click', function () { show(idx - 1); });
  lb.querySelector('.lb-next').addEventListener('click', function () { show(idx + 1); });
  lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
  document.addEventListener('keydown', function (e) {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') show(idx - 1);
    else if (e.key === 'ArrowRight') show(idx + 1);
  });
  var x0 = null;
  lb.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener('touchend', function (e) { if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1)); x0 = null; });
})();

// CAD-style cursor readout (desktop only): page coordinates in mm, like a CAD status bar.
(function () {
  if (!window.matchMedia || !matchMedia('(pointer: fine)').matches) return;
  var r = document.createElement('div');
  r.className = 'cad-readout'; r.setAttribute('aria-hidden', 'true');
  r.innerHTML = '<span><b>X</b> <span class="cx">0.0</span></span><span><b>Y</b> <span class="cy">0.0</span></span><span>mm</span>';
  document.body.appendChild(r);
  var cx = r.querySelector('.cx'), cy = r.querySelector('.cy'), pending = false, px = 0, py = 0;
  var MM = 25.4 / 96;
  document.addEventListener('mousemove', function (e) {
    px = e.pageX; py = e.pageY;
    if (!r.classList.contains('on')) r.classList.add('on');
    if (pending) return; pending = true;
    requestAnimationFrame(function () { cx.textContent = (px * MM).toFixed(1); cy.textContent = (py * MM).toFixed(1); pending = false; });
  });
  document.addEventListener('mouseleave', function () { r.classList.remove('on'); });
})();
