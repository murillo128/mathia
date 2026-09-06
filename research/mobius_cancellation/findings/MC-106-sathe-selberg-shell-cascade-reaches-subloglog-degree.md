# MC-106 — Sathe–Selberg uniformity pushes the positive Hamming-shell cascade through every sub-log-logarithmic degree

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let the source-forced Hamming deformation and radial shell sums from `MC-092`, `MC-095`, and `MC-105` be

\[
\mathcal Q_N(t)=\sum_{k=0}^{D_N}(-t)^k C_{k,N},
\qquad
C_{k,N}=\sum_{\substack{a\ \mathrm{squarefree}\\\omega(a)=k}}W_N(a),
\tag{1}
\]

with the exact pair representation

\[
\mathcal Q_N(t)
=\sum_{m,n\le N}\mu(m)^2\mu(n)^2(-t)^{d_\triangle(m,n)}
 z\!\left(\frac{N^2}{mn}\right),
\qquad
z(x)=\lfloor x\rfloor+\frac12-x.
\tag{2}
\]

Write

\[
L_N:=\log\log N,
\qquad
c_2=\frac{15}{\pi^2}\left(\gamma+\gamma_1-\frac12\right)>0.
\tag{3}
\]

`MC-105` proved, for every **fixed** `k>=2`,

\[
C_{k,N}
\sim
c_2\frac{N^2}{(\log N)^2}
\frac{(2L_N)^{k-2}}{(k-2)!}.
\tag{4}
\]

The fixed-degree restriction can be removed throughout the entire sub-log-logarithmic regime. If `K_N` is any integer sequence satisfying

\[
2\le K_N=o(L_N),
\tag{5}
\]

then, uniformly for `2<=k<=K_N`,

\[
\boxed{
C_{k,N}
=
\left(1+o(1)\right)
 c_2\frac{N^2}{(\log N)^2}
\frac{(2L_N)^{k-2}}{(k-2)!}.
}
\tag{6}
\]

In particular all such shells are eventually positive, and uniformly for `2<=k<K_N`,

\[
\boxed{
\frac{C_{k+1,N}}{C_{k,N}}
=
\left(1+o(1)\right)\frac{2L_N}{k-1}.
}
\tag{7}
\]

Therefore, if additionally `K_N -> infinity`, then

\[
\min_{2\le k<K_N}\frac{C_{k+1,N}}{C_{k,N}}
\longrightarrow\infty,
\tag{8}
\]

and the signed radial partial sum through the moving cutoff is still dominated by its last retained shell:

\[
\boxed{
\sum_{k=2}^{K_N}(-1)^k C_{k,N}
\sim
(-1)^{K_N}C_{K_N,N}.
}
\tag{9}
\]

The hard endpoint remains much smaller. The Korobov–Vinogradov input already used in `MC-098` and `MC-105` gives

\[
\mathcal Q_N(1)=O_A\!\left(\frac{N^2}{(\log N)^A}\right)
\quad\text{for every fixed }A>0,
\tag{10}
\]

while `C_{0,N}=O(N)` and `C_{1,N}=O(N\log\log N)`. Since the factor in `(6)` is at least one for `2<=K_N=o(L_N)` and large `N`, one has `C_{K_N,N}\gg N^2/(\log N)^2`. Hence

\[
\boxed{
\sum_{k>K_N}(-1)^k C_{k,N}
\sim
-(-1)^{K_N}C_{K_N,N}
}
\tag{11}
\]

for every `K_N -> infinity` with `K_N=o(log log N)`.

Thus `MC-105`'s growing-degree obstruction is quantitatively stronger: the endpoint cancellation cannot be captured by **any radial truncation whose Hamming degree is `o(log log N)`**. Any source-specific radial mechanism explaining the endpoint must reach at least the first `Theta(log log N)` scale, or else use a non-radial relation that bypasses shell truncation entirely.

The result does **not** identify the transition inside the `Theta(log log N)` regime, does not assert a Poisson law for the signed source coefficients there, and gives no improved bound for `M(x)`.

## 1. Exact pair coordinates reduce the shell problem to almost-prime counting

As in `MC-105`, write every square-free pair in `(2)` uniquely as

\[
b=(m,n),\qquad m=bd,\qquad n=be,
\tag{12}
\]

where `b,d,e` are pairwise coprime and square-free. Then

\[
d_\triangle(m,n)=\omega(d)+\omega(e),
\tag{13}
\]

and, with `x=N/b`,

\[
z\!\left(\frac{N^2}{mn}\right)
=z\!\left(\frac{x^2}{de}\right).
\tag{14}
\]

Hence

