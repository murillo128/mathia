# XF-117 — PNT window dilution forces multiscale packet entropy

**Status:** `EXACT-DERIVED` + `SOURCE-SPECIFIC` + `MULTISCALE-PACKET-ENTROPY` + `ROBUST-NON-PLANE-WAVE-GATE`. XF-116 proves uniform absolute continuity of the mass-preserving Xi Toeplitz source in every physical lag window and uses it to exclude a bounded number of shrinking coefficient packets. That conclusion extends quantitatively to **every** packet scale: a nonpositive q-scale witness must have growing block `ell_{2,1}` complexity, and it cannot even be approximated in `ell_2` by a packet union whose source-window budget is small.

Keep the XF-108--XF-116 normalization

\[
N=2q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
a:=N\Delta\asymp q^{1/2},
\qquad
L=\log a+c,
\qquad
K=\left\lfloor\frac L\Delta\right\rfloor,
\tag{1}
\]

and the Hermitian Toeplitz section

\[
\widehat T_K=(\widehat\mu_{i-j})_{0\le i,j\le K},
\qquad
\widehat\mu_0=1.
\tag{2}
\]

Write

\[
\mathfrak W_a(h)
:=
\sup_{0\le u\le L}
\sum_{\substack{1\le m\le K\\m\Delta\in[u,u+h]}}
|\widehat\mu_m|
\tag{3}
\]

and, with the constant `c_0>0` from XF-116,

\[
\varepsilon_a
:=
\Delta+a^{-1/2}
+e^{-c_0\sqrt{\log a}}
+\frac{\log a}{a}.
\tag{4}
\]

Then XF-116 gives uniformly for `0<h<=1`

\[
\mathfrak W_a(h+O(\Delta))
\ll_{\psi,c} h+\varepsilon_a.
\tag{5}
\]

Partition the coefficient indices into consecutive physical `h`-cells

\[
I_r(h)
:=
\{j\in\{0,\ldots,K\}: rh\le j\Delta<(r+1)h\},
\tag{6}
\]

and for a unit vector `v` put

\[
b_r(h):=\|v_{I_r(h)}\|_2,
\qquad
\mathcal P_h(v)
:=
\left(\sum_r b_r(h)\right)^2.
\tag{7}
\]

Because `sum_r b_r(h)^2=1`, `mathcal P_h` is the Renyi-`1/2` effective packet count of the block masses `b_r(h)^2`. The new quantitative gate is

\[
\boxed{
 v^*\widehat T_Kv\le0
 \quad\Longrightarrow\quad
 \mathcal P_h(v)
 \gg_{\psi,c}
 \frac1{h+\varepsilon_a},
 \qquad 0<h\le1.
}
\tag{8}
\]

In particular, on every mesoscopic scale `epsilon_a << h_a <= 1`,

\[
\boxed{
\mathcal P_{h_a}(v)\gg \frac1{h_a}.
}
\tag{9}
\]

At the PNT resolution `h_a=epsilon_a`, this already forces

\[
\mathcal P_{\varepsilon_a}(v)
\gg
\varepsilon_a^{-1}
\ge
\exp\!\bigl(c_1\sqrt{\log a}\bigr)
\tag{10}
\]

for some smaller `c_1>0` and all large `a`. Thus the escape left by XF-116 is not merely “the number of packets must grow”: the coefficient mass must acquire a quantitatively one-dimensional packet entropy simultaneously across all physical scales down to the ordinary-PNT error scale.

## 1. Every pair of physical cells has small block operator norm

Let

\[
E_a:=\widehat T_K-I.
\tag{11}
\]

For two cells `I_r(h)` and `I_s(h)`, fix a row index `i` in the first cell. As `j` ranges through the second, the signed lags `(i-j)Delta` lie in one interval of physical width at most `h+O(Delta)`. When `r=s`, removing the diagonal leaves at most one positive and one negative such interval. Hence XF-116 gives both the row and column bounds

\[
\max_i\sum_j |(E_a)_{ij}|
\le
2\mathfrak W_a(h+O(\Delta)),
\qquad
\max_j\sum_i |(E_a)_{ij}|
\le
2\mathfrak W_a(h+O(\Delta))
\tag{12}
\]

for every block `P_r E_a P_s`. The Schur test therefore yields

\[
\boxed{
\|P_rE_aP_s\|_{\rm op}
\le
2\mathfrak W_a(h+O(\Delta))
}
\tag{13}
\]

uniformly in `r,s`, including blocks separated by the full q-scale distance `L`.

Decomposing `v=sum_r v_r`, `v_r=P_rv`, equations `(13)` and `(7)` give

\[
\begin{aligned}
|v^*E_av|
&\le
\sum_{r,s}
\|P_rE_aP_s\|_{\rm op}
\|v_r\|_2\|v_s\|_2\\
&\le
2\mathfrak W_a(h+O(\Delta))
\left(\sum_r b_r(h)\right)^2.
\end{aligned}
\tag{14}
\]

If `v^*T_hat_K v<=0`, then `v^*E_av<=-1`. Substituting `(5)` into `(14)` proves `(8)`.

This is strictly stronger than the support-cover statement of XF-116. A vector may touch very many cells with arbitrarily tiny coefficients; `(8)` measures the actual block `ell_2` masses rather than only the set of nonzero coordinates.

## 2. Low packet complexity is excluded robustly, not only for exact support

The source also has a uniform global `ell^1` bound. Indeed, mass preservation of the deposition and Chebyshev give

\[
\frac1{2a}
\sum_{\lambda_n\le L+O(\Delta)}
\frac{\Lambda(n)}{\sqrt n}
=O_c(1),
\tag{15}
\]

