# PF-224 — reciprocal-prime jumps do not weak-trace regularize raw pant hopping

**Status:** `EXACT-DERIVED + ARITHMETIC-COUNTING + DECISIVE-NEGATIVE/ROUTE-NARROWING`. PF-222 proves that the reciprocal-prime Schur commutator is compact and gives the exact cut-flux expansion

\[
[D,\Omega]=\sum_n \delta_n[D,E_n],
\qquad
\delta_n=\frac1{P_n}-\frac1{P_{n+1}}>0,
\]

with every fixed cut flux in every Schatten class. It also records the crude sufficient trace-class route

\[
\sum_n\delta_n\|B_n\|_1<\infty,
\qquad
B_n:=\Pi_{n+1}K\Pi_n,
\]

because one-seam decoupling bounds the resolvent difference by the raw crossing block. That route is impossible for the **actual canonical prime-flute precision**. Combining PF-215's geometric lower bound on the normalized pant crossing with the exact reciprocal-prime jump shows

\[
\boxed{
\delta_n\|B_n\|
\ge
\frac{c}{\log P_n}
\frac{g_n}{g_n+g_{n+1}}
}
\]

on the tail. Edges for which `g_{n+1}\le2g_n` therefore carry raw weighted hopping at least `c/\log P_n`. Such edges cannot be sparse enough to rescue weak trace class: Baker--Harman--Pintz's polynomial prime-gap envelope implies that a run of consecutive doublings `g_{n+1}>2g_n` has only `O(\log N)` length among the first `N` tail edges. Hence at least `cN/\log N` of those edges satisfy `g_{n+1}\le2g_n`.

Because the oriented blocks `B_n:\mathcal B_n\to\mathcal B_{n+1}` have pairwise orthogonal sources and pairwise orthogonal targets, the singular values of their finite weighted sum are the multiset union of the block singular values. For

\[
T_N:=\sum_{n=n_0}^{N}\delta_n B_n
\]

one therefore obtains

\[
\boxed{
q(T_N):=\sup_{\sigma>0}\sigma N_{T_N}(\sigma)
\ge
c\frac{N}{(\log N)^2}
\longrightarrow\infty.
}
\]

In particular

\[
\boxed{
\sum_n\delta_n\|B_n\|_1=\infty.
}
\]

Thus the reciprocal-prime jump is **not** by itself enough to pay for the raw normalized pant hopping, not even at the weak-`S_1` level. This does **not** show that `[D,\Omega]` or `P[D,\Omega]H` fails weak trace class. The actual cut commutator contains the inverse factors `D=(I+K)^{-1}`, and PF-212 supplies physical-frequency decay absent from the raw precision block. PF-224 therefore sharpens PF-223 in the canonical geometry: the endpoint proof must exploit resolvent shorting/damping, low-high placement, frequency decay, or an equivalent quantitative cancellation **before** summing the one-seam fluxes. A triangle estimate through `\|B_n\|_1` is no longer a live route.

## Claim

Use the simultaneous natural-width PF-205 seam cut on the prime flute and the notation of PF-214--PF-223. Let

\[
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}\ge0,
\qquad
D=(I+K)^{-1},
\tag{1}
\]

and let `\Pi_n` denote the normalized boundary-energy projection of the `n`th cuff module. Write

\[
B_n:=\Pi_{n+1}K\Pi_n.
\tag{2}
\]

PF-222 proves that every fixed `B_n` is smoothing in the boundary variables and therefore belongs to `\mathcal S_p` for every `p>0`; in particular `B_n\in\mathcal S_1`.

With the prime indexing used by PF-205/PF-215,

\[
P_n=p_{n-1},
\qquad
g_n=p_n-p_{n-1}=P_{n+1}-P_n,
\tag{3}
\]

and define

\[
\omega_n=P_n^{-1},
\qquad
\delta_n:=\omega_n-\omega_{n+1}
=\frac{g_n}{P_nP_{n+1}}.
\tag{4}
\]

Then there are `c>0` and `n_0` such that for every `n\ge n_0`,

\[
\boxed{
\delta_n\|B_n\|_1
\ge
\delta_n\|B_n\|
\ge
\frac{c}{\log P_n}
\frac{g_n}{g_n+g_{n+1}}.
}
\tag{5}
\]

Consequently, on the set

\[
\mathcal G:=\{n\ge n_0:g_{n+1}\le2g_n\},
\tag{6}
\]

