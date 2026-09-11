# FD-047 — four-adic dilation controls the lower tail of joint nonsquarefree occupation

**Status:** `EXACT-DERIVED + JOINT-NONSQUAREFREE-OCCUPATION + DILATION-INJECTION + FOUR-ADIC-GEOMETRIC-MEAN + ZERO-FRONTIER-CALIBRATED + LOWER-TAIL-SPARSITY`.

`FD-034` shows that rows divisible by a prime square import a lower-horizon copy of the physical Schur energy into the full projective residual. The accepted joint-occupation clue asks a sharper question: whether the **nonsquarefree rows themselves** retain a positive fraction of the physical energy. The same dilation can be kept before passing to the larger residual. This gives an exact pointwise lower bound for the joint nonsquarefree energy, and `FD-046` then calibrates its multiplicative-chain consequences by the rightmost zeta-zero exponent.

Let

\[
w(r):=\frac{J_2(r)}{r^2},\qquad
\mathcal H(N):=\sum_{s\le N}\frac{\mathbf M(\lfloor N/s\rfloor)}s,
\]

and for fixed `D>=1` write

\[
E_{H,D}:=\sum_{D<r\le H}w(r)\mathcal H(\lfloor H/r\rfloor)^2,
\]

\[
U_{H,D}:=\sum_{\substack{D<r\le H\\\mu(r)=0}}
w(r)\mathcal H(\lfloor H/r\rfloor)^2.
\]

For every fixed nonsquarefree integer `q>1`,

\[
\boxed{
U_{H,D}
\ge
w(q)E_{\lfloor H/q\rfloor,D}
}
\tag{1}
\]

whenever the lower horizon exceeds `D`. In particular, for `q=4`,

\[
\boxed{
U_{H,D}
\ge
\frac34 E_{\lfloor H/4\rfloor,D}.
}
\tag{2}
\]

Thus, on every complete `q`-adic chain `H_j=q^jH_0`, the occupation ratios

\[
u_j:=\frac{U_{H_j,D}}{E_{H_j,D}}
\]

obey a telescoping product inequality. If

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\},
\]

then `FD-046` gives the physical energy exponent `2Theta`, and hence

\[
\boxed{
\liminf_{n\to\infty}
\left(\prod_{j=1}^n u_j\right)^{1/n}
\ge
w(q)q^{-2\Theta}.
}
\tag{3}
\]

For the smallest nonsquarefree dilation `q=4`,

\[
\boxed{
\liminf_{n\to\infty}
\left(\prod_{j=1}^n
\frac{U_{4^jH_0,D}}{E_{4^jH_0,D}}
\right)^{1/n}
\ge
\frac34\,4^{-2\Theta}
\ge
\frac3{64}.
}
\tag{4}
\]

Under RH the calibrated constant in (4) is `3/16`. Unconditionally, arithmetic--geometric mean already yields the direct joint-occupation average bound

\[
\boxed{
\liminf_{n\to\infty}
\frac1n\sum_{j=1}^n
\frac{U_{4^jH_0,D}}{E_{4^jH_0,D}}
\ge\frac3{64}.
}
\tag{5}
\]

More strongly, very small joint occupation has controlled logarithmic density along every such chain. For every `0<eta<1`,

\[
\boxed{
\limsup_{n\to\infty}
\frac1n
\#\left\{1\le j\le n:
\frac{U_{q^jH_0,D}}{E_{q^jH_0,D}}\le\eta
\right\}
\le
\frac{2\Theta\log q-\log w(q)}{\log(1/\eta)}.
}
\tag{6}
\]

The right side tends to zero as `eta` tends to zero. Hence a physical vanishing-occupation mechanism may still occur on sparse horizons, but it cannot occupy a complete multiplicative tail, and thresholds below `w(q)q^{-2Theta}` must fail on a positive lower proportion of every `q`-adic chain.

## 1. A nonsquarefree dilation injects the full lower-horizon energy into `U`

The Jordan weight has the Euler-product form

\[
w(n)=\prod_{p\mid n}(1-p^{-2}).
\tag{7}
\]

