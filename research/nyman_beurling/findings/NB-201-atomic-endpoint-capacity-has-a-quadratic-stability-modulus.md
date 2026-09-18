# NB-201 — Atomic endpoint capacity has a quadratic stability modulus

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + POSITIVE-EULER + ENDPOINT-STABILITY + NB-200-REFINEMENT`.

`NB-200` proves a one-sided asymptotic capacity threshold for positive Euler-shell returns: an `o(1/X_a)` return at bounded endpoint ratio cannot stay below `2πe^Delta`. Its proof deliberately fixes a logarithmic top slab before sending `a->0`, so it does not quantify how the return error controls the distance to that endpoint threshold.

The same atomic argument can be diagonalized. The key is to retain the exact finite-`X_a` carrying-capacity ratio of a shrinking top slab. This gives a quadratic stability law: if the endpoint ratio lies a relative distance `d` below the finite atomic capacity edge, then the positive chord defect is at least order `d^2/X_a`, up to the existing Vinogradov--Korobov prime-number-theorem remainder.

Keep the notation of `NB-194` and `NB-200`:

\[
x_a=e^{r_0/a},\qquad X_a=\log x_a=\frac{r_0}{a},\qquad y_a=e^\Delta x_a,
\]

\[
D_a:=\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=\frac{\Lambda(n)n^{-1-a}}{D_a}\mathbf 1_{[x_a,y_a)}(n),
\]

and

\[
\mathcal A_a(t):=\sum_n w_{n,a}|e^{-it\log n}-1|.
\]

Put

\[
V(x):=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}},
\qquad
\mathcal E_a:=e^{-c_0V(x_a)},
\tag{1}
\]

where `c_0>0` is a sufficiently small fixed constant allowed by the prime-number-theorem remainder already used in `NB-194`. Define the finite atomic capacity edge

\[
\boxed{
\kappa_a^{\rm cap}
:=2\pi e^\Delta\frac{X_a}{X_a+\Delta}.
}
\tag{2}
\]

For an endpoint ordinate write

\[
\kappa_a(t):=\frac{|t|X_a}{x_a},
\qquad
d_a(t):=1-\frac{\kappa_a(t)}{\kappa_a^{\rm cap}}.
\tag{3}
\]

Then there are constants `kappa_0,c,C>0`, depending only on the fixed shell parameters, such that for all sufficiently small `a` and every real `t` satisfying

\[
\kappa_0\le \kappa_a(t)\le\kappa_a^{\rm cap},
\tag{4}
\]

one has

\[
\boxed{
\mathcal A_a(t)
\ge
\frac{c}{X_a}\bigl(d_a(t)^2-C\mathcal E_a\bigr)_+.
}
\tag{5}
\]

Equivalently,

\[
\boxed{
d_a(t)
\le
C\left(\sqrt{X_a\mathcal A_a(t)}+\sqrt{\mathcal E_a}\right).
}
\tag{6}
\]

Since

\[
\frac{\kappa_a^{\rm cap}}{2\pi e^\Delta}
=\frac{X_a}{X_a+\Delta},
\]

(6) also gives the asymptotic threshold modulus

\[
\boxed{
\left(1-\frac{\kappa_a(t)}{2\pi e^\Delta}\right)_+
\le
\frac{\Delta}{X_a}
+C\left(\sqrt{X_a\mathcal A_a(t)}+\sqrt{\mathcal E_a}\right).
}
\tag{7}
\]

Thus `NB-200`'s fixed-gap statement has a quantitative diagonal form. For example, if

\[
\mathcal A_a(t)=O(X_a^{-1-2\gamma})
\]

for a fixed `gamma>0`, then any return in the one-sided endpoint regime must satisfy

\[
2\pi e^\Delta-\kappa_a(t)
=O\!\left(X_a^{-\min\{\gamma,1\}}\right)
\tag{8}
\]

apart from the much smaller Vinogradov--Korobov remainder term. The theorem remains one-sided: it does not construct a return at or above the capacity edge.

## Derivation

### 1. A shrinking top slab has a uniform quantitative source mass

For `0<h<Delta`, let

\[
J_{a,h}:=[x_ae^{\Delta-h},x_ae^\Delta)
\tag{9}
\]

and define the continuous main term

\[
I_a(h)
:=\int_{x_ae^{\Delta-h}}^{x_ae^\Delta}u^{-1-a}\,du
=x_a^{-a}e^{-a\Delta}\frac{e^{ah}-1}{a}.
\tag{10}
\]

Bellotti's prime-number-theorem remainder, in the form already recorded and used in `NB-194`, gives uniformly throughout the fixed multiplicative shell

\[
\psi(u)=u+O\!\left(u\mathcal E_a\right).
\tag{11}
\]

Stieltjes partial summation therefore yields, uniformly for `0<h<Delta`,

\[
\boxed{
\sum_{n\in J_{a,h}}\Lambda(n)n^{-1-a}
=I_a(h)+O(\mathcal E_a).
}
\tag{12}
\]

The important point is that the error in (12) is absolute rather than proportional to `h`; this is exactly why the final stability law contains `sqrt(E_a)` as its resolution floor. Also

\[
D_a=I_a(\Delta)+O(\mathcal E_a)\asymp_{r_0,\Delta}1.
\tag{13}
\]

For `h` sufficiently small but otherwise arbitrary,

\[
I_a(h)\asymp_{r_0,\Delta}h.
\tag{14}
\]

No new short-interval prime theorem is being invoked: (12) follows directly from the quantitative global PNT remainder because the shrinking-slab error is kept explicit.

### 2. Exact atomic capacity of the shrinking slab

Fix the same type of small constant `q>0` used in `NB-200`, and put

\[
\delta_a:=\frac q{X_a}.
\tag{15}
\]

For endpoint ratios bounded below by a fixed `kappa_0>0`, choose `q` small enough that every component of

\[
W_{t,a}:=
\{u\in[x_a,y_a):\operatorname{dist}(t\log u,2\pi\mathbb Z)\le\delta_a\}
\tag{16}
\]

has physical length below one. Hence each favorable component contains at most one integer, and therefore at most one von-Mangoldt atom.

The logarithmic width of `J_(a,h)` is `h`, so the number of favorable components meeting it is at most

\[
N_{a,h}(t)\le\frac{|t|h}{2\pi}+O(1).
\tag{17}
\]

Moreover `Lambda(n)<=log n`, and the function `(log u)u^(-1-a)` is decreasing throughout this large shell. Consequently every atom in `J_(a,h)` has unnormalized mass at most

\[
m_a(h)
:=(X_a+\Delta-h)(x_ae^{\Delta-h})^{-1-a}.
\tag{18}
\]

Ignoring the `O(1)` endpoint cells for a moment, the ratio of the maximal atomic carrying capacity to the PNT main mass is **exactly**

\[
\frac{(|t|h/(2\pi))m_a(h)}{I_a(h)}
=
\frac{\kappa_a(t)}{\kappa_a(h)},
\tag{19}
\]

where

\[
\boxed{
\kappa_a(h)
:=
2\pi e^{\Delta-h}
\frac{X_a}{X_a+\Delta-h}
\frac{1-e^{-ah}}{ah}.
}
\tag{20}
\]

In particular,

\[
\lim_{h\downarrow0}\kappa_a(h)
=2\pi e^\Delta\frac{X_a}{X_a+\Delta}
=\kappa_a^{\rm cap}.
\tag{21}
\]

This identifies the finite-`X_a` edge in (2). It is a **certified one-sided carrying-capacity edge**, not a claim that the actual first return occurs there.

The `O(1)` term in (17) contributes at most

\[
O\!\left(\frac{X_a}{x_a}\right)
\tag{22}
\]

after normalization. This is exponentially smaller than `mathcal E_a` and can be absorbed into the PNT remainder.

### 3. A deficit `d` below capacity creates order-`d^2` missing source mass

The explicit function (20) is smooth at `h=0`, and uniformly for small `a`,

\[
\frac{d}{dh}\log\kappa_a(h)\bigg|_{h=0}
=-1+\frac1{X_a+\Delta}-\frac a2
=-1+o(1).
\tag{23}
\]

Hence there is a fixed `h_0>0` such that, for all sufficiently small `a` and `0<h<h_0`,

\[
\kappa_a(h)
\ge
\kappa_a^{\rm cap}(1-2h).
\tag{24}
\]

Suppose first that `d:=d_a(t)` is small and positive, and choose

\[
h=\frac d4.
\tag{25}
\]

Then (24) gives

\[
\kappa_a(h)
\ge
\kappa_a^{\rm cap}(1-d/2),
\]

while by definition

\[
\kappa_a(t)=\kappa_a^{\rm cap}(1-d).
\]

Therefore

\[
\frac{\kappa_a(t)}{\kappa_a(h)}
\le
\frac{1-d}{1-d/2}
\le1-\frac d2.
\tag{26}
\]

Combining (12), (14), (19), (22), and (26), the normalized source mass in `J_(a,h)` lying **outside** the favorable cells satisfies

\[
\boxed{
\sum_{\substack{n\in J_{a,h}\\ n\notin W_{t,a}}}w_{n,a}
\ge
c_1d^2-C_1\mathcal E_a.
}
\tag{27}
\]

The square is structural. The shrinking slab contains order `h~d` source mass, while the deficit between available atomic capacity and source mass is another factor of order `d`.

If `d` is bounded below by a fixed positive constant, `NB-200` already supplies an order-`1/X_a` chord gap uniformly below a fixed endpoint constant. After changing constants, this is stronger than the `d^2/X_a` bound in (5). Thus (27) is the only new regime needed to prove the full statement.

### 4. Missing mass becomes the quadratic chord gap

Outside `W_(t,a)`,

\[
|e^{-it\log n}-1|
\ge2\sin(\delta_a/2)
\ge\frac q{2X_a}
\tag{28}
\]

for all sufficiently small `a`. Positivity of the Euler weights and (27) now give

\[
\mathcal A_a(t)
\ge
\frac q{2X_a}
\left(c_1d^2-C_1\mathcal E_a\right),
\tag{29}
\]

which proves (5).

If

\[
d^2\le2C\mathcal E_a,
\]

then `d<<sqrt(mathcal E_a)`. Otherwise (5) gives

\[
d^2\ll X_a\mathcal A_a(t).
\]

Combining the two cases proves (6). Finally,

\[
1-\frac{\kappa_a(t)}{2\pi e^\Delta}
=
1-(1-d)\frac{X_a}{X_a+\Delta}
\le
\frac\Delta{X_a}+d,
\tag{30}
\]

which proves (7).

## Stress tests and limits

The theorem does **not** prove that `kappa_a^(cap)` is a sharp return threshold. It is derived from the maximal possible mass per lattice atom, so arithmetic sparsity can only lower the actual capturable mass and push a real return farther out. The result is a one-sided stability statement: approaching a very accurate positive return from below forces the endpoint ratio to approach the certified capacity edge.

Positivity is load-bearing. Equation (27) is a statement about source mass that cannot fit inside favorable cells. A signed or complex synthesis can cancel contributions from distinct cells, so neither the missing-mass estimate nor the quadratic modulus transfers automatically to that setting.

The prime-number-theorem remainder sets the finest scale resolved by this argument. When `d^2` is at or below `mathcal E_a`, the error in the mass of the shrinking slab can be as large as the capacity deficit being tested. Improving (5) below that floor requires stronger local source information, not a sharper rearrangement of the same packing proof.

The finite correction `X_a/(X_a+Delta)` in (2) comes from the elementary atom bound `Lambda(n)<=log n` at the top of the physical shell. It should not be interpreted as a second-order prediction for the first actual return. It merely removes an avoidable `O(1/X_a)` ambiguity when the atomic packing argument itself is diagonalized.

As in `NB-194`--`NB-200`, this remains a source-acquisition theorem. It does not prove that a Nyman--Beurling approximant capable of resolving the target must realize this positive Euler-shell return, and it does not turn the positive source obstruction into a direct lower bound for the optimal Nyman distance.

## Prior-art and novelty audit

The load-bearing external estimate is exactly the quantitative prime-number-theorem remainder already anchored in `research/nyman_beurling/SOURCES.md` and used in `NB-194`. The rest of the proof is Stieltjes partial summation, the elementary bound `Lambda(n)<=log n`, and lattice packing of the logarithmic phase cells.

A focused literature audit covered Bohr/almost-periodic vertical translates of zeta, large-value estimates for Dirichlet polynomials, weighted logarithmic prime-phase distribution, and modern short-interval prime theorems. Those are neighboring frameworks for phase recurrence or source resolution, but no additional theorem is used here and no novelty is claimed for those general mechanisms. The line-local derived content is the exact capacity ratio (19)--(21) for the normalized Euler shell and the resulting quadratic endpoint stability modulus (5)--(7). No `SOURCES.md` change is required.

The mechanism is not uniquely arithmetical in abstract form. Any positive lattice-supported measure with a quantitative macroscopic density law and a comparable pointwise atom cap would inherit an analogous `mass of shrinking slab × relative capacity deficit` square law. What is source-specific here is the von-Mangoldt normalization, its PNT remainder, and the finite edge generated by the `log n` atomic weight on the actual Euler shell.

## Consequence for the research frontier

`NB-200` says that an `o(1/X_a)` positive return cannot remain a fixed distance below `2πe^Delta x_a/X_a`. `NB-201` makes that statement stable: the relative endpoint deficit is controlled by the square root of the normalized chord error, up to the explicit PNT resolution floor and the finite `1/X_a` capacity correction.

This closes the simplest diagonal escape **from below** the atomic threshold. The positive-source frontier is now genuinely at and above capacity: enough phase cells exist there even at the level of the worst-case atom bound, so a further obstruction must use how von-Mangoldt mass actually occupies those cells rather than only how much mass each cell can carry. Independently, the destination bridge and the signed/complex synthesis route remain untouched.