one has

\[
\boxed{
\delta_n\|B_n\|
\ge \frac{c}{\log P_n}.
}
\tag{7}
\]

Moreover there is `c_0>0` such that for all sufficiently large `N`,

\[
\boxed{
\#(\mathcal G\cap[n_0,N])
\ge c_0\frac{N}{\log N}.
}
\tag{8}
\]

For the finite oriented raw-hopping sum

\[
T_N:=\sum_{n=n_0}^{N}\delta_nB_n,
\tag{9}
\]

write

\[
N_{T_N}(\sigma)=\#\{j:s_j(T_N)>\sigma\},
\qquad
q(T_N)=\sup_{\sigma>0}\sigma N_{T_N}(\sigma).
\tag{10}
\]

Then

\[
\boxed{
q(T_N)\ge c\frac{N}{(\log N)^2}	o\infty.
}
\tag{11}
\]

Equivalently, the family of finite raw reciprocal-prime-weighted pant hoppings has no uniform weak-`S_1` bound. If the infinite oriented sum in (9) exists as a bounded operator, it cannot belong to `\mathcal S_{1,\infty}`. Independently of existence of that infinite sum,

\[
\boxed{
\sum_{n\ge n_0}\delta_n\|B_n\|_1=\infty.
}
\tag{12}
\]

Equation (12) rules out exactly PF-222's crude sufficient trace-norm summation. Equations (11)--(12) do not apply to the dressed cut flux `[D,E_n]` and therefore do not decide the actual Schur commutator endpoint.

## 1. The geometric hopping lower bound survives the reciprocal-prime jump

PF-215 gives the canonical prime-side estimate

\[
\|B_n\|
\ge
\frac{c}
{s_n\sqrt{w_nL_n\,w_{n+1}L_{n+1}}},
\tag{13}
\]

where

\[
s_n=\frac{h_n+h_{n+1}}2
\tag{14}
\]

is the exact common-perpendicular scale between the neighboring long cuffs, `w_n` is the PF-205 natural Fermi-area halfwidth, and `L_n` is the physical cuff length.

PF-205/PF-215 provide, after a finite head,

\[
w_n\asymp P_n^{-1},
\qquad
L_n=O(\log P_n),
\qquad
h_n=\frac{g_n}{P_n}(1+o(1)).
\tag{15}
\]

Hence

\[
s_n
\le
C\frac{g_n+g_{n+1}}{P_n}.
\tag{16}
\]

For the width-length factor, monotonicity of `(\log x)/x` on the tail gives directly

\[
\sqrt{w_nL_n\,w_{n+1}L_{n+1}}
\le
C\frac{\log P_n}{P_n}.
\tag{17}
\]

The Baker--Harman--Pintz envelope already used in PF-215 says

\[
g_n=O(P_n^{0.525}).
\tag{18}
\]

In particular `P_{n+1}/P_n=1+O(P_n^{-0.475})`, so for large `n`,

\[
\delta_n
=\frac{g_n}{P_nP_{n+1}}
\ge c\frac{g_n}{P_n^2}.
\tag{19}
\]

Combining (13), (16), (17), and (19),

\[
\begin{aligned}
\delta_n\|B_n\|
&\ge
c\frac{g_n}{P_n^2}
\frac{P_n^2}{(g_n+g_{n+1})\log P_n}\\
&=
\boxed{
\frac{c}{\log P_n}
\frac{g_n}{g_n+g_{n+1}}.
}
\end{aligned}
\tag{20}
\]

Since `B_n\in\mathcal S_1`, `\|B_n\|_1\ge\|B_n\|`, proving (5). If `g_{n+1}\le2g_n`, the gap ratio in (20) is at least `1/3`, giving (7).

The cancellation of the explicit powers of `P_n` in (20) is the key point. PF-221's reciprocal-prime difference is much smaller than the raw coefficient scale, but the thin-pant normalized hopping grows by precisely enough inverse geometric scale that a merely trace-norm-based edge estimate still costs order `1/\log P_n` on a large family of edges.

## 2. Consecutive gap doublings cannot occupy more than logarithmic runs

It remains to show that the favorable set (6) is not exceptionally thin. This requires very little arithmetic beyond the polynomial gap envelope already used elsewhere in the line.

Put

\[
\theta=0.525,
\qquad
\alpha=1-\theta=0.475.
\tag{21}
\]

From (18),

