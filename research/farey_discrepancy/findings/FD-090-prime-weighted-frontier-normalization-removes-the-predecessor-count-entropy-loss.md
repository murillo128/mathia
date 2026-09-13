# FD-090 — prime-weighted frontier normalization removes the predecessor-count entropy loss

**Status:** `EXACT-DERIVED + FALSE-RH-FRONTIER + PRIME-WEIGHTED-NORMALIZED-RECURRENCE + FIXED-STRENGTH-FRONTIER-TRANSPORT + POLYNOMIAL-SCALE-PREDECESSOR + OCCUPATION-COMPOSITION-FRONTIER`.

`FD-089` compresses the positive-energy repeated-prime packet of `FD-088` to canonical physical predecessors

\[
A_p:=\left\lceil\frac Hp\right\rceil,
\qquad p\le H^\alpha,
\]

and obtains a fixed aggregate lower bound over at most `H^alpha` such states. Its final single-state conclusion uses an unweighted pigeonhole, so for fixed `alpha` it loses a factor `H^{-alpha}` and then diagonalizes `alpha\downarrow0` to recover the frontier exponent. That leaves the impression that subpower predecessor complexity is itself responsible for the loss.

It is not. The predecessor family already comes with the correct scale weights. If `M_(p,H)` denotes the **actual masked energy** transported from `V_(A_p,1)` in `FD-089`, then for every fixed `sigma>1/2` the aggregate recurrence implies

\[
\boxed{
\max_{p\le H^\alpha}
\frac{M_{p,H}}{A_p^{2\sigma}}
\ge
\left(
\frac{\eta}{\zeta(2\sigma)-1}-o(1)
\right)
\frac{E_{H,1}}{H^{2\sigma}}.
}
\tag{1}
\]

The reason is simply that `A_p/H=(1+o(1))/p` uniformly over the packet and

\[
\sum_p p^{-2\sigma}<\infty
\qquad(\sigma>1/2).
\]

Thus the `H^alpha` family has **bounded effective entropy after the natural power normalization**. Under false RH, where `Theta>1/2`, one may set `sigma=Theta`. Then one canonical predecessor has a transported coordinate mask whose `2Theta`-normalized energy is a fixed positive fraction of the current horizon's `2Theta`-normalized energy. In particular, for any fixed admissible `alpha>0`, sharp frontier seeds with loss tending to zero produce a predecessor

\[
H^{1-\alpha}\le A_p\le H/2+1
\]

for which both the mask and the full lower state have the complete frontier exponent:

\[
\boxed{
M_{p,H}=A_p^{2\Theta-o(1)},
\qquad
E_{A_p,1}=A_p^{2\Theta-o(1)}.
}
\tag{2}
\]

Therefore diagonalizing `alpha\downarrow0` is **not necessary to preserve the energy exponent**. It is needed only if one specifically wants the lower horizon to remain at scale `H^{1-o(1)}`. The remaining obstruction is sharper: the selected mask need not occupy a fixed fraction of the whole lower state and the lower state need not itself have positive nonsquarefree occupation. The predecessor-count entropy is no longer a separate loss at the frontier-normalized level.

## 1. The load-bearing quantity in `FD-089` is the masked lower-state energy

Retain the false-RH frontier-block setup of `FD-089`, with

\[
\Theta>\frac12,
\qquad
E_{H,1}>H^{2\Theta-\kappa},
\]

and fix an admissible constant `alpha>0`. The repeated-prime truncation and canonical-horizon compression there produce, for primes `p<=H^alpha`, lower horizons

\[
A_p=\left\lceil\frac Hp\right\rceil
\tag{3}
\]

and disjoint lower-coordinate masks `S_(p,H)`. Put

\[
\boxed{
M_{p,H}
:=
\left\|P_{S_{p,H}}V_{A_p,1}\right\|_2^2.
}
\tag{4}
\]

These are not enlarged scalar surrogates. They are exactly the physical lower-state coordinate energies whose unit-weight prime dilations form the compressed packet `C_H` of `FD-089`. Equations (34)--(35) there give

\[
\boxed{
\sum_{p\le H^\alpha}M_{p,H}
\ge
(\eta-o(1))E_{H,1}.
}
\tag{5}
\]

The subsequent inequality `M_(p,H)<=E_(A_p,1)` is useful only after the transport structure in (4)--(5) has been retained. The improvement below is obtained before that enlargement.

Because `alpha<1` is fixed, uniformly for every prime in the packet,

