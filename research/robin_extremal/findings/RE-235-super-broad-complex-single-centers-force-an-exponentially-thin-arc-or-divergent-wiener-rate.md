# RE-235 — Super-broad complex single centers force an exponentially thin arc or divergent Wiener rate

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + COMPLEX-CENTER-DRIFT + SUPER-BROAD-CORRIDOR + WIENER-COST + EXPONENTIALLY-THIN-ARC + REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-220, RE-229, RE-230, RE-234.

RE-234 closes the finite-ray large-center regime

\[
\frac{N_m}{m|a_m|}\to\tau\in(0,\infty)
\]

for complex single centers on a fixed symmetric arc: the effective radial load controls prediction while the full load controls Wiener cost, and every successful finite-ray family pays a normalized rate strictly above six. The remaining large-center direction explicitly left open there is the **super-broad** regime

\[
\frac{N_m}{m|a_m|}\to\infty,
\]

where the delay corridor grows much faster than the center modulus and the finite-ray asymptotics used in RE-234 no longer apply.

That regime has a simpler direct obstruction. For the exact normalized truncated negative-binomial predictor

\[
Q_{m,N,a}(z)
:=z^m a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac za\right)^k,
\qquad
F_{m,N,a}(z):=\frac{Q_{m,N,a}(z)}{Q_{m,N,a}(1)},
\tag{1}
\]

write

\[
a=\rho e^{i\varphi},
\qquad
\tau:=\frac{N}{m\rho}.
\tag{2}
\]

Let `0<alpha<pi/2`, assume full-arc contraction

\[
\max_{|\theta|\le\alpha}
\left|1-\frac{e^{-i\theta}}a\right|<1,
\tag{3}
\]

and suppose `Q(1) != 0`. If

\[
\rho\sin\alpha\ge1,
\qquad
\tau\ge2,
\tag{4}
\]

then the **exact normalized Wiener norm** obeys the nonasymptotic lower bound

\[
\boxed{
\|F_{m,N,a}\|_A
\ge
 e^{-2}
\left(\frac{\sin\alpha}{2}\right)^m
\tau^{m-1}
\left(1+\frac1\rho\right)^N.
}
\tag{5}
\]

Since

\[
\rho\log\left(1+\frac1\rho\right)\ge\log2
\qquad(\rho\ge1),
\tag{6}
\]

(5) yields

\[
\boxed{
\frac1m\log\|F_{m,N,a}\|_A
\ge
\tau\log2
+\left(1-\frac1m\right)\log\tau
+\log\frac{\sin\alpha}{2}
-\frac2m.
}
\tag{7}
\]

Therefore every super-broad sequence with

\[
\rho_m\to\infty,
\qquad
\tau_m=\frac{N_m}{m\rho_m}\to\infty,
\qquad
\inf_m\alpha_m>0
\tag{8}
\]

has

\[
\boxed{
\frac1m\log\|F_m\|_A\to\infty,
\qquad
\frac{\log\|F_m\|_A}{m\alpha_m}\to\infty.
}
\tag{9}
\]

More generally, whenever `rho_m sin(alpha_m)>=1`, bounded normalized Wiener rate can survive super-broad growth only if the observed arc becomes exponentially thin in `tau_m`. Indeed, if

\[
\frac{\log\|F_m\|_A}{m\alpha_m}\le C,
\tag{10}
\]

then (7) forces

\[
\boxed{
\sin\alpha_m
\le
2e^{2/m+C\alpha_m}
\tau_m^{-(1-1/m)}2^{-\tau_m}.
}
\tag{11}
\]

Thus the super-broad branch does not create a cheap fixed-arc escape. Outside the separate inverse-center layer `rho sin(alpha)<1`, a bounded-rate family must squeeze its arc on the scale `2^{-tau}` up to subexponential factors. This is much thinner than any algebraic shrinking in the super-broad load.

## 1. Contraction keeps the center phase inside the symmetric arc cone

The endpoint contraction inequalities in (3) are

\[
\left|1-\frac{e^{\mp i\alpha}}a\right|^2<1.
\tag{12}
\]

Using `a=rho e^{i phi}`, they become

\[
\cos(\varphi+\alpha)>\frac1{2\rho},
\qquad
\cos(\varphi-\alpha)>\frac1{2\rho}.
\tag{13}
\]

Choose the phase representative modulo `2pi` compatible with these two positive cosines. Because `0<2alpha<pi`, both endpoint angles lie in the same positive-cosine half-period, so

\[
|\varphi|<\frac\pi2-\alpha.
\tag{14}
\]

Consequently

