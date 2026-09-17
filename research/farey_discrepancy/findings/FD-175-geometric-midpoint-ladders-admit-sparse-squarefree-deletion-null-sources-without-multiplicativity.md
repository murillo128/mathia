# FD-175 — Geometric midpoint ladders admit sparse squarefree deletion null sources without multiplicativity

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** restricted temporal acquisition / geometric sparse sensing / squarefree ternary counterexample / multiplicativity boundary
- **Depends on:** FD-117, FD-170, FD-171, FD-172, FD-173, FD-174
- **Classification:** `EXACT-DERIVED + PERMANENT-SOURCE + GEOMETRIC-NULL + SQUAREFREE-TERNARY + NONMULTIPLICATIVE`

## Claim

`FD-172`--`FD-174` show that squarefree multiplicativity plus the natural lower prime-amplitude bound turns sparse geometric midpoint observations into Möbius target-rigidity. The multiplicativity hypothesis is genuinely load-bearing: squarefree support, ternary amplitudes, the correct Möbius sign, and even exact agreement on every prime do not suffice.

Fix an integer base `B>=2`. For every finite source cutoff `X` there exists one permanent arithmetic source `a` such that

\[
a(1)=1,
\qquad
a(n)\in\{0,\mu(n)\}\quad(n\ge2),
\tag{1}
\]

with

\[
a(n)=\mu(n)\qquad(n\le X),
\tag{2}
\]

and, if desired, with every prime coefficient left untouched,

\[
a(p)=\mu(p)=-1\qquad(p\text{ prime}),
\tag{3}
\]

but `a` is not identically Möbius and nevertheless

\[
\boxed{
P_a(B^m)=P_\mu(B^m)
\qquad\text{for every }m\ge1.
}
\tag{4}
\]

Here `P_a(H)=mathcal D_(H,a)(1/2)` is the midpoint observable of `FD-170`.

Thus the counterexample never flips a Möbius sign and never creates nonsquarefree support: it only **deletes** selected squarefree composite coefficients. It can begin arbitrarily far out, so every prescribed finite source prefix and all prime-local data can be exactly physical.

The deletion set can also be sparse. For `B>=3` the construction may be chosen with natural density zero. For `B=2`, for every `eta>0` it may be chosen with upper density at most `eta` by starting the construction sufficiently far out.

A slightly stronger version is available: for any fixed multiplicative-rank cutoff `R`, the deleted coefficients may all satisfy `omega(n)>R`. Hence any fixed finite hierarchy of exact low-rank squarefree coefficients can be preserved while the whole geometric midpoint ladder remains blind.

## 1. Midpoint matching is a weighted deletion balance

Let

\[
\delta:=a-\mu,
\qquad
u(n):=1_{2\nmid n}.
\tag{5}
\]

`FD-170` gives, for every `H>=2`,

\[
P_a(H)-P_\mu(H)
=-\frac12\sum_{n\le H}(u*\delta)(n).
\tag{6}
\]

If `S` is a set of squarefree integers and we delete exactly those Möbius coefficients,

\[
a(n)=
\begin{cases}
0,&n\in S,\\
\mu(n),&n\notin S,
\end{cases}
\qquad
\delta(n)=-\mu(n)1_S(n),
\tag{7}
\]

then changing the order of summation in (6) gives

\[
C_H(S):=\sum_{n\le H}(u*\delta)(n)
=
\sum_{\substack{d\in S\\d\le H}}
-\mu(d)\,W_H(d),
\tag{8}
\]

where

\[
W_H(d)
:=\#\{r\le H/d:r\text{ odd}\}
=
\left\lceil\frac{\lfloor H/d\rfloor}{2}\right\rceil.
\tag{9}
\]

Therefore the required midpoint equality at `H` is simply

\[
C_H(S)=0.
\tag{10}
\]

For a fresh deletion in the top half-annulus `H/2<d<=H`, one has `W_H(d)=1`. Such a deletion contributes exactly `-mu(d)`, so fresh squarefree numbers of the two Möbius signs are unit positive and negative correction tokens for the scalar midpoint balance.