\[
C_{k,N}
=
\sum_{\substack{b\le N\\b\ \mathrm{squarefree}}}
\sum_{j=0}^{k}
\sum_{\substack{d,e\le N/b\\d,e\ \mathrm{squarefree}\\(d,e)=1\\(de,b)=1\\\omega(d)=j\\\omega(e)=k-j}}
 z\!\left(\frac{(N/b)^2}{de}\right).
\tag{15}
\]

The new issue relative to `MC-105` is only uniformity when `k` grows. The source kernel is still bounded by `1/2`, the common-factor weight is still summable at scale `b^{-2}`, and the Hamming degree is still exactly the sum of the two distinct-prime counts.

## 2. Sathe–Selberg gives the Landau density uniformly when the degree is `o(log log x)`

Let

\[
A_r^{\mathrm{sf}}(x)
:=
\#\{n\le x:n\text{ square-free},\ \omega(n)=r\}.
\tag{16}
\]

The classical Sathe–Selberg theorem gives a uniform local law for `omega(n)` when `r` is bounded by a fixed multiple of `log log x`. A convenient modern statement is Theorem 16.2 of Dimitris Koukoulopoulos, *The Distribution of Prime Numbers*, Graduate Studies in Mathematics 203, AMS (2019): for `1<=r<=C log log x`, the count of integers with `omega(n)=r` equals the Landau factor

\[
\frac{x}{\log x}\frac{(\log\log x)^{r-1}}{(r-1)!}
\tag{17}
\]

times an analytic Sathe–Selberg correction evaluated at

\[
\alpha=\frac{r-1}{\log\log x},
\tag{18}
\]

with relative error `O_C(r/(log log x)^2)`. The correction equals one at `alpha=0`. The book gives the saddle-point proof and cites Sathe's original 1953 work and Selberg's 1954 note.

The same saddle-point argument applies to the square-free generating series

\[
F_{\mathrm{sf}}(s,w)
:=
\sum_{n\ge1}\frac{\mu(n)^2w^{\omega(n)}}{n^s}
=
\prod_p(1+w p^{-s})
=
\zeta(s)^w H_{\mathrm{sf}}(s,w),
\tag{19}
\]

where

\[
H_{\mathrm{sf}}(s,w)
=
\prod_p(1+w p^{-s})(1-p^{-s})^w
\tag{20}
\]

is analytic in `s` in a fixed half-plane to the left of `1` for `w` in a fixed compact set. Its local factors have no `p^{-s}` term after the zeta factor is removed, so the Euler product is normally convergent there. Moreover

\[
H_{\mathrm{sf}}(1,w)=1+O(w)
\qquad(w\to0).
\tag{21}
\]

Thus, whenever `R_x=o(log log x)`, the square-free Sathe–Selberg formula reduces uniformly to the Landau form

\[
\boxed{
A_r^{\mathrm{sf}}(x)
=
\left(1+o(1)\right)
\frac{x}{\log x}
\frac{(\log\log x)^{r-1}}{(r-1)!}
}
\tag{22}
\]

for `1<=r<=R_x`. This is exactly the fixed-`r` input of `MC-105`, now with enough uniformity for a moving sub-log-logarithmic degree.

A useful equivalent way to see why the square-free restriction costs no main term in this regime is that repeated prime factors contribute one fewer freely chosen distinct prime. At saddle parameter `alpha=r/log log x=o(1)`, their Euler-factor correction is `1+O(alpha)`, so they disappear from the leading Landau density.

## 3. The scaled exact-degree measures remain uniformly Lebesgue

For `1<=r<=R_x=o(log log x)`, define the normalized measure

\[
\nu_{r,x}
:=
\frac{(r-1)!\log x}{x(\log\log x)^{r-1}}
\sum_{\substack{n\le x\\n\ \mathrm{squarefree}\\\omega(n)=r}}
\delta_{n/x}.
\tag{23}
\]

Fix `0<\delta<1`. Applying `(22)` at `ux` and at `x`, uniformly for `u\in[\delta,1]`, gives

\[
\nu_{r,x}([0,u])=u+o(1)
\tag{24}
\]

uniformly for `r<=R_x`: replacing `x` by `ux` changes `log log x` by only `O_\delta(1/log x)`, and multiplying that relative change by `r=o(log log x)` still gives `o(1)`. The same estimate at `u=\delta` shows that the normalized mass in `[0,\delta]` is `\delta+o(1)`.

Consequently the family `nu_{r,x}` converges uniformly, throughout `r=o(log log x)`, to Lebesgue measure on `[0,1]` in the sense needed for bounded Riemann-integrable kernels.

Apply this to

\[
f(u,v)=z\!\left(\frac1{uv}\right).
\tag{25}
\]