\[
P_{n+1}-P_n\le CP_n^\theta.
\tag{22}
\]

Because `x\mapsto x^\alpha` is concave,

\[
P_{n+1}^\alpha-P_n^\alpha
\le
\alpha P_n^{\alpha-1}(P_{n+1}-P_n)
\le C.
\tag{23}
\]

Summing (23) gives the coarse polynomial index bound

\[
\boxed{
P_n\le Cn^{1/\alpha}.
}
\tag{24}
\]

Therefore

\[
\boxed{
g_n\le Cn^{\theta/\alpha}.}
\tag{25}
\]

Now call an edge `n` **bad** when

\[
g_{n+1}>2g_n.
\tag{26}
\]

If `m,m+1,\ldots,m+r-1` are `r` consecutive bad edges, then

\[
g_{m+r}>2^rg_m\ge2^{r+1},
\tag{27}
\]

because gaps between odd primes are at least two. For a run contained among indices at most `N`, (25) also gives

\[
g_{m+r}\le CN^{\theta/\alpha}.
\tag{28}
\]

Thus

\[
r\le C\log N.
\tag{29}
\]

A binary string of `N` edge labels in which every bad run has length at most `R` contains at least `(N-R)/(R+1)` good labels. Applying this with `R=C\log N` proves (8):

\[
\#(\mathcal G\cap[n_0,N])
\ge c\frac{N}{\log N}.
\tag{30}
\]

This is intentionally weaker than any statement about the statistical distribution of consecutive prime-gap ratios. No such distribution theorem is needed. The argument only says that repeated strict doublings cannot persist longer than logarithmically when all gaps in the window have a polynomial upper envelope.

## 3. Two-sided block orthogonality converts the edge count into singular values

The oriented crossing blocks have exact source/target placement

\[
B_n=\Pi_{n+1}B_n\Pi_n.
\tag{31}
\]

Hence for `m\ne n`,

\[
B_n^*B_m=0,
\qquad
B_nB_m^*=0.
\tag{32}
\]

Thus the nonzero singular values of the finite sum (9) are exactly the multiset union of the singular values of the blocks `\delta_nB_n`. In particular every good edge contributes at least one singular value of size

\[
s_1(\delta_nB_n)
=\delta_n\|B_n\|.
\tag{33}
\]

Equation (24) also gives

\[
\log P_n\le C\log N
\qquad(n\le N)
\tag{34}
\]

for large `N`. Combining (7), (8), and (34), there is `c_1>0` such that at threshold

\[
\sigma_N:=\frac{c_1}{\log N},
\tag{35}
\]

one has

\[
N_{T_N}(\sigma_N)
\ge c\frac{N}{\log N}.
\tag{36}
\]

Therefore

\[
\boxed{
q(T_N)
\ge
\sigma_NN_{T_N}(\sigma_N)
\ge
c\frac{N}{(\log N)^2}
\to\infty,
}
\tag{37}
\]

which is (11).

The same orthogonality gives exact additivity of trace norms for the finite sums:

\[
\|T_N\|_1
=
\sum_{n=n_0}^{N}\delta_n\|B_n\|_1.
\tag{38}
\]

Using only the first singular value of every good block,

\[
\|T_N\|_1
\ge
c\frac{N}{(\log N)^2},
\tag{39}
\]

so (12) follows as well.

## 4. Why this does not contradict compactness of the Schur commutator

PF-222 does **not** identify `[D,E_n]` with the raw precision crossing `B_n`. The cut commutator is obtained only after inversion. Schematically, one-seam resolvent identities insert factors of

\[
D=(I+K)^{-1}
\tag{40}
\]

and the corresponding decoupled inverse around the crossing. Those contractions can be strongly scale-sensitive when `B_n` itself is large. PF-215 already warned that large raw conductance can coexist with large diagonal energy, so inversion may suppress the same mode that makes `\|B_n\|` diverge.

Accordingly, (37) proves only

\[
\boxed{
\text{raw }\delta_nB_n\text{ assembly has no weak-}S_1\text{ bound}.}
\tag{41}
\]

It does **not** prove

\[
[D,\Omega]\notin\mathcal S_{1,\infty}
\quad\text{or}\quad
P[D,\Omega]H\notin\mathcal S_{1,\infty}.
\tag{42}
\]