\[
\boxed{
\cos\varphi\ge\sin\alpha.
}
\tag{15}
\]

Set

\[
q:=\left|1-\frac1a\right|.
\tag{16}
\]

Contraction at `theta=0` gives `q<1`. Also

\[
1-q
=
\frac{1-q^2}{1+q}
=
\frac{2\cos\varphi/\rho-1/\rho^2}{1+q}.
\tag{17}
\]

Under `rho sin(alpha)>=1`, equations (15)--(17) imply

\[
2\frac{\cos\varphi}{\rho}-\frac1{\rho^2}
\ge
\frac{\sin\alpha}{\rho},
\tag{18}
\]

and `1+q<=2`, hence

\[
\boxed{
1-q\ge\frac{\sin\alpha}{2\rho}.
}
\tag{19}
\]

This is the only place where the arc width enters the proof. It prevents a complex center from approaching the imaginary contraction boundary cheaply while the arc is still wider than the inverse-center scale.

## 2. The last `rho` negative-binomial levels recover the missing radial factor

Define

\[
S_{m,N}(s)
:=
\sum_{k=0}^{N}
\binom{m+k-1}{k}s^k.
\tag{20}
\]

RE-220 gives the exact phase-independent Wiener identity

\[
\|Q_{m,N,a}\|_A
=
\rho^{-m}
S_{m,N}\!\left(1+\frac1\rho\right).
\tag{21}
\]

At DC, the triangle inequality and the full negative-binomial series give

\[
\begin{aligned}
|Q_{m,N,a}(1)|
&\le
\rho^{-m}S_{m,N}(q)\\
&\le
\rho^{-m}(1-q)^{-m}.
\end{aligned}
\tag{22}
\]

Therefore

\[
\boxed{
\|F_{m,N,a}\|_A
\ge
(1-q)^m
S_{m,N}\!\left(1+\frac1\rho\right).
}
\tag{23}
\]

The super-broad gain comes from retaining not one terminal term of `S`, but an entire block of width comparable to `rho`. Put

\[
s:=1+\frac1\rho,
\qquad
w_k:=\binom{m+k-1}{k}s^k,
\qquad
L:=\lfloor\rho\rfloor.
\tag{24}
\]

For `1<=k<=N`,

\[
\frac{w_{k-1}}{w_k}
=
\frac{k}{(m+k-1)s}
=
\frac1{(1+(m-1)/k)(1+1/\rho)}.
\tag{25}
\]

Because `tau>=2`,

\[
N=m\rho\tau\ge2m\rho,
\tag{26}
\]

so every `k` in the terminal block `N-L<=k<=N` satisfies `k>=m rho`. Hence

\[
\frac{m-1}{k}\le\frac1\rho,
\tag{27}
\]

and (25) gives

\[
\frac{w_{k-1}}{w_k}
\ge
\left(1+\frac1\rho\right)^{-2}.
\tag{28}
\]

After at most `L<=rho` backward steps,

\[
w_{N-j}
\ge
\left(1+\frac1\rho\right)^{-2\rho}w_N
\ge e^{-2}w_N
\qquad(0\le j\le L).
\tag{29}
\]

There are `L+1>rho` such terms. Therefore

\[
\boxed{
S_{m,N}(s)
\ge
e^{-2}\rho
\binom{m+N-1}{N}s^N.
}
\tag{30}
\]

The factor `rho` in (30) is load-bearing. A one-term lower bound leaves one uncancelled radial factor when `rho` is allowed to grow arbitrarily fast with `m`; summing the final `Theta(rho)` levels restores exactly the factor needed for a growth statement uniform in the center speed.

## 3. Radial factors cancel, leaving only the super-broad load

The terminal binomial coefficient has the elementary lower bound

\[
\begin{aligned}
\binom{m+N-1}{N}
&=
\prod_{j=1}^{m-1}\frac{N+j}{j}\\
&\ge
\frac{N^{m-1}}{(m-1)!}\\
&\ge
\left(\frac Nm\right)^{m-1}.
\end{aligned}
\tag{31}
\]

Insert (19), (30), and (31) into (23). Since

\[
\frac Nm=\rho\tau,
\tag{32}
\]

the powers of `rho` cancel exactly:

\[
\begin{aligned}
\|F\|_A
&\ge
 e^{-2}\rho
\left(\frac{\sin\alpha}{2\rho}\right)^m
(\rho\tau)^{m-1}
\left(1+\frac1\rho\right)^N\\
&=
 e^{-2}
\left(\frac{\sin\alpha}{2}\right)^m
\tau^{m-1}
\left(1+\frac1\rho\right)^N.
\end{aligned}
\tag{33}
\]