Fix a nonsquarefree integer `q`. For every row `r>D`, the row `qr` is nonsquarefree, so it is one of the coordinates counted by `U_(H,D)` whenever `qr<=H`. The floor quotient satisfies the exact identity

\[
\left\lfloor\frac{H}{qr}\right\rfloor
=
\left\lfloor
\frac{\lfloor H/q\rfloor}{r}
\right\rfloor.
\tag{8}
\]

The row map `r -> qr` is injective. Moreover, every local Euler factor `1-p^(-2)` lies in `(0,1)`, so overlapping prime divisors can only make the product at `qr` larger than the product of the separate weights:

\[
\boxed{
w(qr)\ge w(q)w(r).}
\tag{9}
\]

Indeed, a prime dividing both `q` and `r` occurs once on the left and twice in `w(q)w(r)`. Summing only the nonsquarefree rows in the image of this injection gives

\[
\begin{aligned}
U_{H,D}
&\ge
\sum_{D<r\le\lfloor H/q\rfloor}
w(qr)
\mathcal H\!\left(
\left\lfloor\frac{H}{qr}\right\rfloor
\right)^2\\
&\ge
w(q)
\sum_{D<r\le\lfloor H/q\rfloor}
w(r)
\mathcal H\!\left(
\left\lfloor
\frac{\lfloor H/q\rfloor}{r}
\right\rfloor
\right)^2,
\end{aligned}
\]

which is exactly (1).

For a prime-square dilation `q=p^2`, `w(p^2)=1-p^(-2)`, so (1) is the joint-occupation version of the lower-scale row copy used inside the projective residual in `FD-034`. The distinction matters: the full residual contains every transverse squarefree contribution as well, whereas (1) lives entirely inside the smaller coordinate set defining `U`.

## 2. Multiplicative chains telescope exactly

Fix `H_0>D` and put

\[
H_j=q^jH_0,\qquad
E_j:=E_{H_j,D},\qquad
U_j:=U_{H_j,D}.
\tag{10}
\]

At these exact integer dilations, (1) becomes

\[
U_j\ge w(q)E_{j-1}.
\tag{11}
\]

For all sufficiently large `j`, `E_j>0`; in fact positivity is already elementary because terminal quotient-one rows contribute. Dividing by `E_j` and multiplying from `j=1` to `n` gives

\[
\boxed{
\prod_{j=1}^n\frac{U_j}{E_j}
\ge
w(q)^n\frac{E_0}{E_n}.
}
\tag{12}
\]

This is the exact same-horizon information that is lost if one first replaces every square-divisor family by an unrelated scalar lower-horizon inequality.

Now use the source-specific growth calibration in `FD-046`. For every `sigma>Theta`,

\[
E_{H,D}\ll_{D,\sigma}H^{2\sigma}.
\tag{13}
\]

Since `H_n=q^nH_0`, equations (12)--(13) imply

\[
\liminf_{n\to\infty}
\frac1n\sum_{j=1}^n
\log\frac{U_j}{E_j}
\ge
\log w(q)-2\Theta\log q.
\tag{14}
\]

Exponentiating proves (3). No assumption that a zero actually occurs on the line `Re(s)=Theta` is needed; the arbitrary `sigma>Theta` bound is enough.

The four-adic specialization uses `w(4)=3/4`. Since Hardy gives `Theta>=1/2` and the nontrivial zeros lie in `0<Re(s)<1`, the calibrated constant lies between `3/16` and the unconditional worst-case value `3/64`. The `q=4` choice is also the strongest guaranteed constant among nonsquarefree integer dilations: every other nonsquarefree integer is at least `8`, while `w(q)<=1` and `Theta>=1/2`.

## 3. The product bound controls the lower tail, not only the mean

Every occupation ratio satisfies `0<u_j<=1`. Rewrite (14) as

\[
\limsup_{n\to\infty}
\frac1n\sum_{j=1}^n
\log\frac1{u_j}
\le
L_q,
\qquad
L_q:=2\Theta\log q-\log w(q).
\tag{15}
\]

If `B_n(eta)` denotes the number of indices `1<=j<=n` for which `u_j<=eta`, then each such index contributes at least `log(1/eta)` to the nonnegative sum in (15). Therefore