Indeed PF-222 already proves `[D,\Omega]` compact, and PF-223 shows abstractly why compactness alone does not decide the endpoint. PF-224 now removes a particular canonical-geometry shortcut: replacing the dressed cut flux by the trace norm of its raw one-pant crossing throws away exactly the inverse/frequency structure that must do the endpoint work.

The remaining live objects are therefore more specific:

- a direct singular-value estimate for `P[D,E_n]H` rather than `B_n`;
- a factorization of the dressed cut flux through PF-212's physical high-frequency Poisson decay before summing in `n`;
- a threshold-counting argument that uses the reciprocal-prime `\delta_n` together with effective ranks after Schur shorting;
- or one of the independent unsmoothed PF-204 / true-short-collar PF-183 routes.

These are alternatives, not conclusions of PF-224.

## 5. Prior art and novelty audit

The imported arithmetic input is exactly the Baker--Harman--Pintz short-interval theorem already pinned in `SOURCES.md` (R. C. Baker, G. Harman, J. Pintz, *The Difference Between Consecutive Primes, II*, Proc. London Math. Soc. 83 (2001), 532--562, DOI `10.1112/S0024611501012690`). PF-224 uses only its coarse consequence `g_n=O(P_n^{0.525})`; the exponent is not claimed sharp and is used solely to prevent super-polynomial growth of the indexed gaps.

No novelty is claimed for two-sided block orthogonality, singular-value counting, `\|B\|_1\ge\|B\|`, or the elementary observation that a sequence which doubles at every step cannot remain polynomially bounded for more than logarithmically many steps. These are standard operator/sequence facts.

The closest operator-theoretic literature found in the current audit concerns fixed-domain Dirichlet-to-Neumann smoothing and Schatten estimates for elliptic resolvent/boundary-map differences. That prior art supports PF-222's fixed-edge ideal regularity but does not provide a uniform theorem converting a degenerating family of raw normalized pant crossings into the missing weak endpoint. PF-223 already records the general Lorentz--Schatten boundary: qualitative compactness or fixed-edge finite-ideal membership imposes no uniform effective-rank control.

The durable project-specific statement is therefore the combination of **canonical PF-215 thin-pant conductance**, the **exact PF-221 reciprocal-prime jump**, and the **prime-gap growth envelope**. It proves that the most direct quantitative strengthening suggested by PF-222 — pay for each cut with `\delta_n\|B_n\|_1` — fails on the actual prime-flute geometry, rather than merely in an abstract block-Jacobi countermodel.

## 6. Falsification and boundary checks

1. The proof uses the actual canonical PF-205/PF-215 seam geometry and not PF-223's abstract packet construction.
2. The lower bound is on the **raw normalized precision crossing** `B_n`. It is not a lower bound on the dressed resolvent cut flux `[D,E_n]`.
3. The argument needs only one singular direction per good edge. No claim is made about the full singular-value profile of `B_n`.
4. Baker--Harman--Pintz is used only for a polynomial indexed gap envelope. A stronger prime-gap theorem would change constants/exponents in (24)--(29) but not the conclusion.
5. The good-edge counting does not assert that `g_{n+1}/g_n` has a limiting distribution, positive natural density below two, or any probabilistic law. It only excludes runs of strict doubling longer than `O(\log N)`.
6. Divergence of `\sum\delta_n\|B_n\|_1` invalidates a sufficient triangle/trace-norm proof. It does not imply divergence of a conditionally cancellative operator series, and it does not refute weak trace class for `[D,\Omega]`.
7. Nothing here changes PF-220's coefficient-adjacent low-sector weak trace estimate, PF-222's compactness theorem, PF-212's high-frequency local estimates, the unsmoothed PF-204 route, or the PF-183 true-short-collar route.
8. No RH consequence or prime/clone separation is claimed. This is an endpoint proof-architecture restriction.

## Consequences for the research line

PF-223 says the smooth route needs a quantitative PF-specific estimate. PF-224 identifies one quantitative estimate that is now decisively **too crude on the actual flute**: raw trace-norm summation of reciprocal-prime-weighted pant crossings.

The smooth-interface frontier should therefore move one layer deeper than `B_n`. The quantity to estimate is the **dressed** low/high cut flux `P[D,E_n]H`, or an equivalent factorization in which the large thin-pant conductance has already been shorted by `D` and PF-212's frequency decay is visible. Any successful proof that first discards those structures and then tries to recover the endpoint solely from `\delta_n\|B_n\|_1` cannot close.