\[
A_p
=
\frac Hp\left(1+O\!\left(\frac pH\right)\right)
=
\frac Hp(1+o(1)).
\tag{6}
\]

The uniformity is important: `p/H<=H^(alpha-1)->0`, so one common `o(1)` applies to the entire predecessor family.

## 2. Power normalization converts the family into a summable prime measure

Fix any constant

\[
\sigma>\frac12
\tag{7}
\]

and define the normalized masked energy

\[
Z_{p,H}^{(\sigma)}
:=
\frac{M_{p,H}}{A_p^{2\sigma}}.
\tag{8}
\]

By (6),

\[
M_{p,H}
=
(1+o(1))H^{2\sigma}p^{-2\sigma}
Z_{p,H}^{(\sigma)}
\tag{9}
\]

uniformly over `p<=H^alpha`. Therefore (5) implies

\[
(\eta-o(1))\frac{E_{H,1}}{H^{2\sigma}}
\le
(1+o(1))
\sum_{p\le H^\alpha}
 p^{-2\sigma}Z_{p,H}^{(\sigma)}.
\tag{10}
\]

Since primes are a subset of the integers `n>=2`,

\[
\sum_p p^{-2\sigma}
\le
\sum_{n=2}^{\infty}n^{-2\sigma}
=
\zeta(2\sigma)-1
<\infty.
\tag{11}
\]

Taking the largest normalized mask in (10) proves (1):

\[
\boxed{
\max_{p\le H^\alpha}Z_{p,H}^{(\sigma)}
\ge
\left(
\frac{\eta}{\zeta(2\sigma)-1}-o(1)
\right)
\frac{E_{H,1}}{H^{2\sigma}}.
}
\tag{12}
\]

This is a weighted pigeonhole, but unlike the cardinality pigeonhole in `FD-089` its constant does not deteriorate with `H^alpha`. The factor `p^{-2sigma}` is exactly the geometric cost of moving the horizon from `H` to `H/p`; summability begins at the same threshold `sigma>1/2` that separates the false-RH frontier from the critical endpoint.

Because the mask is a positive coordinate sub-energy,

\[
M_{p,H}\le E_{A_p,1},
\tag{13}
\]

the same selected prime also obeys

\[
\boxed{
\frac{E_{A_p,1}}{A_p^{2\sigma}}
\ge
\left(
\frac{\eta}{\zeta(2\sigma)-1}-o(1)
\right)
\frac{E_{H,1}}{H^{2\sigma}}.
}
\tag{14}
\]

Thus the scalar lower state inherits the same fixed-strength normalized lower bound, but (12) is the stronger transport statement: the energy is already present on the exact mask used by the prime-dilation carrier.

## 3. At `sigma=Theta`, fixed `alpha` already preserves the full frontier exponent

Assume `Theta>1/2` and specialize (12) to

\[
\sigma=\Theta.
\tag{15}
\]

The series in (11) is then finite. For every fixed occupation level `eta>0` used in the `FD-088`--`FD-089` packet, there is therefore a constant

\[
c_{\Theta,\eta}>0
\tag{16}
\]

such that, on all sufficiently sharp frontier blocks,

\[
\boxed{
\frac{M_{p,H}}{A_p^{2\Theta}}
\ge
c_{\Theta,\eta}
\frac{E_{H,1}}{H^{2\Theta}}
}
\tag{17}
\]

for at least one canonical prime contraction `A_p`.

Now keep `alpha` fixed instead of sending it to zero. As in `FD-089`, the frontier seed loss `kappa` can be chosen arbitrarily small before each extraction. Choose a sequence of such blocks with

\[
\kappa_j\to0,
\qquad
E_{H_j,1}>H_j^{2\Theta-\kappa_j},
\tag{18}
\]

and let `A_j=A_(p_j)` be selected by (17). Since

\[
H_j^{1-\alpha}\le A_j\le H_j/2+1,
\tag{19}
\]

one has

\[
\frac{\log H_j}{\log A_j}
\le
\frac1{1-\alpha}+o(1).
\tag{20}
\]

Equations (17)--(20) yield

\[
M_{p_j,H_j}
\ge
c_{\Theta,\eta}
A_j^{2\Theta}H_j^{-\kappa_j}
=
A_j^{2\Theta-o(1)}.
\tag{21}
\]

On the other hand `M_(p_j,H_j)<=E_(A_j,1)`, while the zero-frontier upper envelope of `FD-046` gives

\[
E_{A_j,1}\le A_j^{2\Theta+o(1)}.
\tag{22}
\]

Therefore

