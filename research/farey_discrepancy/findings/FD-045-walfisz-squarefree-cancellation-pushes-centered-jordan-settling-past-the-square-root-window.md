# FD-045 — Walfisz squarefree cancellation pushes centered Jordan settling past the square-root window

**Status:** `LITERATURE-DERIVED + EXACT-DERIVED + WEIGHTED-SQUAREFREE-TRANSFER + CENTERED-JORDAN-KERNEL + ZERO-FREE-REGION + SUPER-SQUARE-ROOT-FREQUENCY-WINDOW + PHYSICAL-SOURCE-CONDITIONAL`.

`FD-044` factors the centered nonsquarefree Jordan Mellin kernel, uses the Vinogradov--Korobov bound on `zeta(1+it)`, and controls critical packets whose frequency diameter stays below `R^(1/2-eta)`. Its apparent square-root threshold comes only from the crude centered summatory estimate `C(x)=O_sigma(x^sigma)` for every `sigma>1/2` when the infinite kernel is truncated at row horizon `R`.

The centered coefficients have more arithmetic structure than that estimate records. The weighted squarefree Euler product in `FD-044` contains the classical squarefree factor `zeta(s)/zeta(2s)` times an Euler product absolutely convergent throughout `Re(s)>0`. Consequently Walfisz's unconditional squarefree counting error transfers to the weighted Jordan squarefree sum and, after the density main term cancels, to the centered coefficient sum itself.

There is therefore a constant `c>0` such that, with

\[
\Lambda(x):=
\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}},
\]

one has

\[
\boxed{
C(x):=\sum_{r\le x}
 w(r)\bigl(\mathbf 1_{\mu(r)=0}-\delta_{\rm ns}\bigr)
\ll
x^{1/2}e^{-c\Lambda(x)}.
}
\tag{1}
\]

As a result, the finite-row centered Mellin kernel satisfies

\[
\boxed{
K_{R,D}(t)
=\mathfrak K(1-it)+O_D(1)
+O\!\left((1+|t|)R^{-1/2}e^{-c\Lambda(R)}\right),
}
\tag{2}
\]

where `mathfrak K` is the infinite centered kernel from `FD-044`. Hence, for every fixed `D` and every sufficiently small fixed `c_1>0`, uniformly on the **super-square-root** window

\[
|t|\le
R^{1/2}e^{c_1\Lambda(R)},
\tag{3}
\]

\[
\boxed{
|K_{R,D}(t)|
\ll_D
1+\log^{2/3}(2+|t|).
}
\tag{4}
\]

The gain over `FD-044` is not a new power of `R`: Walfisz does not change the classical `x^(1/2)` power barrier in squarefree counting. It does show that the square-root frequency scale itself is **not** the finite-horizon obstruction. The same universal nonsquarefree occupation estimate survives beyond it by a subexponential factor.

## 1. The weighted squarefree Euler product has an explicit classical squarefree factor

Keep the notation of `FD-044`:

\[
w(n)=\frac{J_2(n)}{n^2},
\qquad
s(n)=\mu(n)^2w(n),
\]

and

\[
S(z):=\sum_{n\ge1}\frac{s(n)}{n^z}
=\zeta(z)A(z).
\tag{5}
\]

For a prime `p`, `FD-044` gives

\[
A_p(z)
=(1-p^{-z})\bigl(1+(1-p^{-2})p^{-z}\bigr).
\tag{6}
\]

Writing `u=p^{-z}`, the local factor has the exact factorization

\[
\begin{aligned}
A_p(z)
&=1-u^2-p^{-2}u+p^{-2}u^2\\
&=(1-u^2)
\left(1-\frac{p^{-2}u}{1+u}\right).
\end{aligned}
\tag{7}
\]

Therefore

\[
\boxed{
A(z)=\frac{B(z)}{\zeta(2z)},
\qquad
B(z):=\prod_p
\left(1-\frac{p^{-(z+2)}}{1+p^{-z}}\right),
}
\tag{8}
\]

and hence

\[
\boxed{
S(z)=B(z)\frac{\zeta(z)}{\zeta(2z)}.
}
\tag{9}
\]

For every fixed `sigma_0>0`, the local deviation from one in `B(z)` is `O_(sigma_0)(p^(-2-sigma_0))` uniformly on `Re(z)>=sigma_0`. Thus `B` has an absolutely convergent Dirichlet series

\[
B(z)=\sum_{d\ge1}\frac{b(d)}{d^z}
\tag{10}
\]

throughout `Re(z)>0`. Since

\[
\frac{\zeta(z)}{\zeta(2z)}
=\sum_{n\ge1}\frac{\mu(n)^2}{n^z},
\tag{11}
\]

equation (9) is the coefficient identity

\[
\boxed{s=b*\mu^2.}
\tag{12}
\]

This is the useful structural point: the weighted Jordan squarefree sequence differs from the ordinary squarefree indicator only by an arithmetic smoothing factor whose coefficients are absolutely summable with every positive power weight.

## 2. Walfisz transfers through the absolutely convergent factor

