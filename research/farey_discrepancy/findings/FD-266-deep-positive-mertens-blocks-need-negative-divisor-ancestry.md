# FD-266 — Deep positive Mertens blocks need negative divisor ancestry to evade one-sided slack

- **Date:** 2026-09-22
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** canonical full-grid repair / one-sided slack / deep block variation / signed divisor ancestry / weighted cover obstruction / physical cushion criterion
- **Depends on:** FD-234, FD-260, FD-261, FD-263, FD-265
- **Classification:** `EXACT-DERIVED + ONE-SIDED-LOWER-BOUND + SIGNED-DIVISOR-COVER + DEEP-SHELL-DECOPULING + PHYSICAL-LIFT-CERTIFICATE + SOURCE-ROUTE-SHARPENING`

## Claim

FD-265 shows that the minimum positive slack needed by the canonical full-grid repair is one half of the positive mass of the divisor-smoothed Mertens block field

\[
U_N(q):=M(qN)-M((q-1)N),
\qquad
G_N(d):=\sum_{q\mid d}U_N(q),
\]

up to the `O(x log x)` nearest-integer budget. The remaining difficulty there is that a large raw block population can cancel under the divisor convolution `U_N -> G_N`.

On a complete dyadic coefficient band this cancellation has an exact direction: **a deep block can only be canceled by its proper-divisor ancestry, and every proper divisor is shallow.** If

\[
I_x:=\{d:x<d\le2x\},
\qquad
z^-:=(-z)_+,
\]

define the negative ancestry debt of a deep index by

\[
A_N^-(d)
:=
\sum_{\substack{q\mid d\\q<d}}U_N(q)^-.
\tag{1}
\]

For `d in I_x`, every proper divisor satisfies `q<=d/2<=x`, so (1) uses only blocks from earlier divisor scales. Then

\[
\boxed{
(G_N(d))_+
\ge
\bigl(U_N(d)-A_N^-(d)\bigr)_+.
}
\tag{2}
\]

Consequently, with

\[
\mathcal U_N^+(x)
:=
\sum_{x<d\le2x}
\bigl(U_N(d)-A_N^-(d)\bigr)_+,
\tag{3}
\]

the exact real repair `\widetilde c_N=-G_N/2` obeys

\[
\boxed{
\widetilde R_N^-(x)
:=\sum_{d\in I_x}(-\widetilde c_N(d))_+
\ge
\frac12\mathcal U_N^+(x).
}
\tag{4}
\]

For the nearest-integer repair `c_N` of FD-225/FD-234,

\[
\boxed{
R_N^-(x)
:=\sum_{d\in I_x}(-c_N(d))_+
\ge
\frac12\mathcal U_N^+(x)-O(x\log x).
}
\tag{5}
\]

Thus the post-convolution variation requirement of FD-265 can be replaced by a more local certificate: positive Mertens blocks in the deep shell transfer directly into physical slack unless enough **negative Mertens block mass already exists on their proper divisors**.

There is also an aggregate weighted-cover form. Put

\[
P_N^+(x):=
\sum_{x<d\le2x}U_N(d)^+
\tag{6}
\]

and let

\[
m_{x,+}(q)
:=
\#\{d\in I_x:q\mid d,\ U_N(d)>0\}.
\tag{7}
\]

Then

\[
\boxed{
\mathcal U_N^+(x)
\ge
P_N^+(x)-C_N^-(x),
\qquad
C_N^-(x):=
\sum_{q\le x}U_N(q)^-m_{x,+}(q).
}
\tag{8}
\]

Since `m_(x,+)(q)<=m_x(q)<=2x/q`, where `m_x` is the exact FD-263 replication multiplicity,

\[
\boxed{
C_N^-(x)
\le
2x\sum_{q\le x}\frac{U_N(q)^-}{q}.
}
\tag{9}
\]

Combining (5), (8), and (9) gives the coarse but fully one-sided lower ledger

\[
\boxed{
R_N^-(x)
\ge
\frac12P_N^+(x)
-
x\sum_{q\le x}\frac{U_N(q)^-}{q}
-O(x\log x).
}
\tag{10}
\]

