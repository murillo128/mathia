# MC-498 — Endpoint-start bias is priced by effective quotient fibres

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-DYADIC/HYPERBOLA+DERIVED` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-497` shows, for the quadratic repeated-residue cross-root phase, that a fixed-length short interval can have order-one normalized bias only at a sparse set of physical conductor starts. The unresolved source question was whether the **actual first-exit endpoint map** can put enough reconstruction mass on those exceptional starts.

There is a deterministic intermediate answer. For endpoint-only blocks, arbitrary variable overlap lengths in one dyadic band can be controlled by the **effective support of the actual weighted start measure**, and the physical first-exit endpoint maps have an explicit quotient-fibre bound. Consequently a fixed order-one endpoint bias can survive only if the true winning-endpoint weights have low effective participation after quotienting, or if the quotient fibres themselves are large.

Keep the quadratic setting of `MC-497`: `p` is an odd prime, `chi` is the quadratic character modulo `p`, `a` is a nonzero repeated source residue, `c=h a^{-1} (mod p)`, and

\[
F_c(m):=R_c(m)-\mu_c,
\qquad
S_{c,x}(L):=\sum_{j=1}^{L}F_c(x+j),
\tag{1}
\]

with starts read modulo `p`. `MC-497` proves, uniformly for `1<=L<=p`,

\[
\sum_{x\bmod p}|S_{c,x}(L)|^2
\ll pL+\sqrt p\,L^2.
\tag{2}
\]

The first new step is a maximal version sufficient for variable overlap lengths. For `1<=H<=p`,

\[
\boxed{
\sum_{x\bmod p}
\max_{1\le L\le H}|S_{c,x}(L)|^2
\ll
pH\log^2(2H)+\sqrt p\,H^2\log(2H).
}
\tag{3}
\]

Hence let `\mathcal I` be any finite family of physical intervals with starts `x_i (mod p)`, lengths

\[
H/2\le L_i\le H,
\tag{4}
\]

and nonnegative weights `lambda_i`. Define

\[
w(x):=\sum_{i:x_i=x}\lambda_i,
\qquad
R_{\rm start}:=\frac{\|w\|_1^2}{\|w\|_2^2},
\tag{5}
\]

and

\[
B:=\sum_i\lambda_i S_{c,x_i}(L_i),
\qquad
M:=\sum_i\lambda_iL_i.
\tag{6}
\]

Then

\[
\boxed{
\frac{|B|}{M}
\ll
\frac{1}{\sqrt{R_{\rm start}}}
\left(
\frac pH\log^2(2H)+\sqrt p\log(2H)
\right)^{1/2}.
}
\tag{7}
\]

Thus a fixed order-one centered bias in one dyadic length band requires

\[
\boxed{
R_{\rm start}
\ll_\varepsilon
\frac pH\log^2(2H)+\sqrt p\log(2H).
}
\tag{8}
\]

This replaces the qualitative phrase “the source must concentrate on exceptional starts” by an `l1/l2` admission test for the **actual weighted start pushforward**.

The second new step prices that pushforward for the physical first-exit endpoints. Let the positive source interval be

\[
I=[X,X+Y]\cap\mathbf Z,
\tag{9}
\]

and restrict first-exit labels to one dyadic block `Q<=q,r<=2Q` with

\[
q\equiv r\equiv a\pmod p.
\tag{10}
\]

For the two roots, the endpoint-only shortened intervals begin at

\[
u_q=\left\lceil\frac Xq\right\rceil,
\qquad
v_r=\left\lceil\frac{X+h}{r}\right\rceil.
\tag{11}
\]

Whenever their intersection is nonempty, its physical start is exactly

\[
\boxed{x_{q,r}=\max(u_q,v_r).}
\tag{12}
\]

For `Z>=4Q`, define

\[
D(Z;Q,p)
:=
\left(2+\frac{Z}{2Qp}\right)
\left(1+\frac{8Q^2}{Zp}\right).
\tag{13}
\]

Then for every residue `xi (mod p)`, even before imposing primality,

\[
\boxed{
\#\left\{q\in[Q,2Q]\cap\mathbf Z:
q\equiv a\pmod p,
\left\lceil\frac Zq\right\rceil\equiv\xi\pmod p
\right\}
\le D(Z;Q,p).
}
\tag{14}
\]

