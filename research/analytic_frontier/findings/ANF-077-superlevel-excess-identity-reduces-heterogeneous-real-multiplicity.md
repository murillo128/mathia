# ANF-077 — superlevel excess identity reduces heterogeneous real multiplicity to nested-set defects

**Status:** `EXACT-DERIVED + REAL-MULTIPLICITY + SUPERLEVEL-DECOMPOSITION + SUPPORT-UNIFORM-HETEROGENEITY-GATE + MIXED-ONE-TWO-CRITICAL-CLASS`. `ANF-075` proves that every fixed cap on real support cardinality can be absorbed by narrowing the central notch, while `ANF-076` proves that the finite-real floor `q_real` exactly closes every unbounded-support class with uniform occupancy. The remaining scalar frontier was therefore heterogeneous occupancy on growing support. That frontier has an exact set-functional reduction.

Let `J>=0` be continuous, even and supported in `[-1,1]`, put

\[
F=\widehat J,
\qquad
q=q_{\rm real}(J)>0,
\]

and for every finite set `Y` of distinct real points define

\[
Q(Y):=E_F(Y),
\qquad
\Delta_q(Y):=Q(Y)-q|Y|\ge0,
\qquad
\Delta_q(\varnothing):=0.
\tag{1}
\]

Take an arbitrary finite real multiset with distinct support points `x_1,...,x_r` and positive integer multiplicities `k_1,...,k_r`. Write

\[
K:=\max_i k_i,
\qquad
X_a:=\{x_i:k_i\ge a\}
\quad(1\le a\le K).
\tag{2}
\]

The `X_a` form a nested superlevel chain

\[
X_K\subseteq\cdots\subseteq X_2\subseteq X_1.
\]

Then the full weighted energy has the exact identity

\[
\boxed{
E_F(k;X)
=
q\sum_i k_i^2
+
K\sum_{a=1}^K\Delta_q(X_a)
-
\sum_{1\le a<b\le K}
\Delta_q(X_a\setminus X_b).
}
\tag{3}
\]

Thus `q_real` already supplies the complete uniform quadratic part of every heterogeneous multiplicity vector. The only information lost when one passes from simple supports to weighted supports is an explicit **nested-set excess defect**: positive excesses of the superlevel sets compete against excesses of the multiplicity slices `X_a\setminus X_b`.

At the uniform-occupancy optimum from `ANF-076`, namely spectral amplitude `t=q^{-1}` and affine intercept `A=2`, define

\[
N:=\sum_i k_i,
\qquad
\sigma:=\#\{i:k_i=1\},
\]

and

\[
P(k)
:=
\sum_i k_i^2-2N+\sigma
=
\sum_{k_i\ge2}k_i(k_i-2)
\ge0.
\tag{4}
\]

The affine slack is exactly

\[
\boxed{
q\,\mathcal S(k;X)
=
qP(k)
+
K\sum_{a=1}^K\Delta_q(X_a)
-
\sum_{a<b}\Delta_q(X_a\setminus X_b),
}
\tag{5}
\]

where

\[
\mathcal S(k;X)
:=
\sigma-2N+q^{-1}E_F(k;X).
\]

Equation (5) is an exact support-uniform formulation of the heterogeneous real-multiplicity gate left open by `ANF-076`. No limit, attainment of `q_real`, equal-spacing assumption, or finite support cap enters it.

For the central-notch family of `ANF-034`, there is also a useful quantitative corollary. With the notation of `ANF-074`--`ANF-075`,

\[
J_s=J_{\rm MT}-s\phi_\eta,
\qquad
\beta=s b_\eta,
\qquad
\varepsilon:=\beta\eta,
\]

its spatial kernel satisfies

\[
F_s(t)\ge-\varepsilon
\qquad(t\in\mathbb R).
\tag{6}
\]

Define the purely combinatorial heterogeneity functional

\[
\boxed{
H(k)
:=
\sum_{i<j}
\min(k_i,k_j)\,|k_i-k_j|.
}
\tag{7}
\]

Then, with `q=q_real(J_s)`, every real multiset obeys

\[
\boxed{
E_{F_s}(k;X)
\ge
q\sum_i k_i^2
-2\varepsilon H(k).
}
\tag{8}
\]

Consequently the optimized affine slack satisfies

\[
\boxed{
\mathcal S(k;X)
\ge
P(k)-\frac{2\varepsilon}{q}H(k).
}
\tag{9}
\]

This turns the qualitative phrase “heterogeneous occupancy” into a quantitative obstruction threshold. Any counterexample with `P(k)>0` must satisfy

