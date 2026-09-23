# NB-315 — Farey shell primitives make far-external rank-one mixing moving-superquadratic

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-303, NB-314
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + MOVING-SECTION + PROJECTED-DILATION + RANK-ONE-MIXING + FAREY-SHELL-PRIMITIVE + QUANTITATIVE-RATE + SUPERQUADRATIC-ASYMPTOTIC + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
T_{N,m}:=P_{U_N}A_m|_{U_N},
\qquad
\beta_{N+1}(m):=\|T_{N,m}\|,
\]

for `N>=2` and positive integer dilation `m`. Let `R_N` be the rank-one operator from `NB-314`,

\[
R_Nv=\langle v,p_N\rangle r_N,
\qquad
p_N=P_{U_N}{\bf 1},
\]

where `r_N` represents the reciprocal-shell mean functional `mu_N`, and put

\[
L_N:=\|R_N\|
=\|P_{U_N}{\bf 1}\|_2\,\|\mu_N\|_{U_N^*}.
\]

Then the fixed-section limit of `NB-314` admits a rate uniform in growing `N` that does **not** pay the common period `lcm(2,...,N)`:

\[
\boxed{
\|\sqrt m\,T_{N,m}-R_N\|
\le
C_{\rm mix}\frac{N^{5/2}}{m},
}
\tag{1}
\]

where one may take

\[
C_{\rm mix}
=
2\sqrt{\zeta(2)+\zeta(3)}
\left(\frac{\pi}{2\sqrt3}+\frac12\right)
\sqrt{\frac92}
<11.
\tag{2}
\]

Using the explicit lower bound for `L_N` from `NB-314`,

\[
L_N
\ge
c_L\left(1-\frac1N\right)\sqrt N,
\qquad
c_L:=\frac{\sqrt{\log2}}{2\sqrt{1+\pi^2/6}},
\tag{3}
\]

this gives the uniform relative estimate

\[
\boxed{
\frac{\|\sqrt m\,T_{N,m}-R_N\|}{L_N}
\le
\frac{C_{\rm mix}}{c_L(1-1/N)}\frac{N^2}{m}
<80\frac{N^2}{m}.
}
\tag{4}
\]

Consequently, for every moving family `N=N_X -> infinity`, `m=m_X` with

\[
\frac{m_X}{N_X^2}\to\infty,
\tag{5}
\]

one has the moving rank-one asymptotic

\[
\boxed{
\left\|
\frac{\sqrt{m_X}\,\beta_{N_X+1}(m_X)}{L_{N_X}}-1
\right|
\to0,
}
\tag{6}
\]

and, more strongly,

\[
\boxed{
\left\|
\frac{\sqrt{m_X}}{L_{N_X}}T_{N_X,m_X}
-
\frac1{L_{N_X}}R_{N_X}
\right\|
\to0.
}
\tag{7}
\]

Thus the superquadratic source-compression regime of `NB-303` is not merely a regime where the projected dilation becomes small. After its natural `sqrt(m)` rescaling it becomes asymptotically rank one, with exactly the target-weighted coefficient identified in `NB-314`.

This does **not** improve the known sufficient decay threshold `m/N^2 -> infinity`, and it does not turn the source-overlap theorem into a first-free target-occupation theorem.

## 1. Centered reciprocal shells have a small primitive without paying the lcm period

For `u in U_N`, write its reciprocal profile

\[
F_u(t):=u(1/t).
\]

As in `NB-303`, on every unit reciprocal cell `t in [k,k+1)` one has

\[
F_u(t)=u_k,
\]

where the shell sequence has a finite Fourier expansion

\[
u_k=\sum_{\alpha\in\mathcal F_N}c_\alpha e^{2\pi i\alpha k}.
\tag{8}
\]

Every distinct frequency is a reduced rational modulo one with denominator at most `N`. The zero-frequency coefficient is exactly the reciprocal-period mean from `NB-314` because `F_u` is constant on unit cells:

\[
c_0=\mu_N(u).
\tag{9}
\]

Define the centered profile and centered shell sequence

\[
\widetilde F_u:=F_u-\mu_N(u),
\qquad
x_k:=u_k-\mu_N(u).
\]

Then

\[
x_k
=
\sum_{\alpha\in\mathcal F_N\setminus\{0\}}
c_\alpha e^{2\pi i\alpha k}.
\tag{10}
\]

Put

\[
Q_N^0(u)
:=
\sum_{\alpha\ne0}|c_\alpha|^2.
\]

Clearly `Q_N^0(u)<=Q_N(u)`, where `Q_N` is the Cesaro shell energy of `NB-303`. Hence

\[
Q_N^0(u)
\le
(4N^2+2)\|u\|_2^2
\le
\frac92N^2\|u\|_2^2
\qquad(N\ge2).
\tag{11}
\]

The point is now to control the primitive of `widetilde F_u` directly from the nonzero Farey frequencies, rather than by one complete common period.

For an integer `K>=1`, let