Let

\[
Q(x):=\sum_{n\le x}\mu(n)^2.
\]

Walfisz's classical zero-free-region estimate gives constants `c_0>0` and `x_0` such that

\[
\boxed{
Q(x)=\frac{x}{\zeta(2)}
+O\!\left(
x^{1/2}e^{-c_0\Lambda(x)}
\right)
}
\tag{13}
\]

for `x>=x_0`. This is the only new external theorem used here.

By (12),

\[
\sum_{n\le x}s(n)
=\sum_{d\le x}b(d)Q(x/d).
\tag{14}
\]

The main term is

\[
\frac{x}{\zeta(2)}\sum_{d\le x}\frac{b(d)}d.
\tag{15}
\]

Because (10) converges absolutely already on every line `Re(z)=epsilon>0`, its omitted tail contributes `O_epsilon(x^epsilon)`. Moreover, `A(1)=c_{\rm sf}` from `FD-044`, while (8) gives

\[
\frac{B(1)}{\zeta(2)}=c_{\rm sf}.
\tag{16}
\]

It remains to transfer the error in (13). Fix `theta in (0,1)`. For `d<=x^theta`, `x/d>=x^(1-theta)`, so after decreasing the Walfisz constant if necessary,

\[
\Lambda(x/d)\ge c_\theta\Lambda(x)
\tag{17}
\]

for all sufficiently large `x`. Hence this range contributes

\[
\ll
x^{1/2}e^{-c_2\Lambda(x)}
\sum_d\frac{|b(d)|}{d^{1/2}}
\ll
x^{1/2}e^{-c_2\Lambda(x)}.
\tag{18}
\]

For `d>x^theta`, use the elementary squarefree error `Q(y)=y/zeta(2)+O(y^(1/2))`. Choose any fixed `sigma_0 in (0,1/2)`. Absolute convergence of (10) on `Re(z)=sigma_0` gives

\[
\sum_{d>x^\theta}\frac{|b(d)|}{d^{1/2}}
\le
x^{-\theta(1/2-\sigma_0)}
\sum_d\frac{|b(d)|}{d^{\sigma_0}},
\tag{19}
\]

which is polynomially smaller than the right side of (18). Combining (14)--(19), with a possibly smaller positive constant `c`, gives

\[
\boxed{
\sum_{n\le x}\mu(n)^2w(n)
=c_{\rm sf}x
+O\!\left(x^{1/2}e^{-c\Lambda(x)}\right).
}
\tag{20}
\]

This transfer is elementary once the factorization (8) is exposed; no new squarefree counting theorem is claimed.

## 3. Density centering inherits the Walfisz saving exactly

Define the centered coefficient as in `FD-043`--`FD-044`,

\[
\kappa(n)
:=w(n)\left(\mathbf 1_{\mu(n)=0}-\delta_{\rm ns}\right)
=(1-\delta_{\rm ns})w(n)-s(n).
\tag{21}
\]

`FD-038` gives the exact first-order Jordan-weight sum

\[
\sum_{n\le x}w(n)
=\frac{x}{\zeta(3)}+O(1),
\tag{22}
\]

and

\[
\delta_{\rm ns}=1-\zeta(3)c_{\rm sf}.
\tag{23}
\]

Thus

\[
\frac{1-\delta_{\rm ns}}{\zeta(3)}=c_{\rm sf},
\tag{24}
\]

so the two linear terms in (20)--(22) cancel identically. Equations (20)--(24) prove (1).

This identifies the true source of the `1/2` exponent in the centered row problem: it is the ordinary squarefree counting barrier carried by `1/zeta(2z)`, not an independent Jordan-weight phenomenon. The extra Jordan factor `B(z)` is analytically harmless far to the left of that boundary.

## 4. The finite centered kernel settles beyond square-root frequency

The infinite centered Dirichlet series from `FD-044` is

\[
\mathfrak K(z)
:=\sum_{n\ge1}\frac{\kappa(n)}{n^z}.
\tag{25}
\]

At `z=1-it`, Ford's Vinogradov--Korobov estimate, already anchored for `FD-044`, gives

\[
|\mathfrak K(1-it)|
\ll \log^{2/3}(2+|t|).
\tag{26}
\]

For the tail beyond `R`, Abel summation and (1) give