On `[\delta,1]^2`, this bounded kernel has only finitely many discontinuity hyperbolas `uv=1/q`; each has zero Lebesgue area. The axes contribute at most `O(\delta)` after normalization, uniformly in the allowed degrees. Letting first `x->infinity` and then `\delta->0` yields, uniformly for `j,l>=1` with `j+l<=R_x`,

\[
\boxed{
\sum_{\substack{d,e\le x\\d,e\ \mathrm{squarefree}\\\omega(d)=j\\\omega(e)=l}}
 z\!\left(\frac{x^2}{de}\right)
=
\left(J+o(1)\right)
\frac{x^2(\log\log x)^{j+l-2}}
{(j-1)!(l-1)!(\log x)^2},
}
\tag{26}
\]

where the same source-kernel constant from `MC-097` appears:

\[
J=\int_0^1\!\int_0^1 z\!\left(\frac1{uv}\right)du\,dv
=\gamma+\gamma_1-\frac12>0.
\tag{27}
\]

No independence model is being introduced: `(26)` is a deterministic scaling consequence of Sathe–Selberg and the exact bounded source kernel.

## 4. Coprimality defects are uniformly negligible below the log-log scale

Equation `(15)` additionally requires `(d,e)=1` and `(de,b)=1`. These restrictions do not alter `(26)` at leading order when `j+l=o(log log x)`.

Indeed, forcing a fixed prime `p` into a square-free `j`-factor integer removes one freely varying prime. From `(22)`, uniformly in the present range, the normalized cost is

\[
O\!\left(\frac{j}{p\log\log x}\right).
\tag{28}
\]

Therefore the relative mass of pairs sharing at least one prime is bounded by

\[
\sum_p
O\!\left(
\frac{jl}{p^2(\log\log x)^2}
\right)
=
O\!\left(
\frac{(j+l)^2}{(\log\log x)^2}
\right)
=o(1),
\tag{29}
\]

because `sum_p p^{-2}<infinity`. For fixed square-free `b`, excluding its prime divisors changes the pair mass by

\[
O_b\!\left(\frac{j+l}{\log\log x}\right)=o(1).
\tag{30}
\]

Thus `(26)` remains valid, with the same `J`, under the pairwise-coprime restrictions in `(15)`, uniformly for total degree `o(log log x)`.

The edge splits `j=0` or `j=k` are negligible. They contain only one freely varying almost-prime coordinate and have total size `N^{1+o(1)}` after the `b`-sum, whereas the two-coordinate main scale below is at least `N^2/(log N)^2`.

## 5. The common-factor sum and the degree splits preserve uniformity

Fix first a large constant `B`. For every square-free `b<=B`, put `x=N/b`. Then `log log x=L_N+o(1)`, so `(26)`--`(30)` apply uniformly for all `j+l=k<=K_N`. Summing the degree splits gives the exact binomial identity

\[
\sum_{j=1}^{k-1}
\frac1{(j-1)!(k-j-1)!}
=
\frac{2^{k-2}}{(k-2)!}.
\tag{31}
\]

Therefore the contribution of `b<=B` is

\[
\left(J+o(1)\right)
\frac{N^2L_N^{k-2}}{(\log N)^2}
\frac{2^{k-2}}{(k-2)!}
\sum_{\substack{b<=B\\b\ \mathrm{squarefree}}}\frac1{b^2},
\tag{32}
\]

uniformly for `2<=k<=K_N`.

The truncation in `b` can then be removed uniformly. For `b<=sqrt(N)`, the Sathe–Selberg upper bound and `|z|<=1/2` bound the normalized total contribution by `O(b^{-2})`; hence the tail `b>B` is `O(sum_{b>B}b^{-2})`. For `b>sqrt(N)`, the crude pair count contributes `O(N^{3/2})`, which is negligible against `N^2/(log N)^2`, and the shell factor in `(6)` is at least one in the regime `k=o(L_N)`.

Finally

\[
\sum_{b\ \mathrm{squarefree}}\frac1{b^2}
=\prod_p(1+p^{-2})
=\frac{15}{\pi^2}.
\tag{33}
\]

Combining `(27)`, `(31)`--`(33)` proves `(6)` with `c_2=15J/pi^2`.

## 6. A moving sub-log-log cutoff is still swallowed by the next shell

Dividing `(6)` at consecutive degrees gives `(7)` uniformly. Since `K_N=o(L_N)`,

\[
\frac{2L_N}{K_N-1}\longrightarrow\infty.
\tag{34}
\]

Hence every lower shell is smaller than the next by a factor tending uniformly to infinity, and

\[
\sum_{k=2}^{K_N-1}C_{k,N}=o(C_{K_N,N}).
\tag{35}
\]

All these shells are positive, so `(35)` immediately proves `(9)`.

For `K_N=o(L_N)`, eventually `K_N-2<=L_N`, and therefore

