# MC-389 — Endpoint affine rank forces a fixed excess over the Welch exception budget

## Status

`LITERATURE+DERIVED`.

This finding combines the endpoint-support affine-rank obstruction of MC-388 with Xuancheng Shao's robust restricted-sumset stability theorem to obtain a fixed additive-energy deficit, then converts that deficit through the Bochner representation into a fixed multiplicative improvement over the generic `H/R` exceptional-mode threshold from MC-386.

The fixed constants below are existential: the formulation of Shao's Lemma 4.4 used here gives a sufficiently-small threshold depending on a prescribed `epsilon`, but does not provide a numerical modulus in the statement. No effective numerical value of the final excess constant is claimed.

## Precise claim

Let `W <= F_2^R` have dimension `d`, let `H = |W| = 2^d`, and consider the endpoint Bochner kernel from MC-388

\[
g(K)=\sum_{\xi} p(\xi)(-1)^{\langle \xi,K\rangle},
\qquad
p=\sum_z d_z\,\delta_{\pi(1+e_z)},
\]

where `p` is a probability measure and its distinct support is

\[
S=\{\pi(1+e_z):1\le z\le R\},
\qquad r=|S|\le R.
\]

Assume the high-rank endpoint branch

\[
d\ge \frac{3R}{4}.
\]

Then there exists an absolute constant `c_endpoint > 0` such that the following holds for all sufficiently large `R`.

If `B subset W\setminus\{0\}` is an exceptional set and every good nonzero mode satisfies

\[
|g(K)|\le \varepsilon_R,
\qquad
K\in W\setminus(B\cup\{0\}),
\qquad
\varepsilon_R=o(R^{-1/2}),
\]

then necessarily

\[
|B|\ge (1+c_{\mathrm{endpoint}})\frac{H}{R}.
\]

Thus the endpoint support geometry forces a fixed-factor gap above the generic PSD/rank threshold `H/R` of MC-386. The result is conditional only on the stated good-mode bound; it does not supply that analytic estimate.

## Derivation

### 1. Near-maximal additive energy creates a dense small restricted sumset

For a nonempty finite set `A subset F_2^n`, write `r=|A|` and

\[
r_A(t)=|\{(a,b)\in A^2:a+b=t\}|.
\]

Its ordered additive energy is

\[
E(A)=\sum_t r_A(t)^2.
\]

Since `sum_t r_A(t)=r^2` and `r_A(t) <= r`, there is the exact deficiency identity

\[
r^3-E(A)
 =\sum_t r_A(t)(r-r_A(t))
 =\sum_{(a,b)\in A^2}\bigl(r-r_A(a+b)\bigr).
\]

Fix once and for all

\[
\epsilon_0=\frac1{100}<\frac1{20},
\qquad
\eta=\frac{\epsilon_0}{2}=\frac1{200}.
\]

Define

\[
M=\{(a,b)\in A^2:r_A(a+b)\ge (1-\eta)r\}.
\]

If

