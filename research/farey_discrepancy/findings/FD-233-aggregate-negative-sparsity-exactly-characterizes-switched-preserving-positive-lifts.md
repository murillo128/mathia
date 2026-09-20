# FD-233 — Aggregate-negative sparsity exactly characterizes switched-preserving positive lifts

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response kernel / one-sided slack / positive-cone lifting / dyadic capacity / switched response
- **Depends on:** FD-232, FD-230, FD-225
- **Classification:** `EXACT-DERIVED + POSITIVE-LIFT-IFF + ONE-SIDED-SPARSITY + SWITCHED-RESPONSE-STABILITY + AFFINE-CONE-REDUCTION`

## Claim

FD-232 proved that aggregate sparsity of the negative part is necessary for a signed linear-capacity correction to admit a nonnegative lift without changing its switched response at quadratic scale. The missing converse is true: **the same one-sided condition is also sufficient**. No additional cancellation estimate for the slack is required.

Let

\[
(\mathscr A v)(m)
=
\sum_{d\le m} v_d M\!\left(\left\lfloor\frac md\right\rfloor\right),
\]

let

\[
B_k=[2^k,2^{k+1})\cap\mathbb N,
\qquad
C_k=\sum_{d\in B_k}d\asymp4^k,
\]

and let the switched row orders be the bounded sequence

\[
r_j=q_j+1=(1,4,4,1,4,4,\ldots).
\]

For a coefficient profile `v`, write

\[
\mathcal R_j(v)
:=
(E-I)^{r_j}(\mathscr A v)(2^j),
\]

where `E` shifts the dyadic sample index.

Suppose `b` is signed and linearly bounded,

\[
|b_d|\le C_b d.
\tag{1}
\]

Call `a=b+s` a **switched-preserving positive lift** if

\[
a_d\ge0,\qquad s_d\ge0,
\tag{2}
\]

`a` has a linear envelope, and the added slack changes the switched response only below quadratic scale,

\[
\mathcal R_j(a)-\mathcal R_j(b)
=
\mathcal R_j(s)
=o(4^j).
\tag{3}
\]

Then

\[
\boxed{
\text{a switched-preserving positive lift exists}
\iff
\frac{\sum_{d\in B_k}b_d^-}{C_k}\longrightarrow0.
}
\tag{4}
\]

Moreover, when the right-hand condition holds, the canonical lift already works:

\[
\boxed{
s=b^-,\qquad a=b^+.}
\tag{5}
\]

Thus the necessary condition isolated in FD-232 is exact at the coefficient/divisor-response level. For a correction class modulo signed switched-blind directions, the remaining question is purely whether that affine class contains a representative with vanishing negative-capacity density. Once such a representative exists, no further switched-response estimate for its minimal positive slack is needed.

This does **not** by itself solve discrete source realization in the scale-adapted prime reservoirs. Integer occupancy, finite reservoir capacities and the exact source-side constraints remain separate after the coefficient-level lift.

## 1. Sparse nonnegative band mass is automatically switched-negligible

The converse rests on a simple lemma that was not used in FD-232.

Let `c_d>=0` satisfy a linear envelope

\[
0\le c_d\le C_c d
\tag{6}
\]

and suppose its aggregate mass is sparse on late dyadic bands,

\[
V_k(c):=\sum_{d\in B_k}c_d=o(C_k)=o(4^k).
\tag{7}
\]

Then

\[
\boxed{(\mathscr A c)(m)=o(m^2).}
\tag{8}
\]

Indeed, the elementary bound `|M(n)|<=n` gives

\[
|\mathscr A c(m)|
\le
\sum_{d\le m}c_d\left|M\!\left(\left\lfloor\frac md\right\rfloor\right)\right|
\le
m\sum_{d\le m}\frac{c_d}{d}.
\tag{9}
\]

Choose `J` with `2^J<=m<2^{J+1}`. On `B_k`, `1/d<=2^{-k}`, hence

\[
\sum_{d\le m}\frac{c_d}{d}
\le
O(1)+\sum_{k\le J}2^{-k}V_k(c).
\tag{10}
\]

Given `epsilon>0`, choose `K` so that

\[
V_k(c)\le\epsilon4^k
\qquad(k\ge K).
\]

The finitely many bands below `K` contribute `O_K(1)`, while the remaining bands contribute

\[
\sum_{K\le k\le J}2^{-k}V_k(c)
\le
\epsilon\sum_{K\le k\le J}2^k
\ll
\epsilon2^J.
\tag{11}
\]

After division by `2^J`, first let `J` tend to infinity and then let `epsilon` tend to zero. Therefore

\[
\sum_{d\le m}\frac{c_d}{d}=o(m),
\]

which proves (8) through (9).

Because every switched row has bounded order, `(E-I)^{r_j}` is a fixed finite linear combination of values of `mathscr A c` at `2^{j+t}` with bounded `t`. Equation (8) therefore implies