Therefore `(14)` applies a fortiori to the actual first-exit primes. It is an explicit deterministic bound on how much the reciprocal endpoint quotient can fold one repeated conductor residue class back onto one physical start residue.

Finally, `(7)` and `(14)` combine without assuming that every plus/minus pair overlaps. Let `\mathcal P` be any selected set of nonempty cross-root overlaps whose lengths lie in `(4)`, and give a pair `(q,r)` its endpoint-only factorable weight `alpha_q beta_r>=0`. Split `\mathcal P` according to which endpoint wins the maximum in `(12)`, assigning ties to the plus side. Define the induced winning-endpoint weights

\[
\gamma_q
:=\alpha_q\!\sum_{\substack{r:(q,r)\in\mathcal P\\u_q\ge v_r}}\!\beta_r,
\qquad
\delta_r
:=\beta_r\!\sum_{\substack{q:(q,r)\in\mathcal P\\v_r>u_q}}\!\alpha_q.
\tag{15}
\]

Put

\[
C_+=\sum_q\gamma_q,
\quad C_- =\sum_r\delta_r,
\quad C=C_++C_-,
\quad \theta_\pm=C_\pm/C,
\tag{16}
\]

and, when the corresponding side is nonempty,

\[
\kappa_+
:=\frac{C_+^2}{\sum_q\gamma_q^2},
\qquad
\kappa_-
:=\frac{C_-^2}{\sum_r\delta_r^2}.
\tag{17}
\]

Let

\[
D_+=D(X;Q,p),
\qquad
D_-=D(X+h;Q,p),
\tag{18}
\]

assuming `X,X+h>=4Q`. The actual start pushforward of the pair weights satisfies

\[
\boxed{
\frac1{\sqrt{R_{\rm start}}}
\le
\theta_+\sqrt{\frac{D_+}{\kappa_+}}
+
\theta_-\sqrt{\frac{D_-}{\kappa_-}}.
}
\tag{19}
\]

Combining `(7)` and `(19)` gives the explicit source-frame bound

\[
\boxed{
\frac{|B|}{M}
\ll
\left(
\theta_+\sqrt{\frac{D_+}{\kappa_+}}
+
\theta_-\sqrt{\frac{D_-}{\kappa_-}}
\right)
\left(
\frac pH\log^2(2H)+\sqrt p\log(2H)
\right)^{1/2}.
}
\tag{20}
\]

In particular, if both winning-endpoint populations carrying nonnegligible mass satisfy

\[
\frac{\kappa_\pm}{D_\pm}
\gg
\frac pH\log^2(2H)+\sqrt p\log(2H),
\tag{21}
\]

then their endpoint-only centered bias is `o(1)` of the overlap mass. A surviving order-one bias must therefore exhibit a concrete failure of `(21)`: low effective winning-endpoint participation, large quotient fibres, or concentration in a different dyadic length band. This is the first deterministic source-map tariff after `MC-497`; it does not assume that starts are random or equidistributed.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Dyadic maximalization of the MC-497 second moment

Let `H_0` be the least power of two at least `H`, so `H<=H_0<2H`. Use the standard dyadic partition tree of `{1,...,H_0}`. Every prefix `{1,...,L}`, `L<=H`, is a disjoint union of at most

\[
J:=1+\lceil\log_2 H\rceil
\tag{22}
\]

canonical dyadic blocks, with at most one block of each length `2^k`.

For fixed `x`, Cauchy on that block decomposition gives

\[
|S_{c,x}(L)|^2
\le
J\sum_{I\in\mathcal D(L)}
\left|\sum_{j\in I}F_c(x+j)\right|^2.
\tag{23}
\]

Taking the maximum over `L` and enlarging to all canonical dyadic blocks only increases the right side. At scale `2^k` there are `H_0/2^k` such blocks. Translation in `x` does not change their complete start energy, so `(2)` gives

\[
\begin{aligned}
\sum_x\max_{L\le H}|S_{c,x}(L)|^2
&\ll
J\sum_{k\le\log_2 H_0}
\frac{H_0}{2^k}
\left(p2^k+\sqrt p\,2^{2k}\right)\\
&\ll
pH\log^2(2H)+\sqrt p\,H^2\log(2H),
\end{aligned}
\tag{24}
\]