## 2. Integer geometric dilation creates only a bounded old-support defect

The key elementary fact is that passing from one geometric horizon to the next does not amplify the already-balanced old source by a factor comparable with the horizon. Fix `h`, put `H=B h`, and let

\[
D_B:=\lfloor B/2\rfloor.
\tag{11}
\]

Then for every `d<=h`,

\[
\boxed{
|W_{Bh}(d)-B W_h(d)|\le D_B.
}
\tag{12}
\]

To see this, write

\[
\lfloor h/d\rfloor=N,
\qquad
\lfloor Bh/d\rfloor=BN+r,
\qquad 0\le r\le B-1.
\tag{13}
\]

With `q(t)=ceil(t/2)`, the left side of (12) is

\[
|q(BN+r)-Bq(N)|.
\tag{14}
\]

If `N` is even this equals `ceil(r/2)` and is at most `floor(B/2)`; if `N` is odd it lies between `-floor(B/2)` and zero. This proves (12).

Now suppose the deletions chosen up to `h=B^(m-1)` already satisfy `C_h(S)=0`. The contribution of those old deletions at `H=B^m` is

\[
R_m
:=
\sum_{\substack{d\in S\\d\le h}}
-\mu(d)W_H(d).
\tag{15}
\]

Subtracting the zero quantity `B C_h(S)` and using (12),

\[
R_m
=
\sum_{\substack{d\in S\\d\le h}}
-\mu(d)
\bigl(W_H(d)-B W_h(d)\bigr),
\tag{16}
\]

so if `N_(m-1)=#(S cap [1,h])`,

\[
\boxed{|R_m|\le D_B N_{m-1}.}
\tag{17}
\]

This bounded dilation defect is the mechanism that makes permanent recursive repair possible. The previous midpoint constraint kills the large linear part of every old weight; only one bounded rounding defect per deleted coordinate survives at the next geometric horizon.

## 3. Fresh half-shells have enough Möbius signs to repair every step

Let

\[
N_\pm(H)
:=
\#\{n:H/2<n\le H,\ \mu(n)=\pm1\}.
\tag{18}
\]

The classical squarefree density together with `M(x)=o(x)` gives

\[
N_\pm(H)
=
\frac{3}{2\pi^2}H+o(H).
\tag{19}
\]

Indeed, the sum of the two sign counts is `Q(H)-Q(H/2)` and their difference is `M(H)-M(H/2)`. Both inputs are already anchored locally in `SOURCES.md` by the squarefree-counting and Möbius-cancellation references used elsewhere in this line.

Fix any constant

\[
0<c<\frac{3}{2\pi^2}.
\tag{20}
\]

Choose a starting exponent `m_0` so large that, for every `m>=m_0`, each sign occurs at least `c B^m` times in the top half of the ladder horizon, that `B^(m_0)/2>X`, and

\[
\frac{2D_B}{B^{m_0+1}}<c.
\tag{21}
\]

If prime coefficients are to remain untouched, simply discard primes from the available `mu=-1` pool. They have zero density, so (19) and the same eventual linear lower bound remain valid. More generally, if all squarefree coefficients with `omega(n)<=R` are to remain physical, discard those finitely many fixed-rank layers as well; their total counting function is `o(H)`, so the linear sign supply is unchanged.

At the first active horizon `H_0=B^(m_0)`, choose one allowed squarefree number of each Möbius sign in `(H_0/2,H_0]` and delete both. Their contributions `-mu(d)` cancel, so

\[
C_{H_0}(S)=0,
\qquad N_{m_0}=2.
\tag{22}
\]

All earlier ladder observations remain unchanged because the source agrees with Möbius below `H_0/2`.

