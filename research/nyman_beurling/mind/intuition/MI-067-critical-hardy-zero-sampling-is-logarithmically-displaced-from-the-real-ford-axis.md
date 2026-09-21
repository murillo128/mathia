# MI-067 — Critical Hardy zero sampling is logarithmically displaced from the real Ford axis

**Evidence level:** exact destination-aware synthesis from [NB-259](../../findings/NB-259-critical-depth-tilt-defeats-real-axis-ford-cell-coercivity-at-bounded-hilbert-cost.md), correcting the direct-transfer route left open by NB-258. The statement concerns the resolved scalar carrier and the exact zero-evaluation geometry; it does not identify the full Nyman distance.

NB-258 proves a positive source-energy floor on every fixed **real** Ford interval when the shell-Hilbert cost is bounded and `K<=J^(1-delta)`. The legal critical-zero evaluation is not on that axis. After Euler normalization, a zero at critical depth is sampled at imaginary Ford height

`A_J = log J / Y = Theta(log J)`.

That vertical displacement changes the interpolation cost. On the same `H`-resolved dictionary, imposing `C_J(0)=1` and `C_J(iA_J)=0` has sharp minimum coefficient cost

`||c||_2 ~ J/(A_J K^(3/2))`.

Hence bounded shell-Hilbert cost already occurs at

`K ~ (J/log J)^(2/3)`.

At this crossover the carrier derivative on a fixed complex Ford patch is `O(1/log J)`. One exact notch at `iA_J` therefore suppresses an entire fixed critical-depth Ford cell to `O(1/log J)` while the real-axis carrier still has the order-one energy forced by NB-258. The two facts coexist because analytic continuation across a growing imaginary displacement is not coercive in the source norm used there.

The durable correction is that **a source-band lower bound cannot be transferred to the Hardy/Nyman zero marks without pricing the actual complex sampling geometry**. A successful obstruction must control analytic continuation through the `Theta(log J)` Ford-depth displacement or work with a Hardy/Nyman quantity that is coercive directly on the sampled complex line.

**Boundary.** NB-259 suppresses fixed critical Ford cells, not the full hard `1/H` ordinate window, whose Ford width is `Theta(J)`. It also does not eliminate the shallower replacement layers isolated earlier, nor prove that the final Nyman distance can be made small. Near-Ford channel counts and non-scalar structures remain outside this statement.