which is `(3)`. This is only dyadic maximal bookkeeping applied to the already-audited complete shifted-correlation estimate in `MC-497`; no new character-sum theorem is being asserted.

For `(7)`, group the intervals by their start residue. Since every `L_i<=H`,

\[
|B|
\le
\sum_x w(x)\max_{L\le H}|S_{c,x}(L)|.
\tag{25}
\]

Cauchy, `(3)`, and `M>=(H/2)\|w\|_1` prove `(7)`. Notice that no independence is assumed between interval length and start: the maximalization permits an adversarial length choice at every occupied start.

## 2. The physical endpoint map is a floor/ceiling quotient map

Fix `Z>=4Q` and put

\[
u(q)=\left\lceil\frac Zq\right\rceil,
\qquad Q\le q\le2Q.
\tag{26}
\]

Because `Z>=4Q`, every represented value satisfies `u>=2`. For a fixed integer `u`,

\[
u(q)=u
\quad\Longleftrightarrow\quad
\frac Zu\le q<\frac{Z}{u-1}.
\tag{27}
\]

The interval in `(27)` has length

\[
\frac{Z}{u(u-1)}.
\tag{28}
\]

On the dyadic q-range,

\[
u\ge\frac{Z}{2Q},
\qquad
u-1\ge\frac{Z}{4Q},
\tag{29}
\]

so `(28)` is at most `8Q^2/Z`. An interval of length `L` contains at most `1+L/p` integers in one fixed residue class modulo `p`. Hence every **exact** quotient value `u` is represented by at most

\[
1+\frac{8Q^2}{Zp}
\tag{30}
\]

eligible integers `q`.

As `q` ranges from `Q` to `2Q`, the possible values of `u` lie in an integer interval of width at most `Z/(2Q)+2`. One fixed residue class `u=xi (mod p)` therefore contributes at most

\[
2+\frac{Z}{2Qp}
\tag{31}
\]

exact quotient values. Multiplying `(30)` and `(31)` proves `(14)`.

The proof deliberately counts all integers `q congruent a (mod p)`. Restricting to primes, active first-exit labels, or any thinner source subset only decreases the fibre. Thus `(14)` uses no prime-distribution theorem and cannot fail because of a possible irregular distribution of primes in progressions.

## 3. Winning-endpoint participation controls the weighted start pushforward

Every selected pair in `\mathcal P` has start `max(u_q,v_r)`. Split ties consistently toward `u_q`. Then the total weight assigned to plus endpoint `q` is exactly `gamma_q`, and the total weight assigned to minus endpoint `r` is exactly `delta_r`. Therefore the conductor start measure is

\[
w(\xi)
=
\sum_{q:u_q\equiv\xi\ (p)}\gamma_q
+
\sum_{r:v_r\equiv\xi\ (p)}\delta_r.
\tag{32}
\]

For the plus pushforward, every fibre in `(32)` contains at most `D_+` labels by `(14)`. Cauchy inside each fibre gives

\[
\sum_\xi
\left(\sum_{q:u_q\equiv\xi}\gamma_q\right)^2
\le
D_+\sum_q\gamma_q^2.
\tag{33}
\]

The analogous minus estimate has `D_-`. Minkowski in `l2(F_p)` then yields

\[
\|w\|_2
\le
\sqrt{D_+}\,\|\gamma\|_2
+
\sqrt{D_-}\,\|\delta\|_2.
\tag{34}
\]

Divide by `\|w\|_1=C`, use `(16)`--`(17)`, and obtain `(19)`.

This step is why arbitrary overlap selection does not invalidate the quotient-fibre theorem. Selection can concentrate the **induced winning-endpoint weights**, but that concentration appears explicitly as small `kappa_+` or `kappa_-`; it is not hidden inside an unproved equidistribution assumption. In particular, a sparse exceptional overlap subfamily can still escape `(20)`, but only by paying through the effective participation that the exact source/reconstruction weights actually produce.

## 4. What this resolves from MC-497

`MC-497` left a binary-looking question: do actual first-exit starts overpopulate the sparse exceptional sets of a short quadratic character sum? Equations `(7)` and `(20)` replace that with two quantitative objects that are native to the source frame:

1. the effective support `R_start` of the **weighted** physical start measure; and
2. the winning-endpoint participation ratios `kappa_+`, `kappa_-`, divided by the explicit quotient-fibre costs `D_+`, `D_-`.