Inductively assume the source has been defined through `h=B^(m-1)` and matches the midpoint there. Compute the old-support defect `R_m` at `H=B^m`. If `R_m>0`, delete `R_m` fresh allowed numbers with `mu=+1` from `(H/2,H]`; each contributes `-1`. If `R_m<0`, delete `|R_m|` fresh allowed numbers with `mu=-1`; each contributes `+1`. If `R_m=0`, delete none. Because every new deletion lies above `H/2`, its weight is exactly one, and therefore after this correction

\[
C_H(S)=0.
\tag{23}
\]

Let

\[
\lambda_B:=1+D_B.
\tag{24}
\]

Equations (17) and the construction give

\[
N_m
\le
N_{m-1}+|R_m|
\le
\lambda_B N_{m-1},
\tag{25}
\]

hence

\[
N_m\le2\lambda_B^{m-m_0}.
\tag{26}
\]

At the correction step `m>m_0`, the number of fresh coefficients required is at most

\[
D_B N_{m-1}
\le
2D_B\lambda_B^{m-m_0-1}.
\tag{27}
\]

For `B=2`, `lambda_B/B=1`; for every `B>=3`, `lambda_B/B<1`. Thus (21) implies, uniformly for all later steps,

\[
2D_B\lambda_B^{m-m_0-1}
< c B^m,
\tag{28}
\]

which is within the guaranteed supply of either Möbius sign. The induction therefore never gets stuck and defines one permanent nontrivial source satisfying (4) at every geometric horizon.

## 4. The null source can preserve arbitrarily much local arithmetic structure

The source in (7) is much closer to Möbius than the unrestricted pulse-pair kernel from `FD-171`. It obeys

\[
a(n)\in\{0,\mu(n)\},
\tag{29}
\]

so it preserves squarefree support, the ternary coefficient range, and the Möbius sign cone. By delaying `m_0`, it agrees with Möbius on any prescribed finite prefix. By excluding primes from the correction pool, it also has

\[
a(p)=\mu(p)
\quad\text{for every prime }p,
\tag{30}
\]

and all prime powers are automatically unchanged because both sources vanish there for exponent at least two.

Using the fixed-rank almost-prime count already anchored in this line, the same construction can avoid every squarefree integer with `omega(n)<=R` for any fixed `R`. Thus no finite hierarchy of exact low-multiplicative-rank coefficient constraints restores the geometric target-rigidity. What `FD-172`--`FD-174` use is the **global product coupling** that determines every squarefree composite from the prime coordinates.

The support bound (26) also quantifies sparsity. If `B>=3`, then `lambda_B<B`, so

\[
\frac{N_m}{B^m}
\le
\frac{2}{B^{m_0}}
\left(\frac{\lambda_B}{B}\right)^{m-m_0}
\longrightarrow0.
\tag{31}
\]

Because new deletions are placed only in the top half of each geometric shell, this implies natural density zero for the full deletion set, not merely along the sampled horizons.

For `B=2`, (26) only gives the uniform ladder-scale estimate

\[
\frac{N_m}{2^m}\le2^{1-m_0}.
\tag{32}
\]

Between adjacent dyadic horizons the corresponding upper-density bound is at most `2^(2-m_0)`. Since `m_0` is arbitrary, the deletion set can have upper density smaller than any prescribed positive `eta`. No zero-density claim is made for the dyadic construction from this argument alone.

The constructed source cannot be multiplicative. It is nontrivial, lies inside the coefficient bounds of `FD-172`, and matches the entire geometric ladder; `FD-173` would force it to equal Möbius if multiplicativity were present.

## 5. Representation audit, prior art, and dependency ledger

The working representation is exactly the midpoint temporal convolution of `FD-170`, rewritten as the weighted source balance (8). No new observable or norm is introduced. The construction preserves the native midpoint values on the declared geometric ladder while modifying source coefficients only by squarefree sign-compatible deletions.

The generic layer is a lacunary-repair mechanism: once a previous scalar observation is balanced, integer dilation changes each old counting weight by only `O_B(1)` after subtracting the scaled previous row, while the new top half-shell supplies `Theta(H)` fresh unit coordinates of either correction sign. This is a statement about the row geometry of the changing midpoint operator.

