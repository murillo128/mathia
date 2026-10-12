# VIS-445 — sharp occupation-moment boundary coefficient counts unfilled gaps

## Claim and evidence

Let \(E\subset\mathbb R/2\pi\mathbb Z\) be a nonempty proper finite union of disjoint, nondegenerate closed arcs. Denote its complementary open-gap lengths by \(g_1,\ldots,g_K>0\). For the unit-speed circle flow and a fixed observation length \(L=2\rho\in(0,2\pi)\), set

\[
Z_L(x)=\frac1L\int_{-L/2}^{L/2}\mathbf 1_E(x+u)\,du,\qquad
A_n(L)=\int(1-Z_L(x))^n\,\frac{dx}{2\pi}.
\]

Put \(p_L=(2\pi)^{-1}\sum_i(g_i-L)_+\), the exact Haar first-hit avoidance probability from VIS-441, and

\[
M_L=\#\{i:g_i\ge L\}.
\]

**Exact small-occupation law:** there exists \(\varepsilon=\varepsilon(E,L)>0\) such that, for every \(s\in(0,\varepsilon)\),

\[
\boxed{\quad
m_H\{0<Z_L\le s\}=\frac{L M_L}{\pi}s.
\quad}
\]

In particular, there is a \(q=q(E,L)\in(0,1)\) such that

\[
\boxed{\quad
A_n(L)=p_L+\frac{LM_L}{\pi(n+1)}+O_{E,L}(q^n),
\qquad
\lim_{n\to\infty}\frac{\pi(n+1)}L[A_n(L)-p_L]=M_L.
\quad}
\]

Thus the **leading error coefficient of the integrated occupation-moment approximation** in VIS-444 reads the number of complementary gaps not yet filled by the observation window, including gaps exactly equal to \(L\). The coefficient has integer-valued topological jumps as \(L\) crosses a gap length, although \(A_n(L)\) is continuous in \(L\) at each fixed \(n\).

**Evidence/status:** EXACT-DERIVED + CLASSICAL ENDPOINT LAPLACE PRINCIPLE + MATCHED CIRCLE TARGET CONTROL + NO GENERAL NOVELTY CLAIM. This is a fixed finite-arc statement; it supplies no uniform growing-shell moment bound.

## Derivation: ramps at the boundary of zero occupation

The function \(Z_L\) is continuous and piecewise affine in the starting phase. A window has zero occupation exactly when it lies, apart from possible endpoints, inside one of the complementary gaps. For \(g_i>L\), the corresponding zero set is an interval of center positions of length \(g_i-L\); for \(g_i=L\), it is a single center; for \(g_i<L\), it is absent. The total measure of the zero set is therefore \(p_L\).

At each end of a positive-length zero interval, moving the window a small distance \(h>0\) outward inserts exactly \(h\) of the neighboring target arc, hence \(Z_L=h/L\). At a zero point from \(g_i=L\), the same law holds to both sides: \(Z_L=|h|/L\). These are local exact identities, not derivatives estimated from a sampled image. Since there are finitely many strictly positive target arcs and gap lengths, choose a sufficiently small neighborhood on each relevant side so that no other boundary enters the window; also choose the neighborhoods disjoint. Each gap with \(g_i\ge L\) contributes **exactly two positive sides** to the small-occupation set, each of length \(Ls\) when \(s\) is sufficiently small. Gaps with \(g_i<L\) are separated from zero occupation by a strictly positive minimum locally, and the compact complement of these neighborhoods has a positive occupation floor wherever \(Z_L>0\). Dividing the total \(2LM_Ls\) by \(2\pi\) proves the small-occupation law.

Subtracting the zero-occupation atom from the \(n\)-th moment gives

\[
A_n-p_L=\int_{\{Z_L>0\}}(1-Z_L)^n\,dm_H.
\]

The exact linear small-occupation distribution contributes

\[
\frac{LM_L}{\pi}\int_0^\varepsilon(1-z)^n\,dz
=\frac{LM_L}{\pi(n+1)}
\left[1-(1-\varepsilon)^{n+1}\right].
\]

The remaining phases have \(Z_L\ge\varepsilon\), so their contribution is bounded by \((1-\varepsilon)^n\). This proves both the sharp coefficient and the exponentially small fixed-geometry remainder. When \(M_L=0\), zero occupation is impossible and the entire moment decays exponentially.