This is stronger than counting distinct starts and stronger than assuming uniform distribution. A family may occupy many nominal starts but still fail because almost all reconstruction weight is carried by a few of them; that failure is recorded by `R_start`. Conversely, no detailed comparison with the individual exceptional sets from `MC-497` is necessary once `(21)` holds, because the maximal second moment controls an adversarial choice of every overlap length and every occupied start simultaneously at the stated logarithmic tariff.

The result does **not** establish `(21)` for the full normalized q-vdC reconstruction. The exact outer/staged coefficients must now be inserted into `(15)` and their participation ratios computed. Nor does it treat the lower-prime hard masks inside each overlap; those are not endpoint-only weights and remain the independent arithmetic channel isolated by `MC-495`--`MC-497`.

## 5. Prior art and novelty boundary

The character-sum input is exactly the `MC-497` complete shifted-correlation second moment, whose Weil/pseudorandom-sequence boundary was already audited there. The passage from fixed length to `(3)` is elementary dyadic maximalization, and `(27)`--`(31)` are the classical hyperbola/floor-quotient geometry behind grouping integers by `floor(Z/q)` or `ceil(Z/q)`. Cauchy, Minkowski and participation ratios are standard Hilbert-space bookkeeping.

A targeted audit of neighboring short-character-sum, large-sieve and quotient-grouping languages found no reason to promote any of these abstract ingredients as new theorems, and none is claimed as such. The durable Mathia contribution is the **exact source-frame composition**: the physical first-exit intersection start is the maximum of two reciprocal endpoint quotients, arbitrary overlap selection is absorbed into induced winning-endpoint weights, and the resulting conductor bias is bounded by the explicit participation/fibre inequality `(20)`.

Accordingly this finding claims no novelty for maximal inequalities, floor-quotient fibres, character-sum moments, or `l1/l2` effective support. Its value is to turn the live MC-497 source-distribution requirement into a falsifiable calculation on the actual reconstruction coefficients.

## Boundaries and falsification tests

- **Quadratic character.** The input `(2)` is the quadratic shifted-product second moment from `MC-497`. Higher-order characters require their own complete shifted-correlation bound before `(3)` can be imported.
- **Endpoint-only amplitude.** The pair weights are nonnegative and factor as `alpha_q beta_r`, as in `MC-496`. Lower-prime pair-sieve masks or an inner q-dependent complex coefficient are not controlled by `(20)`.
- **One repeated conductor residue.** The phase `c=h a^{-1}` is fixed only within one class `q,r congruent a (mod p)`. Distinct conductor residues remain separate phase directions.
- **One dyadic q-block and one dyadic overlap-length band.** Global reconstruction must sum the corresponding blocks and charge the resulting logarithmic number of scales rather than treating `(20)` as a one-shot global estimate.
- **Positive large source endpoints for `(14)`.** The displayed fibre constant assumes `Z>=4Q`; the finitely shorter quotient regime must be counted directly and may have larger fibres.
- **Effective participation is not yet estimated.** A source-derived coefficient may concentrate `gamma` or `delta` enough that `(21)` fails. Such concentration is now the exact endpoint-only escape rather than an unspecified exceptional-start possibility.
- **No hard-mask conclusion.** Even if `(21)` closes endpoints, the lower-prime sieve profile in `MC-495` can still create a non-interval conductor weight and requires a separate signed-correlation theorem or obstruction.
- **No Möbius summatory conclusion.** The result prices one short-overlap source mechanism inside the normalized first-exit architecture; it does not improve the known bound for `M(x)`.

## Consequence for the research line

The quadratic short-overlap endpoint branch has advanced from exceptional-set sparsity to an explicit source-weight criterion. It is no longer enough to ask whether first-exit starts look dispersed. In each dyadic q/overlap block, the exact reconstruction must compute the induced winning-endpoint weights `(15)` and test `(21)`.

If those participation ratios dominate the quotient-fibre costs by the threshold in `(21)`, endpoint-only cross-root bias is quantitatively negligible even below the `sqrt(p) log p` completion scale. If they do not, the failure identifies the precise concentrated endpoint subfamily that must be explained or estimated next. The separate lower-prime hard-mask and pre-aggregation q-specific arithmetic channels remain live.