The arithmetic-specific layer is twofold. First, the Farey midpoint identity produces precisely the odd-multiple counting weights `W_H(d)`. Second, Möbius has linearly many squarefree coefficients of each sign in every sufficiently large half-shell; classical squarefree density plus unconditional Möbius cancellation supplies that sign reservoir. Preserving every fixed multiplicative rank uses the already-anchored fixed-rank almost-prime estimate.

The information deliberately lost is global multiplicative compatibility. Prime values, prime-power zeros, squarefree support, coefficient signs and any fixed finite rank can all remain correct. What changes is the relation between a high-rank squarefree composite and the product of its prime coordinates. The capability change is therefore sharp: sparse geometric midpoint target-rigidity in `FD-172`--`FD-174` is not a consequence of coefficient sparsity or sign positivity alone; it comes from the global Euler-product coupling.

A focused prior-art search covered Farey midpoint formulas, Möbius sign densities, geometric/lacunary sampling, and sparse arithmetic-source recovery. It recovered the standard Farey symmetry and the classical squarefree/Mertens inputs, but no direct statement of this recursive geometric-ladder deletion null construction. No new external theorem is load-bearing beyond references already present in `SOURCES.md`: Davenport supplies more than the needed `M(x)=o(x)`, Walfisz supplies squarefree counting, and the fixed-rank strengthening uses the existing Landau/Wright anchor. `SOURCES.md` therefore needs no update.

The result does **not** weaken the `FD-172`--`FD-174` theorems: their multiplicativity hypothesis is removed here. Nor does it show that a multiplicative source can evade sparse acquisition, provide pairwise inversion information, or change the Franel--Landau destination estimate.

Dependency ledger: `FD-170` supplies the midpoint convolution; `FD-171` supplies the unrestricted sparse-time null baseline; `FD-172` identifies multiplicative positivity on dyadic annuli; `FD-173` classifies sparse target-rigidity inside the multiplicative cone; and `FD-174` makes the geometric case finite-scale. The present theorem isolates the exact structural boundary on the other side. No accepted clue changes status.

## Research consequence

The source-restriction frontier opened by `FD-171` is now substantially sharper. **Squarefree ternary fidelity is not enough, even when every prime coefficient is exactly Möbius and the deviations are arbitrarily far out and sparse.** The successful sparse rigidity of `FD-172`--`FD-174` depends on a global multiplicative product law that prevents independent high-rank shell repair.

The next useful question is therefore not whether to add more local coefficient restrictions one at a time. It is to identify the weakest genuinely multiplicative compatibility that blocks the recursion above: for example, how much divisor-product consistency across growing rank or scale is enough to turn the fresh half-shell correction reservoir back into nonnegative prime defects. Pairwise sparse inversion and destination coupling remain separate questions.

The finite-scale geometric first-hit problem of `FD-174` is still meaningful **inside** the multiplicative cone, but outside that cone improved Diophantine first-hit bounds cannot restore target-rigidity: the source can repair each sampled horizon after the prime-power orbit has already been hit.

## Formalization gate

The bounded dilation lemma (12) and the finite recursive repair step are elementary and formalizable. The full permanent-source existence theorem additionally uses asymptotic positive density of both Möbius signs, and the fixed-rank strengthening uses almost-prime counting. Those analytic inputs are not part of the existing bounded midpoint formalization surface. Creating a new execution-ready formalization issue would therefore pull in a much larger analytic dependency stack than the theorem's current verification value warrants; no formalization issue is opened in this pass.

## Related findings

- `FD-170` — consecutive midpoint horizons invert the unrestricted source.
- `FD-171` — omitting temporal rows creates exact permanent null directions over unrestricted sources.
- `FD-172` — squarefree multiplicativity restores dyadic Möbius target-rigidity.
- `FD-173` — prime-power annulus hitting characterizes sparse target-rigidity inside that multiplicative class.
- `FD-174` — integer geometric ladders admit explicit finite-scale certification inside that class.