\[
\frac{(2L_N)^{K_N-2}}{(K_N-2)!}\ge1.
\tag{36}
\]

Thus `(6)` implies `C_{K_N,N}\gg N^2/(log N)^2`. Equations `(10)` and the lower-degree bounds then make the hard endpoint `o(C_{K_N,N})`. Subtracting the partial sum `(9)` from the exact endpoint identity proves `(11)`.

This is a genuine moving-cutoff statement, not an interchange of a fixed-`k` asymptotic with an unbounded sum.

## 7. Prior art and novelty boundary

The uniform exact-`omega` law is classical Sathe–Selberg theory. The principal modern reference used here is Dimitris Koukoulopoulos, *The Distribution of Prime Numbers*, Graduate Studies in Mathematics 203, American Mathematical Society, 2019, Theorem 16.2 and its saddle-point proof. The author-approved preliminary version is publicly available at `https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf`. It states uniformity for `1<=k<=C log log x`, gives the analytic correction at `alpha=(k-1)/log log x`, and records the original sources L. G. Sathe, *On a problem of Hardy on the distribution of integers having a given number of prime factors. II*, J. Indian Math. Soc. (N.S.) 17 (1953), 83--141, and A. Selberg, *Note on a paper by L. G. Sathe*, J. Indian Math. Soc. (N.S.) 18 (1954), 83--87.

The square-free specialization `(19)`--`(22)` is the same classical Selberg–Delange/saddle-point mechanism with the Euler product `prod_p(1+w/p^s)`; no new almost-prime distribution theorem is claimed. The deterministic kernel constant `J`, the common-factor Euler mass, and the exact Hamming decomposition are inherited from `MC-097` and `MC-105`.

A targeted literature search around Sathe–Selberg weighted almost-prime sums, sawtooth kernels, Möbius Hamming shells, symmetric-difference prime-factor distance, and moving exact-degree truncations found no basis for identifying `(6)`--`(11)` with a standard named theorem. **No novelty claim is made.** The durable line-specific content is the uniform transfer of classical Sathe–Selberg density through the already-derived source kernel, upgrading the fixed-degree obstruction of `MC-105` to every moving `o(log log N)` cutoff.

## 8. Boundaries and falsification tests

- The theorem stops deliberately at `k=o(log log N)`. When `k` is a positive proportion of `log log N`, the Sathe–Selberg correction is no longer `1+o(1)` and the simple coefficient in `(6)` must be replaced by a nontrivial saddle-point profile.
- Nothing here proves that `C_{k,N}` remains positive for `k~c log log N`. The bounded sawtooth kernel and the exact coprimality corrections must be carried through the full Sathe–Selberg profile before any such claim is made.
- Equation `(11)` locates a **lower bound on the degree scale needed for radial cancellation**. It does not identify which `Theta(log log N)` shells cancel, whether the cancellation is concentrated or diffuse, or whether a useful recurrence exists there.
- The result remains radial. A non-radial source statistic retaining within-shell phase or relational information can evade it without coupling `Theta(log log N)` radial degrees.
- The square-free saddle-point reduction must retain uniformity under the bounded kernel and coprimality restrictions. Equations `(23)`--`(33)` give the needed route; an adversarial audit should attack precisely the uniform tail removal and the `O((j+l)^2/L_N^2)` common-prime estimate rather than extrapolate the theorem beyond `(5)`.
- The endpoint estimate in `(10)` is only used to show that the known endpoint is negligible relative to the positive sub-log-log shells. No zero-free region stronger than the existing unconditional input is imported.
- No estimate for `M(N)` or `M(N^2)` follows from `(6)`--`(11)`.

The decisive continuation is now the **full saddle-point shell profile at `k=alpha log log N`**. A useful next theorem would carry the actual signed sawtooth/product-fiber kernel, square-free restriction, and coprimality conditions through fixed `alpha>0`, then determine whether the resulting profile changes sign or admits a source-forced cross-degree relation. Replacing the source coefficients by an unsigned Poisson model would not answer that question.

## Consequence for the research line

`MC-105` showed that endpoint cancellation escapes every fixed finite Hamming jet. This finding moves the boundary parametrically: it escapes every radial jet of depth `o(log log N)`. The first regime not classified by the positive Landau cascade is therefore the genuine Sathe–Selberg saddle scale `k=Theta(log log N)`.

That materially narrows the surviving source-specific signed-relation route. A fixed-order recurrence, a slowly growing recurrence of order `o(log log N)`, or a radial statistic inspecting only sub-log-log degrees cannot contain the endpoint cancellation. The next meaningful radial question is no longer whether the degree must grow; it is whether the full `alpha log log N` shell profile contains a sign transition or deterministic coupling strong enough to transport cancellation before absolute values erase it.