\[
\begin{aligned}
\left|
\sum_{n>R}\kappa(n)n^{-1+it}
\right|
&\ll
R^{-1/2}e^{-c\Lambda(R)}\\
&\quad +(1+|t|)
\int_R^\infty
x^{-3/2}e^{-c\Lambda(x)}\,dx\\
&\ll
(1+|t|)R^{-1/2}e^{-c'\Lambda(R)}
\end{aligned}
\tag{27}
\]

for some `c'>0`; decreasing the constant absorbs the slow variation of `Lambda`. Removing the fixed first `D` coefficients costs `O_D(1)`, proving (2) with a renamed constant.

Choose any fixed `c_1` strictly smaller than the decay constant in (27). If (3) holds, the tail in (27) is

\[
O\!\left(e^{-(c-c_1)\Lambda(R)}\right)=o(1).
\tag{28}
\]

Combining (26)--(28) proves (4).

The distinction from `FD-044` is quantitative and real. There the generic `O_sigma(x^sigma)` summatory law gave a uniform settled window `|t|<=R^(1/2-eta)`. The Walfisz transfer permits

\[
R^{1/2}e^{c_1\Lambda(R)},
\tag{29}
\]

which crosses the square-root scale by an unbounded subexponential factor. Nothing here permits `R^(1/2+epsilon)` for any fixed positive `epsilon`.

## 5. Growing critical packets keep the same occupation law in the wider window

Let

\[
P(r)=\sum_{j=1}^m z_jr^{-i\gamma_j},
\qquad
\Omega:=\max_{j,k}|\gamma_j-\gamma_k|.
\tag{30}
\]

If

\[
\Omega\le
R^{1/2}e^{c_1\Lambda(R)},
\tag{31}
\]

then (4), exactly as in `FD-044`, yields

\[
\boxed{
\left|
\|P\|_{\rm ns,R,D}^2
-\delta_{\rm ns}\|P\|_{R,D}^2
\right|
\ll_D
m\bigl(1+\log^{2/3}(2+\Omega)\bigr)
\|z\|_2^2.
}
\tag{32}
\]

Since `Lambda(R)=o(log R)`, condition (31) still has

\[
\log(2+\Omega)=O(\log R).
\tag{33}
\]

Therefore, under the same natural critical conditioning

\[
\|P_R\|_{R,D}^2
\gg
(\log R)\|z_R\|_2^2,
\tag{34}
\]

every family satisfying

\[
m_R=o((\log R)^{1/3})
\tag{35}
\]

and (31) has

\[
\boxed{
\frac{\|P_R\|_{\rm ns,R,D}^2}
     {\|P_R\|_{R,D}^2}
\longrightarrow\delta_{\rm ns}.
}
\tag{36}
\]

Thus `FD-044`'s packet-dimension threshold is unchanged, but its finite-horizon frequency-width restriction was not sharp at the square-root boundary. Any physical escape based on a norm-accurate, naturally conditioned critical packet with dimension `o((log H)^(1/3))` must now push its effective frequency diameter beyond the window (31), or fail one of the other approximation/conditioning hypotheses already isolated there.

## 6. Adversarial checks, prior art, and research boundary

Three possible overclaims were tested explicitly. First, the improvement is not a power saving: the classical Walfisz theorem retains the `x^(1/2)` squarefree exponent, so this finding does not justify a fixed polynomial window beyond `R^(1/2)`. Second, the argument says nothing about whether the physical source actually admits a small-dimensional critical Mellin approximation; that source-specific approximation problem remains open. Third, near-colliding frequencies can still produce coefficient ill-conditioning, exactly as in `FD-043`--`FD-044`; no lower-gap-free theorem can remove that loss without additional structure.

The Euler factor calculation was checked locally: multiplying `(1-p^(-2z))` by `1-p^(-(z+2))/(1+p^(-z))` recovers (6) exactly. The convolution transfer uses absolute convergence of `B` on every half-plane `Re(z)>=sigma_0>0`, so the large-`d` range in (14) is genuinely negligible and no uniform Walfisz estimate in the divisor parameter is being assumed. The density constant is independently consistent because `B(1)/zeta(2)=A(1)=c_sf`, reproducing the constant already obtained in `FD-038` and `FD-044`.

A targeted prior-art audit located Walfisz's classical squarefree error as the standard zero-free-region improvement to `Q(x)=x/zeta(2)+O(sqrt(x))`, and modern squarefree literature continues to cite it in precisely that role. Standard Euler-product references also give `sum mu(n)^2 n^(-s)=zeta(s)/zeta(2s)`. No novelty is claimed for either fact. The Mathia-specific contribution is the factorization (8) of the weighted Jordan squarefree series, the transfer (20) to the centered nonsquarefree coefficient, and its consequence (3)--(4) for the finite Jordan packet window. Walfisz's book is added to `SOURCES.md` as the only new load-bearing literature dependency.

The finding is falsified if the Euler factor identity (7)--(9) fails, if `B` does not converge absolutely on every fixed half-plane `Re(z)>0`, if the Walfisz error cannot be transferred by (14)--(19), or if finite evaluation of the tail contradicts (27). It remains conditional only at the final physical-source step: neither positive occupation for the exact source nor an RH improvement is asserted.

The research frontier narrows accordingly. A critical spectral escape from nonsquarefree occupation is no longer explained merely by reaching the square-root frequency scale. In the small-dimensional, naturally conditioned packet regime it must cross a strictly wider Walfisz window, while the alternative escapes remain macroscopic nonpacket remainder or coefficient coherence. The next source-specific target is still to exploit the exact law `Delta Hcal(n)=mu(rad n)phi(rad n)/n` or the pole expansion of `zeta(s+1)/zeta(s)` to rule out one of those surviving mechanisms.