\[
\boxed{
\frac{H(k)}{P(k)}
>
\frac{q}{2\beta\eta}.
}
\tag{10}
\]

The only heterogeneous multiplicity vectors with zero integer surplus `P(k)=0` are mixtures of multiplicities `1` and `2`. They therefore form the first genuinely critical class. For disjoint finite sets `A,B`, where `A` carries multiplicity one and `B` multiplicity two, (5) reduces to the exact three-set condition

\[
\boxed{
E_F(A+2B)-q\bigl(|A|+4|B|\bigr)
=
2\Delta_q(A\cup B)+2\Delta_q(B)-\Delta_q(A).
}
\tag{11}
\]

Hence all mixed singleton/double configurations pass the `A=2,t=q^{-1}` gate **if and only if**

\[
\boxed{
\Delta_q(A)
\le
2\Delta_q(B)+2\Delta_q(A\cup B)
}
\tag{12}
\]

for every pair of disjoint finite real sets `A,B`. This is now the sharp zero-surplus scalar test. It is not implied by `\Delta_q>=0` alone and is not proved here.

## 1. Exact superlevel decomposition of weighted energy

For finite sets `A,B` write the bilinear energy

\[
B_F(A,B)
:=
\sum_{x\in A}\sum_{y\in B}F(x-y).
\tag{13}
\]

Then `Q(A)=B_F(A,A)`. Since the multiplicity vector has the layer-cake representation

\[
k_i
=
\sum_{a=1}^K\mathbf 1_{\{k_i\ge a\}},
\tag{14}
\]

its weighted structure factor is the sum of the simple structure factors of `X_1,...,X_K`. Therefore

\[
E_F(k;X)
=
\sum_{a=1}^K Q(X_a)
+2\sum_{a<b}B_F(X_a,X_b).
\tag{15}
\]

For `a<b` one has `X_b subseteq X_a`. Put `D_{a,b}:=X_a\setminus X_b`. Since `X_a=X_b disjoint-union D_{a,b}`,

\[
Q(X_a)
=
Q(X_b)+Q(D_{a,b})+2B_F(D_{a,b},X_b),
\]

while

\[
B_F(X_a,X_b)
=
Q(X_b)+B_F(D_{a,b},X_b).
\]

Eliminating the cross term gives the exact polarization identity

\[
\boxed{
2B_F(X_a,X_b)
=
Q(X_a)+Q(X_b)-Q(D_{a,b}).
}
\tag{16}
\]

Substitution into (15) is especially simple: every `Q(X_a)` occurs once on the diagonal and exactly `K-1` more times through the pair terms. Hence

\[
\boxed{
E_F(k;X)
=
K\sum_{a=1}^K Q(X_a)
-
\sum_{a<b}Q(X_a\setminus X_b).
}
\tag{17}
\]

Now insert `Q(Y)=q|Y|+Delta_q(Y)`. The cardinality part of (17) collapses site by site. A site of multiplicity `k_i` contributes `Kk_i` to the first sum. It belongs to `X_a\setminus X_b` precisely when

\[
1\le a\le k_i<b\le K,
\]

which happens `k_i(K-k_i)` times. Thus its net cardinality coefficient is

\[
Kk_i-k_i(K-k_i)=k_i^2.
\tag{18}
\]

Summing (18) proves (3). The identity is algebraic and remains valid when the infimum defining `q_real` is not attained.

## 2. The affine counting penalty separates into integer surplus and excess defect

At `A=2,t=q^{-1}`, multiply the affine slack by `q` and insert (3):

\[
\begin{aligned}
q\mathcal S
&=
q(\sigma-2N)+E_F(k;X)\\
&=
q\left(\sum_i k_i^2-2N+\sigma\right)
+K\sum_a\Delta_q(X_a)
-\sum_{a<b}\Delta_q(X_a\setminus X_b).
\end{aligned}
\tag{19}
\]

This is (5). The first term is entirely combinatorial. For a single occupied site,

\[
k^2-2k+\mathbf 1_{\{k=1\}}
=
\begin{cases}
0,&k=1,\\
k(k-2),&k\ge2.
\end{cases}
\tag{20}
\]

Therefore `P(k)>=0`, and

\[
\boxed{
P(k)=0
\iff
k_i\in\{1,2\}
\text{ for every occupied site.}
}
\tag{21}
\]

This explains why uniform occupancy was easy in `ANF-076`: when every `k_i` is equal, every difference `X_a\setminus X_b` is empty whenever both layers are nonempty, so the negative excess-defect sum in (5) vanishes. More generally, heterogeneity is not dangerous merely because different integers occur. It is dangerous only insofar as the excess energies of the slices can overwhelm both the superlevel-set excesses and the explicit integer surplus `qP(k)`.