For the FD-226 physical normalization

\[
\Lambda_N:=\frac{N}{D\log N},
\qquad x\asymp D,
\]

FD-260--FD-261 imply that any nonnegative physical cushion satisfying the general switched-response hypotheses has band mass

\[
\sum_{d\in I_x}p_N(d)
\ll
\Lambda_Nx^{2-\beta},
\qquad
\beta=\log_2\frac32.
\tag{11}
\]

If it pointwise lifts the canonical rounded repair, equations (5) and (11) force the necessary source condition

\[
\boxed{
\mathcal U_N^+(x)
\ll
\Lambda_Nx^{2-\beta}+x\log x.
}
\tag{12}
\]

Equivalently, the positive deep block mass must be almost entirely covered by negative shallow divisor ancestry, except for the amount permitted by the positive-cushion capacity:

\[
\boxed{
P_N^+(x)
\le
C_N^-(x)
+O\!\left(\Lambda_Nx^{2-\beta}+x\log x\right).
}
\tag{13}
\]

This is a strictly more localized obstruction than negative triangle saturation of the complete `G_N` field. Deep blocks in `(x,2x]` cannot cancel one another under divisor convolution because each appears only in the single coordinate `G_N(d)` with the same index. The only way to erase their positive contribution is through negative proper-divisor ancestry already present below `x`.

## 1. Deep coordinates are unique on a dyadic band

Fix `d in I_x`. Splitting the divisor sum into the top divisor and the proper divisors gives

\[
G_N(d)
=
U_N(d)
+
\sum_{\substack{q\mid d\\q<d}}U_N(q).
\tag{14}
\]

Because every proper divisor of `d` is at most `d/2`, and `d<=2x`, every index in the second term is at most `x`. This elementary observation is the directional counterpart of FD-263's replication fact `m_x(q)=1` for `x<q<=2x`: a deep forcing coordinate is copied once, into its own coefficient, while all cross-talk at that coordinate comes from shallower divisors.

Discarding the positive shallow contributions in (14) gives

\[
G_N(d)
\ge
U_N(d)
-
\sum_{\substack{q\mid d\\q<d}}U_N(q)^-
=
U_N(d)-A_N^-(d).
\tag{15}
\]

Since the positive-part map is monotone, (15) proves (2). Summing and using FD-265's exact identity

\[
(-\widetilde c_N(d))_+
=\frac12(G_N(d))_+
\tag{16}
\]

proves (4).

The direction of the signs matters. Positive shallow blocks can only increase `G_N(d)` and therefore cannot help a physical lift evade negative repair demand. Negative shallow blocks are the only ancestry capable of canceling a positive deep block. Replacing them by absolute values, as in a generic `l^1` ledger, loses exactly this information.

## 2. The escape condition is a weighted signed divisor cover

For `U_N(d)>0`, equation (3) loses at most `A_N^-(d)` from the raw positive block, while for `U_N(d)<=0` both its raw positive contribution and the corresponding lower term vanish. Hence

\[
\begin{aligned}
\mathcal U_N^+(x)
&\ge
\sum_{\substack{d\in I_x\\U_N(d)>0}}
\bigl(U_N(d)-A_N^-(d)\bigr)\\
&=
P_N^+(x)
-
\sum_{\substack{d\in I_x\\U_N(d)>0}}
\sum_{\substack{q\mid d\\q<d}}U_N(q)^-.
\end{aligned}
\tag{17}
\]

Exchange the finite sums. Since every proper divisor involved is at most `x`, the last double sum is exactly

\[
\sum_{q\le x}U_N(q)^-
\#\{d\in I_x:q\mid d,\ U_N(d)>0\}
=C_N^-(x),
\tag{18}
\]

which proves (8).

This has a useful combinatorial interpretation. Give every positive deep block `d` demand `U_N(d)^+`. A negative shallow block `q` carries budget `U_N(q)^-` to each positive deep multiple of `q`. For the canonical repair to avoid paying the uncovered positive mass, these negative shallow budgets must form a weighted divisor cover of the positive deep blocks. The cover is not arbitrary: one unit of negative block amplitude at `q` can be replicated only along the multiples of `q` in the band, exactly the geometry measured by `m_x(q)`.