\[
B_n(eta)\log(1/eta)
\le
\sum_{j=1}^n\log\frac1{u_j},
\]

and (6) follows.

For `q=4`, the unconditional value `Theta<=1` gives the explicit source-independent-in-form bound

\[
\limsup_{n\to\infty}
\frac{B_n(eta)}n
\le
\frac{\log(64/3)}{\log(1/eta)}.
\tag{16}
\]

This has the same worst-case numerical constant that `FD-034` obtained for the **larger projective defect**, but now applies to the joint nonsquarefree fraction itself. Since the nonsquarefree rows are only part of the transverse residual, this is a strictly sharper localization of what may fail. In particular, `U/E` cannot tend to zero along an entire four-adic tail. More quantitatively, whenever `eta<3/64`, a positive lower proportion of the four-adic horizons must satisfy `U/E>eta`.

Under RH, `L_4=log(16/3)`, so both the geometric-mean threshold and the lower-tail density improve accordingly. These conditional constants are calibration statements, not inputs to the unconditional obstruction.

## 4. Relation to the accepted occupation clue and surviving escape

The accepted clue asks whether there is a fixed `c_D>0` such that `U_(H,D)>=c_D E_(H,D)` for every sufficiently large `H`. Equation (1) does **not** prove that statement because the ratio `E_(floor(H/q),D)/E_(H,D)` may be arbitrarily small at isolated horizons. `FD-039` already shows that generic one-Lipschitz shell profiles can exploit sparse low-row amplification, so a multiplicative-chain theorem must not be promoted to pointwise control.

What changes is the allowed shape of a physical escape. It can no longer occupy all members, or even an asymptotically overwhelming lower tail at arbitrarily small thresholds, of any fixed four-adic chain. This directly improves the clue's previous four-adic projective control: `FD-034` bounded the larger angle defect, while (4)--(6) bind the actual joint nonsquarefree energy that the clue asks about.

`FD-046` also shows why the zero-frontier refinement is natural rather than cosmetic. The quadratic ceiling used in `FD-034` corresponds to the worst possible exponent `Theta=1`. The actual physical source has energy exponent `2Theta`, so the multiplicative-chain occupation constant is exactly calibrated by the same zeta-zero frontier. This still leaves all subpower and cross-chain irregularity open. A sequence selecting sparse horizons from different four-adic chains could have `U/E` tending to zero without violating (4)--(6).

Thus the pointwise occupation clue remains open. Its surviving burden is sharper: a counterexample must use cross-scale intermittency sparse enough to evade every fixed nonsquarefree dilation chain, while also surviving the terminal-density, powerful-sieve, finite/growing-packet, Walfisz, and fixed-row power-scale controls already established in `FD-038`--`FD-046`.

## 5. Prior-art and falsification boundary

The row injection, floor identity, and Jordan-weight inequality (8)--(9) are elementary. The prime-square version is already latent in the square-divisor row restriction of `FD-034`; no novelty is claimed for that local dilation algebra. The new line-level consequence is to retain those rows inside the exact **joint nonsquarefree energy** before passing to the larger projective residual, and then combine the resulting telescoping product with the physical zero-frontier energy calibration of `FD-046`.

The only non-elementary input in (3)--(6) is the classical Mertens/zeta zero-frontier growth theorem already anchored through Titchmarsh in `SOURCES.md` and transferred to `E_(H,D)` by `FD-046`. A targeted prior-art search over Farey discrepancy, Mertens-function formulations, Jordan-totient quadratic forms, and nonsquarefree restrictions located the expected Farey/Mertens and local-discrepancy literature, but no theorem matching this joint Jordan-row dilation consequence. No new literature dependency is therefore required here, and no broad novelty claim is made beyond the Mathia-specific synthesis.

The decisive checks are exact. If `q` were squarefree, the image rows `qr` would not all be nonsquarefree and (1) would fail; the nonsquarefree hypothesis is essential. The head cutoff is preserved because `r>D` implies `qr>D`. Overlap of prime divisors strengthens, rather than weakens, (9). The chain argument uses exact integer dilations, not approximate scales. Finally, equal limsup power exponents alone would not prove (3); the telescoping inequality (12) and the uniform upper envelope (13) are both load-bearing.