Equation (5) also gives an exact equivalence for the full real problem at this normalization. The affine inequality holds for every finite real multiset if and only if every finite nested chain produced by positive integer occupancies satisfies

\[
\boxed{
\sum_{a<b}\Delta_q(X_a\setminus X_b)
\le
qP(k)+K\sum_a\Delta_q(X_a).
}
\tag{22}
\]

Thus the missing weighted finite-real floor is not an undefined new variational object: it is equivalent to a concrete inequality for the already-defined simple-support excess functional `Delta_q` on nested sets and their slices.

## 3. The central-notch spatial floor gives a quantitative heterogeneity penalty

For the central notch, let `n_a:=|X_a|`. From (6), for `a<b`,

\[
\begin{aligned}
B_{F_s}(X_a,X_b)
&=
Q(X_b)+B_{F_s}(X_a\setminus X_b,X_b)\\
&\ge
q n_b
-\varepsilon(n_a-n_b)n_b.
\end{aligned}
\tag{23}
\]

The two sets in the last cross term are disjoint, so every term there is an off-diagonal spatial value and may be bounded by `-epsilon` with no diagonal loss. The diagonal layer terms satisfy `Q(X_a)>=q n_a`. Using (15),

\[
E_{F_s}(k;X)
\ge
q\left(
\sum_a n_a+2\sum_{a<b}n_b
\right)
-2\varepsilon
\sum_{a<b}(n_a-n_b)n_b.
\tag{24}
\]

The first bracket is again exact:

\[
\sum_a n_a+2\sum_{a<b}n_b
=
\sum_{b=1}^K(2b-1)n_b
=
\sum_i k_i^2.
\tag{25}
\]

The second term also has a direct occupancy identity. For a pair of sites whose multiplicities are `u<v`, its contribution to

\[
\sum_{a<b}(n_a-n_b)n_b
\]

comes from `1<=a<=u<b<=v`, hence is exactly `u(v-u)`. Therefore

\[
\boxed{
\sum_{a<b}(n_a-n_b)n_b
=
\sum_{i<j}\min(k_i,k_j)|k_i-k_j|
=H(k).
}
\tag{26}
\]

Equations (24)--(26) prove (8), and (9) follows immediately from the definition of `P(k)`.

The bound is deliberately one-sided. It keeps the full simple-support floor `q` on every common superlevel layer and pays the crude spatial floor only across the genuinely heterogeneous part of two nested layers. This is why the penalty vanishes identically on every uniform occupancy ray, unlike the support-count estimate of `ANF-075`.

## 4. Mixed single/double occupancy is the exact zero-surplus gate

Suppose `K=2`. Let

\[
A:=X_1\setminus X_2,
\qquad
B:=X_2,
\]

so `A` is the set of singleton sites and `B` the set of doubled sites. Then `X_1=A\cup B`, and (17) gives the exact identity

\[
\boxed{
E_F(A+2B)
=
2Q(A\cup B)+2Q(B)-Q(A).
}
\tag{27}
\]

Subtracting `q(|A|+4|B|)` yields (11). Because `P=0` for every `1/2` occupancy vector, there is no diagonal integer surplus available to absorb a negative three-set defect. The full mixed-single/double class is therefore controlled exactly by (12), not by a larger weighted optimization problem.

This sharpens the frontier left by `ANF-076`. Equal singles and equal doubles were already closed by `q_real`; their `Delta_q` defect is nonnegative. The first unresolved heterogeneous ray is a **two-species decoration of one simple support**. A falsifier must arrange a singleton subset `A` whose excess `Delta_q(A)` is more than twice the combined excess of both the doubled subset `B` and the union `A union B`.

The spatial-floor estimate alone cannot decide this class. Here

\[
P(k)=0,
\qquad
H(k)=|A||B|,
\]

so (9) only gives

\[
\mathcal S
\ge
-\frac{2\varepsilon}{q}|A||B|.
\tag{28}
\]

Equation (28) is a loss of the crude bound, not evidence of an actual counterexample. The exact test is (12).

For comparison, the next two-level class already has positive surplus. If `u` sites have multiplicity two and `v` sites have multiplicity three, then

\[
P=3v,
\qquad
H=2uv.
\tag{29}
\]

Equation (9) proves safety whenever

\[
\boxed{
u\le\frac{3q}{4\varepsilon}.
}
\tag{30}
\]

Thus even the elementary `2/3` heterogeneous family cannot become dangerous until the number of doubled sites reaches the reciprocal-`beta eta` scale. This is parametrically farther out than the fixed-support statement alone sees when the notch amplitude is small.