Using `m_(x,+)(q)<=m_x(q)` and FD-263's elementary estimate `m_x(q)<=2x/q` gives (9), and then (10) follows from (5).

This is stronger than saying that shallow absolute variation may cancel deep variation. The tariff only charges **negative** shallow blocks, and only when their divisor rays actually meet **positive** deep blocks.

## 3. Positive deep variation is an exact Mertens path statistic

The raw quantity in (6) is itself an exact one-sided variation of the sampled Mertens path `A_q:=M(qN)`. Since

\[
U_N(q)=A_q-A_{q-1},
\]

put

\[
V_N(x):=
\sum_{x<q\le2x}|U_N(q)|.
\tag{19}
\]

Then the elementary positive/negative variation identity gives

\[
\boxed{
P_N^+(x)
=
\frac12
\left(
V_N(x)+M(2xN)-M(xN)
\right).
}
\tag{20}
\]

Thus (13) may be read without the divisor-smoothed field `G_N`: a physical canonical lift requires the positive variation of `M(qN)` across the deep index shell to be paid for either by negative divisor ancestry from earlier block scales or by the limited positive-cushion capacity.

Equation (20) does not by itself provide a lower bound. Large two-sided variation can still be mostly negative, and the endpoint drift can nearly cancel it. The new point is structural: once a positive increment occurs at a deep index, there is no same-scale divisor-convolution mechanism that can hide it. Its only cancellation channel is already visible in the signed ancestry debt (1).

## 4. Prime and ancestry-free channels

The divisor-cover formulation immediately isolates coordinates on which cancellation is especially restricted. If `p in I_x` is prime, its only proper divisor is `1`, so

\[
A_N^-(p)=M(N)^-.
\tag{21}
\]

Therefore (5) implies

\[
\boxed{
R_N^-(x)
\ge
\frac12
\sum_{\substack{x<p\le2x\\p\ {m prime}}}
\bigl(U_N(p)-M(N)^-\bigr)_+
-O(x\log x).
}
\tag{22}
\]

In particular, on horizons with `M(N)>=0`, every positive prime-index block passes into `G_N` without any negative-ancestry loss:

\[
\boxed{
R_N^-(x)
\ge
\frac12
\sum_{x<p\le2x}U_N(p)^+
-O(x\log x).
}
\tag{23}
\]

More generally, any subset `\mathcal D subset I_x` of positive deep blocks whose proper divisors all satisfy `U_N(q)>=0` contributes its full raw mass to the real one-sided demand. No density theorem for such indices is claimed here. The value of (22)--(23) is as a falsification target: a future arithmetic lower bound for positive block variation on a divisor-primitive subfamily would transfer directly to physical slack without first proving an `l^1` lower bound for the whole smoothed field.

Prime density alone is not enough, because it contains no sign or amplitude information about the block increments `U_N(p)`. This corollary therefore does not import the prime number theorem or any short-interval Möbius theorem.

## 5. Physical consequence and the FD-261 phase boundary

Let `p_N(d)>=0` be a physical cushion with

\[
c_N(d)+p_N(d)\ge0.
\]

Then `p_N(d)>=(-c_N(d))_+`, so (5) yields

\[
\frac12\mathcal U_N^+(x)
\le
\sum_{d\in I_x}p_N(d)+O(x\log x).
\tag{24}
\]

Substituting the FD-260 band-capacity bound (11) proves (12), and combining with (8) proves (13).

At `x\asymp D`, this supplies a new route to FD-261's superlinear source-demand threshold. One no longer has to prove that raw deep block population survives an uncontrolled divisor convolution in `l^1`. It is enough to prove that the **uncovered positive block variation** in (3) has the required scale. If

\[
\mathcal U_N^+(D)
\ge
N^{\theta-o(1)}D^{\alpha-o(1)}
\tag{25}
\]

at the same arithmetic amplitude scale as the first switched row, then the general FD-260 depletion contradicts physical liftability once

