# RE-154 — sqrt(p)/log(p) post-selector relocations move the Pareto Robin source by order one

**Status:** `EXACT-DERIVED + MATCHED-SYNTHETIC-SOURCE-OBSTRUCTION + BOUNDED-MULTIPLICATIVE-SELECTOR-BARRIER + PNT-STABLE + PRIOR-ART-BOUNDED`. `RE-153` shows that a regular self-tangent Robin counterexample with selected first-layer frontier prime `p` must satisfy a canonical Pareto-weighted Chebyshev-deficit average at least `sqrt(2)-o(1)`, and that every fixed multiplicative cutoff `Bp` leaves positive kernel mass beyond the cutoff. The residual mass is not merely a formal tail: an asymptotically vanishing fraction of prime-like labels placed strictly **after** any fixed cutoff `Bp` can move that normalized source average by an arbitrary fixed amount while leaving the entire source and generalized CA event history below `Bp` unchanged.

Fix

\[
1<B<C,
\qquad
0<\delta<C-B,
\qquad
a>0,
\tag{1}
\]

and retain the `RE-153` annulus, weight and probability measure

\[
J_p=[p+p^\alpha,U_A(p)],
\qquad
w_p(t)=\sqrt p\log p\,\sqrt t\,(-h'(t)),
\qquad
\nu_p(dt)=\frac{w_p(t)}{Z_p}\,dt,
\tag{2}
\]

where

\[
h(t)=\frac{-\log(1-t^{-1})}{\log t},
\qquad
Z_p=2+o(1).
\tag{3}
\]

For an increasing real label sequence `Q`, define its first-layer Chebyshev source

\[
\vartheta_Q(t):=\sum_{q\in Q,\ q\le t}\log q
\tag{4}
\]

and the normalized Robin source coordinate

\[
\mathcal A_p(Q)
:=
\int_{J_p}
\frac{t-\vartheta_Q(t)}{\sqrt t}
\,d\nu_p(t).
\tag{5}
\]

Let `P` denote the ordinary primes. For every sufficiently large `p`, put

\[
m_p:=\left\lfloor\frac{a\sqrt p}{\log p}\right\rfloor.
\tag{6}
\]

There exist two increasing real prime-like controls `Q_p^+` and `Q_p^-`, each obtained from `P` by exactly `m_p` deletions and `m_p` insertions inside the fixed shell

\[
[Bp,(C+\delta)p],
\tag{7}
\]

such that both controls agree **exactly** with the ordinary primes below `Bp`, yet

\[
\boxed{
\liminf_{p\to\infty}
\bigl(\mathcal A_p(Q_p^+)-\mathcal A_p(P)\bigr)
\ge
\frac a2
\left(
\frac1{B+\delta}-\frac1C
\right)>0,
}
\tag{8}
\]

while

\[
\boxed{
\limsup_{p\to\infty}
\bigl(\mathcal A_p(Q_p^-)-\mathcal A_p(P)\bigr)
\le
-\frac a2
\left(
\frac1B-\frac1C
\right)<0.
}
\tag{9}
\]

Thus the amplitude `a` can move the selected Pareto source by an arbitrarily prescribed fixed amount in either direction. The required surgery uses only

\[
\boxed{m_p\asymp\frac{\sqrt p}{\log p}}
\tag{10}
\]

labels. Relative to the `asymp p/log p` ordinary labels in a fixed proportional shell, this is a fraction `asymp p^(-1/2)`.

The controls remain PNT-dense and differ from the ordinary Chebyshev source by only square-root size on the affected shell:

\[
\boxed{
\sup_x|\pi_{Q_p^\pm}(x)-\pi(x)|\le m_p,
\qquad
\sup_x|\vartheta_{Q_p^\pm}(x)-\vartheta(x)|
\ll_{a,B,C,\delta}\sqrt p.
}
\tag{11}
\]

After the shell has been passed, the counting discrepancy is exactly zero and the residual Chebyshev discrepancy is only `O(sqrt(p)/log p)`. Hence each control has the same prime-number-theorem asymptotics as the ordinary primes, and the family preserves every coarse source envelope that is stable under an added `O(sqrt x)` perturbation at the selected scale.

Consequently, a bounded-multiplicative selector theorem cannot close the `RE-153` barrier merely by combining exact source knowledge through `Bp` with PNT density or a qualitative prime-error envelope. A successful implication must use arithmetic coupling that the surgery deliberately breaks: propagation through multiplicative scales tending to infinity, a sharp signed/constant-level source estimate, or genuinely ordinary-prime/CA structure tying the future shell back to the selected state.

## 1. One label has an exact Robin-kernel influence

Adding one label `q` to a source changes `vartheta_Q(t)` by `log(q)` for every `t>=q`. Its contribution to (5) is therefore the negative of

\[
\Lambda_p(q)
:=
\frac{\log q}{Z_p}
\int_q^{U_A(p)}
\frac{w_p(t)}{\sqrt t}\,dt.
\tag{12}
\]

The special form of the `RE-153` weight makes this influence exact. Since

\[
\frac{w_p(t)}{\sqrt t}
=
\sqrt p\log p\,(-h'(t)),
\tag{13}
\]

we have

\[
\boxed{
\Lambda_p(q)
=
\frac{\sqrt p\log p}{Z_p}
\log q\,
\bigl(h(q)-h(U_A(p))\bigr).
}
\tag{14}
\]

Moreover

\[
\log q\,h(q)
=-\log(1-q^{-1})
=
\frac1q+O(q^{-2}).
\tag{15}
\]

Because `U_A(p)` grows faster than every fixed power of `p`, its contribution in (14) is negligible uniformly for `q/p` in a fixed compact subset of `(1,infinity)`. Combining (3), (14), and (15), for every fixed compact `K subset (1,infinity)` one obtains uniformly for `y in K`

\[
\boxed{
\Lambda_p(yp)
=
\frac{\log p}{2\sqrt p}
\frac1y
+o_K\!\left(\frac{\log p}{\sqrt p}\right).
}
\tag{16}
\]

Equation (16) is the discrete sensitivity law hidden in the Pareto kernel. One post-selector label at multiplicative location `y` has influence of order `log(p)/sqrt(p)`; therefore `sqrt(p)/log(p)` coherent relocations have order-one leverage.

## 2. Construct the positive-shift control

For fixed `B,C,delta`, the ordinary PNT gives `asymp p/log p` primes in each fixed proportional interval `[Bp,(B+delta)p]` and `[Cp,(C+delta)p]`. Since `m_p=o(p/log p)`, there are more than `m_p` ordinary primes in both intervals for all sufficiently large `p`.

To construct `Q_p^+`, delete any `m_p` ordinary primes

\[
r_i\in[Bp,(B+\delta)p]
\qquad(1\le i\le m_p),
\tag{17}
\]

and insert `m_p` distinct non-prime real labels

\[
s_i\in[Cp,Cp+1].
\tag{18}
\]

All changes occur after `Bp`. Adding a label decreases `A_p` by its `Lambda_p` influence, while deleting one increases it, hence

\[
\mathcal A_p(Q_p^+)-\mathcal A_p(P)
=
\sum_{i=1}^{m_p}
\bigl(\Lambda_p(r_i)-\Lambda_p(s_i)\bigr).
\tag{19}
\]

Using (16), uniformly over (17)--(18),

\[
\Lambda_p(r_i)
\ge
\frac{\log p}{2\sqrt p}
\frac1{B+\delta}
+o\!\left(\frac{\log p}{\sqrt p}\right),
\tag{20}
\]

and

\[
\Lambda_p(s_i)
=
\frac{\log p}{2\sqrt p}
\frac1C
+o\!\left(\frac{\log p}{\sqrt p}\right).
\tag{21}
\]

Multiplying the positive influence gap by (6) proves (8).

The interpretation is simple but important: moving only `m_p` labels from an early post-selector shell to a later shell increases the Chebyshev deficit seen by the Robin kernel by a fixed amount, even though the moved proportion tends to zero.

## 3. Construct the negative-shift control

For `Q_p^-`, reverse the direction. Insert `m_p` distinct real labels

\[
q_i\in[Bp,Bp+1]
\tag{22}
\]

and delete any `m_p` ordinary primes

\[
s_i\in[Cp,(C+\delta)p].
\tag{23}
\]

Then

\[
\mathcal A_p(Q_p^-)-\mathcal A_p(P)
=-
\sum_{i=1}^{m_p}
\bigl(\Lambda_p(q_i)-\Lambda_p(s_i)\bigr).
\tag{24}
\]

Equation (16) gives

\[
\Lambda_p(q_i)
=
\frac{\log p}{2\sqrt p}
\frac1B
+o\!\left(\frac{\log p}{\sqrt p}\right),
\tag{25}
\]

while `s_i>=Cp` implies

\[
\Lambda_p(s_i)
\le
\frac{\log p}{2\sqrt p}
\frac1C
+o\!\left(\frac{\log p}{\sqrt p}\right).
\tag{26}
\]

Equations (6) and (24)--(26) prove (9). Since `a` is arbitrary but fixed, the two controls allow any fixed order-one displacement by increasing `a` while the relative fraction of modified labels still tends to zero.

## 4. The surgery preserves PNT-scale density and all pre-cutoff selector data

At every `x`, at most `m_p` labels have been inserted without their compensating deletion, or vice versa. This proves the counting part of (11). The largest logarithmic weight of any changed label is `log p+O(1)`, so throughout the shell

\[
|\vartheta_{Q_p^\pm}(x)-\vartheta(x)|
\le
m_p(\log p+O(1))
=O_{a,B,C}(\sqrt p),
\tag{27}
\]

which is the second part of (11).

After all `m_p` insertions and deletions have occurred, the leading `log p` parts cancel because the two changed sets have equal cardinality. Every paired logarithmic difference is only `O_{B,C}(1)`, hence

\[
\boxed{
\vartheta_{Q_p^\pm}(x)-\vartheta(x)
=O_{a,B,C}\!\left(\frac{\sqrt p}{\log p}\right)
\qquad
(x>(C+\delta)p).
}
\tag{28}
\]

For each fixed `p` the control is only a finite modification of the ordinary prime source. More importantly for a matched asymptotic test, at the affected scale its relative counting disturbance is

\[
\frac{m_p}{p/\log p}
=O_a(p^{-1/2})
\longrightarrow0,
\tag{29}
\]

and its relative Chebyshev disturbance is `O(p^(-1/2))`. Thus PNT-scale density does not see the relocation even though the Pareto source coordinate does.

The selector is matched more strongly than density alone. Both `Q_p^+` and `Q_p^-` equal the ordinary prime set **exactly** on `(1,Bp)`. In the generalized CA event map already used for matched controls in `RE-055`, every event generated by a label `q` lies to the right of `q` for sufficiently large `q`: indeed `lambda_1(q)<1/q` gives `eta_1(q)log eta_1(q)>q log q`, and deeper-layer slopes are smaller still. Therefore modifying only labels `q>=Bp` cannot alter the generalized event staircase below `Bp`.

So a self-tangent selector located at scale `p`—and even any argument that inspects a fixed continuation of the source through `Bp`—receives identical local label/event information from the ordinary source and from these controls. The order-one difference enters only through the later source history consumed by the Robin height kernel.

## 5. What the control actually rules out

`RE-153` by itself showed that the normalized kernel has tail mass `B^(-1/2)` after `Bp`. Conceivably that tail could still have been harmless because PNT density or a generic prime-error envelope rigidly constrained its signed values. Equations (8)--(11) rule out that repair at the corresponding information level.

For every fixed `B`, the source beyond `Bp` can be changed by a vanishing fraction of labels while preserving:

- exact ordinary-prime data below `Bp`;
- the full generalized CA event history below that cutoff;
- PNT-scale counting and Chebyshev density;
- any qualitative error class stable under adding an `O(sqrt x)` disturbance at the selected scale.

Yet the target average changes by a fixed amount. Hence no implication whose only future input consists of those coarse properties can force

\[
\mathcal A_p(P)\le\sqrt2-\eta
\tag{30}
\]

from a bounded-multiplicative selector neighborhood.

This is an information obstruction, not a statement that the ordinary primes permit the surgery. A theorem using a **sharp** square-root constant, a sign constraint, a correlation law, the actual zeta Euler product, or exact global CA consistency can distinguish the controls. Those are precisely stronger source couplings than the PNT-density/local-selector package tested here.

The fixed-cutoff qualifier is also load-bearing. The argument does not rule out a selector theorem whose controlled multiplicative radius `B=B(p)` tends to infinity. In that regime the single-label influence decays like `1/B`, and the necessary relocation count changes. `RE-154` therefore narrows the required propagation scale rather than proving that all selector-to-height propagation is impossible.

## 6. Prior-art and matched-control boundary

Increasing real generalized-prime labels are classical Beurling objects, and `RE-055` already uses exactly this kind of one-source real-label control to test which CA event constraints are genuinely ordinary-prime rigid. No novelty is claimed for generalized primes, for finite modification preserving the PNT, or for the elementary fact that a vanishing relative density perturbation can alter a weighted functional.

A targeted literature audit over generalized-prime Chebyshev functions, Mertens products, and Robin-type criteria did not locate the specific `sqrt(p)/log(p)` relocation law (16)--(26) for the self-tangent Pareto kernel. No external theorem is load-bearing: the influence formula is an exact integration of the canonical `RE-153` weight, and the existence of enough ordinary labels in fixed proportional intervals needs only the ordinary PNT already implicit throughout the line. No `SOURCES.md` update is therefore required.

The synthetic controls are not Robin counterexamples, generalized CA integers, or models of the zeta zero set. They deliberately fail to preserve the future ordinary-prime identity and future global CA coupling. Their legitimate conclusion is narrower: those future couplings contain information that cannot be replaced by bounded selector knowledge plus generic density.

## Research consequence

The source-side frontier after `RE-153` is now sharper. The canonical height average is sensitive at order one to only `Theta(sqrt(p)/log(p))` coherent post-selector label relocations, even though these constitute a `Theta(p^(-1/2))` fraction of the labels in the shell and cost only `O(sqrt(p))` in Chebyshev mass.

Therefore the next useful theorem cannot merely enlarge the clean/self-tangent selector to another **fixed** multiplicative neighborhood and then appeal to PNT regularity outside it. It must either propagate CA-selected information to multiplicative radius tending to infinity, control the signed square-root-scale source with explicit constants/correlation, or exploit an exact ordinary-prime/global-CA identity that forbids the matched relocation. This converts the qualitative broad-kernel warning of `RE-153` into a quantitative source-information barrier.