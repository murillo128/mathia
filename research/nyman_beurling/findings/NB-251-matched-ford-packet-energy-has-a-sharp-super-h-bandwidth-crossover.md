# NB-251 — Matched Ford packet energy has a sharp super-`H` bandwidth crossover

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + SHARP-SCALE-REFINEMENT + MATCHED-CONTROL + LARGE-SIEVE-MEAN-SQUARE + METHOD-BOUNDARY + NB-250-REFINEMENT + SOURCE-ONLY + FRESH-PRIOR-ART-AUDIT`.

`NB-250` identifies the Hardy-projected hard Ford second moment with a depth-marked zero form factor on the natural physical carrier band

\[
X+H\operatorname{supp}\phi,
\]

whose width is `Theta(H)=Theta(X/J)`. Its `NB-231` matched packet stays coherent across that whole band. `NB-250` also notes that ordinary **pairwise** separated-frequency orthogonality for zeros spaced at `Theta(1/X)` would require bandwidth `Theta(X)`.

For the normalized Ford-energy target, however, full pairwise orthogonality is stronger than necessary. The same matched packet has a sharper bandwidth crossover:

\[
\boxed{
W=O(H)\quad\Longrightarrow\quad\text{a nonzero energy floor is possible},
}
\]

whereas a carrier band enlarged by any diverging factor,

\[
\boxed{
\frac WH\to\infty,
}
\]

already sends the matched-packet normalized band energy to zero. This may occur while

\[
\frac WX\to0.
\]

Thus the packet obstruction is sharp at the **Ford window frequency scale `H`**, not at the individual carrier-cell resolution scale `X`. Bandwidth `Theta(X)` is needed to make neighboring `1/X`-spaced frequencies genuinely orthogonal one by one; it is not needed merely to make a `Theta(J)`-point packet contribute `o(1)` after the `J^{-2}` Ford normalization.

This does **not** solve the actual zeta problem. The legal Mellin shell in `NB-250` supplies only a fixed-multiple-`H` band, so it sits exactly on the obstructed side of the crossover. Nor do current inputs give a legal operation that thickens the carrier band by a factor tending to infinity while preserving the depth mark and hard Ford window. The result instead removes one overly strong method-boundary interpretation: the `NB-231` packet cannot be used to rule out every mesoscopic carrier thickening `H\ll W\ll X`.

## 1. Isolate the bandwidth-only packet test

Retain the Ford notation from `NB-230`--`NB-250`:

\[
Q:=\log(10+|t_0|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR\asymp1,
\qquad
J:=\frac RH\to\infty.
\tag{1}
\]

Hence

\[
H=\frac{X}{YJ}.
\tag{2}
\]

Take the same carrier-locked packet used in `NB-231` and `NB-250`:

\[
M:=\lfloor\delta J\rfloor,
\qquad
\gamma_j-t_0:=\frac{2\pi qj}{X},
\qquad
0\le j<M,
\tag{3}
\]

where `q>=1` is fixed and `delta>0` is fixed. At the carrier frequency `X`,

\[
e^{iX(\gamma_j-t_0)}=1
\tag{4}
\]

for every packet point.

Put the points at one common bounded Ford depth `d_*`, as in the matched control. Their common Ford coefficient is

\[
c_*:=e^{-r-d_*}.
\tag{5}
\]

To audit **only** the amount of carrier-frequency averaging required to defeat this packet, introduce a dilation factor `B_J>=1` and inspect frequencies

\[
\boxed{
\xi_{J,B}(u):=X+B_JHu,
\qquad u\in[a,b],
\qquad 0<a<b<\infty.
}
\tag{6}
\]

The associated packet exponential sum is

\[
Z_{J,B}(u)
:=
\frac{c_*}{J}
\sum_{j=0}^{M-1}
 e^{i\xi_{J,B}(u)(\gamma_j-t_0)}.
\tag{7}
\]

Using (2)--(4),

\[
\boxed{
Z_{J,B}(u)
=
\frac{c_*}{J}
\sum_{j=0}^{M-1}
\exp\!\left(
\frac{2\pi iqB_Ju}{YJ}j
\right).
}
\tag{8}
\]

For a fixed nonzero smooth weight `phi` supported in `[a,b]`, define the normalized band energy

\[
\boxed{
\mathcal E_J(B_J)
:=
\int_a^b
|\phi(u)|^2|Z_{J,B}(u)|^2\,du.
}
\tag{9}
\]

At `B_J=1`, apart from the harmless common factor `e^{-u\eta_*}=1+o(1)` appearing in `NB-250`, this is exactly the matched-packet contribution to the sufficient carrier-band norm there. The purpose of allowing general `B_J` is not to assert a new Mellin representation; it is to locate sharply the bandwidth at which **this particular adversarial packet** stops being an obstruction.

The physical width of the tested band is

\[
W_J=(b-a)B_JH.
\tag{10}
\]

So `B_J` is, up to the fixed factor `b-a`, precisely `W_J/H`.

## 2. Every fixed-multiple-`H` band retains a positive energy floor

First suppose that along a subsequence

\[
B_J\to B<\infty,
\qquad
Y\to Y_*\in(0,\infty).
\tag{11}
\]

Since `M/J -> delta`, (8) is a Riemann sum. Uniformly for `u` in compact subsets of `(0,\infty)`,

\[
\frac1J
\sum_{j=0}^{M-1}
\exp\!\left(
\frac{2\pi iqB_Ju}{YJ}j
\right)
\longrightarrow
\int_0^\delta
 e^{2\pi iqBux/Y_*}\,dx.
\tag{12}
\]

Write

\[
D_B(u)
:=
\int_0^\delta
 e^{2\pi iqBux/Y_*}\,dx.
\tag{13}
\]

For `B>0`, this is the elementary sinc-type function

\[
D_B(u)
=
\frac{Y_*}{2\pi iqBu}
\left(
 e^{2\pi iqB\delta u/Y_*}-1
\right),
\tag{14}
\]

with the continuous value `delta` at `Bu=0`. It is analytic in `u` and is not identically zero. Its zeros are discrete. Because `phi` is nonzero on a set of positive measure,

\[
\boxed{
\int_a^b
|\phi(u)|^2|D_B(u)|^2\,du>0.
}
\tag{15}
\]

Dominated convergence therefore gives

\[
\boxed{
\mathcal E_J(B_J)
\longrightarrow
|c_*|^2
\int_a^b
|\phi(u)|^2|D_B(u)|^2\,du
>0.
}
\tag{16}
\]

Consequently, if `B_J` fails to tend to infinity, it has a bounded subsequence; after taking a further subsequence in `B_J` and `Y`, the packet energy has a positive limiting floor. Thus

\[
\boxed{
\mathcal E_J(B_J)\to0
\quad\Longrightarrow\quad
B_J\to\infty
}
\tag{17}
\]

for this matched-control family.

This strengthens the fixed-band statement in `NB-250`. The obstruction is not tied to the exact shell interval `[a,b]`: **every carrier band whose width and offset are only a bounded multiple of `H` leaves order-one normalized packet energy**.

## 3. Any diverging band factor kills the packet in mean square

The converse uses only classical separated-frequency mean-square geometry, but at a weaker scale than full pairwise orthogonality.

In the `u` variable, the frequencies in (8) are

\[
\lambda_j
:=
\frac{2\pi qB_J}{YJ}j,
\qquad 0\le j<M.
\tag{18}
\]

Their separation is

\[
\Delta_\lambda
=
\frac{2\pi qB_J}{YJ}.
\tag{19}
\]

The Montgomery--Vaughan separated-frequency mean-square inequality, equivalently the standard Hilbert-inequality estimate for an exponential polynomial on a fixed interval, gives

\[
\int_a^b
\left|
\sum_{j=0}^{M-1}e^{i\lambda_ju}
\right|^2du
\ll_{a,b,q,Y_-,Y_+}
\left(1+\frac{J}{B_J}\right)M,
\tag{20}
\]

uniformly when `Y` stays in a fixed compact subinterval of `(0,\infty)`. Multiplying by `|c_*|^2/J^2` and bounding `|phi|` gives

\[
\begin{aligned}
\mathcal E_J(B_J)
&\ll_\phi
\frac{M}{J^2}
\left(1+\frac{J}{B_J}\right)\\
&\ll
\frac1J+\frac1{B_J}.
\end{aligned}
\tag{21}
\]

Hence

\[
\boxed{
B_J\to\infty
\quad\Longrightarrow\quad
\mathcal E_J(B_J)\to0.
}
\tag{22}
\]

Combining (17) and (22), the bandwidth-only matched-control problem has the sharp criterion

\[
\boxed{
\mathcal E_J(B_J)\to0
\quad\Longleftrightarrow\quad
B_J\to\infty.
}
\tag{23}
\]

In physical variables this is

\[
\boxed{
\frac{W_J}{H}\to\infty.
}
\tag{24}
\]

No condition `W_J/X -> c>0` is required.

There is an even stronger elementary bound in the mesoscopic range

\[
1\ll B_J\ll J.
\tag{25}
\]

Because `u>=a>0`, the geometric-series denominator in (8) is separated from zero at scale `B_J/J`. For large `J`,

\[
\left|
\frac1J
\sum_{j=0}^{M-1}
 e^{2\pi iqB_Juj/(YJ)}
\right|
\ll
\frac1{B_Ju}
\ll_a
\frac1{B_J}.
\tag{26}
\]

Therefore

\[
\boxed{
\mathcal E_J(B_J)
\ll
B_J^{-2}
\qquad
(1\ll B_J\ll J).
}
\tag{27}
\]

So a band can remain far narrower than the carrier scale and nevertheless destroy this coherent packet. For example, choosing

\[
B_J=J^{1/2}
\tag{28}
\]

gives

\[
W_J\asymp HJ^{1/2},
\qquad
\frac{W_J}{X}\asymp J^{-1/2}\to0,
\tag{29}
\]

while (27) gives packet energy `O(J^{-1})`.

## 4. Why this does not contradict the `W~X` resolution scale

`NB-250`'s equation

\[
W\,\Delta\gamma\gtrsim1
\tag{30}
\]

with `Delta gamma ~ 1/X` asks for neighboring packet points to become individually resolvable by the frequency average. That indeed requires

\[
W\gtrsim X.
\tag{31}
\]

The Ford target asks less. There are `M=Theta(J)` coefficients, each of size `Theta(1/J)`. Their diagonal energy is already only `Theta(1/J)`. To prove total normalized energy `o(1)`, one need not make every off-diagonal pair orthogonal; it is enough for the coherent block to break into a number of effective phase cells tending to infinity.

A band of width

\[
W=B_JH
\tag{32}
\]

creates total phase sweep across the full packet of size

\[
W\cdot\operatorname{diam}_\gamma(\mathcal P)
\asymp
B_JH\frac{J}{X}
\asymp
B_J.
\tag{33}
\]

Thus `B_J -> infinity` creates a growing number of aggregate phase cells even though adjacent points still have phase separation

\[
W\Delta\gamma
\asymp
\frac{B_J}{J}
\to0
\tag{34}
\]

whenever `B_J=o(J)`. Equation (21) is exactly the quantitative distinction:

\[
\boxed{
\text{vanishing normalized packet energy needs }W/H\to\infty;
}
\]

\[
\boxed{
\text{individual adjacent-cell orthogonality needs }W/X\gtrsim1.
}
\]

These are different thresholds because the target is a normalized quadratic energy, not reconstruction of every packet coefficient.

## 5. Stress tests and evidence boundary

The result is deliberately narrow.

First, it does **not** weaken the actual obstruction proved in `NB-250`. The legal Hardy-projected Mellin shell has

\[
W=\Theta(H),
\tag{35}
\]

so `B_J=Theta(1)`. It remains on the positive-floor side of (23). Nothing here manufactures the required super-`H` band.

Second, the family (6) is a **bandwidth-only audit**, not a newly derived source representation. A future attempt to realize `B_J -> infinity` must prove that its operation preserves the Ford depth coefficients, the hard selected-height localization, the source normalization, and the order of Hardy projection before squaring. Simply enlarging the Mellin support, changing `H`, or combining unrelated shells may alter those quantities and cannot be imported by analogy.

Third, the upper bound (20) exploits the actual `Theta(1/X)` spacing of the matched packet. Actual zeta zeros are not known to satisfy such a uniform local separation in the critical Ford layer; multiplicities and tighter clusters are not excluded by the inputs currently used in this line. Therefore (22) is **not** a zeta-zero form-factor theorem. A much tighter cluster could remain coherent over a super-`H` band.

Fourth, this result concerns the sufficient carrier-band norm from `NB-250`, not the exact hard-box quadratic form there. The exact hard-box form may contain additional cancellation, but that can only make the sufficient route less necessary, not invalidate the scale calculation above.

Finally, this remains source-side. It does not establish the hard Ford second moment for actual zeros and does not close the bridge to the Nyman--Beurling approximation distance.

## 6. Prior-art audit and route correction

The mathematical engine in (20) is classical. Montgomery and Vaughan, *Hilbert's Inequality*, J. London Math. Soc. (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`, is already recorded in `SOURCES.md` for exactly this separated-frequency geometry. The fixed-`B` limit is only the finite geometric sum/Dirichlet-kernel calculation. A fresh literature check found no reason to treat either harmonic-analysis fact as new.

The current September 2026 short-interval zeta pair-correlation result of Biao Wang, arXiv:2609.07918, was also rechecked. It supplies Montgomery-type pair correlation in short intervals used to study simple/distinct zeros, but it does not provide a selected-height, depth-marked Ford form factor on a controllably thickened band `X+[aW,bW]`, nor does it create the missing legal super-`H` carrier averaging operation. No new durable source dependency is therefore required here.

The line-local mathematical delta is the scale separation. `NB-250` correctly identifies `W~X` as the threshold for **pairwise carrier-cell resolution**, but the matched packet does not justify treating that as the threshold for **Ford-energy decay**. For the normalized quadratic target, its exact obstruction ends at `W=O(H)`; any `W/H -> infinity` defeats that packet even when `W/X ->0`.

This reopens one precise mesoscopic possibility:

\[
\boxed{
H\ll W\ll X.
}
\tag{36}
\]

The next useful question is not whether ordinary frequency averaging can ever beat the matched packet—it can once a super-`H` band is legally available—but whether the Nyman/zeta source architecture can produce such a growing carrier thickening **without losing the depth mark or hard Ford localization**. Until such an operation is derived, the natural fixed shell remains exactly at the sharp obstruction scale.