\[
\alpha>2-\beta
=1.4150374992\ldots .
\tag{26}
\]

The distinction from FD-263 is important. A dense family of deep positive blocks already adds linearly in (3); it does not need replication because the blocks occupy distinct top coordinates. What can destroy that gain is a sufficiently strong weighted cover by **negative earlier blocks on proper divisors**. The remaining source question is therefore a signed cross-scale incidence problem, not merely a block-amplitude or block-density problem.

The stronger FD-259 cone remains separate. If the positive cushion has nonnegative Möbius increments, its capacity ceiling is inverse-linear and a linear-depth demand can already be critical. Nothing here proves that extra monotonicity.

## 6. Finite sharpness audit

The coordinate inequality is not only formally possible to saturate. It is exactly sharp on a small instance of the actual Mertens block source.

Take `N=134` and `x=8`. Direct Möbius summation through `2144=16*134`, independently checked by a linear sieve and by prime-factor evaluation of `mu`, gives

\[
(U_{134}(9),\ldots,U_{134}(16))
=(7,3,2,-13,0,8,7,-8).
\tag{27}
\]

The shallow negative blocks relevant to these coordinates include

\[
U_{134}(1)=-1,
\qquad
U_{134}(5)=-10,
\qquad
U_{134}(8)=-12,
\]

with the remaining shallow values included according to their actual signs. The uncovered margins from (3) are

\[
6,0,1,0,0,7,0,0,
\]

so

\[
\mathcal U_{134}^+(8)=14.
\tag{28}
\]

Direct divisor convolution gives

\[
(G_{134}(9),\ldots,G_{134}(16))
=(6,-8,1,0,-1,7,-4,-21),
\tag{29}
\]

and hence

\[
\sum_{8<d\le16}(G_{134}(d))_+=14.
\tag{30}
\]

Thus (2)--(4) are attained with equality on this real arithmetic sample:

\[
\widetilde R_{134}^-(8)=7
=\frac12\mathcal U_{134}^+(8).
\tag{31}
\]

The audit is only a sign, endpoint, and sharpness check; the proof is the exact divisor decomposition above and does not depend on computation.

## 7. Prior-art boundary and consequence

A targeted search checked the standard Dirichlet-convolution/Möbius-inversion literature together with neighboring work on Möbius sums in short intervals and short arithmetic progressions. Those sources study cancellation of the Möbius function or general convolution structure, but no matching result was found for the repository-specific object here: consecutive fixed-length Mertens blocks, divisor smoothing into the canonical Farey repair, and the one-sided weighted-cover inequality (2)--(13). No external theorem is load-bearing. The existing `SOURCES.md` anchors for Dirichlet/Möbius structure and short-interval Möbius cancellation therefore remain sufficient; no source update is needed.

The result does **not** prove that positive deep block variation is large, that negative shallow ancestry is small, or that the weighted cover fails for the physical source. It also does not apply unchanged to a switched-only repair whose unrestricted full-grid residual materially changes the forcing increments. Its contribution is to remove one layer of ambiguity from FD-265: same-scale deep blocks cannot cancel each other after divisor smoothing. Any canonical full-grid escape must instead organize a signed cross-scale divisor cover in which earlier negative blocks cancel the later positive ones on their actual multiples.

This gives a concrete source-side target. To obstruct physical liftability it is enough to show, on an unbounded family, that positive deep Mertens block variation survives the negative proper-divisor ancestry tariff at a scale exceeding the FD-260 cushion ceiling. Conversely, any candidate escape with large positive deep variation must exhibit the required negative divisor cover explicitly rather than appeal generically to `l^1` cancellation in `G_N`.

**Verdict.** The one-sided full-grid problem localizes further. Positive blocks at the deepest index scale are unique top coordinates of the divisor transform and can be hidden only by negative mass on their proper divisors. The exact obstruction is the uncovered positive variation `\mathcal U_N^+(x)`, and physical liftability forces it below the current positive-cushion capacity. This converts the surviving arithmetic question from global triangle saturation of a smoothed field into a signed, weighted divisor-ancestry covering problem.