This is (5). Taking logarithms and using

\[
\frac Nm\log\left(1+\frac1\rho\right)
=
\rho\tau\log\left(1+\frac1\rho\right)
\ge\tau\log2
\tag{34}
\]

proves (7).

For a fixed positive arc, the negative term `log(sin(alpha)/2)` is constant while the first term in (7) grows linearly in `tau`. Hence (9) follows immediately. Notice that the proof does not use the prediction error at all. Once contraction and exact DC normalization are imposed, the coefficient geometry itself makes the super-broad fixed-arc limit prohibitively expensive.

Equation (11) is just the contrapositive quantitative form. If the normalized rate in (10) stays bounded, insert that upper bound into (7) and solve for `sin(alpha)`. Thus, as long as the arc remains outside the inverse-center layer `rho sin(alpha)<1`, super-broad load can survive only by forcing an exponentially thin arc.

## 4. What this closes, and what it deliberately leaves open

Together, RE-230, RE-234, and the present result classify the main fixed-arc unbounded-center scalings of this single-center representation. RE-230 excludes the subcritical microscopic load `N/(m|a-1|)->0`; RE-234 prices every finite positive ray `N/(m|a|)->tau in (0,infty)` above six; and (9) shows that the super-broad load `N/(m|a|)->infty` has **divergent** Wiener rate on every fixed positive arc.

This does not turn into a universal theorem about all separated predictors. It is still an obstruction for the truncated negative-binomial single-center architecture, and the global interval remains

\[
\boxed{
1\le C_{\rm sep}\le5.996390.
}
\tag{35}
\]

Nor does (5) close every scale-dependent arc. Two singular layers remain outside its clean fixed-arc conclusion. First, if `rho sin(alpha)<1`, the center is close enough to the imaginary contraction boundary that (19) loses a uniform radial margin. Second, even when `rho sin(alpha)>=1`, equation (11) permits in principle an arc exponentially small in `tau`. Those are now explicit boundary layers rather than an undifferentiated `tau->infinity` escape.

The theorem also assumes contraction. A different single-center representation that is meaningful without the negative-binomial convergence geometry is not covered. Multi-center/minimax predictors, rational predictors, and other polynomial bases remain untouched and are exactly the routes that can change the global approximation geometry rather than push another parameter of the same center to a boundary.

A useful negative control is that no prediction hypothesis appears in (5). The estimate therefore cannot be falsified by constructing a clever exact-remainder cancellation inside the same contracting super-broad parameter set: any such cancellation still has to pay the normalized Wiener norm in (5). The only possible escape is to leave one of the hypotheses that produced the bound, most notably the arc/radial-margin condition or the one-center representation itself.

## 5. Prior-art and falsification audit

The coefficient array in (20) is the standard negative-binomial array, and its normalized partial sums are classically expressible through the regularized incomplete beta function. DLMF §8.18 records large-parameter incomplete-beta asymptotics, while the causal-prediction and superoscillation literature already audited in RE-217 and RE-223 supplies the broad approximation-theory context. A fresh search did not reveal a directly matching theorem for the normalized Wiener cost of this super-broad complex-center truncation.

No external asymptotic theorem is load-bearing here. Equations (12)--(34) use only endpoint contraction, the exact coefficient identity already established in RE-220, the negative-binomial generating function, and elementary finite-product bounds. Accordingly `SOURCES.md` needs no update.

The most sensitive step is the terminal-block estimate (30). Its purpose is not cosmetic: without summing `Theta(rho)` adjacent terms, a crude single-term proof leaves a factor depending on how quickly `rho` grows relative to `m` and would not justify a uniform super-broad conclusion. Equations (25)--(29) explicitly remove that loophole.

The phase geometry is also essential. If the arc shrinks below inverse-center scale, contraction no longer supplies the lower bound (19); the exact DC normalizer may then be much larger than the present estimate prices. The finding therefore does **not** infer anything about that layer by continuity. It records the layer as the next falsifiable boundary if one insists on continuing the one-center program.

## Research consequence

The super-broad corridor is not a cheap alternative to the finite-ray six-plus branch. On any fixed symmetric arc its Wiener rate diverges, and on every arc wider than inverse-center scale a bounded-rate family would have to shrink the arc essentially like `2^{-tau}/tau` or faster.

This removes the last ordinary fixed-arc large-center escape of the complex single-center negative-binomial predictor. Further work on the same architecture is now confined to a very singular coupled limit in which the arc collapses at least as fast as the inverse center or exponentially in the super-broad load. For improving the live bound `C_sep<=5.996390`, changing geometry — multi-center/minimax, rational, or another predictor class — remains the higher-value direction.