\[
E(A)\ge (1-\delta')r^3,
\]

then every pair outside `M` contributes more than `eta r` to the deficiency identity, hence

\[
|A^2\setminus M|\le \frac{\delta'}{\eta}r^2.
\]

Every value in the restricted sumset `A+_M A` has at least `(1-eta)r` representations, so

\[
|A+_M A|\le \frac{r}{1-\eta}\le (1+\epsilon_0)r.
\]

### 2. Shao stability plus high affine rank gives a fixed energy deficit

Shao's Lemma 4.4 states, in the specialization needed here, that for each fixed `epsilon in (0,1/20)` there is a sufficiently small `delta_Shao(epsilon)>0` such that if `X,Y` both have size `N`, a relation `M subset X times Y` contains at least `(1-delta_Shao)N^2` pairs, and

\[
|X+_M Y|\le (1+\epsilon)N,
\]

then `X` is close to a coset `x+L`: at most `epsilon N` elements of `X` lie outside it and at most `3 epsilon N` elements of the coset lie outside `X`.

Apply this with `X=Y=A`, `epsilon=epsilon_0`, and choose

\[
\delta'\le \eta\,\delta_{\mathrm{Shao}}(\epsilon_0).
\]

The previous step gives the hypotheses of the lemma. Therefore there is an affine coset `C=x+L` with

\[
|A\setminus C|\le \epsilon_0 r,
\qquad
|C\setminus A|\le 3\epsilon_0 r.
\]

In particular

\[
|L|=|C|\le (1+3\epsilon_0)r.
\]

Adding one affine dimension for each point outside `C` gives

\[
\dim \operatorname{aff}(A)
 \le \dim L+|A\setminus C|
 \le \log_2((1+3\epsilon_0)r)+\epsilon_0 r.
\]

For sufficiently large `r`, the right-hand side is strictly less than `r/2`. Taking the contrapositive yields fixed constants `delta_0>0` and `r_0` such that

\[
\dim\operatorname{aff}(A)\ge \frac r2,
\quad r\ge r_0
\quad\Longrightarrow\quad
E(A)\le (1-\delta_0)r^3.
\]

The existence of `delta_0` is unconditional; its numerical size is not extracted from the cited formulation of Shao's lemma.

### 3. Endpoint support lies in the high-affine-rank regime

MC-388 proved the exact endpoint identity

\[
\dim\operatorname{aff}(S)
 =d-\dim(W\cap\langle\mathbf 1\rangle)
 \ge d-1.
\]

Under `d>=3R/4`, and since `r<=R`, for sufficiently large `R`,

\[
\dim\operatorname{aff}(S)
 \ge \frac{3R}{4}-1
 \ge \frac R2
 \ge \frac r2.
\]

Hence the fixed energy gap applies:

\[
E(S)\le (1-\delta_0)r^3.
\]

This is the quantitative strengthening that MC-388 left open: the endpoint support is not merely unable to converge to a low-dimensional annihilator coset; it stays a fixed amount below maximal additive energy.

### 4. Near-Welch weighting inherits a fixed fourth-moment contraction

Let

\[
Q:=\sum_{K\in W}|g(K)|^2=H\|p\|_2^2.
\]

Suppose first that

\[
Q\le (1+\alpha)\frac HR.
\]

Because `p` is supported on `r` points,

\[
\|p\|_2^2\ge \frac1r,
\]

so

\[
r\ge \frac{R}{1+\alpha}.
\]

Let `u_S` be the uniform probability measure on `S`. Since

\[
\|p-u_S\|_2^2=\|p\|_2^2-\frac1r,
\]

we obtain

\[
\|p-u_S\|_2^2\le \frac{\alpha}{R}.
\]

The additive-energy gap gives

\[
\|u_S*u_S\|_2^2
 =\frac{E(S)}{r^4}
 \le \frac{1-\delta_0}{r}.
\]

Young's inequality and the fact that both measures have `l^1` norm one imply

\[
\|p*p-u_S*u_S\|_2
 \le 2\|p-u_S\|_2.
\]

Since `||p||_2 >= r^{-1/2}` and `r<=R`,

\[
\frac{\|p*p\|_2}{\|p\|_2}
 \le \sqrt{1-\delta_0}+2\sqrt{\alpha}.
\]

Choose a fixed `alpha_0>0` small enough that

\[
q:=\sqrt{1-\delta_0}+2\sqrt{\alpha_0}<1,
\]

for example

\[
\alpha_0=
\left(\frac{1-\sqrt{1-\delta_0}}{4}\right)^2.
\]

Set

\[
\eta_0:=1-q^2>0.
\]

Whenever `Q <= (1+alpha_0)H/R`, finite-group Plancherel gives

\[
\sum_{K\in W}|g(K)|^4
 =H\|p*p\|_2^2
 \le (1-\eta_0)H\|p\|_2^2
 =(1-\eta_0)Q.
\]

So the endpoint affine-rank gap becomes a fixed contraction of the fourth Fourier moment relative to the second.

### 5. Physical concentration forces more than `H/R` exceptional modes

Let `E=|B|`. On the good modes,

\[
\sum_{K\notin B\cup\{0\}}|g(K)|^2
 \le H\varepsilon_R^2
 =o(H/R).
\]

Welch gives `Q>=H/R`. Therefore the `L^2` mass on `B union {0}` is

\[
U:=\sum_{K\in B\cup\{0\}}|g(K)|^2
 \ge (1-o(1))Q.
\]

Suppose, toward contradiction, that for a fixed small `c>0`,

\[
E<(1+c)\frac HR.
\]

Because `|g(K)|<=1`,

\[
Q\le 1+E+H\varepsilon_R^2
 \le (1+c+o(1))\frac HR.
\]

The high-rank assumption implies `H/R -> infinity`, so the isolated `1` is negligible. Choose

\[
c\le \frac{\alpha_0}{2}.
\]

For large `R`, this puts `Q` inside the near-Welch regime of the previous step. Cauchy-Schwarz on the `E+1` modes in `B union {0}` then gives

\[
U^2
 \le (E+1)\sum_{K\in B\cup\{0\}}|g(K)|^4
 \le (E+1)(1-\eta_0)Q.
\]

Since `U >= (1-o(1))Q`,

\[
E+1
 \ge (1-o(1))\frac{Q}{1-\eta_0}
 \ge (1-o(1))\frac{H}{R(1-\eta_0)}.
\]

Thus

\[
E\ge
\left(\frac{1}{1-\eta_0}-o(1)\right)\frac HR.
\]

Because

\[
\frac{1}{1-\eta_0}>1,
\]

one may choose any fixed positive

\[
c_{\mathrm{endpoint}}
 <\min\left\{\frac{\alpha_0}{2},
 \frac12\left(\frac1{1-\eta_0}-1\right)\right\},
\]

which proves the claimed fixed-factor improvement for all sufficiently large `R`.

## Relevance

MC-386 showed that the generic PSD/rank argument alone cannot force more than approximately `H/R` exceptional modes because annihilator kernels attain that scale. MC-387 showed that abstract near-sharpness must look approximately like an annihilator. MC-388 then proved that the endpoint support has too much affine rank to approach such a low-dimensional coset, but stopped short of converting that qualitative incompatibility into a stronger exceptional count.

This finding completes that conversion. The endpoint support has a fixed additive-energy deficit; near-Welch endpoint weights therefore have a fixed fourth-moment contraction; and a Fourier kernel whose mass is concentrated on only `H/R` modes would violate that contraction. The result is the first fixed multiplicative separation from the generic Welch exception budget in this branch.

The mechanism is still only a structural obstruction. It says that any argument producing `o(R^{-1/2})` control on all but a small family of modes must pay a strictly larger exceptional family than generic rank theory predicts. It does not yet provide the analytic estimate that creates such a good/bad split, nor does it imply an RH-scale bound for `M(x)`.

## Prior-art audit

The external theorem used is Xuancheng Shao, *Additive energies of subsets of discrete cubes*, Proceedings of the Royal Society of Edinburgh Section A: Mathematics **156** (2026), 944–965, DOI `10.1017/prm.2024.126`, especially Lemma 4.4. That lemma gives robust coset stability from an almost-complete relation with small restricted sumset.

The general principle that near-maximal additive energy forces approximate coset structure is therefore prior art and is not claimed here as new. The line-specific derived contribution is the chain

`endpoint affine rank -> fixed support-energy deficit -> near-Welch fourth-moment contraction -> fixed excess over H/R exceptional modes`.

MC-387 previously used the same literature only qualitatively, obtaining `o(1)` closeness to a coset under near-extremality. The fixed-`epsilon` contrapositive here is what supplies a fixed gap rather than another asymptotic stability statement.

## Boundaries and failure modes

- The final constant is existential and ineffective from the cited theorem statement. No numerical improvement factor is claimed.
- The result requires the high-rank endpoint branch `d>=3R/4`; it is not a statement about arbitrary Bochner supports or arbitrary low-dimensional `W`.
- The good-mode hypothesis `epsilon_R=o(R^{-1/2})` is essential to make the total good-mode `L^2` mass negligible relative to the Welch scale `H/R`.
- The result does not prove such a good-mode estimate for the Möbius problem. It only strengthens the necessary exceptional-mode budget conditional on one.
- The argument uses the exact endpoint support structure from MC-388. Replacing it by a generic rank-`R` PSD kernel destroys the affine-rank input and restores the annihilator sharpness of MC-386.
- The use of Shao's stability theorem is genuinely quantitative only at the level of fixed positive constants; extracting an explicit numerical `c_endpoint` would require an explicit modulus through the inverse theorem.
- No statement here upgrades averaged, logarithmic, or short-interval Möbius cancellation to uniform global cancellation.

## Consequences

1. The `H/R` barrier from MC-386 is not the true endpoint barrier in the high-rank branch: endpoint geometry forces a fixed multiplicative excess.
2. Future analytic work in this branch should compare any attainable bad-mode count with `(1+c_endpoint)H/R`, not merely `H/R`.
3. The natural next quantitative question is whether the fixed endpoint energy deficit can be proved directly, with an effective constant, from the explicit projected-simplex support rather than through a qualitative inverse theorem.
4. A direct effective deficit would make the fourth-moment contraction and exceptional-count improvement explicit and could reveal whether the true endpoint gap is much larger than the existential constant established here.
