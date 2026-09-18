# NB-202 — Integer-lattice discrepancy pushes positive Euler returns to the quadratic shell scale

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + POSITIVE-EULER + INTEGER-DISCREPANCY + NB-199--NB-201-REFINEMENT`.

`NB-200` and `NB-201` refine the positive Euler-shell obstruction at the logarithmic endpoint `|t|~x_a/X_a`. Their atomic argument counts favorable phase cells and uses the maximal possible von-Mangoldt mass carried by one integer. That is deliberately worst-case: once the number of cells reaches the number of available prime-sized atoms, the capacity argument stops even if most favorable cells contain no integer at all.

The integer carrier itself supplies another deterministic obstruction. At the angular resolution `1/X_a` relevant to an `o(1/X_a)` positive return, the sequence

\[
\frac{t\log n}{2\pi}\pmod 1,
\qquad x_a\le n<e^\Delta x_a,
\]

has small discrepancy throughout a much larger coupled-frequency corridor. Erdős--Turán reduces the count of favorable integers to exponential sums `sum n^(imt)`, and van der Corput's second-derivative test controls those sums uniformly. Since every von-Mangoldt atom is carried by an integer and has normalized mass `O(X_a/x_a)`, this integer-level discrepancy already prevents almost all positive Euler mass from fitting into the favorable phase windows.

Keep the notation

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

Then there are constants `C_0,c_0,c_1>0`, depending only on the fixed shell parameters `r_0,Delta`, such that for all sufficiently small `a`,

\[
\boxed{
C_0X_a^2\le |t|\le c_0\frac{x_a^2}{X_a^3}
\quad\Longrightarrow\quad
\mathcal A_a(t)\ge\frac{c_1}{X_a}.
}
\tag{1}
\]

Combining (1) with the lower-frequency corridor already supplied by `NB-199` gives, after changing constants,

\[
\boxed{
X_a^2\le |t|\le c_0\frac{x_a^2}{X_a^3}
\quad\Longrightarrow\quad
\mathcal A_a(t)\gg\frac1{X_a}.
}
\tag{2}
\]

Consequently, any positive return sequence in this high-ordinate regime with

\[
X_a\mathcal A_a(t_a)\longrightarrow0
\]

must satisfy

\[
\boxed{
|t_a|\gg\frac{x_a^2}{X_a^3}.
}
\tag{3}
\]

This moves the one-sided positive-return obstruction by the diverging factor `x_a/X_a^2` beyond the atomic endpoint `x_a/X_a`. The scale `x_a^2/X_a^3` is the reach of this particular second-derivative discrepancy argument, not a claim about the true first-return scale.

## 1. Count favorable integers before counting prime mass

Fix a small constant `q>0` and define the favorable integer carrier

\[
E_{a,t}(q)
:=
\left\{
n\in\mathbb Z\cap[x_a,y_a):
\operatorname{dist}(t\log n,2\pi\mathbb Z)\le\frac q{X_a}
\right\}.
\tag{4}
\]

Put

\[
\theta_n:=\frac{t\log n}{2\pi}.
\]

Condition (4) says that `theta_n mod 1` lies in an arc of length

\[
\ell_a(q)=\frac{q}{\pi X_a}.
\tag{5}
\]

Let

\[
N_a:=\#(\mathbb Z\cap[x_a,y_a))\asymp_\Delta x_a.
\]

The one-dimensional Erdős--Turán discrepancy inequality with truncation parameter `M>=1` gives

\[
\#E_{a,t}(q)
\le
\ell_a(q)N_a
+C\left(
\frac{N_a}{M}
+
\sum_{1\le m\le M}\frac{|S_m(t)|}{m}
\right),
\tag{6}
\]

where

\[
S_m(t)
:=
\sum_{x_a\le n<y_a}e^{im t\log n}.
\tag{7}
\]

No prime information has entered yet. Equation (6) is a statement about how many **integers** can lie in all the favorable logarithmic phase windows.

## 2. The logarithmic carrier has a uniform second-derivative discrepancy bound

For a fixed harmonic `m`, write the phase in the `e(u)=e^{2\pi iu}` convention as

\[
f_m(u)=\frac{mt}{2\pi}\log u.
\]

Throughout the fixed multiplicative shell `[x_a,y_a]`,

\[
|f_m''(u)|
=\frac{m|t|}{2\pi u^2}
\asymp_\Delta
\frac{m|t|}{x_a^2}.
\tag{8}
\]

Van der Corput's second-derivative test therefore yields

\[
\boxed{
|S_m(t)|
\ll_\Delta
\sqrt{m|t|}
+
\frac{x_a}{\sqrt{m|t|}}.
}
\tag{9}
\]

Choose

\[
M=\left\lfloor\frac{X_a}{q}\right\rfloor.
\tag{10}
\]

Summing (9) with the Erdős--Turán weights gives

\[
\sum_{m\le M}\frac{|S_m(t)|}{m}
\ll_\Delta
\sqrt{|t|M}
+
\frac{x_a}{\sqrt{|t|}},
\tag{11}
\]

because

\[
\sum_{m\le M}m^{-1/2}\ll\sqrt M,
\qquad
\sum_{m\ge1}m^{-3/2}<\infty.
\]

Substituting (5), (10), and (11) into (6) produces the carrier count

\[
\boxed{
\#E_{a,t}(q)
\ll_\Delta
\frac{q x_a}{X_a}
+
\sqrt{\frac{|t|X_a}{q}}
+
\frac{x_a}{\sqrt{|t|}}.
}
\tag{12}
\]

This is the step unavailable to the pure atomic-capacity argument of `NB-200`--`NB-201`. Counting phase cells alone costs `~|t|`; (12) measures how often those cells actually hit the integer lattice.

## 3. Integer discrepancy bounds the positive Euler mass in favorable cells

The prime-number theorem already used throughout `NB-194`--`NB-201` gives

\[
D_a\asymp_{r_0,\Delta}1.
\tag{13}
\]

Also, for every integer in the shell,

\[
\Lambda(n)n^{-1-a}
\le
(X_a+\Delta)x_a^{-1-a}
\ll_{r_0,\Delta}
\frac{X_a}{x_a}.
\tag{14}
\]

Hence every normalized von-Mangoldt atom satisfies

\[
w_{n,a}\ll_{r_0,\Delta}\frac{X_a}{x_a}.
\tag{15}
\]

Combining (12) and (15), the total normalized source mass that can lie in favorable integer cells obeys

\[
\boxed{
\sum_{n\in E_{a,t}(q)}w_{n,a}
\ll_{r_0,\Delta}
q
+
\frac{X_a}{x_a}
\sqrt{\frac{|t|X_a}{q}}
+
\frac{X_a}{\sqrt{|t|}}.
}
\tag{16}
\]

This estimate automatically includes prime powers: they cannot evade it because they are still integer-supported and satisfy `Lambda(n)<=log n`.

Choose `q>0` first, sufficiently small that the first term on the right of (16) is below, say, `1/6`. Then choose `C_0` sufficiently large and `c_0` sufficiently small so that

\[
|t|\ge C_0X_a^2
\quad\Longrightarrow\quad
\frac{X_a}{\sqrt{|t|}}\le\frac1{6C},
\tag{17}
\]

and

\[
|t|\le c_0\frac{x_a^2}{X_a^3}
\quad\Longrightarrow\quad
\frac{X_a}{x_a}
\sqrt{\frac{|t|X_a}{q}}
\le\frac1{6C},
\tag{18}
\]

where `C` absorbs the fixed constants in (16). For all sufficiently small `a`, (16)--(18) imply

\[
\sum_{n\in E_{a,t}(q)}w_{n,a}\le\frac12.
\tag{19}
\]

At least half of the positive Euler mass therefore lies outside the favorable phase windows.

For every such outside atom,

\[
|e^{-it\log n}-1|
\ge
2\sin\frac{q}{2X_a}
\gg_q\frac1{X_a}.
\tag{20}
\]

Positivity of the weights and (19) now give

\[
\mathcal A_a(t)
\ge
2\sin\frac{q}{2X_a}
\sum_{n\notin E_{a,t}(q)}w_{n,a}
\gg\frac1{X_a},
\tag{21}
\]

which proves (1).

A slightly more informative pre-asymptotic form is

\[
\boxed{
\mathcal A_a(t)
\gg
\frac{q}{X_a}
\left[
1-C\left(
q+
\frac{X_a}{x_a}\sqrt{\frac{|t|X_a}{q}}
+
\frac{X_a}{\sqrt{|t|}}
\right)
\right]_+.
}
\tag{22}
\]

The two error terms in (22) display the method's natural frequency window directly. The low-frequency loss disappears once `|t|/X_a^2` is large; the high-frequency loss remains small while `|t|X_a^3/x_a^2` is small.

## 4. Coupled source-height consequence

At the old atomic endpoint

\[
|t|\asymp\frac{x_a}{X_a},
\]

both discrepancy errors in (22) vanish exponentially in `X_a`. Thus an `o(1/X_a)` positive return is not merely forced toward the finite capacity edge of `NB-201`: it is excluded throughout every bounded endpoint ratio, and much farther beyond it.

For a physical height block `[T,2T]`, a necessary condition for an `o(1/X_a)=o(a)` positive return supplied by this shell is therefore

\[
T\gg\frac{x_a^2}{X_a^3}
\tag{23}
\]

up to fixed constants. Since `x_a=e^{X_a}`, (23) implies

\[
\log T
\ge
2X_a-3\log X_a+O(1).
\tag{24}
\]

Inverting gives

\[
\boxed{
X_a
\le
\frac12\log T
+
\frac32\log\log T
+O(1),
}
\tag{25}
\]

or equivalently

\[
\boxed{
a
\ge
\frac{2r_0}{\log T+3\log\log T+O(1)}.
}
\tag{26}
\]

Thus this positive-shell acquisition test doubles the leading logarithmic width constant relative to what one would infer from the atomic scale `x_a/X_a` alone. Equation (26) is still only a **necessary acquisition condition** under the positive-return hypothesis; it is not a Nyman distance theorem.

## Stress tests and limits

The argument does not assume that favorable cells contain primes with any particular density. It proves something weaker but more robust first: there are too few favorable **integers** at angular width `q/X_a`. Since every prime and prime power is an integer, no adversarial placement of von-Mangoldt mass can beat (16) while the pointwise atom cap (15) holds.

The result does not contradict the classical fact that `alpha log n mod 1` need not be uniformly distributed when `alpha` is fixed. Here the coefficient `t` grows with the shell scale, and the coupled phase has second derivative `~mt/x_a^2`; (12) is a finite-scale discrepancy estimate in that growing-frequency regime.

The upper scale `x_a^2/X_a^3` is a method boundary. It is where the `sqrt{|t|M}` term from the second-derivative estimate becomes large enough, after the `X_a/x_a` atom normalization, to consume a constant fraction of the source mass. Higher-derivative methods, a sharper treatment of `sum n^(imt)`, or genuine prime-specific occupancy could extend the corridor. Nothing here constructs a return immediately above that scale.

Positivity remains load-bearing. Equation (19) says that a positive amount of source mass lies outside the favorable windows, and (21) turns that mass directly into chord defect. A signed or complex synthesis may cancel contributions across different phase sectors and is not controlled by this argument.

As in `NB-194`--`NB-201`, the result is source-acquisition only. It does not prove that a successful Nyman--Beurling approximant must realize an `o(a)` positive Euler-shell return, and it does not establish a lower bound for the optimal Nyman distance.

## Prior-art and novelty audit

The two analytic tools used in (6) and (9) are classical: the one-dimensional Erdős--Turán discrepancy inequality and van der Corput's second-derivative estimate for exponential sums. They are added to `research/nyman_beurling/SOURCES.md` as explicit load-bearing anchors. No novelty is claimed for either tool or for generic discrepancy estimates of logarithmic sequences.

The line-local derived content is their coupling to the normalized von-Mangoldt shell: the favorable-integer count (12), the source-mass capacity estimate (16), and the resulting return-free corridor through `x_a^2/X_a^3`. A focused literature search found extensive work on discrepancy, van der Corput sums, and distribution modulo one for logarithmic sequences, but no source was used that already supplies this Euler-shell acquisition consequence.

The representation audit is deliberately unfavorable to an arithmetic novelty claim. The mechanism is more general than von Mangoldt: any positive measure supported on consecutive integers in a fixed multiplicative shell, with total mass bounded below and point masses `O(X/x)`, inherits the same obstruction. The specifically arithmetic ingredients are only that the Euler shell satisfies those hypotheses and that its target return is the source quantity under study. Therefore this finding should be read as a **carrier-geometry obstruction**, not as new prime-distribution technology.

## Consequence for the research frontier

`NB-200`--`NB-201` showed that cell count plus maximal atom mass controls positive returns up to a finite endpoint edge. `NB-202` shows that this was not the real end of deterministic coercivity: once actual intersection with the integer carrier is counted, `o(1/X_a)` positive returns are excluded through the much larger scale `x_a^2/X_a^3`.

The next positive-source question is now sharper. One can try to extend the integer-phase discrepancy beyond the second-derivative window, perhaps by a higher-derivative/exponent-pair treatment, or introduce genuine von-Mangoldt occupancy to improve on the all-integers carrier bound. Any claimed improvement must distinguish a true source effect from a better generic discrepancy estimate. The independent destination bridge and signed/complex synthesis problems remain unchanged.