The \(\ge\) in \(M_L\) is essential: a gap exactly as long as the window contributes zero Haar mass to \(p_L\) but still has two linear contact sides and therefore contributes a full \(L/[\pi(n+1)]\) term.

## Matched analytic-target control and exact arithmetic audit

Use the two degree-two analytic-polynomial superlevel targets already constructed in VIS-441, with arc endpoints in radians

\[
E_A=[0,\pi/6]\cup[\pi,3\pi/2],
\qquad
E_B=[0,\pi/6]\cup[\pi/2,\pi].
\]

They have the same target mass \(1/3\), regular threshold, full degree-two analytic Fourier support, and directional crossing flux \(2/\pi\). Their complementary gaps are respectively

\[
A:(5\pi/6,\ \pi/2),\qquad B:(\pi/3,\ \pi).
\]

At the common window length \(L=\pi/2\) (radius \(\rho=\pi/4\)), VIS-441 gives \(p_A=1/6\) and \(p_B=1/4\), while \(M_A=2\) and \(M_B=1\). The present theorem gives the distinct *high-moment correction coefficients*

\[
\lim_{n\to\infty}(n+1)(A_n^A-1/6)=1,\qquad
\lim_{n\to\infty}(n+1)(A_n^B-1/4)=1/2.
\]

For an independent **exact rational** control, normalize the circle circumference to one. The arcs become \(A:[0,1/12]\cup[1/2,3/4]\), \(B:[0,1/12]\cup[1/4,1/2]\), with window width \(w=1/4\). Partition the center coordinate at the target endpoints shifted by \(\pm w/2\); on each partition interval \([a,b]\), \(y(x)=1-Z_L(x)\) is affine, so its integral is exactly

\[
\int_a^b y(x)^n\,dx=
\frac{b-a}{n+1}\sum_{j=0}^{n}y(a)^j y(b)^{n-j}.
\]

Summing rational contributions yields, for instance,

\[
A_8^A=\frac{100207}{354294},\quad
A_8^B=\frac{8275}{26244};
\]

at orders \(n=16\) and \(n=32\), the rescaled residual pairs \((n+1)(A_n^A-p_A),(n+1)(A_n^B-p_B)\) are respectively approximately \((1.0038061,0.5064704)\) and \((1.0000120,0.5000191)\). Direct dense-grid window-overlap inspection shows the same zero intervals and linear contact ramps; it is a visual diagnostic, not part of the proof.

## Novelty boundary, controls and research consequence

The endpoint integral \(\int_0^\varepsilon(1-z)^n dz\sim 1/n\) is elementary and is in the family of classical Watson/Laplace boundary asymptotics. The moment-to-zero-atom limit is already classical in VIS-444. This finding claims no new universal moment theorem, no new circle parallel-set formula and no independent mathematical invariant beyond the full exact hitting curve: in fact \(M_L\) is also encoded in the one-sided slopes of the piecewise-linear function \(p_L\). The durable Mathia delta is the **sharp finite-order certificate**, including the gap-equality boundary that VIS-444's upper bound did not resolve, and its same-support matched analytic target audit.

The result is invariant under rotation, rephasing and rescaling of the plot's angular origin, and makes no use of sample resolution or color. It also exposes a critical limitation: the constant \(q(E,L)\) and the allowed small-occupation scale can deteriorate as target arcs shrink or as \(L\) approaches another gap length. Consequently the \(n\to\infty\) limit cannot be interchanged with a growing Wang-shell/target limit without separate uniform geometry and high-order Fourier/Gram transfer estimates. A fixed-moment Gram-to-Haar tariff does **not** by itself recover this \(n\to\infty\) topological coefficient, nor does an abstract circle control establish an exceptional arithmetic height or RH consequence.

A falsification must exhibit a finite-arc target for which a zero-occupation contact has a nonlinear local overlap ramp, a contact with fewer/more than the stated two one-sided contributions per gap with \(g_i\ge L\), or a mismatch in the rational partition test. Critical \(L=g_i\) must not be discarded: dropping equality would immediately contradict the \(A\) control above.

## Dependencies

- VIS-441: exact gap-erosion avoidance law and matched full-degree-two Fourier-support superlevel targets.
- VIS-443: caution that finite correlation orders can miss hitting information.
- VIS-444: integrated occupation moment hierarchy and finite-order upper error bound.