\[
\boxed{
M_{p_j,H_j}=A_j^{2\Theta-o(1)},
\qquad
E_{A_j,1}=A_j^{2\Theta-o(1)}
}
\tag{23}
\]

in the usual frontier-exponent sense. The lower state is a genuine full-frontier-energy horizon even when `alpha` is fixed and the contraction is allowed to be polynomial.

This sharpens the interpretation of `FD-089`. Its unweighted estimate

\[
E_{A_p,1}\ge H^{-\alpha}E_{H,1}
\]

mixes two different effects: the physical scale change and the number of candidate primes. Equation (17) divides out the physical scale change first. After that normalization, the candidate family costs only the finite mass `sum_p p^(-2Theta)` and no asymptotic predecessor-count entropy remains.

## 4. Critical endpoint and stress tests

The threshold `sigma>1/2` is exact for this normalization argument. At `sigma=1/2`, the infinite comparison in (11) diverges and no `H`-independent constant follows. The finite packet still gives an elementary endpoint estimate. From

\[
\sum_{p\le H^\alpha}\frac1p
\le
\sum_{2\le n\le H^\alpha}\frac1n
\le
\alpha\log H+O(1),
\tag{24}
\]

one gets

\[
\boxed{
\max_{p\le H^\alpha}
\frac{M_{p,H}}{A_p}
\gg_{\alpha,\eta}
\frac1{\log H}
\frac{E_{H,1}}H.
}
\tag{25}
\]

So the mechanism degenerates only by a logarithmic factor under this elementary estimate, but the fixed-strength statement (17) is genuinely a `Theta>1/2` phenomenon. In particular, (17) must not be read as an RH proof or continued formally to `Theta=1/2`.

Several other boundaries remain essential.

First, (17) is **frontier-normalized**, not a fixed raw overlap at the parent scale. Rewriting it gives only

\[
M_{p,H}
\gg
E_{H,1}\left(\frac{A_p}{H}\right)^{2\Theta}
\asymp
p^{-2\Theta}E_{H,1}.
\tag{26}
\]

If the selected prime grows, this current-scale share may tend to zero. What has disappeared is the additional loss caused solely by counting the predecessor family.

Second, (23) does not imply a fixed lower-state mask fraction. Both `M_(p,H)` and `E_(A_p,1)` have exponent `2Theta`, but their ratio may still be `A_p^{-o(1)}`. A theorem requiring a fixed projective overlap therefore still needs new input.

Third, the selected lower mask need not be nonsquarefree. In `FD-089`, an original row `r` with `p^2|r` is deflated to `s=r/p`; when `v_p(r)=2` and the remaining factors are squarefree, `s` itself is squarefree. Hence neither (12) nor (23) supplies

\[
U_{A_p,1}\gg E_{A_p,1}.
\]

The occupation/eligibility problem required for recursive use of the packet remains open.

Finally, the argument uses the actual masked identity from `FD-089`; replacing (5) by an arbitrary scalar inequality over unrelated lower states would discard the transport content of (12). The conclusion is source-specific through the preceding `FD-088`--`FD-089` construction even though the final weighted pigeonhole is elementary.

## 5. Prior-art boundary and research consequence

A targeted audit covered the classical Franel--Landau/Farey--Mertens literature, Smith/Jordan GCD-matrix factorization, Jordan-totient multiplicativity, square-divisor dilations, and recent work on Farey local discrepancy and restricted-denominator Farey sequences. Those sources contain the individual Farey/Mertens bridges, Jordan Euler factors, and classical discrepancy estimates, but the search did not locate the Mathia-specific object used here: a row-adaptive nonsquarefree Schur packet first compressed to canonical prime contractions and then normalized by the contraction scale before pigeonholing. No priority claim is inferred from absence of a search hit.

No new external theorem is load-bearing. The convergence in (11) is the elementary absolutely convergent zeta series for `2sigma>1`; the source-specific inputs are already canonical in `FD-046`, `FD-088`, and `FD-089`. `SOURCES.md` therefore requires no update.

The live frontier is now narrower than stated at the end of `FD-089`. **Energy entropy is not what prevents composition.** For every fixed admissible contraction band there is a canonical predecessor whose transported mask preserves the parent's frontier-normalized energy with a fixed constant, and along sharp false-RH blocks that mask already has the full `2Theta` exponent at the lower scale. What is still missing is one of two genuinely stronger statements: either a fixed lower-state mask/occupation fraction that makes this carrier recursively eligible, or a composition theorem that can use frontier-normalized carriers whose raw overlap is only the unavoidable scale factor `p^(-2Theta)`.