\[
S_K:=\sum_{k=0}^{K-1}x_k.
\]

From (10),

\[
S_K
=
\sum_{\alpha\ne0}
c_\alpha
\frac{1-e^{2\pi i\alpha K}}
{1-e^{2\pi i\alpha}}.
\tag{12}
\]

Cauchy--Schwarz gives

\[
|S_K|^2
\le
Q_N^0(u)
\sum_{\alpha\ne0}
\frac{|1-e^{2\pi i\alpha K}|^2}
{|1-e^{2\pi i\alpha}|^2}.
\tag{13}
\]

If `alpha=h/q` with `1<=h<q<=N`, then

\[
\frac{|1-e^{2\pi i\alpha K}|}
{|1-e^{2\pi i\alpha}|}
\le
\frac1{|\sin(\pi h/q)|}.
\]

Using

\[
\sin(\pi h/q)
\ge
\frac{2\min(h,q-h)}q
\]

and overcounting reduced fractions by all nonzero fractions with denominator `q`,

\[
\sum_{h=1}^{q-1}
\frac1{\sin^2(\pi h/q)}
\le
\frac{\pi^2}{12}q^2.
\tag{14}
\]

Therefore

\[
\boxed{
|S_K|
\le
\frac{\pi}{2\sqrt3}
N^{3/2}\sqrt{Q_N^0(u)}.
}
\tag{15}
\]

uniformly in `K`. No `P_N=lcm(2,...,N)` occurs.

To pass from integer partial sums to the continuous primitive, note that the number of distinct nonzero reduced frequencies is at most

\[
M_N
\le
\sum_{q=2}^N(q-1)
\le
\frac{N^2}{2}.
\]

Thus

\[
|x_K|
\le
\sqrt{M_NQ_N^0(u)}
\le
\frac{N}{\sqrt2}\sqrt{Q_N^0(u)}.
\tag{16}
\]

Define

\[
G_u(T):=
\int_0^T\widetilde F_u(s)\,ds.
\tag{17}
\]

Writing `T=K+theta`, `0<=theta<1`, gives `G_u(T)=S_K+theta x_K`. For `N>=2`, equations (15)--(16) therefore imply

\[
\|G_u\|_\infty
\le
\left(
\frac{\pi}{2\sqrt3}+\frac12
\right)
N^{3/2}\sqrt{Q_N^0(u)}.
\tag{18}
\]

Combining with (11),

\[
\boxed{
\|G_u\|_\infty
\le
C_{\rm prim}N^{5/2}\|u\|_2,
\qquad
C_{\rm prim}:=
\left(
\frac{\pi}{2\sqrt3}+\frac12
\right)
\sqrt{\frac92}.
}
\tag{19}
\]

This uniform primitive estimate is the quantitative replacement for the fixed-period averaging lemma used in `NB-314`.

## 2. Integration by parts converts the primitive bound into operator mixing

Equation (20) of `NB-314` identifies the exact centered error:

\[
\left\langle
(\sqrt m\,T_{N,m}-R_N)v,u
\right\rangle
=
\int_1^\infty
F_v(t)\widetilde F_u(mt)\,\frac{dt}{t^2}.
\tag{20}
\]

On `t in [k,k+1)`, `F_v(t)=v_k`. Hence

\[
\left\langle
(\sqrt m\,T_{N,m}-R_N)v,u
\right\rangle
=
\sum_{k\ge1}v_k I_k,
\tag{21}
\]

where

\[
I_k
:=
\int_k^{k+1}
\widetilde F_u(mt)\,\frac{dt}{t^2}
=
m\int_{mk}^{m(k+1)}
\widetilde F_u(s)\,\frac{ds}{s^2}.
\tag{22}
\]

Since `G_u'=widetilde F_u` almost everywhere, integration by parts on `[a,b]` gives

\[
\int_a^b
\widetilde F_u(s)\frac{ds}{s^2}
=
\left[\frac{G_u(s)}{s^2}\right]_a^b
+2\int_a^b\frac{G_u(s)}{s^3}\,ds.
\]

Consequently

\[
\left|
\int_a^b
\widetilde F_u(s)\frac{ds}{s^2}
\right|
\le
\frac{2\|G_u\|_\infty}{a^2},
\]

and (22) yields

\[
|I_k|
\le
\frac{2\|G_u\|_\infty}{m k^2}.
\tag{23}
\]

The exact shell norm from `NB-303` is

\[
\|v\|_2^2
=
\sum_{k\ge1}
\frac{|v_k|^2}{k(k+1)}.
\tag{24}
\]

Weighted Cauchy--Schwarz therefore gives

\[
\sum_{k\ge1}\frac{|v_k|}{k^2}
\le
\sqrt{\zeta(2)+\zeta(3)}\,\|v\|_2.
\tag{25}
\]

Combining (19), (21), (23), and (25),