while the exponential archimedean contribution has total mass `O_c(1)` and the singular correction in `B(xi)-e^xi` contributes only `O(log a/a)`. Therefore

\[
\sum_{m=1}^K|\widehat\mu_m|=O_{\psi,c}(1),
\qquad
\boxed{\|\widehat T_K\|_{\rm op}\le M_{\psi,c}}
\tag{16}
\]

with `M_{psi,c}` independent of `a`.

This makes the packet exclusion stable under an `ell_2` tail. Let `S` be any union of `p` physical `h`-cells and write

\[
x=P_Sv,
\qquad
y=v-x,
\qquad
\eta=\|y\|_2^2.
\tag{17}
\]

The principal-section estimate of XF-116 gives

\[
x^*\widehat T_Kx
\ge
\left(1-2p\mathfrak W_a(h+O(\Delta))\right)\|x\|_2^2.
\tag{18}
\]

If

\[
p(h+\varepsilon_a)\le c_*
\tag{19}
\]

for a sufficiently small constant `c_*=c_*(psi,c)>0`, then `(5)` makes the coefficient in `(18)` at least `3/4`. Combining `(16)`--`(18)` gives

\[
v^*\widehat T_Kv
\ge
\frac34(1-\eta)
-2M_{\psi,c}\sqrt{\eta(1-\eta)}
-M_{\psi,c}\eta.
\tag{20}
\]

The right-hand side is positive for all sufficiently small fixed `eta`, uniformly in `a,p,h,S`. Consequently there is `eta_*=eta_*(psi,c)>0` such that

\[
\boxed{
 v^*\widehat T_Kv\le0,
 \quad p(h+\varepsilon_a)\le c_*
 \quad\Longrightarrow\quad
 \|v_{S^c}\|_2^2\ge\eta_*.
}
\tag{21}
\]

So a nonpositive witness cannot be **approximately** finitely packetized either. At every scale where `p(h+epsilon_a)` is small, a fixed fraction of its coefficient energy must remain outside every such `p`-packet approximation.

## 3. The remaining witness has positive mesoscopic thickness

Let `N_h(S)` denote the least number of physical `h`-cells needed to cover the support of a nonpositive witness. Since `mathcal P_h(v)<=N_h(supp v)`, `(8)` implies

\[
\boxed{
N_h(\operatorname{supp}v)
\gg
\frac1{h+\varepsilon_a}.
}
\tag{22}
\]

For every scale `h>=epsilon_a`,

\[
N_h(\operatorname{supp}v)\,h\gg1.
\tag{23}
\]

Thus the support cannot have vanishing one-dimensional covering content throughout the mesoscopic range. This does **not** say that it occupies a positive fraction of the entire physical interval `[0,L]`, whose length is `log a+O(1)`. Combined with the q-scale span requirement of XF-107, the surviving geometry may still be globally dilute: it must span order `log a`, while carrying at least constant fine-scale physical thickness inside that span.

The robust statement `(21)` is stronger than `(23)`: sprinkling negligible coefficients into many cells cannot fake the conclusion. Whenever the witness is well approximated by a small packet union, the approximation itself is positive and the uniform source norm prevents a vanishing tail from reversing its sign.

## 4. Stress test: the `1/h` packet law is sharp for the XF-116 abstract corner control

The terminal-band control of XF-116 shows that the exponent in `(9)` cannot be improved from window absolute continuity alone. Recall its fixed physical width `h_*>0`,

\[
R\sim\frac{h_*}{\Delta},
\qquad
\nu_m=-\frac5R\cos\frac{\pi m}{2}
\quad(K-R+1\le m\le K),
\tag{24}
\]

with the negative witness supported on the first and last `R` coordinates and of constant modulus there. For `Delta<<h<<h_*`, every physical `h`-cell meeting those edge blocks carries block mass

\[
b_r(h)^2\asymp \frac{h}{h_*},
\tag{25}
\]

and the number of occupied cells is `asymp h_*/h`. Hence

\[
\boxed{
\mathcal P_h(v)\asymp\frac{h_*}{h}.
}
\tag{26}
\]

At the same time, a lag window of width `h` contains `O(h/Delta)` terminal coefficients, each of size `O(Delta/h_*)`, so

\[
\mathfrak W_\nu(h)=O(h/h_*).
\tag{27}
\]

Thus `mathfrak W_nu(h) mathcal P_h(v)=Theta(1)` at the scaling level. The block-Schur mechanism of `(14)` is therefore sharp for the abstract class controlled only by local absolute lag mass. Any stronger Xi conclusion has to use **signed arithmetic correlation between different lag windows**, not merely a better repackaging of `(5)`.

## 5. Prior-art boundary and live frontier

Block Schur estimates, Gershgorin localization, and finite-section Toeplitz analysis are classical. A directed prior-art check again found the standard Böttcher--Silbermann finite-section literature and neighboring block-Toeplitz norm theory; no novelty is claimed for those operator-theoretic tools or for Renyi packet entropy as a generic notion. The line-specific content is the insertion of the actual mass-preserving Guinand--Weil/Vieta source estimate from XF-116 into the block decomposition, producing the q-dependent multiscale bounds `(8)` and `(21)`. No new external theorem is load-bearing, so `SOURCES.md` needs no update.

The source-side frontier is now more rigid. A hypothetical nonpositive q-scale witness must simultaneously evade the full-circle Fejer positivity of XF-115, the broad-support and long-span gates of XF-107/XF-111, and the present **multiscale mass-delocalization** law. The natural next attack is no longer another absolute-value localization estimate. It is a matrix-valued estimate for the signed PNT discrepancy across many separated lag windows, strong enough to exploit cancellation between the `Omega(1/h)` packets that `(8)` now forces.