\[
\boxed{\mathcal R_j(c)=o(4^j).}
\tag{12}
\]

So aggregate-capacity sparsity is already enough to make any nonnegative linear-envelope slack invisible at the switched quadratic scale.

## 2. Necessity is FD-232

Assume a switched-preserving positive lift `a=b+s` exists. From `a_d>=0` and `s_d>=0`, every coordinate satisfies

\[
\boxed{s_d\ge b_d^-.}
\tag{13}
\]

The linear envelopes for `a` and `b` imply a linear envelope for `s`. By (3), `s` is nonnegative and switched-subquadratic. FD-230 therefore applies and yields

\[
\frac{\sum_{d\in B_k}s_d}{C_k}\longrightarrow0.
\tag{14}
\]

Combining (13) and (14) gives

\[
0\le
\frac{\sum_{d\in B_k}b_d^-}{C_k}
\le
\frac{\sum_{d\in B_k}s_d}{C_k}
\longrightarrow0.
\tag{15}
\]

This is exactly the necessary direction established in FD-232.

## 3. The canonical minimal slack proves sufficiency

Now assume

\[
\frac{\sum_{d\in B_k}b_d^-}{C_k}\longrightarrow0.
\tag{16}
\]

Take the smallest possible pointwise slack,

\[
s_d=b_d^-,
\qquad
a_d=b_d+s_d=b_d^+.
\tag{17}
\]

Both `s` and `a` are nonnegative, and (1) gives the required linear envelopes. Condition (16) is precisely the sparse-band hypothesis (7) for `c=s`. The lemma therefore gives

\[
\mathcal R_j(s)=o(4^j).
\tag{18}
\]

By linearity,

\[
\mathcal R_j(a)-\mathcal R_j(b)
=
\mathcal R_j(s)
=o(4^j),
\]

so `a=b^+` is a switched-preserving positive lift. This proves the converse and hence the equivalence (4).

A useful special case is when `b` itself is switched-subquadratic. Then (16) holds if and only if `b^+` is also switched-subquadratic. Thus a signed blind direction is physically liftable at the coefficient level exactly when its negative part is asymptotically negligible in aggregate dyadic capacity.

FD-231 lies on the forbidden side of this dichotomy: its negative part has a fixed positive capacity density on every late band. FD-232 already ruled out its positive lift; FD-233 shows that this failure is not hiding any second analytic condition. The macroscopic negative mass is the whole coefficient-level obstruction.

## 4. The affine one-sided cone distance is now the exact coefficient-level frontier

Let `N_sw` be the signed linear-envelope profiles `h` satisfying

\[
\mathcal R_j(h)=o(4^j).
\]

If `c` is one correction producing the required physical switched response, all profiles `c+h` with `h in N_sw` are equivalent at quadratic switched scale. FD-232 reduced positive realizability to the necessary search condition

\[
\exists h\in N_{\rm sw}:
\qquad
\frac{\sum_{d\in B_k}(c_d+h_d)^-}{C_k}\longrightarrow0.
\tag{19}
\]

FD-233 shows that (19) is also sufficient for **coefficient-level** positive lifting: once such an `h` is found, simply add the negative part of `c+h`. By the sparse-slack lemma, that addition is automatically switched-negligible.

Consequently the remaining divisor-response question is no longer whether a sparse negative part might nevertheless have a large switched response. It cannot. The live question is exactly whether the affine correction class intersects the asymptotic one-sided neighborhood of the positive cone described by (19).

For the Mertens correction coming from the exact FD-225 inversion, there are therefore two decisive outcomes. A positive lower bound on the best achievable late-band negative density would, together with FD-230/FD-232, give an intrinsic coefficient-level capacity obstruction. Conversely, constructing a switched-null adjustment that makes this density vanish would remove the coefficient-level positivity obstruction entirely; the remaining work would then move to integer prime occupancy and finite reservoir capacity.

## 5. Prior-art boundary and verdict

The external prior-art check found only the standard surrounding language of positive/negative parts and Jordan-type decomposition of signed objects, together with generic divisor-convolution material. No external theorem is load-bearing here, and no novelty is claimed for taking `b^+` and `b^-` or for the elementary inequality `|M(n)|<=n`.

The research-specific content is the exact equivalence obtained after combining the Mathia divisor-response representation with FD-230: sparse aggregate negative capacity is both necessary and sufficient for preserving the switched response under a positive lift. The sufficiency estimate is elementary and self-contained, so no new anchor is required in `SOURCES.md`.

**Verdict.** FD-232's one-sided sparsity condition is not merely a veto. It is the exact coefficient-level liftability criterion. The search can now ignore separate switched estimates for a minimal positive slack and focus entirely on the affine optimization problem: can the concrete Mertens correction, modulo legitimate switched-blind directions, be made asymptotically negative-sparse? If yes, coefficient-level positivity is solved automatically; if no, the remaining obstruction is genuinely one-sided and structural.