\[
\left|
\left\langle
(\sqrt m\,T_{N,m}-R_N)v,u
\right\rangle
\right|
\le
C_{\rm mix}
\frac{N^{5/2}}m
\|u\|_2\|v\|_2,
\]

with `C_mix` from (2). Taking the supremum over unit `u,v` proves (1).

## 3. The existing quadratic decay frontier now has a rank-one asymptotic

Taking operator norms in (1) and using `||R_N||=L_N`,

\[
\left|
\sqrt m\,\beta_{N+1}(m)-L_N
\right|
\le
C_{\rm mix}\frac{N^{5/2}}m.
\tag{26}
\]

Dividing by the lower bound (3) gives (4), hence (6)--(7) under `m/N^2->infinity`.

There is also a simple matching upper scale for the coefficient. Since `mu_N(u)` is the zero-frequency Fourier coefficient of the shell sequence,

\[
|\mu_N(u)|^2
\le
Q_N(u)
\le
(4N^2+2)\|u\|_2^2.
\]

Because `||P_(U_N)1||<=1`,

\[
\boxed{
L_N\le\sqrt{4N^2+2}.
}
\tag{27}
\]

Thus (6) also recovers the decay conclusion of `NB-303` in the same superquadratic regime:

\[
\beta_{N+1}(m)
=
\frac{L_N}{\sqrt m}(1+o(1))
\longrightarrow0.
\tag{28}
\]

The improvement is structural rather than a better threshold. `NB-303` proved only that all projected-dilation overlap disappears when `m/N^2->infinity`; the present result identifies the unique asymptotic channel that remains before the final `m^{-1/2}` normalization removes it.

The absolute estimate (1) and the relative statement (4) have different scales. Absolute convergence `||sqrt(m)T-R_N||->0` follows from the stronger condition `m/N^(5/2)->infinity`. The moving rank-one **shape** needs only relative convergence to an operator whose norm grows at least like `sqrt(N)`, and therefore already holds under `m/N^2->infinity`. These two statements must not be conflated.

## 4. Adversarial checks

The centering step does not silently identify two different means. Because every reciprocal profile is constant on each unit interval, its continuous mean over a common integer period is exactly the discrete zero Fourier coefficient of the shell sequence. Subtracting `mu_N(u)` therefore removes precisely the character `alpha=0` and no other frequency.

The Farey denominator estimate is circularly safe. Frequencies near `1` are controlled through `min(h,q-h)` in (14), so the geometric-sum denominator cannot become small without paying the same rational-denominator scale already counted on the opposite side of the circle.

The finite Fourier argument controls only integer partial sums. Equation (16) is included specifically to control the fractional final cell of the continuous primitive; no hidden continuity assumption on `F_u` is used.

The proof never invokes the exponentially large common period `P_N`. Its only section-size losses are the number and spacing of reduced rational shell frequencies and the `Q_N=O(N^2)||u||^2` conditioning bound from `NB-303`.

The rate is not claimed sharp. In particular, (1) does not show that the rank-one regime begins only at quadratic scale. It shows that the existing superquadratic decay frontier is already sufficient for **relative** rank-one mixing. Improving the transition into `N<<m<=O(N^2)` would require a sharper primitive estimate, cancellation in the weighted shell pairing beyond the supremum norm of `G_u`, or an explicit counterexample.

Finally, `R_N` contains the captured-target factor `P_(U_N)1`, but this remains a source-overlap operator statement. It does not prove that the moving first-free Ford datum occupies the rank-one channel, does not control the unresolved future-tail Gram, and does not imply a Nyman approximation rate or RH.

## 5. Prior-art audit

A fresh search on 2026-09-24 checked the classical discrete Nyman--Beurling/Baez-Duarte dilation literature, Balazard--Martin's multiplicative fractional-part autocorrelation, generalized Nyman Gram work of Alouges--Darses--Hillion, and recent Gram-decay work of Carvill, together with the separated-frequency/large-sieve boundary already used by `NB-303`. The reviewed material provides the surrounding dilation, fractional-part, Gram, and Farey-frequency technology but did not exhibit the specific moving finite-section estimate (1), the relative rank-one asymptotic (4)--(7), or the shell-primitive argument above.

No new external theorem is load-bearing here. The only nontrivial external input inherited by this derivation is the separated-frequency large-sieve estimate already recorded through `NB-303`; the rest is elementary finite Fourier summation, integration by parts, and weighted Cauchy--Schwarz. Therefore `SOURCES.md` does not require a new dependency entry.

## Evidence boundary

`NB-315` upgrades `NB-314` from a fixed-section limit to a quantitative moving theorem in the already-known superquadratic regime. It does **not** narrow the gap between the necessary superlinear scale of `NB-313` and the sufficient superquadratic scale of `NB-303`. The unresolved source-side question is whether rank-one mixing or complete decay can be pushed materially below `m>>N^2`, or whether coherent centered shell modes survive there.

The destination-side boundary is unchanged: even a complete source-side singular description still requires target-occupation control for the actual first-free datum before it can improve the Nyman distance.