## 5. A support-uniform class of heterogeneous occupancies is now closed

The central-notch separator of `ANF-034` permits arbitrarily small positive notch amplitude `s` once an admissible width has been fixed. Its exact cost satisfies, using `ANF-074`,

\[
C(J_s)
=
C_{\rm MT}
-\beta\left(1+\frac{\eta^2}{3}\right),
\tag{31}
\]

and `ANF-034` gives

\[
q=q_{\rm real}(J_s)
>
\frac{C(J_s)}{C_{\rm MT}}.
\tag{32}
\]

Hence `q` stays bounded away from zero and in fact tends to the sharp value `1` from the lower-bound side as `beta downarrow 0` in the only sense needed here: the right side of (32) tends to `1`.

Now fix any family `mathcal K` of positive integer occupancy vectors, with arbitrary support cardinality, for which there is a finite constant `L` such that every non-uniform-zero-surplus member satisfies

\[
P(k)>0,
\qquad
H(k)\le L P(k).
\tag{33}
\]

Uniform vectors with `H=P=0` may also be included; they are already safe by (3) or `ANF-076`. Choose `s>0` sufficiently small on the same separator ray that

\[
\frac{2\beta\eta}{q}L<1.
\tag{34}
\]

Then (9) gives `mathcal S>=0` for **every** real support geometry and every cardinality whose occupancy vector lies in `mathcal K`. The same single amplitude `t=q^{-1}` and intercept `A=2` work simultaneously for the whole family. Moreover, by (32), their BGSST objective is

\[
\boxed{
2-\frac{C(J_s)}{q}
>
2-C_{\rm MT}.
}
\tag{35}
\]

Therefore growing support plus nonuniformity is still not sufficient for a shape-level no-go. Any preassigned heterogeneous family with bounded defect ratio `H/P` can be absorbed by shrinking the notch amplitude, without sacrificing the strict Montgomery--Taylor improvement. A counterexample with `P>0` at amplitude `s` must satisfy the quantitative divergence (10). As `s downarrow0`, such a falsifier must become increasingly extreme in the precise combinatorial ratio `H/P`.

The exceptional amplitude-stable core exposed by this argument is the mixed `1/2` class, where `P=0` and `H>0`. It should therefore be tested before broader high-multiplicity searches: either prove the exact excess inequality (12), or produce disjoint finite sets `A,B` for which it fails. A failure would identify a genuine support-uniform heterogeneous obstruction; a proof would remove the only zero-surplus heterogeneous class and force every remaining obstruction to pay the positive integer term in (5).

## 6. Prior art, audit, and remaining boundary

The layer-cake/superlevel representation of nonnegative integer weights is elementary and classical. The neighboring many-particle literature already anchored in `SOURCES.md` — in particular Sütő's positive-Fourier ground-state framework and the Fisher--Ruelle/Procacci stability language — contains the expected quadratic occupation-number and stability mechanisms. A targeted literature search for weighted positive-definite pair energies, superstable occupation bounds, and superlevel decompositions did not identify an external theorem needed for (3), (5), or (11). No novelty is claimed for layer-cake decomposition, polarization, positive-definite Gram geometry, or classical superstability. The Mathia-specific content is the exact interaction of those elementary identities with `q_real`, the affine simple-point penalty, and the central-notch floor. Existing `SOURCES.md` anchors are sufficient; no new load-bearing source is added.

The derivation has five load-bearing checks:

1. `q_real` applies to every nonempty finite **distinct** set `X_a` and `X_a\setminus X_b`; no weighted extension of its definition is assumed.
2. Equation (16) is exact because the superlevel sets are nested; it is not an inequality from positive semidefiniteness.
3. The cardinality cancellation (18) is sitewise and gives `sum k_i^2` exactly.
4. The central-notch bound (8) uses `F_s>=-beta eta` only on disjoint cross-layer pairs, while retaining the sharper `q_real` lower bound on common layers.
5. The objective improvement (35) is exactly the `C/q_real` separator already proved in `ANF-034`; no numerical estimate of `q` or assumption that its infimum is attained enters the argument.

The finding does **not** prove the full real-multiplicity affine certificate, improve the unconditional zeta-zero proportion, or imply RH. It also does not establish the three-set inequality (12). What it does is replace the vague support-uniform heterogeneous frontier by an exact nested-set defect criterion and a quantitative central-notch penalty. The cheapest next scalar test is now the mixed singleton/double gate (12). Only after that gate is decided is it efficient to search more complicated growing-support occupancy patterns or to reopen the complex multi-pair frontier.