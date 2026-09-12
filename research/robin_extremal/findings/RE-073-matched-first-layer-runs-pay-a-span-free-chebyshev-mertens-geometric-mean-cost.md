# RE-073 — matched first-layer runs pay a span-free Chebyshev-Mertens geometric-mean cost

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + MATCHED-FIRST-LAYER-RUN + JOINT-CHEBYSHEV-MERTENS-CAPACITY + SPAN-FREE-TRADEOFF + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-072` proves that a consecutive matched `0 -> 0` first-layer fan run has a one-sided source ledger: the Chebyshev deficit

\[
H_\vartheta(x):=x-\vartheta(x)
\]

increases through every open threshold cell and every matched switch, while the logarithmic Mertens-product error

\[
E_\ell(x):=\sum_{p\le x}-\log(1-p^{-1})-\gamma-\log\log x
\]

decreases. Its separate lower bounds have different scale dependence. The Chebyshev cost is controlled from the initial physical scale, but the reciprocal-prime lower bound contains the largest state scale `W`; a superpolynomially stretched run can therefore make that second bound arbitrarily weak.

The two costs cannot, however, become cheap simultaneously. The exact cell relation

\[
-dE_\ell=g(Z)\,dH_\vartheta,
\qquad
 g(Z)=\frac1{Z\log Z},
\]

combined with the false-RH amplitude floor and Cauchy-Schwarz gives a **span-free geometric-mean law**. The largest physical scale disappears completely.

Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\tag{1}
\]

and work on a sufficiently late common positive CA counterexample block from `RE-040`. Let

\[
\beta_1<\beta_2<\cdots<\beta_m,
\qquad m\ge2,
\tag{2}
\]

be consecutive rightmost-fan breakpoints, with exposed states

\[
C_0<C_1<\cdots<C_m,
\qquad Y_i:=\log C_i,
\tag{3}
\]

such that every complete physical packet from `C_(i-1)` to `C_i` is first-layer-only and has matched fringe pattern

\[
\chi_i^- =\chi_i^+=0.
\tag{4}
\]

For each internal state `C_i`, `1<=i<=m-1`, put

\[
I_i=(\beta_i,\beta_{i+1}),
\qquad
h_i:=\log G(C_i)-\gamma,
\qquad
a_i:=1-e^{-h_i},
\tag{5}
\]

and let `Z_i(b)` be its tangent selector. Write

\[
X:=\min_{0\le i\le m}Y_i=Y_0,
\qquad
w:=\beta_m-\beta_1,
\tag{6}
\]

and define the full run excursions

\[
\Delta_H:=H_\vartheta(Z_R)-H_\vartheta(Z_L)>0,
\tag{7}
\]

\[
\Delta_E:=E_\ell(Z_L)-E_\ell(Z_R)>0.
\tag{8}
\]

Then, for all sufficiently late blocks,

\[
\boxed{
\Delta_H\Delta_E
\ge
\left[
\sum_{i=1}^{m-1}
\int_{I_i}
Z_i'(b)\sqrt{g(Z_i(b))}\,db
\right]^2.
}
\tag{9}
\]

The integrand has the exact closed form

\[
\boxed{
Z_i'(b)\sqrt{g(Z_i)}
=
a_i\,\frac{Z_i}{Y_i}\,
\sqrt{Z_i\log Z_i}\,
\frac{\log Z_i}{\log Z_i+1}.
}
\tag{10}
\]

Using the uniform late-fan regularity `Z_i/Y_i -> 1` and the common positive amplitude floor from `RE-040`, this gives the scale-free consequence

\[
\boxed{
\Delta_H\Delta_E
\gg_J
X^{1-2b_1}\log X\;w^2.
}
\tag{11}
\]

Equivalently,

\[
\boxed{
\sqrt{\Delta_H\Delta_E}
\gg_J
X^{1/2-b_1}\sqrt{\log X}\;w.
}
\tag{12}
\]

No upper scale `W` occurs. Since `b_1<1/2`, a matched first-layer run occupying threshold width bounded below by a positive constant has a geometric-mean source cost that diverges polynomially with the **initial** physical scale. A run may still make its Mertens drop very small by stretching far to the right, but only by paying a reciprocally larger Chebyshev excursion:

\[
\boxed{
\Delta_H
\gg_J
\frac{X^{1-2b_1}\log X\;w^2}{\Delta_E}.
}
\tag{13}
\]

Thus superpolynomial physical stretch is not a joint zero-cost escape for the matched branch. It can redistribute the source burden between the two coordinates, but cannot suppress their geometric mean.

## 1. The continuous cell ledger already carries the product obstruction

`RE-072` gives, exactly on every internal matched cell,

\[
\frac{d}{db}H_\vartheta(Z_i(b))=Z_i'(b)>0,
\tag{14}
\]

and

\[
-\frac{d}{db}E_\ell(Z_i(b))
=g(Z_i(b))Z_i'(b)>0.
\tag{15}
\]

Let

\[
A_c:=\sum_{i=1}^{m-1}\int_{I_i}Z_i'(b)\,db,
\qquad
B_c:=\sum_{i=1}^{m-1}\int_{I_i}g(Z_i(b))Z_i'(b)\,db.
\tag{16}
\]

The matched switch increments from `RE-070`--`RE-071` have the same signs for all sufficiently late blocks. Hence the complete run excursions dominate their continuous pieces:

\[
\Delta_H\ge A_c,
\qquad
\Delta_E\ge B_c.
\tag{17}
\]

Apply Cauchy-Schwarz on the disjoint union of the threshold cells:

\[
\begin{aligned}
A_cB_c
&=\left(\int 1\cdot Z'(b)\,db\right)
  \left(\int g(Z(b))Z'(b)\,db\right)\\
&\ge
\left(\int Z'(b)\sqrt{g(Z(b))}\,db\right)^2.
\end{aligned}
\tag{18}
\]

Together with (17), this is (9). The argument uses only the positive cell ledger; the discrete matched switches can only increase both sides of the source budget. In particular, no packet-cardinality estimate is needed.

## 2. Exact selector speed turns the product into an initial-scale lower bound

For a fixed state `C_i`, the tangent equation is

\[
g(Z_i(b))=g(Y_i)-\frac{ba_i}{Y_i}.
\tag{19}
\]

Differentiating gives the exact speed

\[
Z_i'(b)=\frac{a_i}{Y_i[-g'(Z_i)]},
\tag{20}
\]

while

\[
-g'(Z)=\frac{\log Z+1}{Z^2(\log Z)^2}.
\tag{21}
\]

Substitution of (21) and `g(Z)=1/(Z log Z)` into (20) gives (10) exactly.

The common positive blocks of `RE-040` provide `c_0>0` such that every blockwise maximizer has

\[
A_b(C)=Y^b(e^{h(C)}-1)\ge c_0
\tag{22}
\]

for every `b in J`. Along an internal cell, `h_i` is fixed and the selected state is a maximizer throughout the cell. In the uniform small-height regime this yields, as in `RE-072`,

\[
\boxed{
a_i\ge\frac{c_0}{2}Y_i^{-b_1}}
\tag{23}
\]

for all sufficiently late blocks.

Uniform regularity also gives

\[
\frac{Z_i}{Y_i}=1+o_J(1),
\qquad
\frac{\log Z_i}{\log Z_i+1}=1+o_J(1).
\tag{24}
\]

Therefore (10) and (23) imply uniformly on all internal cells

\[
Z_i'(b)\sqrt{g(Z_i(b))}
\gg_J
Y_i^{1/2-b_1}\sqrt{\log Y_i}.
\tag{25}
\]

Because `b_1<1/2`, the function on the right is eventually increasing. Every `Y_i>=X`, so

\[
Z_i'(b)\sqrt{g(Z_i(b))}
\gg_J
X^{1/2-b_1}\sqrt{\log X}.
\tag{26}
\]

The internal cells partition `(beta_1,beta_m)` up to finitely many endpoints and possible empty cells. Hence

\[
\sum_{i=1}^{m-1}|I_i|=w.
\tag{27}
\]

Integrating (26) and inserting it into (9) proves (11)--(12).

The exponent `1/2-b_1` is the important structural point. The Chebyshev cell density grows like `aY log Y`, while the Mertens cell density is smaller by `1/(Y log Y)`. Their geometric mean is nevertheless

\[
a\sqrt{Y\log Y},
\tag{28}
\]

and the false-RH amplitude floor supplies `a >> Y^{-b_1}`. Because the whole compact fan lies strictly below `b=1/2`, the remaining power is positive.

## 3. This removes the largest-scale loss of the separate reciprocal bound

The separate estimates in `RE-072` are

\[
\Delta_H\gg_J X^{1-b_1}\log X\;w
\tag{29}
\]

and, if `W` is the largest state scale in the run,

\[
\Delta_E\gg_J W^{-b_1}w.
\tag{30}
\]

Equation (30) correctly records that reciprocal-prime normalization weakens as the fan moves to larger physical coordinates. Taken alone, it leaves a conspicuous superpolynomial-stretch escape: `W` can make the guaranteed Mertens decrement smaller than any fixed power of `X`.

Equation (11) shows that this loss is an artifact of asking for a **separate** lower bound on `Delta_E`. The exact cell kernel couples the two coordinates strongly enough that Cauchy-Schwarz removes `W`. If `Delta_E` becomes smaller, the same matched trajectory must make `Delta_H` proportionally larger according to (13). Conversely,

\[
\Delta_E
\gg_J
\frac{X^{1-2b_1}\log X\;w^2}{\Delta_H}.
\tag{31}
\]

The theorem therefore does not prove a span-independent lower bound for either source error separately. Its content is a **joint capacity law**: physical stretch can trade one source burden for the other, but cannot make both vanish at the rate suggested by treating (29) and (30) independently.

This is useful for the live global fan problem because higher-layer/fringe interruptions and matched first-layer runs can now be debited in currencies that do not require a polynomial-span hypothesis. `RE-065` still needs polynomial physical span for its growing-depth event inventory, but the matched branch no longer needs such a hypothesis merely to retain a two-source cost.

## 4. Stress tests and exact boundary

The matched first-layer hypothesis at every traversed switch remains load-bearing. It is what lets `RE-072` assert that both discrete switch increments have the same signs as the continuous cell increments. If a higher-layer event or unmatched fringe endpoint occurs, the switch can carry the separate signed charge mechanisms of `RE-060`--`RE-067`; then (17) need not hold for the complete run even though each source-free cell still satisfies (14)--(15).

The theorem is vacuous when `w=0`, as it should be. A single matched switch with no intervening positive-width cell is governed by `RE-070`--`RE-071`, not by the new geometric-mean term. Empty cells or multiple exposed states meeting at one breakpoint do not affect (27).

Compact containment below `1/2` is also essential to the polynomial form (11). As `b_1` approaches `1/2`, the power `1-2b_1` tends to zero. Equation (9), however, remains the correct exact cell inequality; only the simple initial-scale power extraction degenerates.

The result does **not** contradict hypothetical RH failure. It is a capacity law, not a global upper bound for the source errors. A false-RH spectrum may support a very large Chebyshev excursion together with a small reciprocal-prime decrement, or vice versa. In the polynomially comparable-scale regime, the inequality `b_1>1-Theta` gives

\[
1-2b_1<2\Theta-1,
\tag{32}
\]

so the power in (11) remains below the natural product scale permitted by an off-critical zero. This is the required falsification check: the theorem removes a bookkeeping escape without silently importing an RH-strength source estimate.

Nor is Cauchy-Schwarz itself a novelty claim. Equality in (18) would require `g(Z(b))` to be essentially constant on the cell measure, so a long run spread over very different physical scales can be far from equality. The lower bound is deliberately one-sided and does not claim sharpness for stretched fans.

## 5. Prior-art boundary and research consequence

Bhattacharya--Martin--Simpson study the global joint distribution and persistent comparison of standard and reciprocal prime-counting errors, including the logarithmic Mertens product. Mantovanelli's prime-layer workload gives exact CA event and packet bookkeeping. Both are already anchored in `SOURCES.md`. A targeted current search found no statement of the present adaptive-threshold geometric-mean law; in particular, the global correlation results do not impose the false-RH fan selector, and the classical CA workload does not contain the compact adaptive threshold path used in (9)--(12).

No external theorem is load-bearing here, and no novelty is claimed for Cauchy-Schwarz, the derivative of `g`, or the underlying prime-error correlation. The durable line-specific delta is the splice of the exact `RE-072` two-source cell ledger with the `RE-040` amplitude floor: it converts two asymmetric source costs into one **initial-scale, span-free joint obstruction**.

The live matched-branch question is consequently sharper. A future global argument no longer has to prevent superpolynomial physical stretch merely to keep both source coordinates visible. It can instead ask whether the false-RH common fan can partition a fixed threshold interval into matched runs and charged interruptions while respecting simultaneously the span-free budgets

\[
\Delta_H\Delta_E
\gg_J
X^{1-2b_1}\log X\;w^2
\]

for every maximal matched run and the higher-layer/fringe charge-capacity laws of `RE-060`--`RE-067`. What remains is a global accumulation theorem: show that those local joint budgets and interruption charges cannot all be absorbed by the same off-critical source trajectory, or identify a new architecture that can do so.